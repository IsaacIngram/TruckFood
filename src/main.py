from database import Database
from slack_bot import Bot
from web_driver import WebDriver
from os import environ
import time

# Initialize all APIs
database: Database
bot: Bot
web_driver: WebDriver

def init() -> None:

    # Create the database
    global database, bot, web_driver
    database = Database()

    # Create the Slack bot
    bot = Bot()

    # Create the WebDriver
    run_headlessly = False
    if environ['RUN_HEADLESSLY'] == 1:
        run_headlessly = True
    web_driver = WebDriver(environ['SELENIUM_BROWSER'], run_headlessly)


def run() -> None:

    # Get data from RIT's website
    data = web_driver.get_description()

    # Open a connection to the database
    database.connect(
        environ['DATABASE_HOST'],
        environ['DATABASE_USER'],
        environ['DATABASE_PASSWORD'],
        environ['DATABASE_PORT'],
        environ['DATABASE_NAME']
    )

    # Decide if the data has changed
    if hash(data) != database.get_description():

        # Because it has changed, parse the new start and end date
        new_start, new_end = web_driver.get_dates()

        # Check if an error was encountered when getting the dates
        if new_start is None or new_end is None:
            print("Parsing error! Could not find dates in data: " + data)
            return None

        # Decide if the dates have changed
        if new_start != database.get_start_date() or new_end != database.get_end_date():

            # Send a message to slack
            bot.connect(environ['SLACK_TOKEN'])
            response = bot.send_message(data)

            # Check if Slack provided an error in response
            if not response.validate():
                print("Slack error! Response from Slack was not valid after attempting to send a message.")
                return None

            # Update database contents
            database.set_description(hash(data))
            database.set_start_date(new_start)
            database.set_end_date(new_end)
            database.set_timestamp(response.get("ts", "0"))

        else:
            # Edit the previous message sent to Slack
            bot.connect(environ['SLACK_TOKEN'])
            response = bot.edit_message(data, database.get_timestamp())

            # Check if Slack provided an error in response
            if not response.validate():
                print("Slack error! Response from Slack was not valid after attempting to edit a message.")
                return None

            # Update database contents
            database.set_description(hash(data))
            database.set_start_date(new_start)
            database.set_end_date(new_end)
            database.set_timestamp(response.get("ts", "0"))

    # Close database connection
    database.disconnect()
    # Close the Slack connection
    bot.disconnect()


init()

while True:
    run()
    time.sleep(5)
