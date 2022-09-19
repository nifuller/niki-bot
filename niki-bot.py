from email import contentmanager, message
from http import server
from types import MemberDescriptorType
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

channel_name = "✅subathon-check-in"
bot.message_id = 0

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def start(ctx):
    sent_message = await ctx.send("SUBATHON CHECKIN")
    emoji = '✅'
    await sent_message.add_reaction(emoji)
    bot.message_id = sent_message.id


@bot.command()
async def run(ctx):
    channel = discord.utils.get(ctx.guild.channels, name=channel_name)
    message = await channel.fetch_message(bot.message_id)
    users = set()

    for reaction in message.reactions:
        async for user in reaction.users():
            users.add(user)
    
    with open('list-of-users.txt', 'a') as fp:
        for names in users:
            fp.write("%s\n" % names)
    print("DONE OUTPUTTING")

token = os.getenv("token")
bot.run(token)