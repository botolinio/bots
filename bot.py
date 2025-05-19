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
        await ctx.author.send(f'{message}')
        messages_to_send = textwrap.wrap(message, 145)
        for chunk in reversed(messages_to_send):
            await asyncio.sleep(5)
            await ctx.author.send(chunk)
    except discord.Forbidden:
        await ctx.send('Nie mogę wysłać wiadomości prywatnej (masz je zablokowane).')

bot.run(os.getenv("DISCORD_TOKEN"))
