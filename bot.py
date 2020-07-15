import discord
from discord.ext.commands import Bot
import time
token = "NzMwODg5NzM1MzIwMzcxMzQz.Xws6PA.nOTY09rcJuX5OjW6jWc30xrzLsQ"
client = discord.Client()
bot = Bot("!")

print(client.get_guild(559274968744067103))
#channel = await find_channel(member.guild)
#@bot.command(pass_context=True)
#async def getguild(ctx):
#    return ctx.message.guild.id
    
global boo
boo = True



@client.event
async def on_message(message):
    global boo
    if "sql" in str(message.content).lower() and boo:
        boo = False
        # If the user says !hello we will send back hi
        await message.channel.send("I heard you losers were talking about SQL")
        await message.channel.send("They Suck Bawls")
        time.sleep(0.5)
        boo = True
    elif str(message.content).lower() == '!users':
        boo = False
        #id=getguild()
        await message.channel.send(f"""Number Of SQL Haters: {message.channel.guild.member_count} """)
        boo = True

@client.event
async def on_member_join(member):
    global boo
    boo = False
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"""Welcome to the server {member.mention} I hope you fucking hate SQL like the rest of us""")
            boo = True


# @client.event
# async def on_message(message):
#    channel= message.channel
#    print(channel)
#    msg = str(message.content).lower()
#    print(msg)
#    if msg == "!users":
#        print(id)
#        await channel.send(f"""Number Of SQL Haters: {id.member_count} """)
#   elif msg.find('sql'):
#       await channel.send('Yall talking about Simple query languege?')
#       await channel.send('Fuck Simple Query Languege!')
#       return


# @client.event
# async def on_member_join(member):
##
# for channel in member.server.channels:
# if channel == 'general' or channel == 'tester':
#            await channel.send(f"""Welcome {member.mention}, How much do you hate Simple Query Langueges? """)


client.run(token)
