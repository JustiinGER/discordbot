import discord
import datetime
import random
from discord.ext import commands
from discord.ext.commands import CommandNotFound

d = datetime.datetime.now()
t = datetime.datetime.now()

client = commands.Bot(command_prefix=".")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Dieser Befehl konnte nicht gefunden werden.")

@client.command(aliases=["ui"])
async def userinfo(ctx, member: discord.Member):
    eprofil = discord.Embed(title="Userinformationen", timestamp=t.utcnow(),
                            colour=random.randint(0, 0xffffff),
                            url="https://discordapp.com",
                            description="Informationen über: {}".format(member.mention))
    eprofil.set_thumbnail(url=member.avatar_url)
    eprofil.set_footer(text="Informationen angefordert von: {}".format(ctx.author.name), icon_url=ctx.author.avatar_url)
    eprofil.add_field(name="Name", value=member.name, inline=True)
    eprofil.add_field(name="Nick", value=member.nick, inline=True)
    eprofil.add_field(name="Auf dem Server seit:", value=member.joined_at.strftime("%d/%m/%Y, %H:%M:%S"), inline=False)
    eprofil.add_field(name="Auf Discord seit:", value=member.created_at.strftime("%d/%m/%Y, %H:%M:%S"), inline=True)
    eprofil.add_field(name="Status:", value=member.status, inline=True)
    eprofil.add_field(name="ID:", value=member.id, inline=False)
    await ctx.send(embed=eprofil)

@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Bitte gebe einen User an.")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Diesen User kann ich nicht finden.")
