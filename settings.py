import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

emojiServer = 795084804181065768

emojiList = "emojis.txt"

bearEmojis = ["<:pinkteddy:1133624059205271553>","<:bearLove:1133624085339983882>"]

async def updateEmojiList():
    global bearEmojis
    bearEmojis = []
    f = open(emojiList, "r")
    for line in f:
        line = line.strip()
        bearEmojis.append(line)
    print(bearEmojis)
    f.close()