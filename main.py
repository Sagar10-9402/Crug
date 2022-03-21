import discord 
import random
from discord.ext import commands
from server import keep_alive
from discord_slash import SlashCommand
from googlesearch import search
from quickchart import QuickChart ,QuickChartFunction
from datetime import datetime 
from dotenv import load_dotenv
import os



client = commands.Bot(command_prefix='/')

slash = SlashCommand(client,sync_commands=True)

@client.event
async def on_ready():
  print('Bot is Ready')

@client.event
async def on_member_join(member):
  print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
  print(f'{member} has Remove the server.')


@client.event
async def on_message(message) :
    # bot.process_commands(msg) is a couroutine that must be called here since we are overriding the on_message event
    responses = ['Hello', 'Hi', 'Hey', 'Hi there!']
    # await massege.send(f' {random.choice(responses)} {author}
    author = message.author.mention
    await client.process_commands(message) 
    if str(message.content).lower() == "hi":
        await message.channel.send(f'{random.choice(responses)}... {author}')
    


@slash.slash(name="hi", description="just send a Message")
async def hi(ctx):
    author = ctx.author.mention
    responses = ['Hello', 'Hi', 'Hey', 'Hi there!']
    await ctx.send(f' {random.choice(responses)} {author}, My name is Crug How may I help You ?\nIf you want to know more about features please Enter / or "/help" :slight_smile:')




@slash.slash(name= "find",description="Just send a find and Search something and u got a ans where u got that  ")
async def _find(ctx,*,question):
  responses =['Find on Google.com : https://www.google.com/'
              ,'You need to find on Google']              
  await ctx.send(f"Question : {question}\nAnswer : {random.choice(responses)}")



# @slash.slash(name= "google",description="just find something intresting")
@client.command()
async def google(ctx,*, query):
		author = ctx.author.mention
		await ctx.channel.send(f"Here are the links related to your question {author} !")
		async with ctx.typing():
				for j in search(query, tld="co.in", num=5, stop=5, pause=2): 
						await ctx.send(f"\n:point_right: {j}")
				await ctx.send("Have any more questions:question:\nFeel free to ask again :smiley: !")

################### Embed Funtion #########



@slash.slash(name="Embed_Structure", description="just use slash and say embed like /embed")
async def sendembed(ctx):
    embed = discord.Embed(title="My first page",
                          color=discord.Color.green(),
                          description="my first page embed which i sended to my discord bot")
    embed.add_field(name="field 1 ", value="Embed Field one ", inline=True)
    embed.add_field(name="field 2 ", value="Embed field two", inline=True)
    embed.add_field(name="field 3 ", value="Embed field three", inline=False)
    embed.set_image(url="https://i.stack.imgur.com/8xAac.png")
    embed.set_thumbnail(url="https://i.stack.imgur.com/8xAac.png")
    embed.set_author(name="Sagar", icon_url=client.user.avatar_url,
                     url="https://www.google.com/")
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text="This is the footers of the Embed",
                     icon_url=client.user.avatar_url)
    await ctx.send(embed=embed)
    
################ Time Stamp   #####################

@slash.slash(name="time_stamp", description="Show the Time now ")
async def timestamp(ctx):
    embed = discord.Embed(title= "Time",
                           color=discord.Color.green())
    embed.timestamp = datetime.utcnow()
    await ctx.send(embed=embed)


          
##################### Charts u want #######

@slash.slash(name="Charts_name", description="show me the line chart")
async def line(ctx, *, query):
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.device_pixel_ratio = 3.0
    qc.config = {
        "type": f"{query}",
        "data": {
            "labels": ["Today Sales", "Balance", "Weekly Sales", "Monthly Sales"],
            "datasets": [{
                "label": "Sales",
                "data": [5000, 4600, 6500, 5800]
            }]
        }
    }
    await ctx.send(qc.get_url())



keep_alive()

load_dotenv()

TOKEN = os.getenv("TOKEN")

client.run(TOKEN)

