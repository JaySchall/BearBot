import enum
import sys
import discord
import sqlite3
from discord import app_commands
import random
import settings

bully = False
con = sqlite3.connect("Queue.sqlite3")
cur = con.cursor()

class toggle(enum.Enum):
    enable = 1
    disable = 0
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
        if bully == True and message.author.id == 393827547873280000: #Clair's ID
            if "bear" not in message.author.display_name.lower():
                await message.author.edit(nick="Resident Bear Clair")
            emojiNumber = random.randint(0,len(settings.bearEmojis) - 1)
            try:
                await message.add_reaction(settings.bearEmojis[emojiNumber])
                print("reacted")
            except:
                await message.channel.send(settings.bearEmojis[emojiNumber])
                print("blocked, sent a msg instead")
    
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
    
    @tree.command(name="bullyclair", description="toggles the real features")
    @app_commands.checks.has_permissions(administrator = True)
    async def bully(interaction: discord.Interaction, toggle: toggle):
        if interaction.user.id == 393827547873280000:
            await interaction.response.send_message("Sorry not for Clair")
            return
        if toggle.value == 1:
            bully = True
            await interaction.response.send_message("bullying enabled >:)", ephemeral=True)
        elif toggle.value == 0:
            bully = False
            await interaction.response.send_message("bullying disabled :(", ephemeral=True)
        await interaction.response.send_message(toggle, ephemeral=True)


    client.run(settings.TOKEN)
if __name__ == "__main__":
    run_bot()