import nextcord
import asyncio
import json
from nextcord.utils import get
from nextcord.ext import tasks
from nextcord.ext.commands import CommandNotFound
from nextcord.voice_client import VoiceClient
from nextcord.ext.commands import command,has_permissions
from nextcord.ext import commands
from nextcord import Interaction, message_command, slash_command, user_command
from nextcord.abc import GuildChannel

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}


with open('settings.json', 'r') as json_file:
  settings = json.load(json_file)

class voiceannounce(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("COG ready!")
    @slash_command(description="Lets you leave with a killer, sick, outro")
    async def ready(self, interaction: Interaction):
        if settings["devmode"] == "yes" or interaction.user.id == interaction.guild.owner_id:
            if not interaction.user.voice:
                embed = nextcord.Embed(
                    color = nextcord.Color.red()
                )
                embed.set_author(name=f"Oops..")
                embed.add_field(name="\u200b", value="You are not in a voice channel, or I do not have permissions to see the voice channel.",  inline=False)
                return await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                embed = nextcord.Embed(
                    color = nextcord.Color.green()
                )
                embed.set_author(name=f"Get ready..")
                embed.add_field(name="\u200b", value="Get ready",  inline=False)
                await interaction.response.send_message(embed=embed, ephemeral=True)
            myself = self.client.user.id
            abletojoinvc = 0
            try:
                vc = await interaction.user.voice.channel.connect()
                abletojoinvc = 1
            except Exception as eee:
                abletojoinvc = 0
                failjoinreason = eee
            if abletojoinvc == 1:
                try:
                    musicformat = settings["musicformat"]
                    player = vc.play(nextcord.FFmpegPCMAudio(source=f"./assets/outrostart.{musicformat}"))
                    getvoice = get(self.client.voice_clients, guild=vc.guild)
                    while getvoice.is_playing():
                        await asyncio.sleep(1)
                    #await vc.disconnect()
                    player = vc.play(nextcord.FFmpegPCMAudio(source=f"./assets/outroend.{musicformat}"))
                    await interaction.user.disconnect()
                    while getvoice.is_playing():
                        await asyncio.sleep(1)
                    await vc.disconnect()
                except Exception as fff:
                    if abletojoinvc == 1:
                        await vc.disconnect()
                    return print(f"Hmm, something went wrong playing the audio file! Error:\n{fff}")
            else:
                if abletojoinvc == 0:
                    return print(f"Hmm, something went wrong joining the voice channel. Error:\n{failjoinreason}")
        else:
            embed = nextcord.Embed(
                color = nextcord.Color.green()
            )
            embed.set_author(name=f"Ooops")
            embed.add_field(name="\u200b", value="Only the owner of this server can do that.",  inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=True)


def setup(client):
    client.add_cog(voiceannounce(client))
