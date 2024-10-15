import discord
import os
import requests

from discord.ext import commands

# Token de autenticación del bot de Discord
TOKEN = 'agregarTOKEN'

# Intents requeridos para el bot
intents = discord.Intents.default()

# Prefijo de los comandos
bot = commands.Bot(command_prefix='!', intents=intents)

# Comando para obtener el tiempo meteorológico de Chile
@bot.command(name='tiempo')
async def weather(ctx):
    url = 'https://www.el-tiempo.net/api/json/v2/provincias/08/municipios/08219'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['state']['sky']
        temp = data['state']['temperature']
        humidity = data['state']['humidity']
        
        message = f'El tiempo en Santiago, Chile es: {weather_desc}, Temperatura: {temp}°C, Humedad: {humidity}%'
    else:
        message = 'No se pudo obtener la información meteorológica'
    
    await ctx.send(message)

# Evento de inicio del bot
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Evento para escuchar todos los mensajes y responder a los comandos
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('!'):
        await bot.process_commands(message)

# Conectar el bot a Discord
bot.run(TOKEN)