from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


class WebDriver:
    """
    Contains a Selenium webdriver and the methods necessary to interface with it in the context of this project.
    """

    driver: webdriver

    def __init__(self, browser: str, headless: bool = False):
        """
        Creates this webdriver and establishes a connection
        :param browser:
        :param headless:
        """

        # Determine what type of webdriver to create based on user input
        if browser == "safari":
            # Check whether to run heedlessly
            if headless:
                print("Error: Can't run Safari heedlessly! Safely quitting.")
                quit()
            else:
                self.driver = webdriver.Safari()
        elif browser == "chrome":
            # Check whether to run headlessly
            if headless:
                options = ChromeOptions()
                options.add_argument("--headless")
                self.driver = webdriver.Chrome(options=options)
            else:
                self.driver = webdriver.Chrome()
        elif browser == "firefox":
            # Check whether to run headlessly
            if headless:
                options = FirefoxOptions()
                options.add_argument("--headless")
                self.driver = webdriver.Firefox(options=options)
            else:
                self.driver = webdriver.Firefox()
        elif browser == "chromium-edge":
            # Check whether to run headlessly
            if headless:
                print("Error: Can't run Chromium Edge headlessly! Safely quitting.")
                quit()
            else:
                self.driver = webdriver.ChromiumEdge()
        else:
            print("Error: Given browser '" + browser + "' not found. Supported browsers are 'safari', 'chrome', "
                                                       "'firefox', and 'chromium_edge'. Please use one of these and "
                                                       "try again.")
            print("Safely quitting")
            quit()

    def get_food_trucks(self) -> str:
        """
        Get the food truck information based on RIT's food truck webpage, which can be found here:
        https://www.rit.edu/fa/diningservices/food-trucks
        :return: A properly formatted string containing the food truck information
        """

        # Get the food trucks webpage
        self.driver.get("https://www.rit.edu/fa/diningservices/food-trucks")

        # Get the element that contains all elements related to the food trucks
        container_element = self.driver.find_elements(By.CLASS_NAME, "events-container")

        # Create a list of all elements within the above container
        food_truck_elements = container_element[0].find_elements(By.CSS_SELECTOR, "*")

        # Create the output string. The content of food truck elements will be appended here.
        output: str = ""

        # Iterate through food truck elements and append their content to the output string.
        for element in food_truck_elements:

            # Check if the element is the title string (that begins with "schedule")
            if element.text.lower().split(" ")[0] == "schedule":
                # Add asterisks before this element, since Slack bolds content between single Asterisks
                output = output + "\n*" + element.text + "*\n"
            # Check if the element is a p element, since those should be included in the output
            elif element.tag_name == "P":
                output = output + element.text + "\n"
            # Check if the element is a li element, since those should be included in the output and should be indented
            elif element.tag_name == "LI":
                output = output + "\t" + element.text + "\n"

        return output
