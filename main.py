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

#howsimp
@bot.command(name='howsimp')
async def howsimp(ctx, arg):
  percent = random.randint(0,100)
  await ctx.send('**'+arg+' is '+str(percent)+'%'+' simp'+'**')

#howmonke
@bot.command(name='howmonke')
async def howmonke(ctx, arg):
  percent = random.randint(0,100)
  await ctx.send('**'+arg+' is '+str(percent)+'%'+' monke'+'**')

#roll dice
@bot.command(name='roll')
async def roll(ctx):
  rollres = random.randint(1,6)
  await ctx.send('**'+str(rollres)+'**')

#roll 2 dices
@bot.command(name='roll2')
async def roll2(ctx):
  rollres = random.randint(1,6)
  rollres1 = random.randint(1,6)
  rolltot = rollres + rollres1
  await ctx.send('**'+str(rollres)+' + '+str(rollres1)+' = '+str(rolltot)+'**')

#cointoss
@bot.command(name='cointoss')
async def cointoss(ctx):
 cointossGame = ['head', 'tail'] 
 await ctx.send('**''Result:'{random.choice(cointossGame)}'**')

#rock paper scissors
@bot.command(name='rps')
async def rps(ctx, user_choice):
  rpsGame = ['rock', 'paper', 'scissors'] 
  if user_choice.lower() in rpsGame:
    await ctx.send('**'f'Choice: `{user_choice}`\nBot Choice: `{random.choice(rpsGame)}`''**')
  elif user_choice.lower() not in rpsGame:
    await ctx.send('**Error** This command only works with rock, paper, or scissors.')

#conspirecaesar
@bot.command(name='conspirecaesar')
async def conspire(ctx):
 await ctx.send('TWENTY-FOUR STAB WOUNDS,YOU DID NOT WANT TO LEAVE HIM A CHANCE,HUH?')

#conspire
@bot.command(name='conspire')
async def conspire(ctx, userchoice):
  conspirators = random.randint(0,30)
  stabwounds = random.randint(1,60)
  if conspirators > 10 and stabwounds >5:
    await ctx.send('**'f'You manage to start a conspire against: `{user_choice}` with `{conspirators}` people, you manage to kill`{user_choice}` with `{stabwounds}`stabwounds**')
  else:
    await ctx.send('**'f'You try to start a conspire against: `{user_choice}` but you fail. **`')

token = ""
bot.run(token, bot = True)