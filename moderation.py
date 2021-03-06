import discord
import datetime
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound

t = datetime.datetime.now()

token = open("token.txt", "r").readline()

client = commands.Bot(command_prefix=".")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Dieser Befehl konnte nicht gefunden werden.")


@client.command(aliases=["delete"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount + 1)
    if amount == 1:
        clearmassage = await ctx.send(f"Es wurde **{amount}** Nachricht gelöscht!")
    else:
        clearmassage = await ctx.send(f"Es wurden **{amount}** Nachrichten gelöscht!")
    await asyncio.sleep(5)
    await clearmassage.delete()


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Der User **{member}** wurde wegen **{reason}** vom Server gekickt!")


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Der User **{member}** wurde wegen **{reason}** vom Server gebannt!")


@client.command(aliases=["ar"])
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"Der User **{member}** hat die Rolle **{role}** erhalten!")


@client.command(aliases=["rr"])
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f"Dem User **{member}** wurde die Rolle **{role}** entfernt!")


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


@client.command(aliases=["sm"])
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Slowmode auf **{seconds}** Sekunden gesetzt!")


@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("Der Channel wurde gesperrt!")


@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send("Der Channel wurde entsperrt!")


@client.command(aliases=["cn"])
@commands.has_permissions(manage_nicknames=True)
async def changenick(ctx, member: discord.Member, name):
    await member.edit(nick=name)
    await ctx.send(f"Der User **{member}** wurde zu **{name}** umbenannt!")


@client.command(aliases=["ccn"])
@commands.has_permissions(manage_channels=True)
async def changechannelname(ctx, channel: discord.TextChannel, *, newname):
    await channel.edit(name=newname)
    await ctx.send(f"Der Channel wurde zu **{newname}** umbenannt.")


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Bitte gebe an, wie viele Nachrichten gelöscht werden sollen.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Dir fehlt die manage_messages Berechtigung!")


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Gebe an, wer gebannt werden soll.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Dir fehlt die ban_members Berechtigung!")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Ich konnte diesen User nicht finden.")


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Gebe an, wer gekickt werden soll.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Dir fehlt die kick_members Berechtigung!")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Ich konnte diesen User nicht finden.")


@addrole.error
async def addrole_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Gebe an, welcher User welche Rolle bekommen soll.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Dir fehlt die manage_roles Berechtigung!")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Ich konnte diesen User oder diese Rolle nicht finden.")


@removerole.error
async def removerole_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Gebe an, welchen User welche Rolle entfernt werden soll.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Dir fehlt die manage_roles Berechtigung!")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Ich konnte diesen User oder diese Rolle nicht finden.")


@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Bitte gebe einen User an.")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Diesen User kann ich nicht finden.")


@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Gebe die Zeit in Sekunden an, auf welche der Slowmode gesetzt werden soll")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Das ist keine gültige Zeitangabe!")


@lock.error
async def lock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Dir fehlt die manage_channels Berechtigung!")


@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Dir fehlt die manage_channels Berechtigung!")


@changenick.error
async def changenick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Dir fehlt die manage_nicknames Berechtigung!")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Entweder hast du keinen User oder keinen Nicknamen angegeben!")


@changechannelname.error
async def changechannelname_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Du hast entweder keinen Kanal ausgewählt oder keinen Namen angegeben!")


client.run(token)
