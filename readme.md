Developed by [ZenullTheProtogen](https://twitter.com/flunseydevelops)

What is this bot?
---
This bot allows server owners to play music and disconnect them on the drop
<br>
<br>

Setup
---
Install everything inside of requirments.txt (python packages)

You need to own a Discord Bot Profile. You can make on by [following this link](https://discord.com/developers/applications).

Create a copy of `settings-template.json` and name the copy `settings.json`. Inside of the file, replace the text `insert-token` with your Bot Token.

Next, invite the new bot with the following permissions on your server

1. Connect
2. Speak
3. Move Members
4. Use Voice Activity

Changing the music
---
The music is split into two files, "outrostart" and "outroend".
> Outrostart is the music that plays before the disconnect

> Outroend is what plays after the bot disconnects you

Both files are located in the `/assets/` directory. Just swap them out with your own if you want to change the music.
> The default settings loads MP3 files, however inside of `settings.json` you can change the file format the bot loads by changing the `musicformat` line.
> > For example, you want to change it to load a file called `introstart.wav` you would change it to look like `"musicformat": "wav"`