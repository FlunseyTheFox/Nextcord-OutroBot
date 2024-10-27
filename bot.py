import nextcord
import json
from nextcord.ext import tasks
from nextcord.ext.commands import CommandNotFound
from nextcord.voice_client import VoiceClient
from nextcord.ext.commands import command,has_permissions
from nextcord.ext import commands
from nextcord import Client, Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
with open('settings.json', 'r') as json_file:
  settings = json.load(json_file)

intents = nextcord.Intents.default()  # Define Intents

# Defining client for use
client = commands.Bot(command_prefix = commands.when_mentioned, intents=intents)
# Removing Discord.py's default help command (we're using a custom help menu in info.py)
client.remove_command("help")

# Let's make the bot do tasks when logged into the Discord Servers
@client.event
async def on_ready():
    print("Successfully logged into the Discord Servers!")

# Try and load all COGS inside the "cogs" folder
# This may not play nice with some machines, if so try removing the period in "./cogs"
client.load_extension(f'cogs.outro')

# HANDLES ERRORS
@client.event
async def on_command_error(ctx, error):
    embed = nextcord.Embed(
        color = nextcord.Color.red()
    )
    embed.set_author(name="Error processing command")
    embed.add_field(name="Issuer:", value=ctx.message.author.mention,  inline=True)
    embed.add_field(name="Error:", value=f"Unknown",  inline=True)
    embed.add_field(name="Possible Fix:", value="Unknown / Developer has been notified",  inline=True)
    await ctx.send(embed=embed)
    raise error
client.run(settings["token"])
# DO NOT SHARE YOUR TOKEN OR MONGODB DETAILS, MAKE SURE DATABASE IS 100% SECURE