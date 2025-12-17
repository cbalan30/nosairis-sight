import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChartConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "live_chart_updates"
        self.ping_alert = "live_ping_updates"
        # Join the group to receive messages
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.channel_layer.group_add(self.ping_alert, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        await self.channel_layer.group_discard(self.ping_alert, self.channel_name)

    # This method receives messages from the Group and sends them to the Browser
    async def send_chart_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))

    async def send_ping_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))