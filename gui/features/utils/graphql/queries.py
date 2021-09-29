from gql import gql

EMPTY_CART = gql('''
    mutation MyMutation {
      emptyCart(input: {}) {
        clientMutationId
      }
    }
''')

PRODUCTS = gql('''
    query MyQuery {
      products {
        edges {
          node {
            id
            name
            type
            totalSales
          }
        }
      }
    }
''')
