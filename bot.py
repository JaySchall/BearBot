import sys
import discord
import os
from discord import app_commands
import random
import settings

def run_bot():
    intents = discord.Intents.default()

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("HAIII")
    
    @client.event
    async def on_message(message):
        if message.author.id == 393827547873280000: #Clair's ID
            emojiNumber = random.randint(0,1)
            await message.add_reaction(settings.bearEmojis[emojiNumber])
            print("reacted")
    
    client.run(settings.TOKEN)
if __name__ == "__main__":
    run_bot()