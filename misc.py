import datetime
import random
from discord.ext import commands
from discord.ext.commands import CommandNotFound

t = datetime.datetime.now()
d = datetime.datetime.now()

token = open("token.txt", "r").readline()

client = commands.Bot(command_prefix=".")


def texttocaps(text):
    return text.upper()


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Dieser Befehl konnte nicht gefunden werden.")


@client.command()
async def zeit(ctx):
    await ctx.send(t.strftime("%H:%M:%S"))


@client.command()
async def datum(ctx):
    await ctx.send(d.strftime("%d/%m/%Y"))


@client.command()
async def caps(ctx, *, text: texttocaps):
    await ctx.send(text)


@client.command(aliases=["generatepassword", "passwordgenerator", "createpassword"])
async def pwg(ctx, laenge=0):
    grossbuchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kleinbuchstaben = "abcdefghijklmnopqrstuvwxyz"
    ziffern = "0123456789"
    sonderzeichen = "!?#@&%{}[]§/*+-.,<>="

    passwort = grossbuchstaben + kleinbuchstaben + ziffern + sonderzeichen

    if laenge < 1: return await ctx.send("Gebe eine gültige Länge an!")
    if laenge > 128: return await ctx.send("Die maximale Länge beträgt 128 Zeichen!")

    password = "".join(random.choice(passwort) for i in range(laenge))

    await ctx.send("Das zufällige Passwort wurde Dir per PN geschickt!")
    await ctx.author.send("Dein Passwort lautet: **" + password + "**")


@caps.error
async def caps_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Gebe einen Text an, den ich schreien soll")


@pwg.error
async def pwg_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Gebe an, wie viele Zeichen das Passwort haben soll")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Das ist keine Zahl!")


client.run(token)
