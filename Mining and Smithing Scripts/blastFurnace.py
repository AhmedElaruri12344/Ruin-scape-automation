import pyautogui
import cv2
import numpy as np
import time
import operator
import pygetwindow as gw
import math
import pynput as pp
from pynput.keyboard import Key, Controller

smithy=True

keyboard = Controller()

### Object Markers 
#       Border Witdh = 5 
#       Remeber Color = Checked
#    BANK MARKER 200, 90, 90, 255
#    CONVEYOR BELT MARKER 90, 90, 200, 255
#    BAR RETRIEVAL MARKER  0, 255, 255, 255
#    TILE 60, 60, 240, 255 (Border = 5)


HAYSTACK = 'screen_grab.png'
USERNAME = 'jonslildoner'  #CHANGE
PASSWORD = 'password' #CHANGE
#####TEMPLATE MATCHING#######
def selectItemOnScreen(needle, click = 'left'):
    needle = cv2.imread(needle, 0)
    width, height = needle.shape[::-1]
    result = findNeedle(needle)
    val_min, val_max, min_loc, maxLoc = cv2.minMaxLoc(result)
    if result.__len__()>0:
        center = ( (maxLoc[0] + width/2, maxLoc[1] + height/2 ) )
        print(center)
        pyautogui.moveTo(center[0], center[1], .2)
        if click == 'left':
            pyautogui.click()
        else:
            pyautogui.rightClick()

def findNeedle(needle):
    haystack= HAYSTACK
    pyautogui.screenshot(haystack)
    haystack = cv2.imread(haystack)
    haystack_g = cv2.cvtColor(haystack, cv2.COLOR_BGR2GRAY)
    return cv2.matchTemplate(haystack_g, needle, cv2.TM_CCOEFF_NORMED)

def checkIfUiElem(needle, conf):
    needle = cv2.imread(needle, 0)
    result = findNeedle(needle)
    val_min, val_max, min_loc, maxLoc = cv2.minMaxLoc(result)
    
    if val_max>conf:
        return True
    else:
        return False

######BANKING##########
def depositAll():
    depositAll = 'images\\bank-deposit-inv.png'
    exit = 'images\\bank-x.png'
    selectItemOnScreen(depositAll)
    time.sleep(0.6)
    #pyautogui.press('escape')
    #selectItemOnScreen(exit)

def coalBag():
    coalBag = 'images\\coal-bag.png'
    
    selectItemOnScreen(coalBag)
    time.sleep(0.6)
    #pyautogui.press('escape')
    #selectItemOnScreen(exit)
def withdrawIron():
    withdrawIron = 'images\\iron-ore.png'

    selectItemOnScreen(withdrawIron)
    time.sleep(0.6)

def startSmithing():
    startSmith = 'images\\c-ball-start.png'
    exit = 'images\\bank-x.png'
    selectItemOnScreen(startSmith)
    time.sleep(0.6)
    #pyautogui.press('escape')
    #selectItemOnScreen(exit)



def isInventoryFull():
    conf = .9
    needle = cv2.imread('images\\emotes.png', 0)
    width, height = needle.shape[::-1]
    result = findNeedle(needle)
    val_min, val_max, min_loc, maxLoc = cv2.minMaxLoc(result)
    result = np.where( result >= conf)
    if result.__len__()>0:
        center = ( (maxLoc[0] + width/2, maxLoc[1] + height/2 ) )
        print(center)
        lastSlot = center[0], center[1] - 47  #38 #47
        print(lastSlot)
        if(pyautogui.screenshot().getpixel(lastSlot) == (62, 53, 41)): #63, 53, 43 #62, 53, 41
            return True
        else:
            return False
              

          

"""def logoutHandler():
    # LOGOUT SCREENSHOTS
    logScreen = 'image-lib\\ui-element\\login-screen.png' 
    password = 'image-lib\\ui-element\\password.png'
    clickToPlay = 'image-lib\\ui-element\\click-to-play.png'
    existingUser = 'image-lib\\ui-element\\existing-user.png'
    ok = 'image-lib\\ui-element\\ok.png'
    if checkIfUiElem(logScreen, .95):
        if checkIfUiElem(ok, .8):
            selectItemOnScreen(ok)
            time.sleep(2)
        if checkIfUiElem(existingUser, .8):
            selectItemOnScreen(existingUser)
            time.sleep(2)
        if checkIfUiElem(password, .8):
            needle = cv2.imread(password, 0)
            width, height = needle.shape[::-1]
            result = findNeedle(needle)
            val_min, val_max, min_loc, maxLoc = cv2.minMaxLoc(result)
            center = ( (maxLoc[0] + width/2, maxLoc[1] + height/2 ) )
            pyautogui.moveTo(center[0]+50, center[1], .5)
            pyautogui.click()
            pyautogui.write(PASSWORD)
            pyautogui.press('enter')
            time.sleep(20)
            if checkIfUiElem(clickToPlay, .8):
                selectItemOnScreen(clickToPlay)
                time.sleep(10)
                return True
            else:
                exit(0)
        else:
            exit(0)
    return False"""

def findObjectCenter(color, nearest = False):
    img= HAYSTACK
    pyautogui.screenshot(img)
    objects = getContours(min_area=10,color = color)
    if objects:
        if nearest:
            window = gw.getWindowsWithTitle(f'Runelite - {USERNAME}')[0]
            coord = (window.left,window.top,window.width,window.height)
            player_spot = (coord[0]+(coord[2]/2), coord[1]+(coord[3]/2))
            nearest_point = objects[0]
            nearest_distance = math.dist(objects[0], player_spot)
            for point in objects:
                distance =math.dist(point, player_spot)
                if distance < nearest_distance:
                    nearest_point = point
                    nearest_distance = distance
            pyautogui.moveTo(nearest_point, duration=.2)
            pyautogui.click()
            return True
        pyautogui.moveTo(objects[0], duration=.2)
        pyautogui.click()
        return True
    return False

def tupleMath(tuple1, tuple2, operation):
    if operation == 1:
       return tuple(map(operator.add, tuple1, tuple2))
    if operation == 2:
       return tuple(map(operator.sub, tuple1, tuple2))

def getContours(min_area = 50, color = False, threshold = (5, 5, 5)):
    img= HAYSTACK
    pyautogui.screenshot(img)
    if color:
        img = cv2.imread(img,cv2.IMREAD_COLOR)
        img = cv2.inRange(img, tupleMath(color,threshold,2), tupleMath(color,threshold,1)) # Remove excess
    else:
        img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    _,threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY) # Converting to binary
    contours,_=cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Detecting shapes
    center_array = []
    for cnt in contours :
        area = cv2.contourArea(cnt)
        # Shortlisting the regions based on there area.
        if area > min_area:
            M = cv2.moments(cnt)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            center_array.append((cX,cY))
    return center_array

def miningGuildBankRock():
    bank = (90,90,200)
    belt = (200, 90, 90)
    tile = (240, 60, 60)
    retrieve = (255, 255, 0)
   
    while True:

      
            
            
            findObjectCenter(bank) # run to bank
            time.sleep(6) #this timer is good.
            depositAll()  #deposits steel bars (assume bank fillers have are in place, so nothing else goes into bank)
            withdrawIron() #withdraw iron from bank
            coalBag()     #same picture for coal bag in invy, it fills when bank is opened, dumps when not in bank)
            findObjectCenter(belt, True) #deposit iron to belt
            time.sleep(11) #needs verification/testing
            coalBag() #empties coal bag to inventory
            findObjectCenter(belt, True) #deposit coal to belt
            #time.sleep(.6)
            findObjectCenter(tile) #run to tile next to retrieval
            time.sleep(7) #I think this one is good
            findObjectCenter(retrieve, True)
            time.sleep(.6)
            keyboard.press(Key.space)

                
                
            
    ##exit
        
    #time.sleep(70) # delay before clicking another rock
           
    #if keyboard.is_pressed('p'):
            #exit(0)

def main():
    window = gw.getWindowsWithTitle(f'Runelite - {USERNAME}')[0]
    window.activate()
    miningGuildBankRock()

if __name__ == "__main__":
    main()