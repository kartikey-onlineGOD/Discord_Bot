

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
     

import answer


TOKEN = "MTAzODU0NzQwMDAwMTg2MzgwMQ.GCgGK1.xLY-vP0UssOmNuM7OiiHMLh4lh8dLwPtYqhaE0"



intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='>', intents=intents)
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
  
    print(f'Message {user_message} by {username} on {channel}')
  
    if message.author == client.user:
        return
  
    if channel == "test":
        gg = user_message.lower()
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif gg != "": 
            a = answer.ans(gg)
            await message.channel.send(a)




        
        

            
client.run(TOKEN)

