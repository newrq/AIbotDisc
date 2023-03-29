import disnake
from disnake.ext import commands
import openai

token = 'TOKEN'
bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())
serverGuild = [servId]
openai.api_key = "API_KEY"


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
async def askai(message: disnake.CommandInteraction, userniput: str,):
    print(f"{message.user}")
    await bot.get_channel(1075880230989860925).send("Ответ:")
    aiText = openai.Completion.create(
        model="text-davinci-003",
        prompt=userniput
        ,
        max_tokens=2340,
        temperature=1
    )
    await message.send(aiText['choices'][0]['text'])

bot.run(token)
