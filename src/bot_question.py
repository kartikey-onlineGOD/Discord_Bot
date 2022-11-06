import discord
import random
from discord.ext import commands
from discord.ui import Button, View
import csv
import discord.utils
from csv import writer


intents = discord.Intents.default()
intents.message_content = True
client= commands.Bot(command_prefix='>', intents=intents)

PREFIX=">"

global tech
global fest
global lit
global sport
global concert
tech=0
fest=0
lit=0
sport=0
concert=0

user_data=[]
def tag(tech,lit,fest,sport,concert):
    l=[tech,lit,fest,sport,concert]
    m=["Technology","Literature","Festivals","Sports","Concerts"]
    maxn=max(l)
    return m[l.index(maxn)]


#NAME
@client.command()
async def init(ctx):
    user_id=ctx.author
    username = str(user_id)

    button1 = Button(label="Okay", style=discord.ButtonStyle.blurple, row=0)
    
    async def button1_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init2(ctx)
    button1.callback = button1_callback

    view=View()
    view.add_item(button1)

    await ctx.author.send("Get discord user_id?",view=view)

    global user_data
    user_data.append(username)

    print(username)

    #name function

#AGE
@client.command()
async def init2(ctx):
    button1 = Button(label="18-24", style=discord.ButtonStyle.blurple, row=0)
    
    async def button1_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init3(ctx)
        user_data.append("18-24")
    button1.callback = button1_callback

    button2 = Button(label="24-32", style=discord.ButtonStyle.danger, row=1)
    
    async def button2_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init3(ctx)
        user_data.append("24-32")
    button2.callback = button2_callback
    
    button3 = Button(label="32-40", style=discord.ButtonStyle.success,row=2)
    
    async def button3_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init3(ctx)
        user_data.append("32-40")
    button3.callback = button3_callback
    
    button4 = Button(label="40-60", style=discord.ButtonStyle.success, row=3)

    async def button4_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init3(ctx)
        user_data.append("40-60")
    button4.callback = button4_callback

    button5 = Button(label="60+", style=discord.ButtonStyle.gray, row=4)
    
    async def button5_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init3(ctx)
        user_data.append("60+")
    button5.callback = button5_callback

    view=View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)

    await ctx.author.send("Age", view=view)

#GENDER
@client.command()
async def init3(ctx):
    button1 = Button(label="Female", style=discord.ButtonStyle.blurple, row=0)
    
    async def button1_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init4(ctx)
        user_data.append("Female")
    button1.callback = button1_callback

    button2 = Button(label="Male", style=discord.ButtonStyle.danger, row=1)
    
    async def button2_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init4(ctx)
        user_data.append("Male")
    button2.callback = button2_callback
    
    button3 = Button(label="Prefer not to say", style=discord.ButtonStyle.success,row=2)
    
    async def button3_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init4(ctx)
        user_data.append("Prefer not to say")
    button3.callback = button3_callback
    
    button4 = Button(label="Neither", style=discord.ButtonStyle.success, row=3)

    async def button4_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init4(ctx)
        user_data.append("Neither")
    button4.callback = button4_callback

    view=View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)

    await ctx.author.send("What do you identify yourself as? ", view=view)

#QUEER FEST
@client.command()
async def init4(ctx):
    button1 = Button(label="Yes", style=discord.ButtonStyle.blurple, row=0)
    
    async def button1_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init5(ctx)
        user_data.append("Yes")
    button1.callback = button1_callback

    button2 = Button(label="No", style=discord.ButtonStyle.danger, row=1)
    
    async def button2_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init5(ctx)
        user_data.append("No")
    button2.callback = button2_callback
    
    button3 = Button(label="Maybe", style=discord.ButtonStyle.success,row=2)
    
    async def button3_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
        await init5(ctx)
        user_data.append("Maybe")
    button3.callback = button3_callback

    view=View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)

    await ctx.author.send("Would you like to attend a queer event? ", view=view)

#College of
@client.command()
async def init5(ctx):
    button1 = Button(label="Engineering", style=discord.ButtonStyle.blurple, row=0)
    
    async def button1_callback(interaction):
        global tech
        await interaction.response.send_message("Recorded. Next question: ")
        await init6(ctx)
        user_data.append("Engineering")
        tech+=1
    button1.callback = button1_callback

    button2 = Button(label="Business", style=discord.ButtonStyle.danger, row=1)
    
    async def button2_callback(interaction):
        global tech
        global lit
        await interaction.response.send_message("Recorded. Next question: ")
        await init6(ctx)
        user_data.append("Business")
        tech+=1
        lit+=1
    button2.callback = button2_callback
    
    button3 = Button(label="Liberal arts", style=discord.ButtonStyle.success,row=2)
    
    async def button3_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        
        await interaction.response.send_message("Recorded. Next question: ")
        await init6(ctx)
        user_data.append("Liberal Arts")
        lit+=1
        concert+=1
        fest+=1
    button3.callback = button3_callback
    
    button4 = Button(label="Nursing", style=discord.ButtonStyle.success, row=3)

    async def button4_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded. Next question: ")
        await init6(ctx)
        user_data.append("Nursing")
        sport+=1
    button4.callback = button4_callback

    button5 = Button(label="Undergraduate Studies", style=discord.ButtonStyle.gray, row=4)
    
    async def button5_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded. Next question: ")
        await init6(ctx)
        user_data.append("Undergraduate Studies")
        sport+=1
        concert+=1
        fest+=1
    button5.callback = button5_callback

    view=View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)

    await ctx.author.send("Which college do you study in? ", view=view)

#Type of book
@client.command()
async def init6(ctx):
    button1 = Button(label="The theory of everything", style=discord.ButtonStyle.blurple, row=0)
    
    async def button1_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded. Next question: ")
        await init7(ctx)
        tech+=1
    button1.callback = button1_callback

    button2 = Button(label="Merchant of Venice", style=discord.ButtonStyle.danger, row=1)
    
    async def button2_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded. Next question: ")
        await init7(ctx)
        lit+=1
    button2.callback = button2_callback
    
    button3 = Button(label="Bible", style=discord.ButtonStyle.success,row=2)
    
    async def button3_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded. Next question: ")
        await init7(ctx)
        fest+=1
    button3.callback = button3_callback
    
    button4 = Button(label="I like to listen to songs more", style=discord.ButtonStyle.success, row=3)

    async def button4_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded. Next question: ")
        await init7(ctx)
        concert+=1
    button4.callback = button4_callback

    button5 = Button(label="I don't like to read books", style=discord.ButtonStyle.gray, row=4)
    
    async def button5_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded. Next question: ")
        await init7(ctx)
        sport+=1
    button5.callback = button5_callback

    view=View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)

    await ctx.author.send("What type of book do you read? ", view=view)

#Which event to attend
@client.command()
async def init7(ctx):
    button1 = Button(label="Literature festival", style=discord.ButtonStyle.blurple, row=0)
    
    async def button1_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded all the responses.")
        await record(ctx)
        lit+=1
    button1.callback = button1_callback

    button2 = Button(label="Football Match", style=discord.ButtonStyle.danger, row=1)
    
    async def button2_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded all the responses.")
        await record(ctx)
        sport+=1
    button2.callback = button2_callback
    
    button3 = Button(label="I would rather sit at home and rest", style=discord.ButtonStyle.success,row=2)
    
    async def button3_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded all the responses.")
        await record(ctx)
        tech+=1
    button3.callback = button3_callback
    
    button4 = Button(label="Go to concert", style=discord.ButtonStyle.success, row=3)

    async def button4_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded all the responses.")
        await record(ctx)
        concert+=1
    button4.callback = button4_callback

    button5 = Button(label="Attend a cultural festival", style=discord.ButtonStyle.gray, row=4)
    
    async def button5_callback(interaction):
        global tech
        global fest
        global lit
        global sport
        global concert
        await interaction.response.send_message("Recorded all the responses.")
        await record(ctx)
        fest+=1
    button5.callback = button5_callback

    view=View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)

    await ctx.author.send("What event would you like to attend? ", view=view)

@client.command()
async def record(ctx):
    button = Button(label="Okay",style=discord.ButtonStyle.green, row=0)

    async def button_callback(interaction):
        Tags=tag(tech,lit,fest,sport,concert)

        await interaction.response.send_message("👍")
        filename= "User_Data.csv"
        with open(filename,"w", newline="") as file:
            header=["User_id","Age","Gender","Queer fest","College","Tags"]
            for header in header:
                if header != "Tags":
                    file.write(str(header)+",")
                elif header == "Tags":
                    file.write(str(header))
            file.write("\n")
        file.close()
        user_data.append(Tags)
        with open('User_Data.csv', 'w+',newline="\n") as f_object:
            writer_object=writer(f_object,lineterminator='\n')
            k = user_data
            k = tuple(k)
            ll = [k]
            writer_object.writerows(ll)
            f_object.write("\n")
        f_object.close()

    button.callback=button_callback

    view=View()
    view.add_item(button)

    await ctx.author.send("Press okay to save all your data.",view=view)


@client.event
async def on_ready():
    print("The bot is now ready to use\n-----------------")

@client.command()
async def User_info(ctx):
    file=open("User_Data.csv")
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows=[]
    for row in csvreader:
        rows.append(row)
    
    for i in range(len(rows)):
        if rows[i][0]==str(ctx.author):
            user_id=rows[i][0]
            Age=rows[i][1]
            gender=rows[i][2]
            college=rows[i][4]
            tags=rows[i][5]

    embed=discord.Embed(title="User Info", 
                        description=f'User_id: {user_id}\nAge: {Age}\nGender: {gender}\nCollege: {college}\nDescription: You mostly like things related to these topics - {tags}', 
                        color=discord.Color.blue())
    await ctx.send(embed=embed)

@client.command()
async def Joke(ctx):
    jokes=["What's the difference between roast beef and pea soup? Anyone can roast beef.",
            "One night, I paid $20 to see Prince. But I partied like it was $19.99.",
            "I taught a wolf to meditate. Now he's Aware Wolf.",
            "What do you call a labrador that becomes a magician? A labracadabrador.",
            "What do you call a talking dinosaur? Thesaurus.",
            "What do cats like to eat for breakfast? Mice Krispies."]

    joke=random.choice(jokes)
    await ctx.send(joke)

@client.command()
async def Feedback(ctx):
    button = Button(label="Feedback", style=discord.ButtonStyle.link, url="https://docs.google.com/forms/d/e/1FAIpQLSc_dK7RhBs6PTDhMkA3X7vpfz0OsrRlpUj5MyALsmlwrQMaxA/viewform?usp=sf_link", emoji="🔗", row=0)

    view=View()
    view.add_item(button)
    
    await ctx.reply("What is your preference? ", view=view)

@client.command()
async def Main(ctx):

    Em = discord.Embed(title="Bot Instructions & Commands ",description='Hii guys, this is a bot which will collect all the announcements form different servers and show them to you in either your own server or the servers which have me.\nMy prefix is ">"\nFeel free to drop feedbacck.\nHave a great day!!')
    Em.add_field(name="Main", value="Shows the bot description and commands", inline=True)
    Em.add_field(name="init", value="The first step to converse with this bot", inline=True)
    Em.add_field(name="Joke", value="Tell you a funny joke", inline=True)
    Em.add_field(name="User_info", value="Give you personal info about yourself", inline=True)
    Em.add_field(name="Event_categorised", value="Give you option to select event of a specific category", inline=True)
    Em.add_field(name="Event_regular", value="Tell you about events based on your preferences", inline=True)
    Em.add_field(name="Chat", value="Chat with our AI", inline=True)

    await ctx.send(embed=Em)



#chat,menu
@client.command()
async def Event_categorised(ctx):

    button1 = Button(label="Tech", style=discord.ButtonStyle.blurple, emoji="💻", row=0)
    
    async def button1_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
    button1.callback = button1_callback
    
    button2 = Button(label="Fests", style=discord.ButtonStyle.danger, emoji="🎎", row=0)
    
    async def button2_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
    button2.callback = button2_callback
    
    button3 = Button(label="Literature", style=discord.ButtonStyle.success, emoji="📚", row=1)
    
    async def button3_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
    button3.callback = button3_callback
    
    button4 = Button(label="Sports", style=discord.ButtonStyle.success, emoji="🏈", row=1)

    async def button4_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
    button4.callback = button4_callback

    button5 = Button(label="Concerts", style=discord.ButtonStyle.gray, emoji="🎤", row=2)
    
    async def button5_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
    button5.callback = button5_callback
    
    button6 = Button(label="Filtered", style=discord.ButtonStyle.blurple, emoji="📁", row=2)
    
    async def button6_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
    button6.callback = button6_callback
    
    button7 = Button(label="All", style=discord.ButtonStyle.danger, emoji="🌍", row=3)
    
    async def button7_callback(interaction):
        await interaction.response.send_message("Recorded. Next question: ")
    button7.callback = button7_callback

    view=View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    view.add_item(button6)
    view.add_item(button7)

    await ctx.author.send("Choose which category's event do you want to see? ", view=view)

@client.command()
async def Event_regular(ctx):
    embed=discord.Embed(title="User Info", 
                        description=f'hi guys chai peelo', 
                        color=discord.Color.blue())
    await ctx.send(embed=embed)

def main(TOKEN):
    client.run(TOKEN)