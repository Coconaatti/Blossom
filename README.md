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
**Make sure your commands.JSON file looks like the sample one *(remember to provide color for the embeds).***\
**remember to sync your slash commands using ``!sync``** 

Fourth: [Go to the discord portal](https://discord.com/developers/applications)
Create a new application. Follow a youtube tutorial for that, Just remember to enable the message_content intent as provided in the bot.py\
copy your token **to your .env file**, it might loook something like this:\
``TOKEN=yaddayaddayadda``\
If desired, you can set your own prefix also. change this line ``command_prefix="desired prefix"`` in the bot class in bot.py to your own prefix.
And just like that,the bot is ready to run! :P. If you're having any issues running the bot, report it in the issues.

<hr>

## Usage
the bot can be accesssed using prefix or slash commands.

### Prefix commands

|command| description |
|----|------|
| ``!ls <table> <arg>`` | Shows an embed of your commands from the database. |
| ``!cat <table> <arg> <arg2> <arg3> ...`` | Concatenates your commands' content. Can have various arguments. |  
| ``!change`` | Changes your commands' content. You can either add, remove or modify a command or a command's content |

### Slash commands

|command|description|
|----|------|
| ``cat`` | Concatenates your commands' content. This one CANNOT Have multiple arguments. However, it has an auto-complete function with a simple fuzzy finder that I'm workikng on (inspiration of fzf taken from R.danny bot). So it's both an ls and a cat command |
| ``add`` | adds commands to a specific table|
| ``rm`` | removes commands to a specific table| 
| ``mod``| modifies commands' content|

## Preview
Here's a litte preview on a copy of the bot (below my own personal bot :p)
<img width="746" height="248" alt="image" src="https://github.com/user-attachments/assets/d52bb7fa-0c90-496a-afbc-05f249d0c0e3" />
<img width="738" height="358" alt="image" src="https://github.com/user-attachments/assets/b1615b9d-bb38-445f-922d-3c7efecdadd6" />
<img width="675" height="388" alt="image" src="https://github.com/user-attachments/assets/0df173c8-4cae-4b4d-9913-2cf9331e295c" />
<img width="770" height="432" alt="image" src="https://github.com/user-attachments/assets/e94ef234-4dac-451c-b9fa-02717c99e63c" />
<img width="777" height="295" alt="image" src="https://github.com/user-attachments/assets/f0cf5a15-9c7a-4664-af26-27817978baca" />
<img width="767" height="506" alt="image" src="https://github.com/user-attachments/assets/ffaccef6-8279-4e09-b449-8af0d3a059d5" />
<img width="467" height="562" alt="image" src="https://github.com/user-attachments/assets/63c3c0c9-df8c-40d3-adae-c631aeb349b4" />\
<img width="371" height="168" alt="image" src="https://github.com/user-attachments/assets/210cbe03-988e-4e71-a333-f01dd4e3bb64" />


## Bugs
There are some bugs known, such as having to restart your bot just to see your newly added / removed commands. Please report them in the issues, I will work on them progressively. This is my actual first project so don't expect anything fascinating. I'm just practicing and I found the idea very creative.\
I plan to add other features of course.
