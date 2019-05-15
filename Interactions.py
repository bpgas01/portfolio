import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions
import random


server = discord.Server(id='412474290496208907')
bot = commands.Bot(command_prefix='!', description=' -- Linkbot extra commands -- ')


token = 'NTUxMzUzMDk3NjQ2MTEyNzc4.D1vvpw.v-sgyjZUNzgEtnDRsOJGKZMxwTI' # Unique Bot token (allows script to connect to bot user)
reaction_list = ['~3~']
patron_list = ['yourself']
mods = '<@161504618017325057>'+' <@257720428968017920>'+' <@205011905025146880>'+' <@384971944740651009>' #For use on MDD server only

cookie = ['gave the :cookie: to','throwed the :cookie: at ','yeeted the :cookie: at ','slammed a :cookie: into'] #List of possible actions for command

slap_opt = ['lightly slapped','full force backhanded'] #List of possible actions for command



@bot.event
async def on_ready():# When the bot has finshed loading, and is online, a message will print to the console
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



# async is used, because if the commands weren't desgined as co-routines, the bot would only be able to run ONE command at a time, which isn't great if you have multiple using it 

        
@bot.command(pass_context=True)                     #Defining the first custom command. This allows members of the server to hug each other
async def hug(ctx, user_name: discord.User = None): # CTX is similar to self in a class, it is a placeholder. user_name is a key word argument, that takes an @mention. But if nothing is entered, it stays as its default value (None)
    'Give someone a big hug.... <3'                 # Giving the command a description
    if user_name == None:                           # If a user is not @mentioned, the user_name value is equal to None. And runs the below code
        reac = random.choice(reaction_list)         # Choose a random reaction from the reaction list
        selectRand = random.choice(patron_list)     # Choose a random user ID from the user list
        selectRandom = str(selectRand)              # Convert the random selection to a string value
        await ctx.bot.say("You just hugged `{}`{}".format(selectRandom,reac)) # Send a message back to discord. Formatting in the randomly selected user and reaction.
    else:
        reac = random.choice(reaction_list) # If user has a value assigned (@mention) the following code runs
        await ctx.bot.say("You just hugged `{}`{}".format(user_name,reac)) # Send a message back to discord. Formatting in the defined username and reaction.

    
@bot.command(pass_context=True, hidden=True)                                #Define the next command. This time the command is hidden from the built in !help command (because I don't need people spamming it)
async def helpuser(ctx, user:discord.User, reason):                         # Set placeholder, check for @mention, and check for string input
    'Request help with something -- This notifies moderators. Do not spam'  # Set command definition
    await ctx.bot.say('A mod has been notified. Please wait')               # Send message back to discord
    await bot.send_message(bot.get_channel('575172629867266057'), content='This person `{0}` needs help'.format(user))  # Send a message to a paticular channel using the bot.send_message() function. This allows for more option, like setting channel location (with channel ID) etc
    await bot.send_message(bot.get_channel('575172629867266057'), content='Reason: {0}'.format(reason))                 # Format in reason
    await bot.send_message(bot.get_channel('575172629867266057'), content='{0} '.format(mods))                          # Format in the list of server moderators
    
@bot.command(name='cookie', pass_context='True') # Define the next custom command
async def _cookie(ctx, user:discord.User=None): # This command and the next one are very similar to the hug command. The only difference is that the wording is different
    'Give a cookie'
    if user == None:
        await ctx.bot.say('You just threw a cookie into the void... What a waste...')
    else:
        await ctx.bot.say('You just **{}** `{}`'.format(random.choice(cookie), user))


@bot.command(name='kek', pass_context=True)
async def _kek(ctx, user:discord.User=None):
    'KEKEKEKEKEKEKEKEKEKEKEKEKEKEKEK'
    if user == None:
        await ctx.bot.say('KEK')
    else:
        await ctx.bot.say("{} you've been ***KEKED***".format(user))
             

@bot.command(name="no", pass_context=True, hidden=True) # This command was designed as a joke for moderators to use to say no to server members
@has_permissions(administrator=True) # Make sure only people with admin level permissions can use it
async def _no(ctx):
    await ctx.bot.say('https://tenor.com/view/steve-carell-no-please-no-gif-5026106') #Send a NO gif


@bot.command(name="slap", pass_context=True, hidden=True) # This command was also designed as a joke.
@has_permissions(administrator=True) # Make sure only people with admin level permissions can use it
async def _slap(ctx, user:discord.User=None):
    'slap someone?'
    if user == None:
        await ctx.bot.say('You meekly swing your hand through the air')
    else:
        await ctx.bot.say('You just *{}* `{}`'.format(random.choice(slap_opt),user)) # Send a message to discord, randomly select a slap action from the list.
    

    
    
    
bot.run(token) # Start the bot. 
