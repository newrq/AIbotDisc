import disnake
from disnake.ext import commands
import openai

token = 'token'
bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())
serverGuild = [1041342566773309461]
openai.api_key = "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"


@bot.event
async def on_ready():
    print("Bot is ready")


@bot.slash_command(name="hello", description="Выводит привет с твоим иминем", guild_ids=[1041342566773309461])
async def hello(message: disnake.CommandInteraction, name: str):
    await message.send(f"ПРИВЕТ {name} !!!")


@bot.event
async def on_message(message: disnake.InteractionMessage):
    if "lol" in message.content.lower():
        await message.add_reaction("🤡")


@bot.slash_command(name="ai", description="Спросить аи что-то.", guild_ids=[1041342566773309461])
async def askAI(message, userniput: str):
    await message.send("Генерирую...")
    aiText = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userniput}
        ],
        max_tokens=2340,
        temperature=1
    )
    await message.send(aiText['choices'][0]['message']['content'])


bot.run(token)
