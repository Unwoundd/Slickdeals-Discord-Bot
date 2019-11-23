import base64
import discord
from time import sleep
from creds import get_token
import slickdeals_feed
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

channel = client.get_channel(1232423418372)
# await channel.send('hello')

@client.event
async def on_message(message):
    print(message.author, " : ",  message.content)
    mention_user = "<@"+str(message.author.id)+">"
    # print(message.member)
    if message.author == client.user:
        return
    
    user_msg = message.content.lower().strip()
    # print(message.guild)
    # print(message.author.id)
    term_delay = 5.0
    if message.content.startswith('$hello'):
        sleep(1.5)
        await message.channel.send(mention_user + " I am awaiting your orders master")
    
    elif "!sd" ==  user_msg.strip():
        sleep(0.5)
        hold_msgs = slickdeals_feed.get_frontpage()[0:5]
        for entry in hold_msgs:
            await message.channel.send(entry)
            sleep(term_delay)
        await message.channel.send(mention_user + " Your wish is my command master, check out these latest deals ")


    elif "!sd" in user_msg:
        search_term = user_msg.split(" ")[1:]
        search_str = "+".join(search_term)
        link = f"https://slickdeals.net/newsearch.php?src=SearchBarV2&q={search_str}&searcharea=deals&searchin=first&rss=1"
        if user_msg.split(" ")[-1].isnumeric():
            grab_x = int(user_msg.split(" ")[-1])
            hold_msgs = slickdeals_feed.get_item(link)[0:grab_x]
        else:
            hold_msgs = slickdeals_feed.get_item(link)[0:5]

        for entry in hold_msgs:
            await message.channel.send(entry)
            sleep(term_delay)
        await message.channel.send(mention_user + " I will serve you the slickest of deals master ")
        sleep(2)
        await message.channel.send("<:peeposmile:612092175613689877>")

def fetch_token():
    token = str(get_token())
    return token

client.run(fetch_token())
