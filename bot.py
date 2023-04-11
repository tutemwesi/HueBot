#!/usr/bin/python
import os
import discord
from phue import Bridge
import random
from dotenv import load_dotenv
import datetime
import math

b = Bridge('') 
lights = b.get_light_objects('id')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def get_moon_phase(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    A = math.floor(year / 100)
    B = 2 - A + math.floor(A / 4)
    JD = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + B - 1524.5

    age_days = JD - 2451550.1
    if age_days < 0:
        age_days += 29.53

    phase = (age_days / 29.53) % 1

    return phase

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

phase = get_moon_phase(year, month, day)

if phase < 0.125 or phase >= 0.875:
    phase_name = "🌑 New Moon"
elif phase < 0.25:
    phase_name = "🌒 Waxing Crescent"
elif phase < 0.375:
    phase_name = "🌓 First Quarter"
elif phase < 0.5:
    phase_name = "🌔 Waxing Gibbous"
elif phase < 0.625:
    phase_name = "🌝 Full Moon"
elif phase < 0.75:
    phase_name = "🌖 Waning Gibbous"
elif phase < 0.875:
    phase_name = "🌗 Last Quarter"
else:
    phase_name = "🌘 Waning Crescent"

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!light on'):
        b.set_light('Study', 'on', True)
        await message.channel.send('Turned on💡')

    if message.content.startswith('!light off'):
        b.set_light('Study', 'on', False)
        await message.channel.send('Turned off 💡')

    if message.content.startswith('!moon'):
        await message.channel.send("The current Moon phase is: {}".format(phase_name))    
   
    if message.content.startswith('!help'):
        embedVar = discord.Embed(title="Hello Friend. I am HueBot.", description="The following commands are currently supported:", color=0x00ff00)
        embedVar.add_field(name="Turn 💡 On", value="!light on", inline=True)
        embedVar.add_field(name="Turn 💡 Off", value="!light off", inline=True)
        embedVar.add_field(name="Show current moon phase", value="!moon", inline=False)
        embedVar.set_author(name="HueBot", url="https://tutemwesi.com", icon_url="https://i.imgur.com/MxlRE7P.png")
        embedVar.set_footer(text="It has been a pleasure serving your electromagnetic radiation needs.\nThis command was requested by: {}".format(message.author))
        await message.channel.send(embed=embedVar)


client.run(TOKEN)
