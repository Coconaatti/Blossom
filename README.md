# Blossom
A discord bot that's designed to take notes, nothing special :p 

<hr>

## Foreword
I think we all know Rose bot on telegram. A bot that has some moderation tools and helps in channel management. But it also has a special feature, and that is taking notes. I was grabbed by how the bot could take notes.\
However, as time passed, notes started to stack over each other. and everything looked a little messy for me. seaarching for notes got harder. And it just, striked me.\
I was very annoyed by this. So I decided to create a bot that would help me do that in a way that's "more organized". This is where blossom appears, a bot that has buttons interface and a paginator, alongside a beautiful embed that displays your notes perfectly, even among other devices. (yes, it is sort of "cross platform"). As well as other functionalities to help in taking notes better.\
Blossom took me about 2 months to make, please note that I'm a beginner programmer that had absolutely no idea about OOP, asyncIO, external libraries, decorators, etc etc..\
I also had a mental breakdown while making this, and I was in the middle of my school journey. Time was short and thinking was hard. So despite this having bugs that I didn't want to fix, **I still wanted to publish this in search of contributors and new ideas.**\
Funny enough because I won't actually be hosting this, I will just provide a tutorial on how to set this up without encountering errors. Maybe in the future I can host this.\
So I hope you like it. And I hope you recommend this to your friends also.


<hr>

## Installation
### Setting up the environment
First: clone the source in your directory
Second: we need to setup a virtual environment and install the dependencies for the bot. They aren't much for now, just *discord.py and decouple*
```
python -m venv .
source bin/activate
pip install discord.py python-decouple
```

Third: place your own database and JSON file under the 'extras' directory. I will provide some samples for you to look at.\
**Please note that I used sqlite to make this possible, not PostgreSQL or OracleSQL. I don't own a server and that's why I used sqlite as it's designed for embedded devices.**
**Make sure that there are 3 columns in your database: cid (PRIMARY KEY), Commands (TEXT) , Content (TEXT). If otherwise, you need to ALTER your columns or create new ones.\
Commands is for the command name, and content is for the content of the command.**\
**Make sure your commands.JSON file looks like the sample one *(remember to provide color for the embeds).***
**remember to sync your slash commands using ``!sync`` **

Fourth: [Go to the discord portal](https://discord.com/developers/applications)
Create a new application. Follow a youtube tutorial for that, Just remember to enable the message_content intent as provided in the bot.py\
copy your token **to your .env file**, it might loook something like this:\
``TOKEN=yaddayaddayadda``\
If desired, you can set your own prefix also. change this line ``command_prefix="desired prefix"`` in the bot class in bot.py to your own prefix.
And just like that,the bot is ready to run! :P. If you're having any issues running the bot, report it in the issues.

<hr>

## Usage
the bot can be accesssed using prefix or slash commands.

Prefix commands
|----|------|
|command| description |
| ``!ls <table> <arg>`` | Shows an embed of your commands from the database. |
| ``!cat <table> <arg> <arg2> <arg3> ...`` | Concatenates your commands' content. Can have various arguments. |  
