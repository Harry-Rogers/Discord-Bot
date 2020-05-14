# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:46:16 2020

@author: Harry
"""
#Use webscraper for info finding

import discord
from discord.ext import commands
import datetime 

Monday = "None"
Tuesday = "None"
Wednesday = "2am-8am"
Thursday = "None"
Friday = "2am-8am"
Saturday = "2am-8am"
Sunday = "None" 

days = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
d = datetime.datetime.now()
date = d.strftime("%A")


print(datetime.datetime.now())
print(date)

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print("Ready :)")


@client.command()
async def lincolngym(ctx):
    await ctx.send('https://www.google.com/maps/dir//Pacific+Gym,+83+Waterloo+St,+Lincoln+LN6+7AQ/@53.2228814,-0.6244766,12z/data=!4m9!4m8!1m0!1m5!1m1!1s0x48785ad664d1b4e7:0x21af33d7eea5d478!2m2!1d-0.5544378!2d53.2229019!3e0')
    await ctx.send(f'Time taken: {round(client.latency * 1000)}ms')

@client.command()
async def norwichgym(ctx):
    await ctx.send('Info here')
    await ctx.send('https://www.google.com/maps/dir/Costessey,+Norwich+NR8+5GJ,+UK/the+gym+hall+road/@52.6253585,1.1993726,13z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x47d9dfd87d6e5bf5:0x304a674954ba12c2!2m2!1d1.177951!2d52.6650417!1m5!1m1!1s0x47d9e401174c5ead:0x9a0bff303eae329!2m2!1d1.2885236!2d52.6062814')
    await ctx.send(f'Time taken: {round(client.latency * 1000)}ms')
    
    
@client.command()
async def work(ctx):
    await ctx.send("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday")
    await ctx.send(days)
    await ctx.send(datetime.datetime.now())
    await ctx.send(date)
    if date == days:
        ctx.send("Work day")
    
client.run("tokengoeshere")
