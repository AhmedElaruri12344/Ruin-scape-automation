# import libraries
import pygetwindow as gw
import pyautogui as pg
import numpy as np
import time
import cv2
import keyboard
import math
import operator
import datetime
# define global variables
X = 42 # x-coordinate pixels till next inventory slot. 2560x1440 resolution.
Y = 36 # y-coordinate pixels till next inventory slot. 2560x1440 resolution.
empty_slot = (62, 53, 41) # RGB for empty inventory slot
level_up = (182, 168, 138) # RGB for level-up message background

# get Runelite window
USERNAME = 'slendiemania' # CHANGE ME!
window = gw.getWindowsWithTitle(f'RuneLite - {USERNAME}')[0]
title = f'Runelite - {USERNAME}'
window.activate()

#####################################################################################################
#                            FUNCTION DECLARATION & DERIVED FUNCTIONS                               #
#####################################################################################################

# define custom functions
def sleep(seconds):
	time.sleep(seconds)

def click(x,y):
	pg.moveTo(x,y)
	time.sleep(0.1)
	pg.click()

def clickCenter(image,title=title,confidence=.95,sleep=0):
	center = pg.center(pg.locateOnWindow(image,title,confidence=confidence))
	pg.moveTo(center.x,center.y)
	time.sleep(0.1)
	pg.click()
	time.sleep(sleep) # additional sleep beyond 0.1s

"""def logoutHandler():

	def getTime():
		t = time.localtime()
		current_time = time.strftime("%I:%M:%S %p",t)
		print(current_time)

	if pg.locateOnWindow('Logout Handler\\disconnected.png',title,confidence=.9):
		print('Forcibly logged out from server at:'), getTime()
		clickCenter('Logout Handler\\disconnected.png',sleep=1) # click OK on "You were disconnected from the server."
		clickCenter('Logout Handler\\existing-user.png',sleep=1) # click on Existing User
		pg.typewrite('ibot7days',interval=.1) # type in password
		pg.press('enter') # login
		time.sleep(10) # delay for login
		clickCenter('Logout Handler\\CHTP.png',confidence=.9,sleep=2) # "CLICK HERE TO PLAY"
		return True
	elif pg.locateOnWindow('Logout Handler\\existing-user.png',title,confidence=.9):
		clickCenter('Logout Handler\\existing-user.png',sleep=1) # click on Existing User
		time.sleep(1)
		pg.typewrite('ibot7days',interval=.1) # type in password
		pg.press('enter') # login
		time.sleep(10) # delay for login
		clickCenter('Logout Handler\\CHTP.png',confidence=.9,sleep=2) # "CLICK HERE TO PLAY"
		return True
	else:
		return False"""

def findColorMiddle(window,boundaries):
	img = pg.screenshot(region=(window.left,window.top,window.width,window.height))
	img = cv2.cvtColor(np.array(img),cv2.COLOR_BGR2RGB)
	for (lower,upper) in boundaries:
		lower = np.array(lower,dtype="uint8")
		upper = np.array(upper,dtype="uint8")
		mask = cv2.inRange(img, lower, upper)
		img = cv2.bitwise_and(img,img, mask = mask)
		img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	npcoord = cv2.findNonZero(img.astype(np.uint8))
	if npcoord is None:
		return None,None
	else:
		coord = tuple(npcoord)
		x,y = float(coord[0][0][0]),float(coord[0][0][1])
		x,y = int(x),int(y)
		return x,y

#####################################################################################################
#                                         MAIN FUNCTION                                             #
#####################################################################################################

print('\nPROGRAM STARTING!\n')

# ENTITY HIDER, HIDE LOCAL PLAYER 2D.

NPC = [([225, 225, 0],[255, 255, 0])]
slot_1 = (2096,1123)
counter = 1

# turn on auto-retaliate if necessary
pg.press('f1'), sleep(0.6) # select combat options
try:
	clickCenter('images\\auto-retaliate.png',confidence=.9)
except:
	pass
pg.press('f2') # select inventory

while True:
	# check to see if logged out
	"""if logoutHandler() == False:
		pass"""
	"""# try and dragon battleaxe spec
	if pg.locateOnWindow('images\\full-spec.png',title,confidence=.9):
		clickCenter('images\\dbaxe.png',confidence=.7,sleep=0.2)
		#click(slot_1[0],slot_1[1]), sleep(0.2)
		clickCenter('images\\full-spec.png',title,confidence=.9), sleep(0.2)
		clickCenter('images\\ob-sword.png',confidence=.7,sleep=0.2)
		#clickCenter('images\\dscim.png',confidence=.7,sleep=0.6)
		#click(slot_1[0],slot_1[1]), sleep(0.2)
	else:
		pass"""
	# attack a yak
	if any(findColorMiddle(window,NPC)):
		x,y = findColorMiddle(window,NPC)
		click(x,y)
		print('Approximately',counter,'Yaks killed.')
		counter+=1
		sleep(2) # yaks + xp globes
		#sleep(5) # experiments + xp globes
	else:
		continue
	# check to see if still in combat
	if pg.locateOnWindow('images\\combat4.png',title,confidence=.8):
	
		while pg.locateOnWindow('images\\combat4.png',title,confidence=.8):
			sleep(0.1)
			
			pg.locateOnWindow('images\\combat4.png',title,confidence=.8)
		
	else:
		continue