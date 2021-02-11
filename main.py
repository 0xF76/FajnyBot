import discord
import json
from decouple import config

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

        # Get chosen IDs from saved file
        self.chosenIDs = open('chosen.txt', 'r+').read().split(" ")
        self.chosenIDs.pop()

    async def on_message(self, message):
        if message.author == self.user:
            return

        elif message.content.startswith('$losuj') or message.content.startswith('$pseudolosuj'):
            msg = message.content
            if (msg.startswith('$losuj')):
                msg = msg[len('$losuj'):]
            else:
                msg = msg[len('$pseudolosuj'):]

            try:
                amount = int(msg)
            except ValueError: 
                amount = 1
            
            for _ in range(amount):
                await message_handlers.selectStudent(self, message)
        
        elif message.content.startswith('$fact'):
            await message_handlers.randomFact(message)

        elif message.content.startswith('$cat'):
            await message_handlers.randomCat(message)

client = Client()
client.run(config('BOT_TOKEN'))
