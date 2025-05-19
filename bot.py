import discord
from discord.ext import commands
import asyncio
import textwrap
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

@bot.command()
async def dm(ctx, *, message: str):
    await asyncio.sleep(10)
    try:
        messages_to_send = textwrap.wrap(message, 145)
        counter = 0
        for chunk in reversed(messages_to_send):
            await asyncio.sleep(5)
            await ctx.author.send(chunk)
            await asyncio.sleep(5)
            await ctx.author.send(chunk)
            if counter == 4:
                await asyncio.sleep(480)
            elif counter == 9:
                await asyncio.sleep(360)
            counter += 1
    except discord.Forbidden:
        await ctx.send('Nie mogę wysłać wiadomości prywatnej (masz je zablokowane).')

@bot.command()
async def dm2(ctx, *, message: str):
    await asyncio.sleep(1320)
    try:
        messages_to_send = textwrap.wrap(message, 145)
        counter = 1
        for chunk in reversed(messages_to_send):
            await asyncio.sleep(5)
            await ctx.author.send(chunk)
            await asyncio.sleep(5)
            await ctx.author.send(chunk)
            if counter % 5 == 0:
                await asyncio.sleep(360)
            counter += 1
    except discord.Forbidden:
        await ctx.send('Nie mogę wysłać wiadomości prywatnej (masz je zablokowane).')

bot.run(os.getenv("DISCORD_TOKEN"))
