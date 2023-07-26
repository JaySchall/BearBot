import sys
import discord
import os
from discord import app_commands
import random
import settings

def run_bot():
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)
    
    
    @client.event
    async def on_ready():
        print("HAIII")
        #synced = await tree.sync()
        #print(f"Synced {len(synced)} commands")
        await settings.updateEmojiList()
    
    @client.event
    async def on_message(message):
        if message.author.id == 209440277981560833: #Not Clair's ID
            emojiNumber = random.randint(0,len(settings.bearEmojis) - 1)
            await message.add_reaction(settings.bearEmojis[emojiNumber])
            print("reacted")
    
    @tree.command(name="updateemojis", description="updates the list of emojis")
    @app_commands.checks.has_permissions(administrator = True)
    async def bearemojis(interaction: discord.Interaction):
        guild = client.get_guild(settings.emojiServer)
        f = open(settings.emojiList, "w")
        for emoji in guild.emojis:
            if "bear" in emoji.name:
                f.write(str(emoji) + "\n")
        f.close()
        await settings.updateEmojiList()
        await interaction.response.send_message("Updated List")

    @tree.command(name="bearflood", description="floods a message with bears, run in same channel as message")
    @app_commands.checks.has_permissions(administrator = True)
    async def bearflood(interaction: discord.Interaction, messageid: str):
        channel = interaction.channel
        try:
            message = await channel.fetch_message(int(messageid))
            print(message.content)
        except:
            await interaction.response.send_message("invalid message id")
            return
        await interaction.response.send_message("flooding message")
        for emoji in settings.bearEmojis:
            await message.add_reaction(emoji)
        


    client.run(settings.TOKEN)
if __name__ == "__main__":
    run_bot()