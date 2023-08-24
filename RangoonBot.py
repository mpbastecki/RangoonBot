import discord
from discord.ext import commands
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')     

intents = discord.Intents.default() # or .all() if you ticked all, that is easier
intents.members = False # If you ticked the SERVER MEMBERS INTENT
intents.message_content = True

bot = commands.Bot(command_prefix='+', intents=intents)


#startup events for the bot
@bot.event
async def on_ready():
    await bot.get_channel(1061502200397963336).send("I am fried :crab:")#techfloor botlog 881993586751713290
    await bot.change_presence(activity=discord.Game("on the beach"))

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

fortunes = ["It is certain", "As I see it, yes", "Reply hazy, try again", "Don't count on it",
         "It is decidedly so", "Most likely", "Ask again later", "My reply is no",
         "Without a doubt", "Outlook good", "Better not tell you now", "My sources say no",
         "Yes definitely", "Yes", "Cannot predict now", "Outlook not so good",
         "You may rely on it", "Signs point to yes", "Concentrate and ask again", "Very Doubtful",
         "Suck an egg"]

@bot.command()
async def m8ball(ctx,arg):
    await ctx.send(random.choice(fortunes))

@bot.command(name = "commands")
async def helpme(ctx):
    await ctx.send("My commands are: \n m8ball - ask me a question \n ping - pong")

with open("token.txt", "r") as f:
    key = f.read()

bot.run(key)