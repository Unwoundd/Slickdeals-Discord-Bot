import base64
import discord
from time import sleep
from creds import get_token
from queue import Queue
import slickdeals_feed
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


buffer = Queue()


channel = client.get_channel(1232423418372)
# await channel.send('hello')


@client.event
async def on_message(message):
#    message.
    print(message.author, " : ",  message.content)

    mention_user = "<@"+str(message.author.id)+">"

    # print(message.member)
    if message.author == client.user:
        return

    # print(message.guild)
    # print(message.author.id)
    if message.content.startswith('$hello'):
        sleep(1.5)
        await message.channel.send(mention_user + " I am awaiting your orders master")
    
    elif "!sd" ==  message.content.lower().strip() and len(message.content.split()) == 1:
        sleep(0.5)
        hold_msgs = slickdeals_feed.get_frontpage()[0:5]
        for entry in hold_msgs:
            await message.channel.send(entry)
            sleep(0.4)

        await message.channel.send(mention_user + " I will serve you the slickest of deals master ")
    elif "!sd" in message.content.lower():
        search_term = message.content.lower().split(" ")[1:]
        search_str = "+".join(search_term)
        link = f"https://slickdeals.net/newsearch.php?src=SearchBarV2&q={search_str}&searcharea=deals&searchin=first&rss=1"
        hold_msgs = slickdeals_feed.get_item(link)[0:5]
        for entry in hold_msgs:
            await message.channel.send(entry)
            sleep(0.4)

        await message.channel.send(mention_user + " I will serve you the slickest of deals master ")
       
#    elif "based" in messa#ge.content.lower():
        #sleep(1.5)
        #await message.channel.send(mention_user + " based\n and\n redpilled\n :pill: ")
        #sleep(1.5)

def fetch_token():
    token = str(get_token())
    return token

client.run(fetch_token())
