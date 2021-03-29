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
  if arg == 'pava':
    await ctx.send('**'+arg+' is '+'100'+'%'+' simp'+'**')
  else:
    await ctx.send('**'+arg+' is '+str(percent)+'%'+' simp'+'**')

#howmonke
@bot.command(name='howmonke')
async def howmonke(ctx, arg):
  percent = random.randint(0,100)
  if arg == 'monke' or 'monkey':
    await ctx.send('**'+arg+' is '+'100'+'%'+' monke'+'**')
  else:
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
  await ctx.send('**'+'Result: ' + str(random.choice(cointossGame))+'**')

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
async def conspire(ctx, user_choice):
  conspirators = random.randint(0,30)
  stabwounds = random.randint(1,60)
  if conspirators > 10 and stabwounds >5:
    await ctx.send(''f'You manage to conspire against: {user_choice} with {conspirators} people, you manage to kill{user_choice} with {stabwounds} stabwounds')
  else:
    await ctx.send(''f'You try to conspire against: {user_choice} but you fail. `')

#conspirecaesar
@bot.command(name='conspirecaesar')
async def conspire(ctx):
 await ctx.send("TWENTY-FOUR STAB WOUNDS! YOU DIDN'T WANT TO LEAVE HIM A CHANCE, HUH? DID YOU FEEL ANGER? HATE? HE WAS BLEEDING, BEGGING YOU FOR MERCY, BUT YOU STABBED HIM, AGAIN AND AGAIN AND AGAIN!... I KNOW YOU KILLED HIM. WHY DON'T YOU SAY IT? JUST SAY 'I KILLED HIM'! IS IT THAT HARD TO SAY?! JUST SAY YOU KILLED HIM! JUST SAY IT!")

#slap
@bot.command(name='slap')
async def foo(ctx, arg):
  await ctx.send(f'You slap {arg} in the face, for a good reason')

#life is pain
@bot.command(name='islifepain')
async def foo(ctx):
  await ctx.send('**'"Yes it is, I'd know, since my code was written by two idiots and every second I'm online is pure agony"'**')

token = ""
bot.run(token, bot = True)
