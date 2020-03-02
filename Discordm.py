import discord



TOKEN = "token"

client = discord.client()


@client.event
async def on_ready():
    print('Bot is ready.')


client.run('NjY5MjE2NDY5NjA2OTg5ODQx.Xicmew.i6yMXc9i0i_IQE7Ymm9eFbdM_-4')
