import discord
import os
import random
import time
from discord.ext.commands import Bot
bot = Bot(command_prefix=';')
secure_random = random.SystemRandom()

#start and set status
@bot.event
async def on_ready():
	print(f'Logged in as {bot.user}')

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))

  
  

#ask stuff
answers = ('The answer was inside of you all along','Ask someone else','Mayhaps...','Almost certainly','The cheese holds your answer','insert clever answer here','Yes, quite','Why would you care?','My sources say yes','Absolutely not','Of course','Uhhh... yeah, sure','Hard to tell','Obama knows')
@bot.command(name='ask')
async def ask(ctx):
  await ctx.send('**'+(secure_random.choice(answers))+'**')

#howdumb
@bot.command(name='howdumb')
async def howdumb(ctx, arg):
  percent = random.randint(0,100)
  await ctx.send('**'+arg+' is '+str(percent)+'%'+' dumb'+'**')

#roll 2 dices
@bot.command(name='roll')
async def roll(ctx):
  rollres = random.randint(1,6)
  rollres1 = random.randint(1,6)
  rolltot = rollres + rollres1
  await ctx.send('**'+str(rollres)+' + '+str(rollres1)+' = '+str(rolltot)+'**')

#rock paper scissors
@bot.command(name='rps')
async def rps(ctx, user_choice):
  rpsGame = ['rock', 'paper', 'scissors'] 
  if user_choice.lower() in rpsGame:
    await ctx.send('**'f'Choice: `{user_choice}`\nBot Choice: `{random.choice(rpsGame)}`''**')
  elif user_choice.lower() not in rpsGame:
    await ctx.send('**Error** This command only works with rock, paper, or scissors.')

#conspire
@bot.command(name='conspire')
async def conspire(ctx, userchoice):


token = ""
bot.run(token, bot = True)