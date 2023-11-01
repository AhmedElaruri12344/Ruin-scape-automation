from datetime import datetime
import pygetwindow as gw
import pyautogui as pag
import time,os
pag.PAUSE=.03
os.chdir(os.path.dirname(os.path.abspath(__file__)))
window = gw.getWindowsWithTitle('RuneLite - LouvelleGI')[0]
window.activate()
def search(needle):
    haystack = pag.screenshot('search.png',region=(0,0,1920,1080))
    findpic = pag.locate(needle,haystack,confidence=0.75)
    if findpic == None:
        now = datetime.now()
        HMS = now.strftime("%H:%M:%S")
        #pag.alert(text="Error: needle not found",title=HMS,button='OK')
        #exit()
    else:    
        x,y = pag.center(findpic)
        return x,y
def MOG():
    haystack = pag.screenshot('search.png',region=(0,0,1920,1080))
    findmog = pag.locate('MOGImg.png',haystack,confidence=.68)
    if findmog == None:
        return False
    else:
        x,y = pag.center(findmog)
        print("FOUND MOG")
        return x,y
def init():
    while True:
        time.sleep(1)
        pag.moveTo(search('TreeImg.png'));pag.click();time.sleep(6.75)#Climb tree
        print("Tree climbed")
        if MOG() != False:#roof 1
            pag.moveTo(MOG());pag.click();time.sleep(2)
            pag.moveTo(search('Roof1Img.png'));pag.click();time.sleep(3.5)
        else:
            pag.moveTo(search('Roof1Img.png'));pag.click();time.sleep(5)
            print("JUMP 1")

        if MOG() != False:#roof 2
            pag.moveTo(MOG());pag.click();time.sleep(2)
            pag.moveTo(search('Roof2Img.png'));pag.click();time.sleep(5)
        else:
            pag.moveTo(search('Roof2Img.png'));pag.click();time.sleep(4.75)

        if MOG() != False:#roof 3
            pag.moveTo(MOG());pag.click();time.sleep(2)
            pag.moveTo(search('Roof3Img.png'));pag.click();time.sleep(4.75)
        elif search('Roof3Img.png')!= None:
            pag.moveTo(search('Roof3Img.png'));pag.click();time.sleep(4.75)
        else:
            pag.moveTo(search('FALL.png'));pag.click(); time.sleep(7)
            pag.moveTo((1430, 694));pag.click();time.sleep(5.5)
            continue

        if MOG() != False:#roof 4
            pag.moveTo(MOG());pag.click();time.sleep(2)
            pag.moveTo(search('Roof4Img.png'));pag.click();time.sleep(4.75)
        else:
            pag.moveTo(search('Roof4Img.png'));pag.click();time.sleep(5.75)

        if MOG() != False:#roof 5
            pag.moveTo(MOG());pag.click();time.sleep(2)
            pag.moveTo(search('Roof5Img.png'));pag.click();time.sleep(4.75)
        else:
            pag.moveTo(search('Roof5Img.png'));pag.click();time.sleep(6.5)

        pag.moveTo(search('Roof6Img.png')); pag.click();time.sleep(7)#roof 6
        if search('Roof7Img.png') != None:
            pag.moveTo(search('Roof7Img.png')); pag.click();time.sleep(5.25)#roof 7
        else:
            pag.moveTo(819, 359);pag.click(); time.sleep(3.45)
            pag.moveTo(932, 510);pag.click();time.sleep(2.4)


if __name__ =='__main__':
    init()