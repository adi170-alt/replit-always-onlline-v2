import discord
from discord.ext import commands, tasks
import colorama
from colorama import Fore
import asyncio
import keep_alive
from asyncio import sleep
import datetime

import os

#-----SETUP-----#

keep_alive.keep_alive()
prefix = "$$"
#use the .env feature to hide your token

presence1 = "Hi!"
presence2 = "Nice to meet you!"
presence3 = "I'm Iblis#1069"
presence4 = "so"
presence5 = "ehmmm"
presence6 = "Bye I guess?"
presence7 = "..."
presence8 = "Never gonna give you up!"

now = datetime.datetime.now()
presencetime = (now.strftime("it is %H:%M , %Y-%m-%d (utc 0)"))

token = os.getenv("TOKEN")
#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)


async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=presencetime))
        await asyncio.sleep(60)
        #await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=presence1))
        #await asyncio.sleep(3)
        #await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=presence2))
        #await asyncio.sleep(3)
        #await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=presence3))
        #await asyncio.sleep(3)
        #await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=presence4))
        #await asyncio.sleep(3)
        #await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=presence5))
        #await asyncio.sleep(3)
        #await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=presence6))
        #await asyncio.sleep(3)
        #await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=presence7))
        #await asyncio.sleep(3)
        #await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=presence8))
        #await asyncio.sleep(2)


@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)

@bot.event
async def on_ready():
  bot.loop.create_task(status_task())
  # activity = discord.Game(name="Iblis#1069", type=4)
  # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Iblis#1069"))
  # await bot.change_presence(status=discord.Status.idle, activity=activity)
  # activity = discord.status(status=discord.Status.idle, activity=activity)
  print(f'''{Fore.RED}

 ______     __         __     __     ______     __  __     ______    
/\  __ \   /\ \       /\ \  _ \ \   /\  __ \   /\ \_\ \   /\  ___\   
\ \  __ \  \ \ \____  \ \ \/ ".\ \  \ \  __ \  \ \____ \  \ \___  \  
 \ \_\ \_\  \ \_____\  \ \__/".~\_\  \ \_\ \_\  \/\_____\  \/\_____\ 
  \/_/\/_/   \/_____/   \/_/   \/_/   \/_/\/_/   \/_____/   \/_____/ 
                                                                     
{Fore.GREEN}

  ______     __   __     __         __         __     __   __     ______    
 /\  __ \   /\ "-.\ \   /\ \       /\ \       /\ \   /\ "-.\ \   /\  ___\   
 \ \ \/\ \  \ \ \-.  \  \ \ \____  \ \ \____  \ \ \  \ \ \-.  \  \ \  __\   
  \ \_____\  \ \_\ \"\_\  \ \_____\  \ \_____\  \ \_\  \ \_\ \"\_\  \ \_____\  Made by AdrianOstrowski2
   \/_____/   \/_/ \/_/   \/_____/   \/_____/   \/_/   \/_/ \/_/   \/_____/  Aka adi1708
                                                                           

Your acount/bot Is now onlline!
''')

  print('------')
  print('Logged in as:')
  print(bot.user.name)
  print(bot.user.id)
  print('------')

bot.run(token, bot=False)

