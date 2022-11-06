

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
import Chatbot_Trainer as ct 
ct.main()   
import Answers
     


TOKEN = "MTAzODUzNTY5OTkxNTM0NTk0MA.GpIUUg.nhNDQ8aD0_o1GLPqJHcBBsK3nCq3Fdvw5Zefb8"



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
        if gg != "": 
            a = Answers.mm(gg)
            await message.channel.send(a)

            if "events" in a: 
                text = username +  " your events are coming up"
                await message.channel.send(text)




        
        

            
client.run(TOKEN)

