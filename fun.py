import discord
import datetime
import random
from discord.ext import commands
from discord.ext.commands import CommandNotFound

d = datetime.datetime.now()
t = datetime.datetime.now()

token = open("token.txt", "r").readline()

client = commands.Bot(command_prefix=".")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Dieser Befehl konnte nicht gefunden werden.")
        
@client.command(aliases=["8ball", "miesmuschel", "mm"])
async def _8ball(ctx, *, question):
    responses = ["Definitiv!",
                 "Ohne jegliche Zweifel!",
                 "Ja!",
                 "Es kommt drauf an",
                 "Nein!",
                 "Ganz sicher nicht!",
                 "Frag mich noch einmal in einer Stunde",
                 "Das steht noch nicht fest",
                 "Nö",
                 "Auf jeden Fall!",
                 "Vielleicht",
                 "Das ist mir zu privat",
                 "Ich will darüber nicht reden",
                 "Die Sterne stehen gut",
                 "Ich tendiere zu: Ja",
                 "Ich tendiere zu: Nein",
                 "Nerv mich nicht!"]
    emiesmuschel = discord.Embed(title="Magische Miesmuschel", timestamp=t.utcnow(),
                                 colour=random.randint(0, 0xffffff))
    emiesmuschel.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTiHVLVXiIyGiVSYa1IZO5AMSibq8kZ4ZK2ti5YO6WMU9B_YqrL&usqp=CAU")
    emiesmuschel.add_field(name="Frage:", value=question, inline=False)
    emiesmuschel.add_field(name="Antwort:", value=random.choice(responses))
    emiesmuschel.set_footer(text="Frage angefordert von: {}".format(ctx.author.name))
    await ctx.send(embed=emiesmuschel)
    
@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Du musst eine Frage angeben.")
        
client.run(token)        
