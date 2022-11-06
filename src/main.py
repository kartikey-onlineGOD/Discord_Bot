

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
def train():
    import Chatbot_Trainer as ct 
    ct.main()   
import Answers

import bot_question as bq

import sys
sys.path.insert(0, 'C:/Users/karti/OneDrive/Documents/GitHub/Discord_Bot/Events')
     
import event_main as evm



TOKEN = "MTAzODg1NjM1MzE1MTcxMzQxMA.G5rgRn.viGZFVi98rubt-vD8cwIDnSh0cr_COGwMmUblU"



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
        if gg[0] != ">": 
            a = Answers.mm(gg)
            await message.channel.send(a)

            if "events" in a: 
                text = evm.main()

                uname = str(message.author)

                k = []

                choice = "This has to be read of the csv file"
                choice = "Tech Events"

                import csv 
                with open("Assets\\User_Data.csv", newline = "") as csvfile: 
                    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
                    for row in spamreader:
                        k = k + [row]

                


                text = sorted(text, key = lambda x: x[1])  

                user = []
                for i in range(len(k)): 
                    if k[i][0] == uname: 
                        user = k[i]

                user_choice = user[5]

                if user_choice == "Technology": 
                    user_choice = "Tech Event"

                elif user_choice == "Sports": 
                    user_choice = "Sports Event"

                elif user_choice == "Concerts": 
                    user_choice = "Concert Event"

                elif user_choice == "Literature": 
                    user_choice = "Literature Event"

                elif user_choice == "Festival": 
                    user_choice = "Festival Event"


                j = 1

                for i in range(len(text)): 
                    if text[i][1] == user_choice:
                        k = str(j) + ".   "+text[i][0] + "\n\n"
                        j = j+1
                        await message.channel.send(k)


                    


def runner(): 
    train()
    evm.bot_create()

    
#runner()
train()


import threading

client.run(TOKEN)


