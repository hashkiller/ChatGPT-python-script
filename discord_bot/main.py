import discord
import asyncio

# Entrez votre token de bot
TOKEN = 'YOUR_BOT_TOKEN'

YOUR_CHANNEL_ID = 'chanel id'

client = discord.Client()

@client.event
async def on_ready():
    # Envoie "Salut !" toutes les heures
    while True:
        await client.wait_until_ready()
        channel = client.get_channel(YOUR_CHANNEL_ID)
        await channel.send("Salut !")
        await asyncio.sleep(3600)

client.run(TOKEN)