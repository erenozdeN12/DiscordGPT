import discord
from discord. ext import commands
import aiohttp
import openai as ai

ai.api_key="YOUR OPENAI KEY HERE"
token = "YOUR DISCORD BOT TOKEN HERE"


bot = commands. Bot (command_prefix="$$", intents=discord.Intents.all())
@bot.event
async def on_ready():
    print ("Bot has Connected to Discord! ")
    await bot.change_presence(activity=discord.Streaming(name="STREAM IT UP!", url="https://www.twitch.tv/erenozden01"))


@bot.command ()
async def gpt(ctx: commands.Context, *, prompt: str):
    async with aiohttp.ClientSession() as session :
        payload = {
            "model":"text-davinci-003",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 50,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "best_of": 1,
        }
        headers = {"Authorization": f"Bearer {ai.api_key}"}
        async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
            resp = await resp.json()
            embed = discord.Embed(title="GPT's Answer", description=resp["choices"][0]["text"])
            await ctx.reply(embed=embed)

bot.run(token)
