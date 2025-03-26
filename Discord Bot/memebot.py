import discord

""" This method is called when the bot has successfully connected to Discord and is ready to start interacting with the API."""
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
intents = discord.Intents.default()
intents.message_content = True

"""Starting client and authenticating with Discord"""
client = MyClient(intents=intents)
client.run('MTM1NDI1MDkxMzE3MDMyOTc5Mg.GPI5Wt.xL9NdtPJCG39fRJ9XR9yQ-vymECc_nT1MJvnhE')

"""Reading and responding to messages"""
async def on_message(self, message):
    if message.author == self.user:
        return
    
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')