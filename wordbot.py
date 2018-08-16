import asyncio      
import discord
from discord.ext import commands
token = ""           
client = discord.Client()   
bot = commands.Bot(command_prefix='!')  
#https://discordapp.com/api/oauth2/authorize?client_id=257405403288174592&permissions=8&scope=bot
@bot.event
async def on_ready(): #Print when ready 
    print("BOT READY")          
questionwords = "is", "can", "are","ya'll","wdym","who", "what", "where", "whom", "whose", "why", "which", "how", "when", "howdy"
Greeting = "hello", "hi", "hey", "hola", "yo", "Hello", "Hi", "Hey", "Hola", "Yo"
personal = "i ", " i ", "i'm", "im"
question = "?", "anyone", "right", " wonder "
statement = "time","gay","worse","better","would","break","did","save","broke","is","this","in","its","it's","out"
reaction = "litty", "lit","cool","lol","wow","ha","gg","xd","!"
#"i " in string_lowered or " i " in string_lowered or "i'm" in string_lowered or "im" in string_lowered:
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    string = message.content
    string_lowered = string.lower()
    if message.author.id == "297495225847382016":
        await bot.send_message(message.channel, "Shutup you're dating a freshman")# say hello to a retard
        return
    if string_lowered.startswith(questionwords) or string_lowerd in question and string_lowered in string_lowered:     
        print(message.content + ": question-Conversation")
        await bot.send_message(message.channel, "this is a question and conversation") #question and conversation attacks
        return
    elif message.content.startswith(questionwords) or string_lowered in question:
        print(message.content + ": question")   
        await bot.send_message(message.channel, "this is a question") #question attacks
        return
    elif string_lowered in personal:
         print(message.content + ": personal statement")    
         await bot.send_message(message.channel, "This is a personal statement") # Personal Attacks
         return
    elif string_lowered in statement:
        print(message.content + ": Statement")
        await bot.send_message(message.channel, "this is a Statement")# idk think of somthing 
        return
    elif "you" in string_lowered or "ok" in string_lowered:
        print(message.content + ": Conversation Statement")
        await bot.send_message(message.channel, "This is a Converstaion") # talk to user but slightly attack the person
        return
    elif string_lowerd in reaction:
        print(message.content + ": Reaction")
        await bot.send_message(message.channel, "This is a Reaction")# attack them for thinking its cool to react like that
        return
    elif message.content.startswith(Greeting):
        print(message.content + ": Greeting")
        await bot.send_message(message.channel, "This is a Greeting")# say hello to a retard        
        return
    else:
        print(message.content + " <- Fix this") #did not understand the sentence structure
    
bot.run(token)  