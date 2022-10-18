import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
import web

driver: webdriver = None

# Create driver based on program arguments ([browser] [(optional) path_to_browser_executable])
if len(sys.argv) == 2:
    driver = web.init_driver(sys.argv[1])
elif len(sys.argv) == 3:
    driver = web.init_driver(sys.argv[1], path=sys.argv[2])
else:
    print("Error: Incorrect arguments. Usage: main.py [browser] [(optional) path_to_browser_executable]")
    exit()

driver.get("https://www.rit.edu/fa/diningservices/food-trucks")
events_container_element = driver.find_elements(By.CLASS_NAME, "events-container")
all_elements = events_container_element[0].find_elements(By.CSS_SELECTOR, "*")

output: str = ""

for element in all_elements:

    if element.text.lower().split(" ")[0] == "schedule":
        output = output + "\n*" + element.text + "*\n"
    elif element.tag_name == "P":
        output = output+element.text + "\n"
    elif element.tag_name == "LI":
        output = output + "\t" + element.text + "\n"

print(output)
