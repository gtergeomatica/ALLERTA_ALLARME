#!/usr/bin/python
#--------------------------------------
#     ___                  
#    / _ )___ __________ __
#   / _  / -_) __/ __/ // /
#  /____/\__/_/ /_/  \_, / 
#                  /___/  
#     ___            __    _       
#    / _ )___  ___  / /__ (_)__ ___
#   / _  / _ \/ _ \/  '_// / -_|_-<
#  /____/\___/\___/_/\_\/_/\__/___/
#
#     Berry Bookies Horse Race Game
#
# First steps in teaching myself Python and 
# using Berryclip includes selection with
# Berryclip, racing with Berryclip, odds 
# assignment & calculation,horse names,
# main loop & feedback by Jim Flewker
# - thanks to Matt Hawkins for Berryclip
#
# Author   : Jim Flewker
# Date     : 16/10/2013
#
# Modified : Matt Hawkins
# Date     : 19/10/2013
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import RPi.GPIO as GPIO
import time
import random

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

# List of LED GPIO numbers, GREEN - YELLOW - RED
Horses = [11,9,10,22,17,4]

# List of 12 betting odds factors and associated dictionary of strings
odds = [10,2,4,2.5,7,1,15,1.5,8,6,3,11]
o_strings = {1:'evens',2:'2-1',4:'4-1',2.5:'5-2',7:'7-1',10:'10-1',15:'15-1',11:'11-1',8:'8-1',6:'6-1',3:'3-1',1.5:'3-2'}

# Set Switch GPIO as input
GPIO.setup(7 , GPIO.IN)

# Configure GPIO8 as an output Buzzer
GPIO.setup(8, GPIO.OUT)

# Set up the GPIO pins as outputs and set False
for x in range(6):
  GPIO.setup(Horses[x], GPIO.OUT)
  GPIO.output(Horses[x], False)
  
# Turn Buzzer off
GPIO.output(8, False)

# Horse name lists, 14 in each
horses_green  = ['Jess of Greendale','Mean Green Machine','Green Shoots','The Green Door','Verdigris','Guiseppe Verdi','Lincoln Green','50 Shades of Green','Verdana','Green T','Grassed Up','Vert-I-Go','Miss Moss','Pistachio']
horses_yellow = ['Captain Custard','Keen As Mustard','Yellow Riever','Mellow Yellow','Daffy Dill','Lil Buttercup','Dan de Lion','Yellowbelly','Amarillo Way','Amber Vector','Golden Fetlocks','Lemon Drizzle','Scary Canary','Maizie Doats']
horses_red    = ['Red Rump','Red Myst','Le Cheval Rouge','Ruddy Miracle','The Big Blusher','El Caballo Rojo','King Crimson','Scarlet Fever','Bo Red','Helen Reddy','The Martian','Danger Ranger','Cardinal Syn','Raspberry Pie']

# THESE VALUES CAN BE CUSTOMISED:
# start with 100 in funds - change the funds value to increase starting pot
funds=100

# set a fixed amount for each bet, this can also be customised
bet=10

# wait time in seconds between horses in the selection/betting routine
waiting_time=8

# LEAVE THESE AS IS
race_number=1
start_betting=True
base_funds=funds

# FUNCTIONS

def horse_naming(hs_green,hs_yellow,hs_red):
    gran1=random.randint(0,13)
    gran2=gran1
    while gran2==gran1:
        gran2=random.randint(0,13)
    yran1=random.randint(0,13)
    yran2=yran1
    while yran2==yran1:
        yran2=random.randint(0,13)
    rran1=random.randint(0,13)
    rran2=rran1
    while rran2==rran1:
        rran2=random.randint(0,13)
    hnames_list=[hs_green[gran1],hs_green[gran2],hs_yellow[yran1],hs_yellow[yran2],hs_red[rran1],hs_red[rran2]]
    return hnames_list
    

def horse_selection(funds,b_odds,od_strings,hnames_list):
  for x in range(6):
      GPIO.output(Horses[x], False)
  switch_pressed=False
  selected_horse=-1
  current_horse=0
  print('BETTING ON RACE NUMBER '+str(race_number))
  print('Your current funds: '+str(funds))
  print('Place your bet using Berryclip.')
  while switch_pressed==False:
      if current_horse==6:
          current_horse=0
      GPIO.output(Horses[current_horse],True)
      horse_name=hnames_list[current_horse]
      h=b_odds[current_horse]
      odds_st=od_strings[h]
      print('-'*50)
      print('Horse is '+horse_name+'.')
      print('Odds for this horse are: '+odds_st)
      print('''To bet on this horse, press the BUTTON while its light is on. Otherwise, just WAIT for the next horse!''')
      start_time=time.time()
      now_time=start_time
      target_time=start_time+waiting_time

      while switch_pressed==False and now_time<target_time:
          if GPIO.input(7)==1:
              switch_pressed=True
              GPIO.output(8, True)
              time.sleep(0.4)
              GPIO.output(8, False)
          else:
              now_time=time.time()
              if now_time>=target_time:
                  GPIO.output(Horses[current_horse],False)
                  current_horse=current_horse+1
                  GPIO.output(8, True)
                  time.sleep(0.1)
                  GPIO.output(8, False)
                  time.sleep(0.05)
                  GPIO.output(8, True)
                  time.sleep(0.1)
                  GPIO.output(8, False)
  print('You placed a bet on '+horse_name+', horse number '+str(current_horse+1)+'.')
  funds=funds-bet
  return current_horse,funds
 
def race(race_number):
    print('RACE NUMBER '+str(race_number))
    print('Your current funds: '+str(funds))
    for x in range(6):
        GPIO.output(Horses[x], False)
    start_time=time.time()
    now_time=start_time
    target_time=start_time+20
    old_horse=0
    result=race_action(target_time,0)
    return result
    
def race_action(target_time,old_horse):
    print("THEY'RE OFF!")
    now_time=time.time()
    hoss=''
    while now_time<target_time:
        GPIO.output(Horses[old_horse],False)
        lead_horse=random.randint(0,5)
        GPIO.output(Horses[lead_horse],True)
        old_horse=lead_horse
        hoss=hoss+str(lead_horse+1)+'/> '
        print hoss
        time.sleep(1)
        now_time=time.time()

    horse_name=str(lead_horse+1)
    print('HORSE '+horse_name+' WON')
    time.sleep(2)
    return lead_horse

def randomise_odds():
    temp_odds=odds
    random.shuffle(temp_odds)
    return temp_odds

# END OF FUNCTIONS
print('')
print('                               _(\_/)     ')
print('                             ,((((^`\     ')
print('                            ((((  (6 \    ')
print('                          ,((((( ,    \   ')
print('      ,,,_              ,(((((  /"._  ,`, ')
print('     ((((\\ ,...       ,((((   /    `-.-''')
print('     )))  ;''    `"''"''""((((   (        ')
print('    (((  /            (((      \  ')
print('     )) |                      |  ')
print('    ((  |        .       ''     | ')
print('    ))  \     _ ''      `t   ,.'')')
print('    (   |   y;- -,-""''"-.\   \/  ')
print('    )   / ./  ) /         `\  \   ')
print('       |./   ( (           / /''  ')
print('       ||     \\          //''|   ')
print('       ||      \\       _//''||   ')
print('       ||       ))     |_/  ||    ')
print('       \_\     |_/          ||    ')
print('       `''"                  \_\  ')
print('                            `''"  ') 
print('')
print('BET WITH BERRYCLIP BOOKIES')
print('-'*50)

# MAIN LOOP BELOW

while start_betting==True or continue_betting==True:
    bodds=randomise_odds()
    names_list=horse_naming(horses_green,horses_yellow,horses_red)
    print('HORSES AND ODDS FOR THIS RACE')
    print('-'*50)
    for n in range(len(names_list)):
        o_key=bodds[n]
        print names_list[n] +' at '+ o_strings[o_key]
    print('-'*50)
    chosen_horse,funds=horse_selection(funds,bodds,o_strings,names_list)
    print('-'*50)
    result=race(race_number)
    winner_name=names_list[result]
    winner_odds_key=bodds[result]
    factor=winner_odds_key
    winning_odds=o_strings[winner_odds_key]
    win_amount=int(bet+(bet*factor))
    print('-'*50)
    print('The winner was '+winner_name)
    print('Winning odds were '+winning_odds)

    if chosen_horse==result:
        funds=funds+win_amount
        print('C O N G R A T U L A T I O N S !')
        print('You backed the winner and won '+str(win_amount)+' including your stake.')
    else:
        print('A bet on the winner won '+str(win_amount)+' including stake.')
        print('Better luck next time.')
        
    print('-'*50)
    print('Funds: '+str(funds))

    if funds>=bet:
        response=raw_input('Bet on another race y/n?')
        response=response.lower()
        if response.startswith('n'):
            continue_betting=False
            break
        else:
            continue_betting=True
            race_number=race_number+1
    else:
        response=raw_input('You have run out of betting funds. Start again y/n?')
        response=response.lower()
        if response.startswith('y'):
            start_betting=True
            race_number=1
            funds=100
        else:
            start_betting=False
            break

# END OF MAIN LOOP

# Feedback & Tidy

print('-'*50)
print('YOUR GAMBLING CAREER:')
r_string=' race'+('s'*(race_number>1))+'.'
print('You bet on '+str(race_number)+r_string)
if funds>base_funds:     
    profit=funds-100
    print('And you made a PROFIT of '+str(profit)+'.')
elif funds==base_funds:
    print('Phew! You broke even with '+str(base_funds)+'.')
else:
    loss=base_funds-funds
    print('And you have '+str(funds)+' left, a loss of '+str(loss)+'.')
    print('We bookies always win in the long run, you know.')

GPIO.cleanup()