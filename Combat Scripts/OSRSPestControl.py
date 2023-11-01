import pyautogui as pg
from OSRSutils import findColor,findColorMiddle,pixelClick,login

BOUNDARIESO = [([90,90,200],[90,90,200])]
BOUNDARIESP = [([255,0,255],[255,0,255])]
BOUNDARIESB = [([255,255,0],[255,255,0])]
pswd = pg.password("bigmoosestink","Password Storage")
window = pg.getWindowsWithTitle('RuneLite - slendiemania')[0] #change this to correct window
title = window.title
window.activate()

while True:
    if pg.locateOnWindow('Images\\Utils\\Disconnect.png',title,confidence=.9) != None:
        login(pswd,title)
    x,y = findColor(window,BOUNDARIESO,0)
    while x == None:
        a,b = findColorMiddle(window,BOUNDARIESB)
        if a == None:
            a,b = findColor(window,BOUNDARIESP,-1)
            pixelClick(a,b,3)
        elif a !=None:
            pixelClick(a,b,5)
        combat = pg.locateOnWindow('Images\\Utils\\Combat.png',title,confidence = .9)
        x,y = findColorMiddle(window,BOUNDARIESO)
        while combat != None:
            pg.sleep(2)
            x,y = findColorMiddle(window,BOUNDARIESO)
            combat = pg.locateOnWindow('Images\\Utils\\Combat.png',title,confidence = .9)
    pixelClick(x,y,2)
         