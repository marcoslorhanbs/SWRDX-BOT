import discord
#url = 'https://discord.com/api/oauth2/authorize?client_id=713697581087195197&permissions=8&scope=bot'
from discord.ext.commands import AutoShardedBot, when_mentioned_or

#evento de modulos
modulos = ["comando"]

#evento do client
client = AutoShardedBot(command_prefix="!", case_insensitive=True)

#evento do on_ready
@client.event
async def on_ready():
    print(f"{client.user.name} Online.")

#Carrear modulos e token
if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)
    
    client.run("NzEzNjk3NTgxMDg3MTk1MTk3.Xsj8fA.jnbczjV2L9uHDJ3DQvVwRbXdUBM")