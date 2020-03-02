import discord

class MyClient(discord.client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

    async def on_messege(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('NjY5MjE2NDY5NjA2OTg5ODQx.Xicmew.i6yMXc9i0i_IQE7Ymm9eFbdM_-4')

