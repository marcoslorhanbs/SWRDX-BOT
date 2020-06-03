import discord
#url = 'https://discord.com/api/oauth2/authorize?client_id=713697581087195197&permissions=8&scope=bot'
from discord.ext import commands
import MakePontos
import time
UserId = ""
#definir classe
class comando(commands.Cog):
    def __init__(self, client):
        self.client = client
#=======Comandos:

    #====== !ajuda
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def ajuda(self, ctx):
        await ctx.send("Precisa de Ajuda? Permita-me ajudar. \n Lista de comandos:  \n `!ajuda !aram !joinAram !regras !pointer` ")
        await ctx.send("É Recomendado que todos se cadastrem no Pointer(!pointer + @usuario) pois receberão recompensas, por participar da comunidade")

    #====== !aram
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def aram(self, ctx):
        await ctx.send("**!ATENÇÃO!** @everyone \n Um Jogador esta buscando uma partida ARAM!")
    #===== !joinAran @username
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def joinAram(self, ctx, *, usuario:discord.Member=None):
        if (usuario is None):
            await ctx.send("!joinAram + @usuario")
            return
        username = usuario.name
        embed=discord.Embed(title="Buscador de Partida Aram", url="https://images4.alphacoders.com/909/thumb-1920-909912.png", description="Para Entrar no Grupo: !joinAramP(numero do jogador) @username")
        embed.set_author(name=username, url="https://cdn.discordapp.com/app-icons/713697581087195197/dabbaff9bccdd718e29c70791556b9af.png", icon_url="https://cdn.discordapp.com/app-icons/713697581087195197/dabbaff9bccdd718e29c70791556b9af.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/713697581087195197/dabbaff9bccdd718e29c70791556b9af.png")
        embed.add_field(name="Jogador1:", value=username, inline=True)
        embed.add_field(name="Jogador2:", value="Player2", inline=True)
        embed.add_field(name="Jogador3:", value="Player3", inline=True)
        embed.add_field(name="Jogador4:", value="Player4", inline=True)
        embed.add_field(name="Jogador5:", value="Player5", inline=True)
        embed.set_footer(text="Para Sair da Busca digite: !StopAram @username")
        await ctx.send(embed=embed)
        
    #===== !Regras
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def regras(self, ctx):
        embed=discord.Embed(title="Regras", description="Regras para manter a comunidade organizada.")
        #embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/713697581087195197/dabbaff9bccdd718e29c70791556b9af.png")
        embed.add_field(name="**Fica Proibido o uso de comentarios:**", value="Racistas \n LGBTQFobicos \n Machistas \n Xingamentos", inline=True)
        embed.add_field(name="**Fica Proibido o uso de:**", value="Links(Exceto Spotfy) \n imagens fora de Contexto(nudez, aleatoriedade, camera...) \n Videos(exceto in game) \n Emotes com duplo sentido", inline=True)
        embed.set_footer(text="Esperamos que a comunidade prospere, para isso contamos com você \n ou o minion(bot) vai brigar com você")
        await ctx.send(embed=embed)

    #===== !Garen
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def garen(self, ctx):
        embed=discord.Embed(title="Garen", description="Um guerreiro nobre e orgulhoso, Garen faz parte da Vanguarda Destemida.")
        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/leagueoflegends/images/9/97/Garen_OriginalSquare.png")
        embed.add_field(name="**Runas:**", value="Precisão + Determinação", inline=True)
        embed.add_field(name="**Habilidades:**", value="**Q:** Ataque... **W:** Escudo + Vel **E:** Bayblade **R:** Ult",inline=True)
        embed.add_field(name="**Lanes:**", value="TOP, JG, ADC", inline=True)
        embed.set_footer(text="Popular entre seus companheiros e respeitado o suficiente por seus inimigos")
        await ctx.send(embed=embed)

    #===== !SWRDX
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def swrdx(self, ctx):
        await ctx.send("Para Participar da SWRDX você deve ter o cargo de **Comunitario**")
        await ctx.send("Para obter o cargo de comunitario basta dedicar mais tempo na comunidade.")
        await ctx.send("**Como?** Jogando, batendo papo, participando das lives. E Então observar o seu **!pointer @username**")
        await ctx.send("quando seu pointer chegar á **100** você irá ganhar o cargo de Comunitario!")
        await ctx.send("Todos os usuarios que tiverem o cargo comunitario irão ser analisados e convidados para o clube.")
        await ctx.send("Uma Mensagem será enviada para seu inbox pedindo seu nickname")
    #===== !Pointer
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def pointer(self, ctx, *, usuario:discord.Member=None):
        if (usuario is None):
            await ctx.send("!pointer + @usuario")
            return
        username = usuario.name
        MakePontos.cursor.execute(""" SELECT * FROM pontuation """)
        showall = MakePontos.cursor.fetchall()
        MakePontos.cursor.execute("""
        SELECT id FROM pontuation
        WHERE username = ?
        """, (username,))
        oldIde = MakePontos.cursor.fetchone()
        ide = oldIde
        print(ide)
        if(ide is not None):
            ide = oldIde[0]
            MakePontos.cursor.execute(f""" SELECT pontos FROM pontuation WHERE id = {ide} """)
            Getpontos = MakePontos.cursor.fetchone()
            pontos = Getpontos[0]
            import testeHora
            if(testeHora.ended == 0):
                addPontos = pontos + 20
                MakePontos.cursor.execute(f""" UPDATE pontuation SET pontos = ? WHERE id = ? """, (addPontos, ide))
                MakePontos.conn.commit()
                MakePontos.cursor.execute(f""" SELECT pontos FROM pontuation WHERE id = {ide} """)
                Getpontos = MakePontos.cursor.fetchone()
                pontos = Getpontos[0]
                testeHora.cont = 10
                testeHora.ended = 10
                testeHora.Run()
            #print(f"Funcionou CARALHO {username} voce tem {pontos} pontos")
            await ctx.send(f"Olá **{username}**, você tem **{pontos}** pontos!")
        elif(ide is None):
            MakePontos.cursor.execute("""
            INSERT INTO pontuation(username, pontos)
            VALUES(?,?)
            """, (username, 10))
            MakePontos.conn.commit()
            #print(f"Funcionou Porra {username} voce foi cadastrado")
            await ctx.send(f"Parabéns **{username}**, você recebeu **10 pontos** por se cadastrar no pointer")
    #===== !Loja
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def loja(self, ctx, *, usuario:discord.Member=None):
        if(usuario is None):
            await ctx.send("!loja + @usuario")
        username = usuario.name
        try:
            global UserId
            MakePontos.cursor.execute(""" SELECT id FROM pontuation WHERE username = ? """, (username, ))
            identifier = MakePontos.cursor.fetchone()
            print(identifier)
            UserId = identifier[0]
            print(UserId)
        except:
            await ctx.send("Ops, houve um erro, certifique-se de estar cadastrado no pointer!")

        embed=discord.Embed(title="Loja", description="Produtos para usar na comunidade")
        #embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/713697581087195197/dabbaff9bccdd718e29c70791556b9af.png")
        embed.add_field(name="**Cargos:**", value="1 - Comunitário [1] \n 2 - Criador de Memes[120]", inline=True)
        embed.add_field(name="**In Game LOL**", value="3 - Entrar no clube SWRDX (DIRETO) [200]", inline=True)
        embed.set_footer(text="[] = Preço. \n Para Comprar qualquer um destes itens utilizando seus points basta digitar **!buy IDdoItem**")
        await ctx.send(embed=embed)
    #===== !Buy
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def buy(self, ctx, *, item=None):
        if (item is None):
            await ctx.send("!buy itemID")
        MakePontos.cursor.execute(f""" SELECT pontos FROM pontuation WHERE id = {UserId} """)
        GetPontuacao = MakePontos.cursor.fetchone()
        ActualPoints = GetPontuacao[0]
        if(item == '1'):
            if(ActualPoints >= 1):
                ActualPoints -= 1
                MakePontos.cursor.execute(f""" UPDATE pontuation SET pontos = ? WHERE id = ? """, (ActualPoints, UserId))
                MakePontos.conn.commit()
                MakePontos.cursor.execute(f""" SELECT pontos FROM pontuation WHERE id = {UserId} """)
                GetPontuacao = MakePontos.cursor.fetchone()
                ActualPoints = GetPontuacao[0]
                await ctx.send(f"Item de ID: {item} Comprado! \n Novo Saldo: {ActualPoints}")
                await ctx.send(f"Parabéns, você agora é um Comunitário.")
            else:
                await ctx.send(f"Ops, você nao tem pontos suficientes. \n Seus Pontos: {ActualPoints}")
        elif(item == '2'):
            ActualPoints -= 120
        elif(item == '3'):
            ActualPoints -= 200
                
            
def setup(client):
    client.add_cog(comando(client))