import json

from channels.generic.websocket import WebsocketConsumer

class PongPlayer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.load(text_data)
        key_pressed = text_data_json["key_pressed"]


