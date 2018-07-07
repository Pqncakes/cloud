# Cloud v1 - 

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print ("Cloud is ready and running.")
    print ("My Username currently is: " + bot.user.name)
    print ("my current ID is: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='Beta - *help'))
 
@bot.command(pass_context=True)
async def Cloud ():
    await bot.say ("Coming Soon!")

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
async def game(ctx, *args):
     if ctx.message.author.id == '379187195187298304':
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
        await bot.say(":white_check_mark: Success!")
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
        await bot.say("**{0}** has been kicked. :white_check_mark:")
     else:
        await bot.say(":x: You Do Not Have Permission to use this command")     

@bot.event
async def on_message(message):
    if message.content.startswith('_whatcanyoudo?'):
        msg = await client.send_message(message.channel, '''`Bot Commands And Features:
Lmfao tests
test 2
Cloud v1.5
'''                                    
bot.run("NDY1MDY5MDA2OTQ1MTI0MzYy.DiIKwA.OW5Fu3ulaAayPpTpVRrsrUGCOao")   
