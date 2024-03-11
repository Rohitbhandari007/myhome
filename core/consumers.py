import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from .utils import save_light_data
from channels.db import database_sync_to_async


class HomeConsumer(AsyncWebsocketConsumer):
    """
    Represents a consumer for handling websocket connections related to a home.

    Attributes:
        room_name (str): The name of the home.
        room_group_name (str): The group name for the home's chat room.
    """

    async def connect(self):
        """
        Called when a websocket connection is established.
        Retrieves the home name from the URL route, adds the consumer to the
        corresponding group, and accepts the connection.
        """
        self.room_name = self.scope["url_route"]["kwargs"]["home_name"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """
        Called when a websocket connection is closed.
        Removes the consumer from the home's chat room group.
        """
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        """
        Called when a message is received from the websocket.
        Parses the received JSON data and sends it to the home's chat room group.
        """
        text_data_json = json.loads(text_data)
        text_data_json["saved"] = False
        
        if text_data_json["save"]:
            await save_light_data(text_data_json)
            text_data_json["saved"] = True
            
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "light.data", "data": text_data_json}
        )

    async def light_data(self, event):
        """
        Called when a message is received from the home's chat room group.
        Sends the received data back to the consumer as a JSON string.
        """
        data = event["data"]
        await self.send(text_data=json.dumps(data))
