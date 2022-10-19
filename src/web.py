from selenium import webdriver
from selenium.webdriver import FirefoxOptions


def init_driver(browser: str, path: str = None) -> webdriver:
    """
    Initialize the webdriver using the specified browser at the given executable file
    :param browser: The browser to use as a string. Currently accepted browsers are "safari", "chrome", "firefox", or
    "chromium_edge"
    :param path: The executable file path to this browser
    :return: A Selenium webdriver
    """
    if browser == "safari":
        if path is None:
            return webdriver.Safari()
        else:
            return webdriver.Safari(executable_path=path)
    elif browser == "chrome":
        if path is None:
            return webdriver.Chrome()
        else:
            return webdriver.Chrome(executable_path=path)
    elif browser == "firefox":
        if path is None:
            options = FirefoxOptions()
            options.add_argument("--headless")
            return webdriver.Firefox(options=options)
        else:
            return webdriver.Firefox(executable_path=path)
    elif browser == "chromium_edge":
        if path is None:
            return webdriver.ChromiumEdge()
        else:
            return webdriver.ChromiumEdge(executable_path=path)
    else:
        print("Error: Given browser '" + browser + "' not found. Supported browsers are 'safari', 'chrome', 'firefox',"
                                                   "and 'chromium_edge'. Please use one of these and try again.")
        exit()

