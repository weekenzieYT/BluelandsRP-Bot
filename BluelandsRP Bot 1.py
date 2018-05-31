import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
  
Client = discord.Client()
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)
  
@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='https://bluelandsrp.wixsite.com/official'))
  
@client.command(pass_context=True)
async def rules(ctx):
    await client.say("""RULES:
1. This server uses the BluelandsRP Official Bot which helps us keep track of who's who.
2. Do NOT tag staff members for no reason.
3. We are all here to have a good time, keep chat respectful. 
4. Please do not speak poorly about other entertainers. 
5. Inflammatory chat about race, religion and gender will not be tolerated. 
6. Having fun and a bit of banter is fine but please respect everyone.
7. Do not ask for Mod.
8. Do not advertise. Do not self promote.
9. Do not spam.
10. Don't talk in #music without a link
For More Info goto #welcome""")

@client.command(pass_context=True)
async def website(ctx):
    await client.say("""https://bluelandsrp.wixsite.com/official""")

@client.command(pass_context=True)
async def join(ctx):
    await client.say("""Join Our Discord! https://discord.gg/fkYq6v""")

@client.command(pass_context=True)
async def afk(ctx):
    await client.say("""You are now AFK!""")

@client.command(pass_context=True)
async def unafk(ctx):
    await client.say("""You nolonger AFK!""")

@client.command(pass_context=True)
async def server(ctx):
    await client.say("""Pick Which Server you want to see the status of. Say !PCSERVER For the Minecraft PC server or say !PS4SERVER For the Minecraft PS4 Server!""")

@client.command(pass_context=True)
async def pcserver(ctx):
    await client.say("""BLRP.minehut.gg (IN DEVELOPMENT)""")

@client.command(pass_context=True)
async def ps4server(ctx):
    await client.say("""Message @weekenzieYT#6467 to see if PS4 Server is online!""")

@client.command(pass_context=True)
async def apply(ctx):
    await client.say("""**Minecraft PC Server Staff App:** https://goo.gl/forms/tCqxQALpa1rUyJIo2
**Minecraft PS4 Server Staff App:** https://goo.gl/forms/8KK0sqanoCWo8zki1
**Developer / IT Job Application:** https://goo.gl/forms/ECLT95WgHHjLdRsJ2""")

@client.command(pass_context=True)
async def report(ctx):
    await client.say("""**A admin will be with you shortly.**""")

@client.command(pass_context=True)
async def credits(ctx):
    await client.say("""Thanks To:
weekenzieYT For Creating the bot & Founder of BluelandsRP
Markus Co-Founder / Developer & IT For BluelandsRP
The Staff Thanks For Working with us!
The Community Thanks To You for making us be were we are today!""")

#command1
@client.command(pass_context = True)
async def invite(ctx):
    x = await client.invites_from(ctx.message.server)
    x = ["<" + y.url + ">" for y in x]
    print(x)
    embed = discord.Embed(title = "Invite Links", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
  
#command2
@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
  
#command3
@client.command(pass_context=True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)
  
#command4
@client.command(pass_context = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
  
#command5
@client.command(pass_context=True)       
async def clear(ctx, number):
    if not ctx.message.author.server_permissions.administrator:
        return
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
 
#command6
@client.command(pass_context = True)
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to ban!")
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")
 
    embed = discord.Embed(description = "**%s** has been banned!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)
 
#command7
@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to kick!")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")
 
    embed = discord.Embed(description = "**%s** has been kicked!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)
 
#command8
@client.command(pass_context = True)
async def listservers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
 
#command9
@client.command(pass_context = True)
async def info(ctx):
    await client.say("""**Useful Links:**
Discord Invite: https://discord.gg/uzWYRsd
 
Roles:
@Founder - Founder of BluelandsRP
@Co-Founder - Co-Founder of BluelandsRP
@Developer / IT - Helps BluelandsRP with Developing and IT!
@Admin  - Admins of BluelandsRP
@BLRP Moderator - Moderators of BluelandRP
@Trial-Mod - Newest member to the BluelandsRP Staff team
 
Any issues please **PM** @Founder or @Co-Founder directly.
 
!website - Gives you a link to our official website!
!invite - Gives you a link to add the bot to your own server!
!join - Gives you a link to join BluelandsRP Official Discord!
!credits - gives a list of people who helped make the bot!
!afk - Tell the server you are AFK!
!unafk - Tell the Server you are no longer AFK!
!radio - Gives you a link to BluelandsRP Radio!
!server - Tells you what servers are online from BluelandsRP!
!pcserver - Ask if the Minecraft PC Server is online!
!ps4server - Ask if the Minecraft PS4 Server is online!

Visit our website! https://bluelandsrp.wixsite.com/official""")



client.run("NDM2NTAwNjQxNzQ2MTI0ODEw.DbochA.aJDr1wJp-8XXIRSx8yH7wjNmBGM") 
