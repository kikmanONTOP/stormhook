import discord
from discord.ext import commands
from colorama import init, Fore
import asyncio
import time
import fade 
import random
import requests
stormhook = '''
                                                                   
                                                                                              
.s5SSSs.  .s5SSSSs. .s5SSSs.  .s5SSSs.  .s5ssSs.      .s    s.  .s5SSSs.  .s5SSSs.  .s    s.  
      SS.    SSS          SS.       SS.    SS SS.           SS.       SS.       SS.       SS. 
sS    `:;    S%S    sS    S%S sS    S%S sS SS S%S     sS    S%S sS    S%S sS    S%S sS    S%S 
`:;;;;.      S%S    SS    S%S SS .sS;:' SS :; S%S     SSSs. S%S SS    S%S SS    S%S SSSSs.S:' 
      ;;.    S%S    SS    S%S SS    ;,  SS    S%S     SS    S%S SS    S%S SS    S%S SS  "SS.  
      `:;    `:;    SS    `:; SS    `:; SS    `:;     SS    `:; SS    `:; SS    `:; SS    `:; 
.,;   ;,.    ;,.    SS    ;,. SS    ;,. SS    ;,.     SS    ;,. SS    ;,. SS    ;,. SS    ;,. 
`:;;;;;:'    ;:'    `:;;;;;:' `:    ;:' :;    ;:'     :;    ;:' `:;;;;;:' `:;;;;;:' :;    ;:' 
                                                Made by kikmanONTOP                    
                                                github.com/kikmanONTOP
           '''                                      

messages_per_webhook = 20
message_interval = 0
faded_text = fade.greenblue(stormhook)
print(faded_text)
intents = discord.Intents.all()
bot = discord.Client(intents=intents)
token = input(Fore.LIGHTCYAN_EX + "Discord bot token: ")
guild_id = input("Server id: ")
spam_message = input("Spam message: ")
webhook_count = int(input("Number of webhooks to create: "))
print(Fore.CYAN + ".....")

async def send_messages(webhook_url, count):
    for i in range(count):
        message_content = f"@everyone DOWNLOAD THIS TOOL https://github.com/kikmanONTOP/stormhook" + spam_message
        
        requests.post(webhook_url, json={"content": message_content})
        
        print(f"Spammed {i + 1} sent successfully.")
        await asyncio.sleep(0)

@bot.event
async def on_ready():
    print(f"Stormhook is ready as {bot.user}")

    guild = bot.get_guild(int(guild_id))

    if guild is None:
        print("Server id error")
        return
    
    if guild:
        text_channels = [channel for channel in guild.text_channels if channel.name]
        
        for i in range(webhook_count):
            channel = random.choice(text_channels)

            webhook = await channel.create_webhook(name=f"Delete this server XDD {i + 1}")
            print(f"Webhook {i + 1} created in {guild.name}/{channel.name}: {webhook.url}")

            await send_messages(webhook.url, messages_per_webhook)


bot.run(token)