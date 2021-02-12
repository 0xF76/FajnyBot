# FajnyBot
> FajnyBot is a bot written with [discord.py]((https://discordpy.readthedocs.io/en/latest/index.html#)) for math classes in 1st High School in Kraków.

## 🛰️ Technology:
- [discord.py](https://discordpy.readthedocs.io/en/latest/index.html#)
- [random](https://docs.python.org/3/library/random.html)
- [json](https://docs.python.org/3/library/json.html)
- [requests](https://pypi.org/project/requests/)
- [bs4](https://pypi.org/project/beautifulsoup4/)
- [urllib3](https://pypi.org/project/urllib3/)

## 🚀 Getting started
```
$ git clone git@github.com:0xF76/FajnyBot.git
$ cd FajnyBot
$ pip install -r requirements.txt
```
After installation finishes You can use `python3 main.py` to start the bot

## ⚙️ Configuration
Rename `data.json.example` to `data.json` and fill out the values:
```json
{
    "1": "Name Surname",
    "2": "Name Surname",
    .
    .
    .
    "n": "Name Surname"
}
```
For numbers with no assigned student, enter `"x": null`.


Rename `.env.example` to `.env` and fill out the file:
```env
BOT_TOKEN=<BOT_TOKEN>
```
In order to get bot token see [Discord Developers Documentation](https://discord.com/developers/docs/intro)

## 📋 Available commands
* 🎲 pick random person from `data.json`\
`$losuj <amount, default is 1>`
* 📰 random fact\
`$fact`
* 🐱 random cat image\
`$cat`
* 🐶 random dog image\
`$dog`
