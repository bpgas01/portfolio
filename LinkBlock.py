# @Author Duncan Sykes 2019
# Version 1.3

import csv                          # Import Libaries
import discord                      
import time
import re
import random
from checkLink import link_Check


# NOTE: This code is a hot mess. It still contains redundant code. 

TOKEN = 'NTUxMzUzMDk3NjQ2MTEyNzc4.D1vvpw.v-sgyjZUNzgEtnDRsOJGKZMxwTI' # Token used to connect to the discord API (bot user account)
client = discord.Client()                       #init the discord library
checker = link_Check()                          # Init the linkCheck() module
links = checker.List_return()                   # Call on the List_return function to load in the blocked sites for reference


@client.event
async def on_ready():                           #Shows feedback in console to show that the code is running correctly
    print("Linkbot Online.. Checking your links")
    await client.change_presence(game=discord.Game(name="with all the bots..."))
    em = discord.Embed(title='ALERT', description='Bot went online at ' + time.asctime(), colour=0x00ee00)
    await client.send_message(client.get_channel('547778462862278659'), embed=em) #Bot goes online now

@client.event
async def on_server_join(server):
    try:
    TempFileRead = open(r"servers.txt", "r+")   # Tells developer how many servers linkBot is deployed on
    TempFileRead.write(ServerCount + 1)         # Works by writing to a file every time a new server is discovered
    TempFileRead.close() 
    em = discord.Embed(title='**LinkBot NOW ONLINE**', description='Hello, members of **' + server.name + '**!')
    await client.send_message(discord.utils.get(client.get_all_channels(), server__name=server.name, name='general'), embed=em)

@client.event
async def on_message(message):                  # starts asynchronous event to check for new messages. 
                               

    if message.author == client.user:           # checks message author to ensure the bot does not reply to itself
        return

    # The following code checks to see if any messages that are sent, begin with: www., https:// etc
    elif message.content.startswith('www.') or message.content.startswith('https://') or message.content.startswith('http://') or message.content.startswith('"www.') or message.content.startswith('"http://') or message.content.startswith('"https://'):
        # ---------------------- REMOVE LETTERS FOR CHARACTER REFERENCE -------------------
        s = str(message.content)
        translated = s.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
        translist = list(translated)
        print(translist)

        # Set up a variable which contains some JSON for embbeding into discord. This message would be sent to the bot log channel
        log = discord.Embed(title='**Explicit Link Detected**', description='Posted by: ' + message.author.mention)
        log.add_field(name='*The Link:*  ', value='||' + message.content + '||')
        log.add_field(name='**Comment: **', value='Oh HELLLLLLL NOOOOOOO - Warn this user: ' + message.author.mention)

        # Double check the message content
        if message.content.startswith('www.') or message.content.startswith('https://') or message.content.startswith('http://') or message.content.startswith('"www.') or message.content.startswith('"http://') or message.content.startswith('"https://'):
            # --------------------------- BAD LINKS --------------------------------------- Set up the embedding for bad links
            bad = discord.Embed(title='OOF: ' + time.asctime(), colour=0xff0000)
            bad.add_field(name='***EXPLICIT LINK DETECTED***', value='Why you do this'+message.author.mention)
            bad.add_field(name='NOTE: ', value='*If you think you have been wrongly accused, please contact one of the mods*')
  
            # --------------------------- CHECKER ----------------------------------------- 
            # This was supposed to PM the offender- but I scrapped that idea
            # msg = "HEY STOP RIGHT THERE, Please don't send that link again. The moderaters have been notified of your wrong-doing...."

            
            one = checker.LinkSearch(message.content) # Call on the linksearch function to check the user input against the blocked links. (linkcheck.py)

            # --------------------------- RETURN RESPONSE ---------------------------------
            
            if one == True: # If One returns true, meaning a blocked link is detected, the code sends the following back to discord
                print('BAD LINK DETECTED - - CHECK LOG LINKS') 
                await client.send_message(message.channel, embed=bad)# The embedded BAD message
                await client.delete_message(message) # Deletes the sent link, or offenders message (containing the bad link)
                await client.send_message(client.get_channel('418827778528641041'), embed=log) #Send the log message to the log channel
                # await message.author.send(msg)-


            if one == False: # If nothing bad is detected, ignore it. We don't want to block EVERYTHING
                pass


                


client.run(TOKEN)
