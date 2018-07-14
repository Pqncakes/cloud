# Cloud v1 - 

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import os
import pickle

bot = commands.Bot(command_prefix='r+')

@bot.event
async def on_ready():
    print ("Cloud is ready and running.")
    print ("My Username currently is: " + bot.user.name)
    print ("my current ID is: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='v1.0.0 - r+bothelp'))
  
@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.manage_roles or ctx.message.author.id == '379187195187298304':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)

@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

@bot.command(pass_context = True)
async def softban(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.manage_roles or ctx.message.author.id == '379187195187298304':
        role = discord.utils.get(member.server.roles, name='Blinded')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was blinded by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)

@bot.command(pass_context = True)
async def unsoftb(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.manage_roles or ctx.message.author.id == '379187195187298304':
        role = discord.utils.get(member.server.roles, name='Blinded')
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was unblinded by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)

@bot.command(pass_context = True)
async def status(ctx, *args):
     if ctx.message.author.id == '444863988069826580':
        mesg = ' '.join(args)
        await bot.delete_message(ctx.message)
        return await bot.change_presence(game=discord.Game(name=mesg))
     else:
        await bot.say("Only The Bot Owner can use this command!")

@bot.command(pass_context = True)
async def setnick(ctx, member: discord.Member, *args):
     if ctx.message.author.server_permissions.manage_nicknames or ctx.message.author.id == '379187195187298304':
        mesg = ' '.join(args)
        await bot.change_nickname(member, mesg)
        embed=discord.Embed(title="Nickname Changed!", description=":white_check_mark: User's Nickname Has been Changed To: " +member.nick,  color=0x00ffff)
        await bot.say(embed=embed) 
     else:
        await bot.say("You Do Not have permission to use this command.")

@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.manage_roles or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)

@bot.command(pass_context = True)
async def ban(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.ban_members :
        await bot.ban(member)
        await bot.say("**{0}** has been banned. :white_check_mark:")
     else:
        await bot.say(":x: You Do Not Have Permission to use this command") 
     
@bot.command(pass_context = True)
async def kick(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.kick_members :
        await bot.kick(member)
        await bot.say(":white_check_mark:`User Has been kicked:` " +member.name)
     else:
        await bot.say(":x: You Do Not Have Permission to use this command")  
   
@bot.command(pass_context = True)
async def bothelp():
    await bot.say('''
***Bot Help***
--------------------
**Bot Prefix: r+**

r+bothelp - Shows this message

r+say - Usage: *say [message]* -**Makes the bot say something**

r+kick - Usage: *kick @User* -**Kicks a User from the server.**

r+ban - Usage: *ban @User* -**Bans a User from the server.**

r+softban - Note: Must Have Blinded Role Setup - Usage: *softban @User* -**Hides a User from all server channels and catigories**

r+unsoftb - Usage: *unsoftb @User* -**Removes the softban from a user**

r+game - Only usable by the bot owner*

r+setnick - Usage: *setnick @User [Nickname]* -**Sets a users nickname.**

r+mute - Note: Must have Muted role setup - Usage: *mute @User* - **Makes a user unable to talk.**

r+unmute - Usage: *unmute @User* -**Removes the mute from a user.**

r+block - **Checks If You've Blocked The Bot.

r+poke - Usage: *poke @User* - **Pokes a user**

r+botinfo - **Shows The Bot Information**

r+bugreport - **Opens a ticket to report bot bugs, Bugs will only be filed from reports in the RedRevamp Official Discord.
----------------------------------------------------------------------------------------------------------------------
More to come soon!
''')

@bot.command(pass_context=True)
async def block(ctx):
    await bot.say("If you recived a message from the bot then your good to go, If you didn't recive anything, you've blocked the bot.")
    await bot.send_message(ctx.message.author, ':tada: I see you recived this message! Your Good To Go!')

@bot.command(pass_context=True)
async def poke(ctx, member: discord.Member):
    await bot.say("**You have poked:** " +member.name)
    await bot.send_message(member, ':point_right: You Have been Poked!')

@bot.command(pass_context = True)
async def botinfo(ctx):
        embed=discord.Embed(title="Bot Info ", description="Bot Name & Tag: RedRevamp#5660 ; Create by Insane#5632 ; Status: Online",  color=0x00ffff)
        await bot.say(embed=embed)

@bot.command(pass_context = True)
async def bugreport(ctx, *args):
    server = ctx.message.server
    await bot.create_channel(server, 'report-369543387', type=discord.ChannelType.text)
    return await bot.say("Please Tag Insane#5632 in the ticket with your bug report!")
  
bot.run("NDY1MTc3Nzk3NDM5MTI3NTUz.DiqfCg.nmw0xdF64YM_mjyf9aKpusiCe6I")        


