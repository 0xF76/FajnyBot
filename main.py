import discord
import json
from decouple import config
import re

import message_handlers

class Client(discord.Client):
    data = {}
    chosenIDs = []

    async def on_ready(self):
        print('Logged on as {}!'.format(self.user))

        # Get students
        dataFromFile = json.load(open('data.json'))
        self.data = {
            key: dataFromFile[key]
            for key in dataFromFile
            if dataFromFile[key] != None
        }

        open('chosen.txt', 'a+').close()

        # Get chosen IDs from saved file
        self.chosenIDs = open('chosen.txt', 'r').read().split(' ')
        self.chosenIDs.pop()

    async def on_message(self, message):
        if message.author == self.user:
            return

        if re.match('^\$l(|[osuj]{4})[\s]*\d*$', message.content): # If the intend is to select a student
            amount = message.content[re.search('^\$l[losuj]*\s*', message.content).span()[1]:]
            try:
                amount = int(amount)
            except ValueError: 
                amount = 1
            
            for _ in range(amount):
                await message_handlers.selectStudent(self, message)
        
        elif message.content.startswith('$round'):
            await message_handlers.round(self, message)
        
        elif message.content.startswith('$reset'):
            await message_handlers.reset(self, message)

        elif message.content.startswith('$fact'):
            await message_handlers.randomFact(message)

        elif message.content.startswith('$cat') or message.content.startswith('$pussy'):
            await message_handlers.randomCat(message)
        
        elif message.content.startswith("$dog") or message.content.startswith('$doggo'):
            await message_handlers.randomDog(message)

client = Client()
client.run(config('BOT_TOKEN'))
