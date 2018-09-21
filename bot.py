import discord
import os
import requests
from discord.ext import commands


bot = commands.Bot(command_prefix='*', description='A bot made for the Elitists Clan Family. Author - Evo')
token = os.environ.get("b2EG0rNoCURJcgRyhEoAbNJAdeLhzCT4")

mem = discord.Member
role = discord.Role
guild = discord.Guild

dv = discord.__version__

game = discord.Game("with Elitists")


@bot.event
async def on_ready():
    print("Discord Version: " + dv)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    # for member in bot.get_all_members():
    #     print("Name: " + member.name, member.created_at, member.permissions_in)

    await bot.change_presence(status=discord.Status.do_not_disturb, activity=game)


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#
#     await message.channel.send('Hello! ' + message.author.mention)
#     user = discord.get(message.author.mention)
#     print(user)

@bot.command()
async def legendschest(ctx):
    await ctx.send("Thank you! " + ctx.author.mention + ". You have been entered into the drawing for"
                                                        " a shot at getting a **Legendary League War Chest** "
                                                        ":crgbthumbs:")
    print(ctx.author.display_name)


@bot.command()
async def rm(ctx):
    for member in bot.get_all_members():
        print(member.role)


    # if a in [role.name for role in guild.roles]:
    #     print(ctx.author.display_name)
    #     return
    # print("Bad")
    # for roles in mem.roles:
    #     if ctx == roles:
    #         print(mem.display_name)
    # await ctx.send(role.name)
    # for member in bot.get_all_members():
    #     print(member.role.name)
        # for role in member.roles:
        #     if role.name == ctx:
        #         await ctx.send(member.name)


@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)


@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there! " + ctx.author.mention)
    opt = ctx.author.display_name
    print(opt)


@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Elitists Clan Family Bot", description="Jus Chillin'", color=0xeee657)

    # give info about you here
    embed.add_field(name="Creator", value="Evo#7307")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Join Elitists!", value="https://discord.gg/TDreACq")

    await ctx.send(embed=embed)


bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee680)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('NDg5MTkzNDU0MDMxNzMyNzU5.DnnMog.zNnBv_pZFa3d-s7DmMxgxdwWcjw')

