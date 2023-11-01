import pyautogui as pag
import time
from OSRSutils import drop, locateCenterOnWindow, pixelClick, findColorMiddle, login

'''pswd = pag.password("Enter password","Password Storage")
if pswd == None:
    exit()'''

window = pag.getWindowsWithTitle('Runelite - jonslildoner')[0] #change this to correct window
title = window.title
window.activate()

boundariesb = [([225, 225, 0],[255, 255, 0])] # Used in aerialFishing to find fish spots
boundariesy = [([34,247,250],[34, 247, 250])]

boundariesp = [([245,245,0],[255,255,0])] # CHINS, BGR
boundariesg = [([0,150,0],[0,150,0])] # CHINS
boundariesr = [([20,0,255],[30,20,255])] # CHINS

# define custom functions
def click(x,y):
   pag.moveTo(x,y)
   time.sleep(0.1)
   pag.click()
     

def sleep(seconds):
    time.sleep(seconds)

def aerialFishing():
    while True:
        # look for disconnect reconnect if disconnected
        #if pag.locateOnWindow('Images\\Utils\\Disconnect.png',title,confidence=.9) != None:
            #login(pswd,title)
        # click middle fishing spot
        for z in range(70):
            try:
                x,y = findColorMiddle(window,boundariesb)
            except:
                print("Color not found")
                continue
            if x or y != None:
                pixelClick(x,y,0.5)
        # look for bluegill
        fish = pag.locateOnWindow('Images\\SkillInv\\Bluegill.png',title,confidence = .9)
        while fish != None:
            # cut up a bluegill
            pag.click(fish)
            pag.click(locateCenterOnWindow('Images\\SkillInv\\knife.png',title,confidence = .9))
            # look for bluegill
            fish = pag.locateOnWindow('Images\\SkillInv\\Bluegill.png',title,confidence = .9)
        continue

def chinhunt():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    t = 3.3 # was 3.3
    t2 = 2.69 # was 2.7; 2.6 too short
    while True:
        # look for disconnect reconnect if disconnected
        #if pag.locateOnWindow('Images\\Utils\\Disconnect.png',title,confidence=.9) != None:
            #login(pswd,title)
        if any(findColorMiddle(window,boundariesp)): # lay trap on ground
            counter1+=1
            print('\n',counter1,'expired traps.\n')
            x,y = findColorMiddle(window,boundariesp)
            click(x,y)
            time.sleep(2.79) # 4.99 stable; 2.79 stable
            continue
        elif any(findColorMiddle(window,boundariesg)): # successful trap
            counter2+=1
            print('\n',counter2,'chins caught.\n')
            x,y = findColorMiddle(window,boundariesg)
            click(x,y)
            time.sleep(t)
            click(2096,1127) # click 1st slot box
            time.sleep(t2)
            continue
        elif any(findColorMiddle(window,boundariesr)): # failed trap
            counter3+=1
            print('\n',counter3,'chins escaped.\n')
            x,y = findColorMiddle(window,boundariesr)
            click(x,y)
            time.sleep(t)
            click(2096,1127) # click 1st slot box
            time.sleep(t2)
            sleep(2)
            continue
        else:
            print('nothing to click...waiting')
            time.sleep(0.5)
            continue

if __name__ == '__main__':
    #dic = {'Falconry': rabbitHunt,'AerialFishing': aerialFishing,'Chinchompas': chinhunt}
    #innit = pag.prompt(text='"Falconry": Falconry bot, "AerialFishing": Aerial fishing bot, "Chinchompas": Chincompas bot',title='Hunter Bot Selection',default='AerialFishing')
    #dic[innit]()
    chinhunt()