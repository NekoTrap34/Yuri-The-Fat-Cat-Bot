# Import
import os
import discord
from discord.ext import commands
import youtube_dl

client = discord.Client(command_prefix="!")

@client.event
async def on_ready():
  print("Yeah yeah fuck you, meow")

# When a certain word is used, the bot will respond to that user
@client.event
async def on_message(message):
  # Meow
  if message.content.startswith("meow"):
    await message.channel.send("Fuck you, give me food")

  if message.content.startswith("Meow"):
    await message.channel.send("GIMME FOOD")

  # Door
  if message.content.startswith("door"):
    await message.channel.send("please let me in")

  if message.content.startswith("Door"):
    await message.channel.send("LET ME IN!!!!!!!!!! PLEASE!!!!!!!")

  # Food
  if message.content.startswith("food"):
    await message.channel.send("Gib food")

  if message.content.startswith("Food"):
    await message.channel.send("Yes, NOW!")

  # Wall
  if message.content.startswith("walls"):
    await message.channel.send("I'm in your walls")

  if message.content.startswith("wall"):
    await message.channel.send("I'm in your wall!!")

  if message.content.startswith("Walls"):
    await message.channel.send("Sorry I just broke in")
  
  if message.content.startswith("Wall"):
    await message.channel.send("It's broken")

  # Yuri
  if message.content.startswith("yuri"):
    await message.channel.send("yes")
  
  if message.content.startswith("Yuri"):
    await message.channel.send("Yes")

  # Huey
  if message.content.startswith("Huey"):
    await message.channel.send("Fuck you")
  
  if message.content.startswith("huey"):
    await message.channel.send("fuck you")

client = commands.Bot(command_prefix="!")

# !play
@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

# !leave
@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

# !pause
@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")

# !resume
@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

my_secret = os.environ['BOT_TOKEN']
client.run(my_secret)