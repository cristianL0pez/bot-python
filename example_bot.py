#importamos libreria
import discord
#definimos client como el cliente de la libreria
client = discord.Client()


#cargamos evento y esperamos el onready para iniciar el bot  e imprimimos
@client.event
async def on_ready():
    print('Estamos Logeados!!{0.user}'.format(client))
#el async esperara el message  si el autor es igual que el cliente retorna ? 
@client.event
async def on_message(message):
    if message.author ==client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send('wena wena')

client.run('OTM3NDYwNzA4OTY5NDMxMTIw.YfcEUg.mTa7BWodqMgAW7lBXvXYJySGWYM')
