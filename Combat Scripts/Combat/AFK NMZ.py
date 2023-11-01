# import libraries
import pygetwindow as gw
import pyautogui as pg
import time
import numpy as np
# define global variables
X = 42 # x-coordinate pixels till next inventory slot. 2560x1440 resolution.
Y = 36 # y-coordinate pixels till next inventory slot. 2560x1440 resolution.
empty_slot = (62, 53, 41) # RGB for empty inventory slot
level_up = (182, 168, 138) # RGB for level-up message background

# get Runelite window
USERNAME = 'Aragorn GI' # CHANGE ME!
window = gw.getWindowsWithTitle(f'RuneLite - {USERNAME}')[0]
title = f'RuneLite - {USERNAME}'
window.activate()

def click(x,y):
	pg.moveTo(x,y)
	time.sleep(0.1)
	pg.click()

def rclick(x,y):
	pg.moveTo(x,y)
	time.sleep(0.1)
	pg.rightClick()

def sleep(seconds):
	time.sleep(seconds)

def clickCenter(image,title=title,confidence=.95,sleep=0):
	center = pg.center(pg.locateOnWindow(image,title,confidence=confidence))
	pg.moveTo(center.x,center.y)
	time.sleep(0.1)
	pg.click()
	time.sleep(sleep) # additional sleep beyond 0.1s

def rclickCenter(image,title=title,confidence=.95,sleep=0):
	center = pg.center(pg.locateOnWindow(image,title,confidence=confidence))
	pg.moveTo(center.x,center.y)
	time.sleep(0.1)
	pg.rightClick()
	time.sleep(sleep) # additional sleep beyond 0.1s

def getTime():
	t = time.localtime()
	current_time = time.strftime("%I:%M:%S %p",t)
	print(current_time)

######################################################################################################################

# 48 DOSES OVERLOAD.
# 60 DOSES OF ABSORB.
# LOCATOR ORB!

# SET SLOT 1 X,Y COORDS!!!
slot1_x = 2093
slot1_y = 572

# SET YOUR QUICK PRAYERS: RAPID HEAL & PIETY!!!
print('\nSET YOUR QUICK PRAYERS TO RAPID HEAL AND PIETY!!!\n')

# print start time
print('Program starts at:'), getTime()

# define locator orb function (40 points of damage)
def locatorOrb(): # click 4x
	clickCenter('images\\locator-orb.png',sleep=0.3)
	pg.click(), sleep(0.3)
	pg.click(), sleep(0.3)
	pg.click(), sleep(0.3)

# define prayer flick function
def flickPrayer():
	mouse = pg.position() # get current mouse position
	clickCenter('images\\quick-prayer.png',confidence=.7) # turn on prayer
	pg.click(), sleep(0.1) # turn off prayer
	pg.moveTo(mouse.x,mouse.y) # move mouse back

# define absorb drinking functions
def AbsorbR4(): # drink absorbs across row 4
	click(slot1_x,slot1_y+3*Y)
	click(slot1_x+X,slot1_y+3*Y)
	click(slot1_x+2*X,slot1_y+3*Y)
	click(slot1_x+3*X,slot1_y+3*Y)

def AbsorbR5(): # drink absorbs across row 5
	click(slot1_x,slot1_y+4*Y)
	click(slot1_x+X,slot1_y+4*Y)
	click(slot1_x+2*X,slot1_y+4*Y)
	click(slot1_x+3*X,slot1_y+4*Y)

def AbsorbR6(): # drink absorbs across row 6
	click(slot1_x,slot1_y+5*Y)
	click(slot1_x+X,slot1_y+5*Y)
	click(slot1_x+2*X,slot1_y+5*Y)
	click(slot1_x+3*X,slot1_y+5*Y)

# drink 1-dose of overload from slot 2
click(slot1_x+X,slot1_y) # 0.1s
print('\nDrinking from overload in slot 2.'), getTime()
sleep(10) # 10s

# flick prayer
flickPrayer() # 0.2s

# more locator orb to 1 hp
locatorOrb() # 1.2s
locatorOrb() # 1.2s

# drink initial absorbs to 1000
AbsorbR6() # 0.4s
AbsorbR6() # 0.4s
for i in range(4): # 1.2s
	click(slot1_x,slot1_y+6*Y) # absorb in slot 25
	click(slot1_x+X,slot1_y+6*Y) # absorb in slot 26
	click(slot1_x+2*X,slot1_y+6*Y) # absorb in slot 27

# flick prayer
flickPrayer() # 0.2s

## 14.9s estimated total delay from above
### 20s from getTime() = 5s difference

# adjust sleep to reach total delay of 30s
sleep(30-20)

# print time
print('\nTime after initialization, should be 30s after start:'), getTime()

# flick prayer for 270s to reach total of 5 minutes (300s) for next overload
for i in range(9): # 9 sets of 30s = 4.5 min = 270s
    flickPrayer() # 0.2s
    sleep(29.8) # wait a total of 30s

# print time
print('\nShould be 5 mins after start:'), getTime(), print('\n')

# overload slot 2
for j in range(3): # drink 3 remaining doses overload
	# drink overload
	click(slot1_x+X,slot1_y) # 0.1s
	print('Drinking from overload in slot 2.')
	getTime()
	# DRINK ABSORBS ROW 4
	AbsorbR4() # 0.4s
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')

# overload slot 1
for j in range(4): # drink 4 doses overload
	# drink overload
	click(slot1_x,slot1_y)
	print('Drinking from overload in slot 1.')
	getTime()
	# DRINK ABSORBS ROW 6
	AbsorbR6()
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')

# overload slot 3
for j in range(4): # drink 4 doses overload
	# drink overload
	click(slot1_x+2*X,slot1_y)
	print('Drinking from overload in slot 3.')
	getTime()
	# DRINK ABSORBS ROW 4
	AbsorbR4()
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')

# overload slot 4
for j in range(4): # drink 4 doses overload
	# drink overload
	click(slot1_x+3*X,slot1_y)
	print('Drinking from overload in slot 4.')
	getTime()
	# DRINK ABSORBS ROW 4
	AbsorbR4()
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')

# overload slot 5
for j in range(4): # drink 4 doses overload
	# drink overload
	click(slot1_x,slot1_y+Y)
	print('Drinking from overload in slot 5.')
	getTime()
	# DRINK ABSORBS ROW 4
	AbsorbR4()
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')

# overload slot 6
for j in range(4): # drink 4 doses overload
	# drink overload
	click(slot1_x+X,slot1_y+Y)
	print('Drinking from overload in slot 6.')
	getTime()
	# DRINK ABSORBS ROW 5
	AbsorbR5()
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')

# overload slot 7
for j in range(4): # drink 4 doses overload
	# drink overload
	click(slot1_x+2*X,slot1_y+Y)
	print('Drinking from overload in slot 7.')
	getTime()
	# DRINK ABSORBS ROW 5
	AbsorbR5()
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')

# overload slot 8
for j in range(4): # drink 4 doses overload
	# drink overload
	click(slot1_x+3*X,slot1_y+Y)
	print('Drinking from overload in slot 8.')
	getTime()
	# DRINK ABSORBS ROW 5
	AbsorbR5()
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')

# overload slot 9
for j in range(4): # drink 4 doses overload
	# drink overload
	click(slot1_x,slot1_y+2*Y)
	print('Drinking from overload in slot 9.')
	getTime()
	# DRINK ABSORBS ROW 5
	AbsorbR5()
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')

# overload slot 10
for j in range(4): # drink 4 doses overload
	# drink overload
	click(slot1_x+X,slot1_y+2*Y)
	print('Drinking from overload in slot 10.')
	getTime()
	# DRINK ABSORBS ROW 6
	AbsorbR6()
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')

# overload slot 11
for j in range(4): # drink 4 doses overload
	# drink overload
	click(slot1_x+2*X,slot1_y+2*Y)
	print('Drinking from overload in slot 11.')
	getTime()
	# DRINK ABSORBS ROW 6
	AbsorbR6()
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')

# overload slot 12
for j in range(4): # drink 4 doses overload
	# drink overload
	click(slot1_x+3*X,slot1_y+2*Y)
	print('Drinking from overload in slot 12.')
	getTime()
	# DRINK ABSORBS ROW 6
	AbsorbR6()
	# flick prayer to 30s
	flickPrayer() # 0.2s
	sleep(24.3) # sleep to 30s (minus 5s from getTime, 1s leeway)
	# flick prayer for 4.5 mins until next overload
	for i in range(9): # 9 sets of 30s = 270s = 4.5 mins
		flickPrayer() # 0.2s
		sleep(29.8) # wait a total of 30s
print('\n')