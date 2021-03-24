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
    await message.channel.send(embed = discord.Embed(title='{} - {}'.format(choice[0], choice[1]), color=0x1ac8eb))

    if len(self.chosenIDs) == 0:
        await message.channel.send(embed = discord.Embed(title='***Nowa runda***', color=0xff0000))


async def round(self, message):
    await message.channel.send('Ilosc wylosowanych osob w tej rundzie: {}'.format(len(self.chosenIDs)))

async def reset(self, message):
    self.chosenIDs = []
    open('chosen.txt', 'w+').close()

    await message.channel.send(embed = discord.Embed(title='***Zresetowano runde***', color=0xff0000))

async def randomFact(message):
    print('Random fact sent!')
    raw_fact = BeautifulSoup(requests.get(config('FACT_URL')).content, 'html.parser')
    fact = raw_fact.find_all('p', class_='fact')[0].text

    await message.channel.send(embed = discord.Embed(title=fact, description='Via schneierfacts.com', color=0x12aa30))

async def randomCat(message):
    try:
        urllib.request.urlretrieve('https://cataas.com/cat', 'cat.jpg')
        embed = discord.Embed(color=0xff98fa)
        file = discord.File('cat.jpg', filename='cat.jpg')
        embed.set_image(url='attachment://cat.jpg')
        print('Random cat sent!')
        await message.channel.send(file=file, embed=embed)
    except:
        print('Random cat error...')
        await message.channel.send(embed = discord.Embed(title='Catto is gone :(', color=0xff0000))

async def randomDog(message):
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random').json()
        embed = discord.Embed(color=0xff98fa)
        embed.set_image(url=response['message'])
        print("Random dog sent!")
        await message.channel.send(embed=embed)
    except:
        print('Random dog error...')
        await message.channel.send(embed = discord.Embed(title='Doggo is gone :(', color=0xff0000))