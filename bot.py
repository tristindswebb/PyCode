import discord
import responses
from config import TOKEN
from button_test import *

check_roles = ["Warrior","Mage","Ninja","Archer"]


intents = discord.Intents.default()
intents.message_content = True

async def send_message(message, user_message, is_private):
    try:
        response = responses.bot_response(user_message)
        user_roles = [item.name for item in message.author.roles]
        role_len = [item for item in check_roles if item in user_roles]
        if user_message == "createhero" and len(role_len) == 0:
            buttoncheck = selectKnight()
            await message.author.send(response) if is_private else await message.channel.send(response, view=buttoncheck)
        elif user_message == "createhero" and len(role_len) != 0:
            buttoncheck = None
            await message.author.send(" :x: • You already have a role!") if is_private else await message.channel.send(" :x: • You already have a role!", view=buttoncheck)
        else:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_bot():
    intents.message_content = True
    client = discord.Client(intents=intents)
    @client.event
    async def on_ready():
        print(f"{client.user} is now running")
        for guild in client.guilds:
            print(f'Guild Name: {guild.name}')
            print(f'Guild ID: {guild.id}')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        if user_message[0:6] == "!setup":
            await on_setup(message)
            
    
            
    client.run(TOKEN)
