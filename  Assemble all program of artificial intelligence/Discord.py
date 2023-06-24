# from chat import dack
import discord

client = discord.Client(intents = discord.Intents.all())

help = """Enter\t/chat\t\t\tbefore writing your message!
Enter\t/imagine\t before writing your image of imagination prompt!
"""

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("/chat"):
        await message.channel.send(dack(message.content))

    elif message.content.startswith("/imagine"):
        # await message.channel.send(f"Your image generating <t:{int(time.time() + 60)}:R>")
        # time.sleep(60)
        await message.channel.send("This project is in progress ! ! ! . . .")

    else:
        await message.channel.send(help)


client.run('MTA2NzMxNzEwNDczNjQ2OTA2Mw.Ge1Sc6.U784DeCiz-RifeT1LSz5NYUmHzGoZ_BNliR-Xo')