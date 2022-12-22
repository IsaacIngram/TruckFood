import datetime

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from datetime import date


def _month_string_to_number(name: str):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    s = name.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except ValueError:
        raise ValueError('Not a month')


class WebDriver:
    """
    Contains a Selenium webdriver and the methods necessary to interface with it in the context of this project.
    """

    driver: webdriver

    def __init__(self, browser: str, headless: bool = False) -> None:
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

    def get_description(self) -> str:
        """
        Get the currently posted information about food truck's from RIT's webpage which can be found here:
        https://www.rit.edu/fa/diningservices/food-trucks
        :return: A string
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

    def terminate(self) -> None:
        """
        Terminate this webdriver
        :return: None
        """
        self.driver.close()

    def get_dates(self) -> (datetime.date, datetime.date):
        """
        Gets a tuple with the start date and end date of the food trucks according to the description
        :return: A datetime.date, datetime.date tuple
        """

        # Variables for storing info while we parse
        start_month_string: str = ""
        start_day: int = 0
        end_month_string: str = ""
        end_day: int = 0

        # Split the first line of the description
        split_line = self.get_description().split("\n")[0].split(" ")

        # Iterate through every word
        for i in range(len(split_line)):
            # Skip over all non-numeric words
            if split_line[i].isnumeric():
                # Decide whether to set the start date or end date
                if start_day == 0:
                    # Setting the start date
                    start_day = int(split_line[i])
                    start_month_string = split_line[i-1]
                    print("Start day: " + str(start_day))
                else:
                    # Setting the end date
                    end_day = int(split_line[i])
                    end_month_string = split_line[i-1]
                    print("End day: " + str(end_day))
                    break

        # In the case that one of the days was not set, return empty dates
        if start_day == 0 or end_day == 0:
            return (None, None)

        # Get rid of unnecessary punctuation and whitespace
        start_month_string = start_month_string.strip()
        start_month_string.replace(",", "")
        start_month_string.replace(".", "")
        end_month_string = end_month_string.strip()
        end_month_string.replace(",", "")
        end_month_string.replace(".", "")

        # Switch to all lowercase
        start_month_string = start_month_string.lower()
        end_month_string = end_month_string.lower()

        # Get numerical month values
        start_month = _month_string_to_number(start_month_string)
        end_month = _month_string_to_number(end_month_string)

        # Get current year
        year = datetime.datetime.now().year

        # Create datetime objects
        start = datetime.datetime(year, start_month, start_day)
        end = datetime.datetime(year, end_month, end_day)

        return start, end

