import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()  
client = commands.Bot(command_prefix = "*") 


@client.event 
async def on_ready():
        print("BluelandsRP Bot is now Online!") 

@client.event
async def on_message(message):
        if message.content.upper().startswith('!WEBSITE'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> https://bluelandsrp.wixsite.com/official" % (userID))
        if message.content.upper().startswith('!SAY'):
                args = message.content.split(" ")
                #args[0] = !SAY
                #args[1] = Hey
                #args[2] = There
                #args[1:] = Hey There
                await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
     
        if message.content.upper().startswith('!CREDITS'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> Thanks To: weekenzieYT For Creating the Bot, Markus Developer / IT For BluelandsRP, The Staff Thanks For Working with us!, The Community Thanks To You for making us be were we are today!" % (userID))

        if message.content.upper().startswith('!INVITE'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> Invite the bot here! https://discordapp.com/oauth2/authorize?client_id=436500641746124810&permissions=0&scope=bot " % (userID))
        if message.content == "hi":
                await client.send_message(message.channel, "Hello!")
        if message.content.upper().startswith('!JOIN'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> Join Our Discord! https://discord.gg/fkYq6v" % (userID)) 

        if message.content.upper().startswith('!AFK'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> Is now AFK!" % (userID))

        if message.content.upper().startswith('!UNAFK'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> Is nolonger AFK!" % (userID))

        if message.content.upper().startswith('!RADIO'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> Coming Soon!" % (userID))
                
        if message.content.upper().startswith('!SERVER'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> Pick Which Server you want to see the status of. Say !PCSERVER For the Minecraft PC server or say !PS4SERVER For the Minecraft PS4 Server!" % (userID)) 

        if message.content.upper().startswith('!PCSERVER'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> BLRP.minehut.gg" % (userID))

        if message.content.upper().startswith('!PS4SERVER'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> Message @weekenzieYT#6467 to see if PS4 Server is online!" % (userID))

        if message.content.upper().startswith('!HELP'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> **Help:**  **!website** - Gives you a link to our official website! **!invite** - Gives you a link to add the bot to your own server! **!join** - Gives you a link to join BluelandsRP Official Discord! **!credits** - gives a list of people who helped make the bot!  **!afk** - Tell the server you are AFK!   **!unafk** - Tell the Server you are no longer AFK! **!radio** - Gives you a link to BluelandsRP Radio! **!server** - Tells you what servers are online from BluelandsRP! **!pcserver** - Ask if the Minecraft PC Server is online!  **!ps4server** - Ask if the Minecraft PS4 Server is online!" % (userID))
    


         





bot.login(process.env.tocken);
