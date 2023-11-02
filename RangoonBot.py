import discord
from discord.ext import commands
from discord import option
import random
from random import randint
from random import seed    
import TenGiphPy
import fortune

intents = discord.Intents.default() # or .all() if you ticked all, that is easier
intents.members = False # If you ticked the SERVER MEMBERS INTENT
intents.message_content = True

with open("tenorkey.txt", "r") as g:
    tenorkey = g.read()

t = TenGiphPy.Tenor(token=tenorkey)

prefix = '+'
bot = commands.Bot(command_prefix=prefix, intents=intents)


#startup events for the bot
@bot.event
async def on_ready():
    #await bot.get_channel(1061502200397963336).send("I am fried :crab:")
    await bot.change_presence(activity=discord.Game("on the beach"))
count1 = 0
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    global count1
    if(count1 >30):
        count1 = 0
        if(randint(1,100) < 9):
            await message.channel.send("crab")
    else:
        print(count1)
        count1 += 1

#ping
@bot.slash_command(description = "Pong")
async def ping(ctx):
    await ctx.respond("Pong")
    
#pong
@bot.slash_command(description = "Ping")
async def pong(ctx):
    await ctx.respond("Ping")

#reads fortunes
fortunes2 = ["It is certain", "As I see it, yes", "Reply hazy, try again", "Don't count on it",
         "It is decidedly so", "Most likely", "Ask again later", "My reply is no",
         "Without a doubt", "Outlook good", "Better not tell you now", "My sources say no",
         "Yes definitely", "Yes", "Cannot predict now", "Outlook not so good",
         "You may rely on it", "Signs point to yes", "Concentrate and ask again", "Very Doubtful",
         "Suck an egg"]
    
@bot.slash_command(description="Ask a yes/no question to be answered")
@option("question", description = "Yes/No question to be answered")
async def m8ball(ctx,question):
    await ctx.respond("Question: " + question + "\nAnswer: " + random.choice(fortunes2))

images = ['1.gif', '2.png','3.gif','4.png','5.gif','6.gif','7.png']

#crab
@bot.slash_command(description="crab")
async def crab(ctx):
    await ctx.respond(file=discord.File(("./images/" + random.choice(images))))

#rolls dice user specifies
@bot.slash_command(description="Roll any dice size and number")
@option("size", description = "Size of dice")
@option("count", description = "Number of dice")
async def dice(ctx, size, count):
    dicestring = count + " D" + size
    for x in range(int(count)):
        dicestring += "\nYou rolled a " + str(randint(1,int(size)))
    await ctx.respond(dicestring)

@bot.slash_command(name='fortunes', aliases=['cookie', 'quote', 'fact', 'factoid'])
@option("category", description = "Can be fortune, factoid, people, quote")
async def fortunes(ctx, category='random'):
    """Fortune Cookie! (You can also specify category[factoid,fortune,people,quote])"""
    categories = ['fortune', 'factoid', 'people','quote']
    if category in categories:
        await ctx.respond(f"```fix\n{fortune.get_random_fortune(f'fortunes/{category}')}\n```")
    else:
        await ctx.respond(f"```fix\n{fortune.get_random_fortune(f'fortunes/{random.choice(categories)}')}\n```")




giftag = "crab"
"""@bot.slash_command(description="Random crab gif")
async def randomcrab(ctx):
    #getgifurl = await t.arandom(str(giftag))
    #await ctx.respond(f'{getgifurl}')
    #await ctx.respond(await t.arandom("Crab"))
    
    apikey = ""  # click to set to your apikey
    lmt = 8
    ckey = "crab"  # set the client_key for the integration and use the same value for all API calls

# our test search
    search_term = "excited"

# get the top 8 GIFs for the search term
    r = await requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))

    if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        await ctx.respond(top_8gifs)
    else:
        top_8gifs = None
        await ctx.respond("Tenor is being difficult")
   """ 

helpString = "My prefix is " + prefix + """\nMy commands are:\n m8ball - ask me a question \n ping - pong \n crab \n"""

#help command to list all available actions
#@commands.has_role("Test") parameter you can use to restrict a command to only a specific role
@bot.slash_command(description="Shows available commands")
async def commands(ctx):
    await ctx.respond(helpString)



with open("token.txt", "r") as f:
    key = f.read()

bot.run(key)