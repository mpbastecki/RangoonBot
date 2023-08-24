import discord
from discord.ext import commands
import random
    

intents = discord.Intents.default() # or .all() if you ticked all, that is easier
intents.members = False # If you ticked the SERVER MEMBERS INTENT
intents.message_content = True

prefix = '+'
bot = commands.Bot(command_prefix=prefix, intents=intents)


#startup events for the bot
@bot.event
async def on_ready():
    await bot.get_channel(1061502200397963336).send("I am fried :crab:")#techfloor botlog 881993586751713290
    await bot.change_presence(activity=discord.Game("on the beach"))

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")
    
@bot.slash_command(description = "Pong")
async def ping(ctx):
    await ctx.respond("Pong")

fortunes = ["It is certain", "As I see it, yes", "Reply hazy, try again", "Don't count on it",
         "It is decidedly so", "Most likely", "Ask again later", "My reply is no",
         "Without a doubt", "Outlook good", "Better not tell you now", "My sources say no",
         "Yes definitely", "Yes", "Cannot predict now", "Outlook not so good",
         "You may rely on it", "Signs point to yes", "Concentrate and ask again", "Very Doubtful",
         "Suck an egg"]

@bot.command()
async def m8ball(ctx,arg):
    await ctx.send(random.choice(fortunes))
    
@bot.slash_command(description="Ask a yes/no question to be answered")
async def m8ball(ctx,question):
    await ctx.respond("Question: " + question + "\nAnswer: " + random.choice(fortunes))

images = ['1.gif', '2.png','3.gif','4.png','5.gif','6.gif','7.png']

@bot.command()
async def crab(ctx):
    await ctx.send(file=discord.File(("./images/" + random.choice(images))))

@bot.slash_command(description="crab")
async def crab(ctx):
    await ctx.respond(file=discord.File(("./images/" + random.choice(images))))


helpString = "My prefix is " + prefix + """\nMy commands are:\n m8ball - ask me a question \n ping - pong \n crab \n"""

#help command to list all available actions
@bot.command(name = "commands")
#@commands.has_role("Test") parameter you can use to restrict a command to only a specific role
async def helpme(ctx):
    await ctx.send(helpString)

@bot.slash_command(description="Shows available commands")
async def commands(ctx):
    await ctx.respond(helpString)



with open("token.txt", "r") as f:
    key = f.read()

bot.run(key)