import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import aiohttp

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
  print("Im Ready")


@bot.slash_command(name = "dog", description="Sends a photo of a cute dog")
async def dog(interaction: Interaction):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/animal/dog')
      dogjson = await request.json()


    embed = nextcord.Embed(title="Dog Image", color=nextcord.Colour.purple())
    embed.set_image(url=dogjson["image"])
    await interaction.response.send_message(embed=embed)
@bot.slash_command(name="cat", description="sends a cute image of cat")
async def cat(interaction: Interaction):
  request = await session.get('https://some-random-api.ml/animal/dog')
  catjson = await request.json()
  embed=nextcord.Embed(title="Cat Image", description="Sends a cute image of cat", color=nextcord.Colour.purple())
  embed.set_image(url=catjson["image"])
  await interaction.response.send_message(embed=embed)
