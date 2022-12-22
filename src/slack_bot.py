import os

from slack import WebClient


class Bot:

    client: WebClient

    def __init__(self, token: str):
        """
        Create a new Slack Bot
        :param token: The Slack token
        """
        self.client = WebClient(token)

    def send_message(self, message: str):
        """
        Send a message to Slack
        :param message: A string
        :return: The response from Slack
        """
        response = self.client.chat_postMessage(channel=os.environ["SLACK_CHANNEL"], text=message)
        return response

    def edit_message(self, new_message: str, timestamp: str) -> None:
        """
        Edit a Slack message with a certain timestamp
        :param new_message: A string
        :param timestamp: A string
        :return: None
        """
        self.client.chat_update(channel=os.environ["SLACK_CHANNEL"], ts=timestamp, text=new_message)
