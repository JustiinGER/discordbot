import discord
import datetime
import random
from discord.ext import commands
from discord.ext.commands import CommandNotFound

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
                 "Ich will darüber nicht reden",
                 "Die Sterne stehen gut",
                 "Ich tendiere zu: Ja",
                 "Ich tendiere zu: Nein",
                 "Nerv mich nicht!"]
    emiesmuschel = discord.Embed(title="Magische Miesmuschel", timestamp=t.utcnow(),
                                 colour=random.randint(0, 0xffffff))
    emiesmuschel.set_thumbnail(
        url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTiHVLVXiIyGiVSYa1IZO5AMSibq8kZ4ZK2ti5YO6WMU9B_YqrL&usqp=CAU")
    emiesmuschel.add_field(name="Frage:", value=question, inline=False)
    emiesmuschel.add_field(name="Antwort:", value=random.choice(responses))
    emiesmuschel.set_footer(text="Frage angefordert von: {}".format(ctx.author.name))
    await ctx.send(embed=emiesmuschel)


@client.command(aliases=["witz", "witze"])
async def joke(ctx):
    jokes = ["Wer sitzt auf dem Baum und ruft Aha? \n Ein Uhu mit Sprachfehler!",
             "Was sagt man über einen Spanner, der gestorben ist? \n Er ist weg vom Fenster!",
             "Was macht ein Pirat am Computer? \n Er drückt die Enter-Taste.",
             "Warum steht ein Pilz im Wald? \n Weil die Tannen zapfen.",
             "Was liegt am Strand und redet undeutlich? \n Eine Nuschel.",
             "Treffen sich zwei Magneten. \n Da sagt der eine: Was soll ich heute bloß anziehen?",
             "Was ist grün und steht vor der Tür? \n Ein Klopfsalat.",
             "Was ist rot und steht im Wald? \n Ein Kirsch!",
             "Was ist ein Keks unter einem Baum? \n Ein schattiges Plätzchen.",
             "Ich habe gerade den DJ angerufen. \n Er hat aufgelegt",
             "Was macht ein Clown im Büro? \n Faxen!",
             "Wieso können Bienen so gut rechnen? \n Weil sie sich den ganzen Tag mit Summen beschäftigen.",
             "Wieso gehen Ameisen nie in die Kirche? \n Weil sie in Sekten sind!",
             "Was hat die Farbe Khaki und schwimmt in der Toilette? \n Das Klokodil!",
             "Was ist das Weiße in Vogelkacke? \n Auch Vogelkacke.",
             "Wo machen Kühe Urlaub? \n In Kuhba"]
    ejoke = discord.Embed(title="Flachwitze", timestamp=t.utcnow(),
                          colour=random.randint(0, 0xffffff))
    ejoke.set_thumbnail(
        url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/face-with-tears-of-joy_1f602.png")
    ejoke.add_field(name="Witz:", value=random.choice(jokes))
    ejoke.set_footer(text="Witz angefordert von: {}".format(ctx.author.name))
    await ctx.send(embed=ejoke)


@client.command()
async def otaku(ctx):
    number = random.randint(0, 100)
    await ctx.send(f"Du bist zu **{number}%** ein Otaku!")


@client.command()
async def lovecalc(ctx, name1, name2):
    number = random.randint(0, 100)
    await ctx.send(f"{name1} und {name2} passen zu **{number}%** zusammen!")


@client.command()
async def rich(ctx, member: discord.Member = None):
    money = random.randint(0, 10000000)
    if member is None:
        member = ctx.message.author
    else:
        member = member
    await ctx.send(f"{member} hat ein geschätztes Vermögen von **{money}€**!")


@client.command()
async def roll(ctx, upto: int = None):
    if upto is None:
        number = random.randint(0, 100)
    else:
        number = random.randint(0, upto)
    await ctx.send(f"Die Zahl lautet **{number}**")


@client.command()
async def regel(ctx, nummer: int):
    if nummer == 34:
        await ctx.send("Regel 34 besagt: Wenn es existiert, dann gibt es auch pornografische Inhalte davon.")
    else:
        await ctx.send("Diese Regel konnte ich leider nicht finden.")


@client.command()
async def kill(ctx, user: discord.User):
    possibilities = [f"**{ctx.author.name}** hat **{user.name}** mit einem Stein erschlagen.",
                     f"**{ctx.author.name}** hat **{user.name}** mit einer Schaufel erschlagen.",
                     f"**{ctx.author.name}** hat **{user.name}** mit einem Dildo zu tode penetriert."]
    ekill = discord.Embed(timestamp=t.utcnow(),
                          colour=random.randint(0, 0xffffff))
    ekill.add_field(name="Killfeed:", value=random.choice(possibilities))
    await ctx.send(embed=ekill)


@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Du musst eine Frage angeben.")


@lovecalc.error
async def lovecalc_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Du musst zwei Namen angeben!")


@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Das ist keine Zahl.")


@kill.error
async def kill_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Du hast keinen User angegeben!")


client.run(token)
