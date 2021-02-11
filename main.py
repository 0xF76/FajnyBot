import discord
import random
import json
import requests
from bs4 import BeautifulSoup
import urllib.request

FACT_URL = 'https://www.schneierfacts.com/'

from decouple import config

class Client(discord.Client):
    data = {}
    chosenIDs = []

    async def on_ready(self):
        print('Logged on as {}!'.format(self.user))

        dataFromFile = json.load(open('data.json'))
        self.data = {
            key: dataFromFile[key]
            for key in dataFromFile
            if dataFromFile[key] != None
        }

    async def on_message(self, message):
        if message.author == self.user:
            return

        elif message.content.startswith('$losuj') or message.content.startswith('$pseudolosuj'):
            notChosen = {
                key: self.data[key]
                for key in self.data
                if key not in self.chosenIDs
            }

            chosen = random.choice(list(notChosen.items()))
            if (len(self.chosenIDs) < len(self.data)):
                self.chosenIDs.append(chosen[0])
            else:
                self.chosenIDs = []

            print('{} - {}'.format(chosen[0], chosen[1]))
            await message.channel.send(embed = discord.Embed(title=chosen[1], color=0x1ac8eb))
        
        elif message.content.startswith('$fact'):
            print('Random fact sent!')
            raw_fact = BeautifulSoup(requests.get(FACT_URL).content, 'html.parser')
            fact = raw_fact.find_all('p', class_='fact')[0].text

            await message.channel.send(embed = discord.Embed(title=fact, description='Via schneierfacts.com', color=0x12aa30))

        elif message.content.startswith('$cat'):
            print('Random cat sent!')
            urllib.request.urlretrieve("https://cataas.com/cat", "cat.jpg")
            embed = discord.Embed(color=0xff98fa)
            file = discord.File('cat.jpg', filename='cat.jpg')
            embed.set_image(url='attachment://cat.jpg')
            await message.channel.send(file=file, embed=embed)
client = Client()
client.run(config('BOT_TOKEN'))