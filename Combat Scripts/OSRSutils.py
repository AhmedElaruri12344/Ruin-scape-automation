import collections
import pygetwindow as gw
import pyautogui as pag
import numpy as np
import cv2

def drop(image,title, **kwargs):
    pag.keyDown('shift')
    pag.click(pag.locateOnWindow(image,title,**kwargs))
    pag.keyUp('shift')
    
def dropInv():
    pag.keyDown('shift')
    for y in range(757,974,36):
        for x in range (1458,1583,38):
            pag.click(x,y)
            pag.sleep(.001)
    pag.keyUp('shift')

def findColor(window,boundaries,order):
    img = pag.screenshot(region=(window.left,window.top,window.width,window.height))
    img = cv2.cvtColor(np.array(img),cv2.COLOR_BGR2RGB)
    for (lower,upper) in boundaries:
        lower = np.array(lower,dtype="uint8")
        upper = np.array(upper,dtype="uint8")
        mask = cv2.inRange(img, lower, upper)
        img = cv2.bitwise_and(img,img, mask = mask)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    npcoord = cv2.findNonZero(img.astype(np.uint8))
    if npcoord is None:
        print("none loop")
        return None,None
    else:
        coord = npcoord.tolist()
        x,y=float(coord[order][0][0]),float(coord[order][0][1])
        x,y=int(x),int(y)
        print('''type(x),type(y)''','Color found at:',x,',',y)
        return x,y

def findColorMiddle(window,boundaries):
    img = pag.screenshot(region=(window.left,window.top,window.width,window.height))
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
        coord = npcoord.tolist()
        x,y=float(coord[int(len(coord)/2)][0][0]),float(coord[int(len(coord)/2)][0][1])
        x,y=int(x),int(y)
        print('''type(x),type(y)''','Color found at:',x,',',y)
        return x,y
    
def jiggler():
    pag.moveRel(2,0,.02)
    pag.moveRel(-2,0,.02)

def locateCenterOnWindow(image,title, **kwargs):
    coords = pag.locateOnWindow(image,title,**kwargs)
    Point = collections.namedtuple('Point','x y')
    if coords is None:
        return None
    else:
        return Point(coords[0] + int(coords[2] / 2), coords[1] + int(coords[3] / 2))

def login(pswd,title):
    pag.click(pag.locateOnWindow('Images\\Utils\\Ok.png',title,confidence=.9))
    pag.click(pag.locateOnWindow('Images\\Utils\\ExistingUser.png',title,confidence=.9))
    if pag.locateOnWindow('Images\\Utils\\Warning.png',title,confidence=.9) != None:
        pag.click(pag.locateOnWindow('Images\\Utils\\Continue.png',title,confidence=.9))
    if pag.locateOnWindow('Images\\Utils\\EnterPass.png',title,confidence=.9) != None:
        pag.write(pswd)
        pag.press('enter')
    else:
        return exit()
    while pag.locateOnWindow('Images\\Utils\\Play.png',title,confidence=.9) == None:
        pag.sleep(1)
    pag.click(pag.locateOnWindow('Images\\Utils\\Play.png',title,confidence=.9))
    

def longClick(x,y,sleep):
    pag.mouseDown(x,y)
    pag.sleep(sleep)
    pag.mouseUp()

def lowHealth():
    if pag.pixelMatchesColor(1416,867,(43,38,31),tolerance=5):
        return True
        
    else:
        return False

def pixelClick(x,y,sleep):
    pag.moveTo(x,y)
    pag.click()
    pag.sleep(sleep)

def positionCamStandard():
    window = gw.getWindowsWithTitle('RuneLite - Aragorn GI')[0]
    window.activate()
    pag.moveTo(1479,43,1,pag.easeOutQuad)
    pag.click()
    pag.moveTo(1447,43,.03,pag.easeOutQuad)
    pag.keyDown('up')
    pag.sleep(2.5)
    pag.keyUp('up')
    pag.sleep(.1)

def setTimer():
    timer = pag.prompt(text="Minutes",title='Timer',default='10')
    print(timer)
    if timer == None:
        exit()
    else:
        return(float(timer)*60)

if __name__ == "__main__":
    pswd = pag.password("Enter password","Password Storage")
    window = pag.getWindowsWithTitle('RuneLite - Aragorn GI')[0]
    title = window.title
    window.activate()
    login(pswd,title)