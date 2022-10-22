from slack import WebClient


class Bot:

    client: WebClient

    def __init__(self, token: str):
        self.client = WebClient(token)

    def send_message(self, message: str):
        response = self.client.chat_postMessage(channel="#truckfood-bot", text=message)
        return response

    def edit_message(self, new_message: str, timestamp: str):
        self.client.chat_update(channel="#truckfood-bot", ts=timestamp, text=new_message)
