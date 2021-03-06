# D0GU#5777

import discord
import os
import json
from dotenv import load_dotenv, set_key, find_dotenv
from PIL import Image
from discord.ext import commands
import shutil
import random

# Config loading
dotenv_file = find_dotenv()
load_dotenv(dotenv_file)
TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX')

bot = commands.Bot(command_prefix=COMMAND_PREFIX)

#encyclopedia and reference file backup on start
if os.path.exists("references.json"):
    shutil.copy("references.json", "references.json.bak")
if os.path.exists("encyclopedia.json"):
    shutil.copy("encyclopedia.json", "encyclopedia.json.bak")
if os.path.exists("responses.json"):
    shutil.copy("responses.json", "responses.json.bak")

#creates reference and encyclopedia files if they do not exist.
if os.path.exists("encyclopedia.json") == False:
    with open("encyclopedia.json", "w") as json_file2:
        json_file2.write("{}")

if os.path.exists("encyclopedia.json") == False:
    with open("references.json", "w") as json_file:
        json_file.write("{}")

if os.path.exists("responses.json") == False:
    with open("responses.json", "w") as json_file3:
        json_file3.write('{"love":[],"hug":[],"kiss":[],"morning":[],"night":[]}')
    

#-------------------#
# One-shot commands #
# ------------------#


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}~, thanks for coming around cutie~'
    )

@bot.command(name='commands')
async def command_help(ctx):  # Command list
    embed=discord.Embed(title="Command List", description="Available Commands", color=0xfce94f)
    embed.add_field(name="~commands", value="Shows this help menu.", inline=False)
    embed.add_field(name="~mbuild", value="Builds message database for the current server.", inline=False)
    embed.add_field(name="~wordusage [word]", value="Shows how many times a specific word has been used on the current server", inline=False)
    embed.add_field(name="~create.reference [name]", value="Creates a new character reference for the given name.", inline=False)
    embed.add_field(name="~update.reference [name] [parameter] [content]", value="Updates one parameter of a given character reference", inline=False)
    embed.add_field(name="~update.reference.all ", value="Allows user to update all parameters of given character reference.", inline=False)
    embed.add_field(name="~update.reference.image [name] <image attachment>", value="Updates reference image for given character reference.", inline=False)
    embed.add_field(name="~image.add [name] <image attachment>", value="Adds image for current character reference.", inline=False)
    embed.add_field(name="~image.get [name] [index / \"all\"]", value="Gets one or all images for given character reference", inline=False)
    embed.add_field(name="~reference [name]", value="Displays the given character reference.", inline=False)
    embed.add_field(name="~create.entry [name]", value="Creates a new encyclopedia entry for the given monster.", inline=False)
    embed.add_field(name="~update.entry [name] [parameter] [content]", value="Updates one parameter for the given monster entry.", inline=False)
    embed.add_field(name="~update.entry.all ", value="Allows user to enter all monster entry parameters in one command.", inline=False)
    embed.add_field(name="~update.entry.image [name] <image attachment>", value="Updates the reference image for the given monster entry", inline=False)
    embed.add_field(name="~entry.image.add [name] <image attachment>", value="Adds an image to the gven monster entry.", inline=False)
    embed.add_field(name="~entry.image.get [name] [index / \"all\"]", value="Gets one or all images for given monster entry", inline=False)
    embed.add_field(name="~entry [name]", value="Displays the given monster entry.", inline=False)
    await ctx.send(embed=embed)

@bot.command(name='change.prefix')
async def newprefix(ctx, new_prefix): #Changes the command prefix
    set_key(dotenv_file, "COMMAND_PREFIX", new_prefix)
    await ctx.send("New prefix set!")
    os.system("sh restart.sh")


@bot.command(name='log')
async def log(ctx,threat): #randomly generates threat level and log number for entry creation
    l = ["l","lower","low"]
    h = ["h","higher","high"]
    if threat in h or l:
        if threat.lower() in l:
            await ctx.send(f"Threat level: {random.randint(0,50)}\nLog number: {random.randint(1000,2000)}")
        elif threat.lower() in h:
            await ctx.send(f"Threat level: {random.randint(50,100)}\nLog number: {random.randint(1000,2000)}")
    else:
        await ctx.send("Please enter a proper threat level (high/low)")
        
        
        
#-------------------#
# Response commands #
# ------------------#

@bot.command(name = "response.add")
async def create_reference(ctx, type, content):
    types = ["love","hug","kiss","morning","night"]    
    responses = {}
    try:
        with open("responses.json", "r") as json_data:
                responses = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    if type in types:
        if type == types[0]:
            if content not in responses[types[0]]:
                responses[types[0]].append(content)
        if type == types[1]:
            if content not in responses[types[1]]:
                responses[types[1]].append(content)
        if type == types[2]:
            if content not in responses[types[2]]:
                responses[types[2]].append(content)
        if type == types[3]:
            if content not in responses[types[3]]:
                responses[types[3]].append(content)
        if type == types[4]:
            if content not in responses[types[4]]:
                responses[types[4]].append(content)
        
            
    
        with open("responses.json", "w") as fileout:
            fileout.write(json.dumps(responses))
        await ctx.send("Response Added")
    else:
        await ctx.send("Wrong type argument")


@bot.command(name='ily')
async def i_love_you(ctx): #Tells the message author that they are loved
    responses = {}
    try:
        with open("responses.json", "r") as json_data:
                responses = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    # Takes the username minus id number of the message author
    author = str(ctx.message.author.display_name).split("#")[0] 
    
    response = random.choice(responses["love"])
    await ctx.send(response.format(author))

@bot.command(name='hug')
async def hug(ctx): #Hugs Mizu
    responses = {}
    try:
        with open("responses.json", "r") as json_data:
                responses = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    # Takes the username minus id number of the message author
    author = str(ctx.message.author.display_name).split("#")[0] 
    
    response = random.choice(responses["hug"])
    await ctx.send(response.format(author))

@bot.command(name='kiss')
async def kiss(ctx): #Kisses Mizu
    responses = {}
    try:
        with open("responses.json", "r") as json_data:
                responses = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    # Takes the username minus id number of the message author
    author = str(ctx.message.author.display_name).split("#")[0] 

    response = random.choice(responses["kiss"])
    await ctx.send(response.format(author))

@bot.command(name='morning')
async def morning(ctx): #Says good morning to Mizu
    responses = {}
    try:
        with open("responses.json", "r") as json_data:
                responses = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    # Takes the username minus id number of the message author
    author = str(ctx.message.author.display_name).split("#")[0] 
    
    response = random.choice(responses["morning"])
    await ctx.send(response.format(author))

@bot.command(name='night')
async def night(ctx): #Says goodnight to Mizu
    responses = {}
    try:
        with open("responses.json", "r") as json_data:
                responses = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    # Takes the username minus id number of the message author
    author = str(ctx.message.author.display_name).split("#")[0] 
    
    #response = f"Mmm~ I love you too {author}"
    response = random.choice(responses["night"])
    await ctx.send(response.format(author))


#----------------------------#
# Message Database Functions #
# ---------------------------#

@bot.command(name = 'mbuild')
async def build_message_list(ctx):
    text_channels = []
    guild = ctx.message.guild

    try:
        with open(f"{str(guild.id)}msg_history.json", "r") as json_file:
            message_history = json.load(json_file)
    except:
        message_history = {}

    await ctx.send(
        "(re)Building Message database...\n"
        "May take a few minutes depending on message count..."
        )

    for channel in guild.text_channels:
        text_channels.append(channel)

    for channel in text_channels:
        async for msg in channel.history(limit=10000):
            if msg.id not in message_history:
                message_history[msg.id] = {'user': str(msg.author.name), 'content': str(msg.content)}
                print(f'{str(msg.author.name)} : {str(msg.content)}')
            else:
             return
        
    with open(f"{str(guild.id)}_msg_history.json", "w") as json_data:
            json_data.write(json.dumps(message_history))
    
    await ctx.send(f"<@{str(ctx.message.author.id)}>, Message Database Built!")
        
@bot.command(name="wordusage") 
async def wordusage(ctx, word: str): # Checks how many times a word is used within the user's guild.
    count = 0
    guild = ctx.message.guild
    print(f"current guild id is: {guild.id}")
    try:
        with open(f"{str(guild.id)}_msg_history.json", "r") as json_file:
            message_history = json.load(json_file)
    except:
        await ctx.send(
            "Could not find message database\n"
            f"Please type '{COMMAND_PREFIX}mbuild' to build message database"
        )
        
    for msg in message_history:
        if word.lower() in message_history[msg]['content'].lower():
            print(message_history[msg]["content"])
            count += 1
    await ctx.send(f"The word {word} has been used {count} times on this server")



#----------------------#
# Character References #
# ---------------------#


@bot.command(name = "create.reference")
async def create_reference(ctx, name):
    references = {}
    try:
        with open("references.json", "r") as json_data:
                references = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    if name in references:
        await ctx.send("Name already in references")
    else:
        references[name] = {
            "species": "",
            "age": "",
            "height": "",
            "description": "",
            "referenceimage": "",
            "images": []
        }
        with open("references.json", "w") as fileout:
            fileout.write(json.dumps(references))
        await ctx.send(f"Reference for character {name} has been created")

@bot.command(name = "update.reference.name")
async def create_reference(ctx, name, new_name):
    references = {}
    try:
        with open("references.json", "r") as json_data:
                references = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    if name in references:
        references[new_name] = references[name] 
    else:
        await ctx.send(f"No entry with name {name}")
        return

    
    with open("references.json", "w") as fileout:
        fileout.write(json.dumps(references))
    await ctx.send(f"name for {new_name} has been updated")


@bot.command(name = "update.reference")
async def update_reference(ctx, name, parameter: str, content):
    references = {}
    try:
        with open("references.json", "r") as json_data:
                references = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")
    
    if parameter == "age":
        references[name]["age"] = content
    elif parameter == "height":
        references[name]["height"] = content
    elif parameter == "description":
        references[name]["description"] = content

    with open("references.json", "w") as json_data:
        json_data.write(json.dumps(references))

    await ctx.send(f"{name}'s {parameter} has been updated")


@bot.command(name = "update.reference.all")
async def update_reference_all(ctx, name, age, height, desc):
    references = {}
    try:
        with open("references.json", "r") as json_data:
                references = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    references[name]["age"] = age
    references[name]["height"] = height
    references[name]["description"] = desc

    for attach in ctx.message.attachments:
        references[name]['referenceimage'] = str(attach.url)

    with open("references.json", "w") as json_data:
        json_data.write(json.dumps(references))

    await ctx.send(f"{name}'s everything has been updated")




@bot.command(name = "update.reference.image")
async def update_reference_image(ctx, name):
    references = {}
    try:
        with open("references.json", "r") as json_data:
                references = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    if name in references:
        for attach in ctx.message.attachments:
            references[name]['referenceimage'] = (str(attach.url))
    
    with open("references.json", "w") as json_data:
        json_data.write(json.dumps(references))
            
    await ctx.send(f"{name}'s reference image updated")


@bot.command(name = "image.add")
async def image_add(ctx, name):
    references = {}
    try:
        with open("references.json", "r") as json_data:
                references = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    if name in references:
        for attach in ctx.message.attachments:
            references[name]['images'].append(str(attach.url))
            

    with open("references.json", "w") as json_data:
        json_data.write(json.dumps(references))

    await ctx.send(f"{name} image added!")


@bot.command(name = "image.get")
async def image_get(ctx, name, index):
    references = {}
    try:
        with open("references.json", "r") as json_data:
                references = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    if index == "all":
        for entry in references[name]["images"]:
            await ctx.send(entry)
    else:
        image = references[name]["images"][int(index)-1]
        await ctx.message.delete()
        await ctx.send(image)

@bot.command(name = "image.remove")
async def image_add(ctx, name, index):
    references = {}
    try:
        with open("references.json", "r") as json_data:
                references = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    try:
        references[name]["images"].pop(int(index)-1)
        
        with open("references.json", "w") as json_data:
            json_data.write(json.dumps(references))

        await ctx.send(f"{name} image removed")
    except:
        await ctx.send("Index does not exist")
            

    
    

@bot.command(name = "reference")
async def reference(ctx, name):
    references = {}
    try:
        with open("references.json", "r") as json_data:
                references = json.load(json_data)
    except:
        await ctx.send("reference file could not be opened, contact D0GU#5777")

    age = (str(references[name]['age']))
    height = (str(references[name]['height']))
    desc = references[name]['description']
    image = references[name]['referenceimage']

    if name in references:
        embed = discord.Embed(title=name, description="Character Reference", color=0x73d216)
        embed.add_field(name="Age", value=age, inline=True)
        embed.add_field(name="Height", value=(height+"cm"), inline=True)
        embed.add_field(name="Description", value=desc, inline=False)
        embed.set_image(url=image)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Character not in references")



#----------------------#
# Monster Encyclopedia #
# ---------------------#


@bot.command(name = "entry.list")
async def entry_list(ctx):
    encyclopedia = {}
    try:
        with open("encyclopedia.json", "r") as json_data:
                encyclopedia = json.load(json_data)
    except:
        await ctx.send("encyclopedia file could not be opened, contact D0GU#5777")

    

    embed = discord.Embed(title="Monster Encyclopedia 1", description="Listing", color=0x73d216)
    i = 0
    listnum = 1
    for entry in encyclopedia:
        print(entry)
        if i < 25:  
            embed.add_field(name=entry, value=encyclopedia[entry]['species'] , inline=True)
            i+=1
        else:
            listnum += 1
            await ctx.send(embed=embed)
            embed = discord.Embed(title=f"Monster Encyclopedia {listnum}", description="Listing", color=0x73d216)
            i = 0

    await ctx.send(embed=embed)
    

@bot.command(name = "create.entry")
async def create_entry(ctx, entry):
    encyclopedia = {}
    try:
        with open("encyclopedia.json", "r") as json_data:
                encyclopedia = json.load(json_data)
    except:
        await ctx.send("encyclopedia file could not be opened, contact D0GU#5777")

    if entry in encyclopedia:
        await ctx.send("Entry already in encyclopedia")
    else:
        encyclopedia[entry] = {
            "monsterid": "",
            "species": "",
            "threatlevel": "",
            "height": "",
            "maturity": "",
            "lore": "",
            "referenceimage": "",
            "images": []
        }
        with open("encyclopedia.json", "w") as fileout:
            fileout.write(json.dumps(encyclopedia))
        await ctx.send(f"Entry for {entry} has been created")

@bot.command(name = "update.entry.name")
async def create_entry(ctx, entry, new_entry):
    encyclopedia = {}
    try:
        with open("encyclopedia.json", "r") as json_data:
                encyclopedia = json.load(json_data)
    except:
        await ctx.send("encyclopedia file could not be opened, contact D0GU#5777")

    if entry in encyclopedia:
        encyclopedia[new_entry] = encyclopedia[entry]
    else:
        await ctx.send(await ctx.send(f"No entry with ID {entry}"))


    with open("encyclopedia.json", "w") as fileout:
        fileout.write(json.dumps(encyclopedia))
    await ctx.send(f"Id for {new_entry} has been updated")


@bot.command(name = "update.entry")
async def update_entry(ctx, entry, parameter: str, content):
    encyclopedia = {}
    try:
        with open("encyclopedia.json", "r") as json_data:
                encyclopedia = json.load(json_data)
    except:
        await ctx.send("encyclopedia file could not be opened, contact D0GU#5777")
    
    if parameter == "monsterid":
        encyclopedia[entry]["monsterid"] = content
    elif parameter == "species":
        encyclopedia[entry]["species"] = content
    elif parameter == "threatlevel":
        encyclopedia[entry]["threatlevel"] = content
    elif parameter == "height":
        encyclopedia[entry]["height"] = content
    elif parameter == "maturity":
        encyclopedia[entry]["maturity"] = content
    elif parameter == "lore":
        encyclopedia[entry]["lore"] = content


    with open("encyclopedia.json", "w") as json_data:
        json_data.write(json.dumps(encyclopedia))

    await ctx.send(f"{entry}'s {parameter} has been updated")


@bot.command(name = "update.entry.all")
async def update_entry_all(ctx, entry, species, threatlevel, height, maturity, lore):
    encyclopedia = {}
    try:
        with open("encyclopedia.json", "r") as json_data:
                encyclopedia = json.load(json_data)
    except:
        await ctx.send("encyclopedia file could not be opened, contact D0GU#5777")
    
    encyclopedia[entry]["monsterid"] = entry    
    encyclopedia[entry]["species"] = species
    encyclopedia[entry]["threatlevel"] = threatlevel
    encyclopedia[entry]["height"] = height
    encyclopedia[entry]["maturity"] = maturity
    encyclopedia[entry]["lore"] = lore

    for attach in ctx.message.attachments:
            encyclopedia[entry]['referenceimage'] = str(attach.url)

    with open("encyclopedia.json", "w") as json_data:
        json_data.write(json.dumps(encyclopedia))

    await ctx.send(f"{entry}'s everything has been updated")


@bot.command(name = "update.entry.image")
async def update_entry_image(ctx, entry):
    encyclopedia = {}
    try:
        with open("encyclopedia.json", "r") as json_data:
                encyclopedia = json.load(json_data)
    except:
        await ctx.send("encyclopedia file could not be opened, contact D0GU#5777")

    if entry in encyclopedia:
        for attach in ctx.message.attachments:
            encyclopedia[entry]['referenceimage'] = str(attach.url)
    
    with open("encyclopedia.json", "w") as json_data:
        json_data.write(json.dumps(encyclopedia))
            
    await ctx.send(f"{entry}'s reference image updated")


@bot.command(name = "entry.image.add")
async def entry_image_add(ctx, entry):
    encyclopedia = {}
    try:
        with open("encyclopedia.json", "r") as json_data:
                encyclopedia = json.load(json_data)
    except:
        await ctx.send("encyclopedia file could not be opened, contact D0GU#5777")

    if entry in encyclopedia:
        for attach in ctx.message.attachments:
            encyclopedia[entry]["images"].append(str(attach.url))

    with open("encyclopedia.json", "w") as json_data:
        json_data.write(json.dumps(encyclopedia))

    await ctx.send(f"{entry} image added!")


@bot.command(name = "entry.image.get")
async def entry_image_get(ctx, entry, index):
    encyclopedia = {}
    try:
        with open("encyclopedia.json", "r") as json_data:
                encyclopedia = json.load(json_data)
    except:
        await ctx.send("encyclopedia file could not be opened, contact D0GU#5777")

    if index == "all":
        for image in encyclopedia[entry]["images"]:
            await ctx.send(image)
    else:
        image = encyclopedia[entry]["images"][int(index)-1]
        await ctx.message.delete()
        await ctx.send(image)

@bot.command(name = "entry.image.remove")
async def entry_image_remove(ctx, entry, index):
    encyclopedia = {}
    try:
        with open("encyclopedia.json", "r") as json_data:
                encyclopedia = json.load(json_data)
    except:
        await ctx.send("encyclopedia file could not be opened, contact D0GU#5777")

    try:
        encyclopedia[entry]["images"].pop(int(index)-1)
        with open("encyclopedia.json", "w") as json_data:
            json_data.write(json.dumps(encyclopedia))

        await ctx.send(f"{entry} image removed!")
    except:
        await ctx.send("Index does not exist")

    
    

@bot.command(name = "entry")
async def entry(ctx, entry):
    encyclopedia = {}
    try:
        with open("encyclopedia.json", "r") as json_data:
                encyclopedia = json.load(json_data)
    except:
        await ctx.send("encyclopedia file could not be opened, contact D0GU#5777")

    species = (str(encyclopedia[entry]['species']))
    threatlevel = (str(encyclopedia[entry]['threatlevel']))
    height = (str(encyclopedia[entry]['height']))
    maturity = (str(encyclopedia[entry]['maturity']))
    lore = encyclopedia[entry]['lore']

    if entry in encyclopedia:
        embed = discord.Embed(title=entry, description="Monster ID", color=0x73d216)
        embed.add_field(name="Species", value=species, inline=True)
        embed.add_field(name="Threat Level", value=threatlevel, inline=False)
        embed.add_field(name="Height", value=(height + "cm"), inline=False)
        embed.add_field(name="Maturity", value=maturity, inline=False)
        embed.add_field(name="Lore", value=lore, inline=False)
        embed.set_image(url=encyclopedia[entry]['referenceimage'])
        await ctx.send(embed=embed)
    else:
        await ctx.send("Entry not in Encyclopedia")





bot.run(TOKEN)