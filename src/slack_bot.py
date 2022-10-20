from slack import WebClient


class Bot:

    client: WebClient

    def __init__(self, token: str):
        self.client = WebClient(token)

    def post_message(self, message: str):
        response = self.client.chat_postMessage(channel="#truckfood-bot", text=message)
        return response
