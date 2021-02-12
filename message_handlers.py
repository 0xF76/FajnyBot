import discord
import random
import requests
from bs4 import BeautifulSoup
from decouple import config
import urllib.request

async def selectStudent(self, message):
    notChosen = {
        key: self.data[key]
        for key in self.data
        if key not in self.chosenIDs
    }
    choice = random.choice(list(notChosen.items()))
    chosenFile = open('chosen.txt', 'a')
    
    if (len(self.chosenIDs) + 1 < len(self.data)):
        self.chosenIDs.append(choice[0])
        chosenFile.write('{} '.format(choice[0]))
    else:
        self.chosenIDs = []
        chosenFile.seek(0)
        chosenFile.truncate()

    chosenFile.close()
    print('{} - {}'.format(choice[0], choice[1]))
    await message.channel.send(embed = discord.Embed(title=choice[1], color=0x1ac8eb))

async def randomFact(message):
    print('Random fact sent!')
    raw_fact = BeautifulSoup(requests.get(config('FACT_URL')).content, 'html.parser')
    fact = raw_fact.find_all('p', class_='fact')[0].text

    await message.channel.send(embed = discord.Embed(title=fact, description='Via schneierfacts.com', color=0x12aa30))

async def randomCat(message):
    print('Random cat sent!')
    urllib.request.urlretrieve('https://cataas.com/cat', 'cat.jpg')
    embed = discord.Embed(color=0xff98fa)
    file = discord.File('cat.jpg', filename='cat.jpg')
    embed.set_image(url='attachment://cat.jpg')
    await message.channel.send(file=file, embed=embed)