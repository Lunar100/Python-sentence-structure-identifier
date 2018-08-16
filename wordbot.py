import asyncio      
import discord
from discord.ext import commands
token = "NDc5MTA5NTA5MTU2MDQ0ODAx.DlUdTQ.cBLukHYTg5R-A35hjiClkOQNA4Q"
client = discord.Client()
bot = commands.Bot(command_prefix='!')
#https://discordapp.com/api/oauth2/authorize?client_id=257405403288174592&permissions=8&scope=bot
@bot.event
async def on_ready(): #Print when ready 
    print("word knower Ready")  
questionwords = "ARE","are","Are","Ya'll","ya'll","wdym","who", "what", "where", "whom", "whose", "why", "which", "how", "when","Who","WHO","What","WHAT","Where","WHERE","Whom","WHOM","Whose","WHOSE","Why","WHY","Which","WHICH","How","HOW","When","WHEN", "Howdy", "howdy"
Greeting = "hello", "hi", "hey", "hola", "yo", "Hello", "Hi", "Hey", "Hola", "Yo"
@bot.event  
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith(questionwords) and "you" in message.content:      
        print(message.content + ": question-Conversation")
        await bot.send_message(message.channel, "this is a question and conversation") #question and conversation attacks
        return
    elif message.content.startswith(questionwords) or "?" in message.content or "anyone" in message.content:
        print(message.content + ": question")   
        await bot.send_message(message.channel, "this is a question") #question attacks
        return
    elif "personal" in message.content or "I " in message.content or " i " in message.content or " I " in message.content or "I'm" in message.content or "Im" in message.content:
         print(message.content + ": personal statement")    
         await bot.send_message(message.channel, "This is a personal statement") # Personal Attacks
         return 
    elif "you" in message.content:
        print(message.content + ": Conversation Statement")
        await bot.send_message(message.channel, "This is a Converstaion") # talk to user but slightly attack the person
        return
    elif "worse" in message.content or "better" in message.content or "would" in message.content or "break" in message.content or "did" in message.content or "save" in message.content or "broke" in message.content or "is" in message.content or "this" in message.content or "in" in message.content or "its" in message.content or "it's" in message.content or "out" in message.content:
        print(message.content + ": Statement")
        await bot.send_message(message.channel, "this is a Statement")# idk think of somthing 
        return
    elif "litty" in message.content or "lit" in message.content or "Cool" in message.content or "lol" in message.content or "wow" in message.content or "ha" in message.content or "gg" in message.content or "xd" in message.content or "!" in message.content:
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