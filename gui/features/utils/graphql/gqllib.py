from time import sleep

import requests
from gql import Client
from requests.auth import HTTPBasicAuth
from retrying import retry

from gui.features.utils.graphql.requests_override import RequestsHTTPTransport


class GraphQlLib:

    def __init__(self, graphql_server, user, password, timeout, logger=None):
        """
        The constructor of the class.
        kepler web site.
        :param user: The username of the kepler app.
        :param password: The password of the kepler app.
        :param logger: An instance of a logger object to be used to log information about steps
        """
        try:
            self.logger = logger
            self.graphql_server = graphql_server
            _transport = RequestsHTTPTransport(
                url=self.graphql_server,
                use_json=True,
                verify=False,
                timeout=timeout,
                auth=HTTPBasicAuth(user, password)
            )
            if logger:
                logger.info("Trying to connect to the GraphQL server...")
            self.client = Client(transport=_transport, fetch_schema_from_transport=True, retries=None)
            if logger:
                logger.success("Successfully connected to the GraphQL server.")
        except Exception as e:
            mnj = f"Sorry, Not able to connect to the GraphQL server: {self.graphql_server} " \
                  f"with user {user}. More details: {e}"
            if logger:
                logger.error(mnj)
                raise Exception(mnj)
            else:
                raise Exception(mnj)

    def execute_query(self, gql):
        """
        This method executes a GraphQL query, use this one if it is not a negative test, where the query is supposed to work.
        If the status code of the request is not 200, it will thrown an exception.
        param gql: the graphql query object to be executed
        return: A data json object or an exception if fails
        """
        return self.client.execute(gql)

    def get_result_query(self, gql):
        """
        This method executes the GraphQL query, and will return the results of the query. This can be used for negative tests since
        it will return the errors of the request, the status code, and the data.
        param gql: the graphql query object to be executed
        return: ExecutionResult object
        """
        return self.client._get_result(gql)


def connect_to_graphql(context):
    current_attempt = 0
    context.logger.info(f"Trying to connect to 'graphql' server.")

    try:
        if not is_graphql_connected(context):
            graphql_server = context.config.userdata.get('graphql_endpoint')
            context.logger.info(f"Using Graphql server: {graphql_server}")
            context.graphql = GraphQlLib(graphql_server,
                                         context.config.userdata.get('username'),
                                         context.config.userdata.get('password'),
                                         timeout=int(context.config.userdata.get('default_requests_timeout')),
                                         logger=context.logger)
    except Exception as e:
        context.logger.warning(f"{e}, trying to connect again!!")
        sleep(5)
    finally:
        current_attempt += 1


def is_graphql_connected(context):
    try:
        # context.graphql
        if getattr(context, "graphql", None) and context.graphql_token:
            context.logger.info("Re-using connection to the graphql server!!")
            return True
        else:
            context.logger.warning("Not connected yet to the graphql server!!")
            return False
    except Exception as e:
        context.logger.warning(f"Not connected yet to the graphql server!!. Error: {e}")
        return False


@retry(stop_max_attempt_number=5, wait_fixed=5000)
def execute_gql(context, query, do_assert=True):
    """
    This method executes a graphql query and save the results into the context global variable to be accessible later on other steps
    """
    try:
        context.logger.info(f"The following query will be executed:\n{query}{query.loc.source.body}")
        context.graphql.result = context.graphql.get_result_query(query)
    except Exception as e:
        context.logger.warning(f"Retrying execute_gql method!! Error: {e}")
        raise Exception(e)

    if do_assert:
        if context.graphql.result.errors:
            context.logger.warning(f"There is an error with the Graphql/Hasura query, "
                                   f"please take a look carefully: {context.graphql.result.errors}")
        assert context.graphql.result.errors is None, f"Error: context.graphql.result.error is not None " \
                                                      f"trying to execute query {query.loc.source.body}"
