import os

from slack import WebClient


class Bot:

    client: WebClient

    def connect(self, token: str):
        """
        Connect to Slack
        :param token:
        :return:
        """
        self.client = WebClient(token)

    def disconnect(self):
        self.client = None

    def send_message(self, message: str):
        """
        Send a message to Slack
        :param message: A string
        :return: The response from Slack
        """
        if self.client is None:
            return None
        else:
            response = self.client.chat_postMessage(channel=os.environ["SLACK_CHANNEL"], text=message)
            return response

    def edit_message(self, new_message: str, timestamp: str) -> None:
        """
        Edit a Slack message with a certain timestamp
        :param new_message: A string
        :param timestamp: A string
        :return: None
        """
        if self.client is None:
            return None
        else:
            self.client.chat_update(channel=os.environ["SLACK_CHANNEL"], ts=timestamp, text=new_message)
