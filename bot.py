#!/usr/bin/python
import os
import discord
from phue import Bridge
import random
from dotenv import load_dotenv
import datetime
from datetime import date
import math
import requests
import random
import locale
import wikipedia
from datetime import datetime
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from tabulate import tabulate
import time
import asyncio
import openai
import speedtest
import akinator




b = Bridge('') 
lights = b.get_light_objects('id')
lights_list = b.get_light_objects()
locale.setlocale(locale.LC_ALL, '')
akinator_game = akinator.Akinator()

facts = [
    'One million Earths could fit inside the Sun – and the Sun is considered an average-size star.',
    'For years it was believed that Earth was the only planet in our solar system with liquid water. More recently, NASA revealed its strongest evidence yet that there is intermittent running water on Mars, too!',
    'Comets are leftovers from the creation of our solar system about 4.5 billion years ago – they consist of sand, ice and carbon dioxide',
    'You wouldn’t be able to walk on Jupiter, Saturn, Uranus or Neptune because they have no solid surface!',
    'If you could fly a plane to Pluto, the trip would take more than 800 years!',
    'The highest mountain known to man is on an asteroid called Vesta. Measuring a whopping 22km in height, it is three times as tall as Mount Everest!'
    'Did you know that the shortest war in history was between Zanzibar and England, and it only lasted 38 minutes?',
    'If you shuffle a deck of cards properly, chances are that exact order has never been seen before in the history of the universe.',
    'A group of flamingos is called a flamboyance.',
    'The world\'s oldest piece of chewing gum is over 9,000 years old.',
    'Pirates wore eye patches not because they had a missing eye, but to improve their night vision.',
    'A group of crows is called a murder.',
    'A cockroach can live for several weeks without its head.',
    'The first computer programmer was a woman named Ada Lovelace.',
    'A cat has 32 muscles in each ear.',
    'If you lift a kangaroo\'s tail off the ground, it can\'t hop.',
    'The longest recorded flight of a chicken is 13 seconds.',
    'There are more possible iterations of a game of chess than there are atoms in the known universe.',
    'The world\'s largest grand piano was built by a 15-year-old in New Zealand.',
    'The only letter that doesn\'t appear in any U.S. state name is \'Q\'.',
    'An ostrich\'s eye is bigger than its brain.',
    'A small child could swim through the veins of a blue whale.',
    'A group of hedgehogs is called a prickle.',
    'The oldest known creature in the world was a mollusk named Ming who lived to be 507 years old.',
    'A group of porcupines is called a prickle.',
    'A snail can sleep for 3 years.',
    'The world\'s largest snowflake on record was 15 inches wide and 8 inches thick.',
    'The oldest known living tree is over 4,800 years old.',
    'There is a species of jellyfish that is immortal.',
    'A group of ferrets is called a business.',
    'A group of rhinos is called a crash.',
    'The average person will spend six months of their life waiting for red lights to turn green.',
    'A group of kangaroos is called a mob.',
    'The world\'s largest rubber duck weighs over 27,000 pounds.',
    'A group of unicorns is called a blessing.',
    'The oldest known goldfish lived to be 43 years old.',
    'A crocodile can\'t stick its tongue out.',
    'The world\'s largest snow maze was over 7,000 square meters.',
    'The Moon is about 238,855 miles away from Earth.',
    'Venus is about 24 million miles away from Earth at its closest approach.',
    'Mars is about 33.9 million miles away from Earth at its closest approach.',
    'Jupiter is about 365 million miles away from Earth at opposition.',
    'Saturn is about 746 million miles away from Earth at opposition.',
    'Uranus is about 1.6 billion miles away from Earth at opposition.',
    'Neptune is about 2.7 billion miles away from Earth at opposition.',
    'Pluto is about 2.9 billion miles away from Earth at its closest approach.',
    'Alpha Centauri, the nearest star system to our own, is about 4.37 light-years (25.5 trillion miles away) from Earth.',
    'Betelgeuse, a red supergiant star in the constellation Orion, is about 640 light-years (3.7 quadrillion miles away)( from Earth.',
    'The Andromeda Galaxy, the nearest galaxy to our own, is about 2.5 million light-years (14.6 quintillion miles away) from Earth.'
]



ballet = [
    '**Assemblé** *(assam blay)*\n Lifting off the floor on one leg, and landing on two. Legs assemble at the same time and return to fifth position.',
    '**Grande Jeté** *(grand jeh tay)*\n A big jump from one foot to the other in which the working leg is brushed into the air and appears to have been thrown.',
    '**Plié** *(plee ay)*\n Means bent, bending - of the knee or knees.',
    '**Pirouette** *(peer o wet)*\n A rotation or spin - a complete turn of the body on one foot, on point or demi-pointe.',
    '**Tour en l`air** *(tour on lair)*\n A turn in the air - usually a male dancer`s step, although ballerinas may do them to depending on the choreography.',
    '**Arabesque** *(Ah rah besk)*\n A position on one leg with the other leg raised behind the body and extended in a straight line.',
    '**Attitude** *(ah tea tude)*\n A variation on the arabesque. The extended leg is raised behind the body but bent at the knee at an angle of 90 degrees.',
    '**Croisé** *(quo say)*\n A dancer stands with legs crossed at an angle to the audience. The disengaged leg may be crossed in the front or in the back.',
    '**Turn-out**\n The dancer turns his or her feet and legs out from the hip joints to a 90-degree position.',
    '**Battement** *(bat mahn)*\n A beating movement of the working leg. Can be done to the front, side, or back.',
    '**Chassé** *(sha say)*\n A sliding step where one foot chases the other.',
    '**Développé** *(dayv-law-pay)*\n A movement where the working leg is developed from a position to the front, side, or back.',
    '**Fouetté** *(foo-tay)*\n A turn on one foot where the working leg is whipped around.',
    '**Glissade** *(glee sahd)*\n A gliding step where one foot "slides" along the floor to meet the other foot.',
    '**Pas de bourrée** *(pah duh boo-ray)*\n A series of small, quick steps that can be done in any direction.',
    '**Pas de chat** *(pah duh shah)*\n A step where the working foot is brought up to the opposite knee before stepping onto the other foot.',
    '**Pas de deux** *(pah duh duh)*\n A dance for two people.',
    '**Petit allegro** *(puh-tee al-luh-groh)*\n A series of small, fast jumps.',
    '**Relevé** *(reh-luh-vay)*\n A rising up onto the balls of the feet.',
    '**Sauté** *(soh-tay)*\n A jump where both feet leave the floor at the same time.',
    '**Sissonne** *(sih-sohn)*\n A jump from two feet to one foot.',
    '**Battement Tendu** *(baht-mahn tahn-doo)*\n A stretched beating action of the working foot along the floor until only the toes remain touching. The foot returns to the original position.',
    '**Battement Glissé** *(baht-mahn glee-say)*\n A gliding battement where the working foot slides along the floor from a closed position to an open position and back.',
    '**Battement Fondu** *(baht-mahn fawn-dew)*\n A bending action of the supporting leg, while the working leg makes a battement tendu or other movement.',
    '**Battement Frappé** *(baht-mahn frah-pay)*\n A striking action of the working foot against the floor, typically brushing out to the front, side, or back.',
    '**En Pointe** *(awn pwan-t)*\n Dancing on the tips of the toes with special pointe shoes.',
    '**First Position** *(Première)*\n The feet turned out and heels together. The legs are straight.',
    '**Second Position** *(Deuxième)*\n The feet are turned out and apart from each other. The legs are straight.',
    '**Third Position** *(Troisième)*\n One foot is placed in front of the other with the heel touching the middle of the other foot. The legs are straight.',
    '**Fourth Position** *(Quatrième)*\n One foot is placed in front of the other, with a distance of about one foot apart. The legs are straight.',
    '**Fifth Position** *(Cinquième)*\n One foot is placed in front of the other, with the heel of the front foot touching the toe of the back foot. The legs are straight.'
]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)






@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(1087880407380410439)
    transition_time = 0 
    colors = [{'hue': 0, 'sat': 254, 'bri': 254},   # Red
          {'hue': 25500, 'sat': 254, 'bri': 254},  # Green
          {'hue': 46920, 'sat': 254, 'bri': 254}]  # Blue
    for i in range(1):
            for color in colors:
               
                b.set_light('Study', {'on': True, 'transitiontime': transition_time * 10, **color})
                time.sleep(transition_time)
    b.set_light('Study', {'on': False})      
    await channel.send('I am here to serve your electromagnetic radiation needs. As well as other things. Do **!help** to see what I can do')


    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
        
    if  in [user.id for user in message.mentions]:
        user = await client.fetch_user()
        b.set_light('Study', 'on', True)
        b.set_light('Study', {'hue': 65535, 'sat': 254, 'bri': 255})
        b.set_light('Study', 'on', False)
        b.set_light('Study', 'on', True)
        b.set_light('Study', {'hue':8402, 'sat': 140, 'bri': 64})

        await message.channel.send(f"Hey {user.mention}, {message.author.mention} just mentioned you!")

    if message.content.lower().startswith('hello'):
        if client.user.mentioned_in(message):
            await message.channel.send(f"Hello {message.author.mention}!")
    elif client.user.mentioned_in(message):
        await message.channel.send("You called?")

    if message.content.startswith('Good Bot.'):
        await message.channel.send('Thank you, {}'.format(message.author))

    if message.content.startswith('🤖'):
        await message.channel.send('Oh look, a friend!')

    if message.content.startswith('fingers and toes'):
        await message.channel.send('Fingers & Toes?! Fingers & Toes!? Robot ❤️ Fingers & Toes! YUMMY! 🤖🖖🦶')     

    if message.content.startswith('!facts'):
        random_fact = random.choice(facts)
        await message.channel.send(random_fact)

    if message.content.startswith('🩰'):
        random_ballet = random.choice(ballet)
        await message.channel.send(random_ballet)

    if message.content.startswith('🩰 all'):
        for item in ballet:
            await message.channel.send(item) 

    if message.content.startswith('!ai'):
        messagetext = message.content[3:]
        split = messagetext.split(' ')
        if len(split) > 1:
           messagetext = ' '.join(split[1:])
        await message.channel.send('You said: ' + messagetext)     

    if message.content.startswith('Who are the monkeys?'):
        await message.channel.send(' is a   🐒\n is a  🐒\n is a  🐒')

    if message.content.startswith('!cat'):
        await message.channel.send('https://i.imgur.com/5TrXF.gif')    

    if message.content.startswith('!light on'):
        b.set_light('Study', 'on', True)
        await message.channel.send('Turned on💡')

    if message.content.startswith('!light off'):
        b.set_light('Study', 'on', False)
        await message.channel.send('Turned off 💡')

    if message.content.startswith('!light dim'):
        b.set_light('Study', 'bri', 64)
        await message.channel.send('Dimmed 💡')

    if message.content.startswith('!light bright'):
        b.set_light('Study', 'bri', 255)
        await message.channel.send('Full Brightness 💡')

    if message.content.startswith('!light all off'):
        for light in lights_list:
            light.on = False
        await message.channel.send('Turned off all💡')

    if message.content.startswith('!rainbow'):
        transition_time = 3
        colors = [{'hue': 0, 'sat': 254, 'bri': 254},   # Red
          {'hue': 25500, 'sat': 254, 'bri': 254},  # Green
          {'hue': 46920, 'sat': 254, 'bri': 254}]  # Blue
        for i in range(3):
            for color in colors:
                # Set light color with transition time
                b.set_light('Study', {'on': True, 'transitiontime': transition_time * 10, **color})
                time.sleep(transition_time)
        b.set_light('Study', {'on': False})        




    if message.content.startswith('!light status'):
        rows = []
        name_max_length = max(len(light.name) for light in lights_list) 
        for light in lights_list:
            status = '🟢' if light.on else '🔴'
            rows.append([light.name.ljust(name_max_length), status]) 
        table = tabulate(rows, tablefmt='plain')
        await message.channel.send(f"```\n{table}\n```")


    if message.content.startswith('!dob'):
        dob_input = await message.channel.send(f'Hey {message.author.mention}! What is your Date of Birth? (Please enter in the format dd mm yyyy)')
        dob_message = await client.wait_for('message', check=lambda msg: msg.author == message.author)
        dob_str = dob_message.content
        dob = datetime.strptime(dob_str, '%d %m %Y')
        age = relativedelta(datetime.now(), dob)
        years = age.years
        months = age.months
        days = age.days
        weeks = days // 7
        hours = age.hours
        minutes = age.minutes
        seconds = age.seconds
        hours_since_birth = (datetime.now() - dob).total_seconds() / 3600
        seconds_since_birth = (datetime.now() - dob).total_seconds()

        current_month = datetime.now().month
        current_day = datetime.now().day
        full_moons = ((datetime.now().year - dob.year) * 12 + (current_month - dob.month)) - int(current_day >= 29.5)
        days_since_birth = (datetime.now() - dob).days
        miles_per_year = 58400000000  
        days_per_year = 365.24
        miles_around_sun = days_since_birth * 1.6e6 / 1e9  

        seconds_str = locale.format_string("%.0f", seconds_since_birth, grouping=True)

        output = (f"**{message.author}** was born on **{dob_str}**, they are **{years} years, {months} months, {weeks} weeks, {days} days, "
                  f"{hours} hours, {minutes} minutes, and {seconds} seconds old.**\n"
                  f"**{locale.format_string('%d', hours_since_birth, grouping=True)} hours** and **{seconds_str} seconds** have passed since they were born!\n"
                  f"They have seen approximately **{full_moons} full moons** in their lifetime.\n"
                  f"They have traveled approximately **{miles_around_sun:.2f} billion miles** around the Sun.\n")
        await message.channel.send(output)
        await message.channel.send('We are currently travelling at around **66,667 mph**. Please ensure your seatbelt is fastened.')

    if message.content.startswith('!moon'):
        def get_moon_phase(year, month, day):
            if month < 3:
                year -= 1
                month += 12
            A = math.floor(year / 100)
            B = 2 - A + math.floor(A / 4)
            JD = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + B - 1524.5

            phase = (JD - 2451550.1) % 29.53058867
            phase /= 29.53058867

            return phase


        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        phase = get_moon_phase(year, month, day)

        if phase < 0.0625 or phase >= 0.9375:
            phase_name = "🌑 New Moon"
            b.set_light('Study', 'on', False)
        elif phase < 0.1875:
            phase_name = "🌒 Waxing Crescent"
            b.set_light('Study', {'on': True, 'bri': 32})
        elif phase < 0.3125:
            phase_name = "🌓 First Quarter"
            b.set_light('Study', {'on': True, 'bri': 64})
        elif phase < 0.4375:
            phase_name = "🌔 Waxing Gibbous"
            b.set_light('Study', {'on': True, 'bri': 128})
        elif phase < 0.5625:
            phase_name = "🌝 Full Moon"
            b.set_light('Study', {'on': True, 'bri': 255})
        elif phase < 0.6875:
            phase_name = "🌖 Waning Gibbous"
            b.set_light('Study', {'on': True, 'bri': 128})
        elif phase < 0.8125:
            phase_name = "🌗 Last Quarter"
            b.set_light('Study', {'on': True, 'bri': 64})
        else:
            phase_name = "🌘 Waning Crescent"
            b.set_light('Study', {'on': True, 'bri': 32})
        await message.channel.send("The current Moon phase is:\n {}".format(phase_name))

    if message.content.startswith('!iss'):
        iss_response = requests.get("http://api.open-notify.org/iss-now.json")

        if iss_response.status_code == 200:
                iss_data = iss_response.json()
                latitude = iss_data["iss_position"]["latitude"]
                longitude = iss_data["iss_position"]["longitude"]

                geocode_url = f"https://api.opencagedata.com/geocode/v1/json?q={latitude}+{longitude}&key="
                geocode_response = requests.get(geocode_url)

        if geocode_response.status_code == 200:
                     geocode_data = geocode_response.json()
                     location = geocode_data["results"][0]["formatted"]
        await message.channel.send("🛰️ The ISS  is currently above:\n{}".format(location))


    if message.content.startswith('!wiki'):
        await message.channel.send('What shall I search the wikiwoo for?')
        response = await client.wait_for('message', check=lambda m: m.author == message.author, timeout=10)

        try:
            page = wikipedia.page(response.content)

            # Return the summary of the page
            await message.channel.send(f"Here's what I found on Wikipedia: {page.title}\n{page.url}")
        
        except wikipedia.exceptions.PageError:
            await message.channel.send(f'Sorry, I could not find a page for "{response.content}".')

    if message.content.startswith('!light morse'):
        morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'}
        user_input = message.content.split('!light morse ')[1].upper()
        morse_code = ''

        for letter in user_input:
            morse_code += morse_dict.get(letter, '') + ' '
        for char in morse_code:
            if char == ".":
                b.set_light(7, 'on', True, transitiontime=0)
                time.sleep(0.2)
                b.set_light(7, 'on', False, transitiontime=0)
                time.sleep(0.2)
            elif char == "-":
                b.set_light(7, 'on', True, transitiontime=0)
                time.sleep(0.6)
                b.set_light(7, 'on', False, transitiontime=0)
                time.sleep(0.2)
            else:
                time.sleep(0.4)
        await message.channel.send(morse_code)

    if message.content.startswith('!weather'):
        api_key = ""
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": "Gloucester,UK",
            "units": "metric",
            "appid": api_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
        await message.channel.send(f"Current weather in Gloucester, UK:\n"
          f"{data['weather'][0]['description'].capitalize()}, \n"
          f"🌡️ {data['main']['temp']}°C\n"
          f"🥵 Humidity {data['main']['humidity']}%\n"
          f"🍃 Wind {data['wind']['speed']} m/s")


    if message.content.startswith('!mood'):
        await message.channel.send(f'Hello {message.author.mention}, let\'s see your mood. Click the icon below...')
        
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in ['😊', '😔']

        try:
            reaction_emojis = ['😊', '😔']
            async for mood_msg in message.channel.history(limit=1):
                for emoji in reaction_emojis:
                    await mood_msg.add_reaction(emoji)

            reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)

            if str(reaction.emoji) == '😊':
                await message.channel.send('You are happy!')
            elif str(reaction.emoji) == '😔':
                await message.channel.send('You are sad!')
        except asyncio.TimeoutError:
            await message.channel.send('Timeout. Please try again.')

    if message.content.startswith('!gpt'):
        openai.api_key = ""
        model_engine = "text-davinci-002"
        def chat(prompt):
            response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            message = response.choices[0].text.strip()
            return message
    
        prompt = message.content[4:]
        response = chat(prompt)
        chunks = [response[i:i+1990] for i in range(0, len(response), 1990)]
        for chunk in chunks:
            await message.channel.send(f"```{chunk}```")

    if message.content.startswith('!speed'):
        await message.channel.send('Starting test...')
        st = speedtest.Speedtest(secure=True)
        closest_server = st.get_best_server()
        download_speed = st.download()
        upload_speed = st.upload()
        ping_time = st.results.ping
        download_speed_mbps = round(download_speed / (10**6), 2)
        upload_speed_mbps = round(upload_speed / (10**6), 2)
        message_text = (
            "```Server: {}\n"
            "Download speed: {} Mbps\n"
            "Upload speed: {} Mbps\n"
            "Latency (ping time): {} ms\n```"
        ).format(
            closest_server['host'],
            download_speed_mbps,
            upload_speed_mbps,
            ping_time,
        )
        await message.channel.send(message_text)

    if message.content.startswith('!ak'):
        await message.channel.send("Let's start a new game! Think of a real or fictional character and I'll try to guess who it is.")
        await message.channel.send("Please reply 'Yes' , No' , 'idk', 'probably' or 'probably not'")
        akinator_game.start_game()

        question = akinator_game.question
        await message.channel.send(question)

        while akinator_game.progression <= 80:
            def check(m):
                return m.author == message.author and m.channel == message.channel

            try:
                answer = await client.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                await message.channel.send("Sorry, you took too long to answer!")
                return

            if answer.content.lower() == 'b':
                question = akinator_game.back()
                akinator_game.progression -= 1 
            else:
                question = akinator_game.answer(answer.content.lower())
                akinator_game.progression += 1 

            if akinator_game.progression >= 80:
                guess = akinator_game.win()
                await message.channel.send("My final guess is:")
                await message.channel.send(f"{guess['name']} ({guess['description']})")

                try:
                    answer = await client.wait_for('message', timeout=30.0, check=check)
                except asyncio.TimeoutError:
                    await message.channel.send("Sorry, you took too long to answer!")
                    return

                if answer.content.lower() == 'yes':
                    await message.channel.send("I win! Thanks for playing.")
                else:
                    await message.channel.send("I give up. Better luck next time!")

            else:
                await message.channel.send(question)




          
   
    if message.content.startswith('!help'):
        embedVar = discord.Embed(title="Hello Friend. I am HueBot.", description="The following commands are currently supported:", color=0x00ff00)
        embedVar.add_field(name="Turn 💡 On", value="!light on", inline=True)
        embedVar.add_field(name="Turn 💡 Off", value="!light off", inline=True)
        embedVar.add_field(name="Dim 💡", value="!light dim", inline=True)
        embedVar.add_field(name="Bright 💡", value="!light bright", inline=True)
        embedVar.add_field(name="Turn off all 💡", value="!light all off", inline=True)
        embedVar.add_field(name="See the status of all 💡", value="!light status", inline=True )
        embedVar.add_field(name="Morse Code 💡", value="!light morse *word*", inline=True)
        embedVar.add_field(name="Show current moon phase 🌒", value="!moon", inline=False)
        embedVar.add_field(name="Show current location of the ISS 🛰️", value="!iss", inline=False)
        embedVar.add_field(name="Show current weather 🌦️", value="!weather", inline=False)
        embedVar.add_field(name="The best 😹 gif ever", value="!cat", inline=False)
        embedVar.add_field(name="Stats based on your date of birth", value="!dob", inline=False)
        embedVar.add_field(name="Search Wikipedia for the term provided 📖", value="!wiki", inline=False)
        embedVar.add_field(name="Tell me your mood", value="!mood", inline=False)
        embedVar.set_author(name="HueBot", url="https://tutemwesi.com", icon_url="https://i.imgur.com/MxlRE7P.png")
        embedVar.set_footer(text="It has been a pleasure serving your electromagnetic radiation needs.\nThis command was requested by: {}".format(message.author))
        await message.channel.send(embed=embedVar)


client.run(TOKEN)
