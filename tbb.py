import discord
from discord.ext import commands
from discord.ext.commands.bot import when_mentioned_or
import random
import json
import requests
import asyncio
from discord import Color
import datetime
import io
import base64
from threading import Timer
import time
import xml.etree.ElementTree as ET

TOKEN = ""

bot_prefixes = ['tbb ', 'TBB ', 'Tbb ', 'tBB ']
client = commands.Bot(command_prefix=(
    when_mentioned_or(*bot_prefixes)), case_insensitive=True)
client.remove_command('help')

greetings = ('hello', 'hi', 'hey', 'oi', 'heyo', 'o/')
rip = ('rip', 'f')

greeting_reply = ["hello!", "heyy :)", "hiiiii",
                  "Bonjour!", "Hola", 'oi', 'heyo', 'o/']
xD = ['xD', 'XD', 'Lmao', 'Ha ha ha', 'lol']
oof = ['oofs', 'big oof', 'oof']
yes = ['Yups', 'yesss', 'ikr!']
f = ['f', 'rip']

muted = []
titles = []

global choice
choice = 0

global check1
check1 = False

owner_id = 569828290253160449
bot_id = 750746526745100309

search_api = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={search_term}&format=json"
wiki_api = "https://en.wikipedia.org/wiki/{title}"

arxiv_api = "http://export.arxiv.org/api/query?search_query={search_term}"


def main():
    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="This Boring World :/"))
        print(client.user.name)
        print(client.user.id)
        print('------')
        choice = 0

    @client.command()
    async def kick(ctx, member: discord.Member, *, reason=''):
        msg = ctx.message.content.split(' ')

        if(ctx.message.author.name == 'Krish'):
            await member.kick(reason=reason)
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("Kicked " + msg[2])
        else:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("HAHA, You can't Kick !")

    @client.command()
    async def ban(ctx, member: discord.Member, *, reason=''):
        msg = ctx.message.content.split(' ')

        if(ctx.message.author.name == 'Krish'):
            await member.ban(reason=reason)
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("Banned " + msg[2])
        else:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("HAHA, You can't Ban!")

    @client.command()
    async def unban(ctx, member, *, reason=''):
        msg = ctx.message.content.split(' ')
        member = msg[2]
        member = member[3:-1]
        user = await client.fetch_user(member)

        print(int(member))
        if(ctx.message.author.name == 'Krish'):
            await ctx.guild.unban(user)
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("UnBanned " + msg[2])
        else:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("HAHA, You can't UnBan!")

    @client.command()
    async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)

    @client.command()
    async def joincall(ctx):
        try:
            channel = ctx.message.author.voice.channel
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("Joined ;)")
            await channel.connect()

        except:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("You Join First😤")

    @client.command()
    async def leavecall(ctx):
        await ctx.voice_client.disconnect()
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.send("Left the call ;)")

    @client.command()
    async def spam(ctx):
        msg = ctx.message.content.split(' ')

        if(any(map(str.isdigit, msg[-1]))):
            spam = msg[2:-1]
            n = int(msg[-1])
        else:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("Cmon, Atleast Tell Me How Many Times To Spam!")

        spam_msg = ''
        for i in range(0, len(spam)):
            spam_msg += spam[i]+' '

        if("@everyone" in spam_msg):
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("<@!"+str(ctx.message.author.id)+"> Heyy! Dont Disturb Everyone")
            return
        elif("@here" in spam_msg):
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("<@!"+str(ctx.message.author.id)+"> Heyy! Dont Disturb Everyone Here")
            return
        else:
            if(ctx.message.author.name == 'Krish'):
                for i in range(1, n+1):
                    await ctx.send(spam_msg)
            else:
                if(n > 5):
                    if("569828290253160449" in spam_msg):
                        async with ctx.typing():
                            await asyncio.sleep(1)
                            await ctx.send("Dare You Use This Against Krish")
                        return
                if(n > 35):
                    async with ctx.typing():
                        await asyncio.sleep(1)
                        await ctx.send("Only Krish Can Spam for more than 25 times ;)")
                    return
                if(n > 10):
                    if(ctx.message.author.id == "533964838041419776"):
                        async with ctx.typing():
                            await asyncio.sleep(1)
                            await ctx.send("Ya Dont Spam more than 10 xP")
                else:
                    for i in range(1, n+1):
                        await ctx.send(spam_msg)

    @client.command()
    async def mute(ctx, user: discord.User):
        try:
            if(user.id == owner_id):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("HOW DARE YOU TRY TO MUTE THE CREATOR!, NOW I WILL MUTE YOU")
                muted.append(ctx.message.author.id)
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("Ha Ha"+" <@!"+str(ctx.message.author.id)+"> is MUTED!!")
                return

            if(user.id == bot_id):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("DARE YOU USE MY OWN COMMANDS AGAINST ME, NOW I WILL MUTE YOU")
                muted.append(ctx.message.author.id)
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("Ha Ha"+" <@!"+str(ctx.message.author.id)+"> is MUTED!!")
                return

            muted.append(user.id)
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("Ha Ha"+" <@!"+str(user.id)+"> is MUTED!!")
        except:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("Yo! Tag Properly!")

    @client.command()
    async def unmute(ctx, user: discord.User):

        if(ctx.message.author.id != user.id):
            try:
                muted.remove(user.id)
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("<@!"+str(user.id)+"> is UNMUTED!!")
            except:
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("Yo! Tag Properly!")
        else:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("Ha Ha You Cant Unmute Yourself!")

    @client.command()
    async def say(ctx, msg):
        message = ctx.message.content
        msg = message[7:]
        if(ctx.message.author.name == 'Krish'):
            await ctx.channel.purge(limit=1)
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send(msg)
        else:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("I only Listen to <@!569828290253160449> ;)")

    @client.command()
    async def wiki(ctx):
        global check1

        check1 = True

        message = ctx.message.content
        msg = message[9:]
        search = search_api.replace("{search_term}", msg)
        response = requests.get(search)

        jprint(response.json())

        q = response.json()['query']
        s = q['search']

        jprint(q)

        result = ''

        for i in s:
            if "may refer to" not in i["snippet"]:
                a = i['title']
                titles.append(a)

        for i in range(1, len(titles)+1):
            title = titles[i-1]
            search_title = title.replace(' ', '_')
            result = result + \
                str(i)+":  **["+title+"](" + \
                wiki_api.replace('{title}', search_title)+")**    " + '\n\n'

        def check(message: discord.Message):
            return message.author.id == ctx.author.id and message.channel == ctx.channel

        if len(titles) != 0:
            global choice
            async with ctx.typing():
                await asyncio.sleep(1)
                embed = discord.Embed(
                    color=14452770, title="Wiki Search Results For **"+msg+"**", description=result)
                await ctx.send(embed=embed)
                embed = discord.Embed(
                    color=717055, description="Enter A Number From the above list to choose")
                choose = await ctx.send(embed=embed)

            for i in range(1, 4):
                retries_left = 3 - i

                if i < 3:
                    error = f"You have `{retries_left}/{3}` chances left"
                else:
                    error = 'Please try again by using `tbb wiki` command'

                try:
                    message = await client.wait_for('message', timeout=60, check=check)
                    res_user = await client.get_context(message)

                    pos = []
                    for i in range(1, len(titles)+1):
                        pos.append(i)

                    try:
                        temp = int(message.content)
                        if temp not in pos:
                            print("False")
                            await message.channel.send("Enter a Integer Between 1 and "+str(len(titles))+", "+error)
                        else:
                            choice = temp
                            print("True")
                            await ctx.send(wiki_api.format(title=titles[choice-1].replace(" ", "_")))
                            break

                    except:
                        await message.channel.send("Oi, Enter A Valid Integer "+error)

                except asyncio.TimeoutError:
                    embed = discord.Embed(
                        colour=Color.red(), description=f"Time's up {ctx.author.mention}")
                    await choose.edit(embed=embed)
                    break

        else:
            embed = discord.Embed(color=14452770, title="Wiki Search Results For **" +
                                  msg+"**", description="Sorry, No Search Results Were Found!")
            await ctx.send(embed=embed)
            titles.clear()
            choice = 0
            check1 = False
            return

        titles.clear()
        choice = 0
        check1 = False
        print("Check iS False")

    def jprint(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    @client.command()
    async def arxiv(ctx):
        global check1
        global choice

        check1 = True
        choice = 0

        message = ctx.message.content
        msg = message[10:]
        search = arxiv_api.replace("{search_term}", msg)
        response = requests.get(search)

        root = ET.fromstring(response.content)
        ns = {'d': 'http://www.w3.org/2005/Atom'}
        data = []
        entry = []

        for item in root.findall(".d:entry/", ns):
            tag = str(item.tag.encode('utf8'))
            tag = tag[31:-1]

            if tag == 'title':
                title = str(item.text.encode('utf8'))
                title = title[2:-1]
                title = title.replace("\\n ", "")
                entry.append(title)

            if tag == 'summary':
                entry.append(str(item.text))

            if tag == "link":
                attrib = str(item.attrib)

                if "\'title\': \'pdf\'" in attrib:
                    entry.append(str(item.attrib['href']))
                    data.append(entry)
                    entry = []

        desc = ""
        k = 1

        for i in data:
            for j in range(len(i)):
                if j == 0:
                    desc = desc + str(k)+":  **[" + i[j] + "]"
                    print(i[j])
                    print(" ")
                if j == 2:
                    desc = desc + "("+i[j]+")**"+" \n\n"
            k = k + 1

        def check(message: discord.Message):
            return message.author.id == ctx.author.id and message.channel == ctx.channel

        if desc != " ":
            async with ctx.typing():
                embed = discord.Embed(
                    color=14452770, title="ARXIV Search Results For **"+msg+"**", description=desc)
                await ctx.send(embed=embed)
                embed = discord.Embed(
                    color=717055, description="Enter A Number From the above list to choose")
                choose = await ctx.send(embed=embed)

            for i in range(1, 4):
                retries_left = 3 - i

                if i < 3:
                    error = f"You have `{retries_left}/{3}` chances left"
                else:
                    error = 'Please try again by using `tbb arxiv` command'

                try:
                    message = await client.wait_for('message', timeout=60, check=check)
                    res_user = await client.get_context(message)

                    pos = []
                    for i in range(1, len(data)+1):
                        pos.append(i)

                    try:
                        temp = int(message.content)
                        if temp not in pos:
                            print("False")
                            await message.channel.send("Enter a Integer Between 1 and "+str(len(data))+", "+error)
                        else:
                            choice = temp
                            print("True")
                            url = data[choice-1][2]
                            title = data[choice-1][0]
                            summ = data[choice-1][1]

                            if len(summ) > 1000:
                                summ = summ[0:1000] + "..."

                            async with ctx.typing():
                                embed = discord.Embed(color=14452770)
                                embed.add_field(
                                    name="Title :", value=title, inline=False)
                                embed.add_field(
                                    name="Summary :", value=summ, inline=False)
                                res = requests.get(url)
                                file = io.BytesIO(res.content)
                                await ctx.send(embed=embed)
                            async with ctx.typing():
                                await ctx.send(file=discord.File(file, filename=title+'.pdf'))
                            break

                    except:
                        await message.channel.send("Oi, Enter A Valid Integer "+error)

                except asyncio.TimeoutError:
                    embed = discord.Embed(
                        colour=Color.red(), description=f"Time's up {ctx.author.mention}")
                    await choose.edit(embed=embed)
                    break
        else:
            embed = discord.Embed(color=14452770, title="ARXIV Search Results For **" +
                                  msg+"**", description="Sorry, No Search Results Were Found!")
            await ctx.send(embed=embed)
            date.clear()
            choice = 0
            check1 = False
            return

        titles.clear()
        choice = 0
        check1 = False
        print("Check iS False")

    @client.command()
    async def help(ctx):
        msg = ctx.message.content.split(' ')
        try:
            command = msg[2]

            if(command == 'wiki'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```Searches Something on wikipedia for you and gives you the results \ntbb wiki <term-to-search>```""")

            if(command == 'arxiv'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```Searches Research Papers on arXiv for you and gives you the summary and the pdf of the paper \n\ntbb arxive <paper-to-search>```""")

            if(command == 'clear'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```Clears certain 'n' number of msgs \ntbb clear <n>```""")

            if(command == 'spam'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```Spam someone by tagging them or spam anything 'n' number of times\ntbb spam <msg to spam> <n>```""")

            if(command == 'kick'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```Kicks a certain user \ntbb kick <@user> \n \nHaha but you cant use it ;)```""")

            if(command == 'ban'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```Bans the user from the server \ntbb ban <@user> \n \nSadly you cant use it :(```""")

            if(command == 'unban'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```UnBans the user from the server \ntbb unban <@user> \n \nSadly you cant use it :(```""")

            if(command == 'say'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```Says a particular msg \ntbb say <msg> \n \nHaha but you cant use it ;)```""")

            if(command == 'mute'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```Deletes all the incoming msgs of that user and dosent let that person speak \ntbb mute <@user> \n\n*Precaution : Once you Mute Someone, only Krish Can Unmute!*```""")

            if(command == 'unmute'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```Undoes the actions of the mute command \ntbb unmute <@user> \n \nYou Cant Unmute Yourself tho, you need to ask someone to do it ;)```""")

            if(command == 'joincall'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```Joins the voice channel you are in \ntbb joinchannel ```""")

            if(command == 'leavecall'):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send("""```Leaves the voice channel it was in \ntbb leavechannel ```""")

        except:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("""```PREFIX : tbb \n\n - wiki \n - arxiv \n - clear \n - spam \n - kick \n - ban \n - unban \n - say \n - mute \n - unmute \n - joincall \n - leavecall \n \nYou Can Type tbb help <command> for more info on that command```""")

    @client.event
    async def on_message(message):
        print('Message from {0.author}: {0.content}'.format(message))

        with open("D:\\Python-Projects\discord_msgs.txt", 'a') as filehandle:
            try:
                filehandle.write(str(message.author.name) +
                                 ": "+message.content + '\n')
                filehandle.close()
            except:
                filehandle.write(message.content + '\n')
                filehandle.close()

        if muted.__contains__(message.author.id):
            await message.delete()

        if (message.author.bot == True):
            return

        if (message.content.lower().startswith(greetings) and len(message.content) <= 5):
            await message.channel.send(random.choice(greeting_reply)+" <@!"+str(message.author.id)+">")

        if (message.content.lower().startswith('xd') and len(message.content) == 2):
            await message.channel.send(random.choice(xD))

        if (message.content.lower().startswith('ikr') and len(message.content) == 3):
            await message.channel.send(random.choice(yes))

        if (message.content.lower().startswith(';-;') and len(message.content) == 3):
            await message.channel.send(';-;')

        if (message.content.lower().startswith(rip) and len(message.content) <= 3):
            await message.channel.send(random.choice(f))

        if ('oof' in message.content.lower()):
            await message.channel.send(random.choice(oof))

        global check1

        if check1:
            print("Check is True")
        else:
            print("Check is False")
            await client.process_commands(message)

    client.run(TOKEN)
    creds = None


if __name__ == '__main__':
    main()
