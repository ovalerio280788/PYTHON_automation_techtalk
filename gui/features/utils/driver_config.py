from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException


def setup_browser(context):
    context.logger.info("Setting up driver")
    browser = context.config.userdata.get('browser')

    if browser == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.manager.showAlertOnComplete", False)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
        context.driver = webdriver.Firefox(firefox_profile=fp)
    elif browser == "chrome":
        try:
            options = webdriver.ChromeOptions()
            options.add_argument({
                "download.prompt_for_download": True,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            })
            context.driver = webdriver.Chrome()
        except SessionNotCreatedException as e:
            context.logger.error(e)
            raise
    else:
        msj = "Not a valid browser name provided!!"
        context.logger.critical(msj)
        raise Exception(msj)

    set_browser_default_size(context)
    context.driver.delete_all_cookies()
    context.driver.implicitly_wait(context.implicit_wait)
    context.driver.set_page_load_timeout(context.timeout)


def set_browser_default_size(context):
    context.logger.info("Setting browser size")
    try:
        context.driver.maximize_window()
    except Exception as e:
        context.logger.warning(f"Browser could not be maximized, setting the window size to 1920x1080. More info: {e}")
        context.driver.set_window_size(1920, 1080)


def clean_browser(context):
    context.logger.info("Closing the driver")
    try:
        context.driver.quit()
        context.logger.info("Driver Closed")
    except Exception as e:
        context.logger.error(e)
