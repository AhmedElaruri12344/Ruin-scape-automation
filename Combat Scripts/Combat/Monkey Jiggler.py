# import libraries and define global variables.
import pygetwindow as gw
import pyautogui as pg
import time
import win32api, win32con

USERNAME = "Aragorn GI" # CHANGE ME
window = gw.getWindowsWithTitle(f'Runelite - {USERNAME}')[0]
window.activate()

# define custom functions
def click(x,y):
    try:
        win32api.SetCursorPos((x,y))
        time.sleep(0.1) # mouse movement delay; 70 ms stable
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    except:
        print('\nNoneType encountered.\n')
        return

def sleep(seconds):
	time.sleep(seconds)

# ZOOM OUT, PAN UP, FACE WEST!

def monkeyJiggler():

    #t = 5 # chins
    t = 3 # bursting
    #i = 5 # chins
    i = 15 # bursting
    #j = 10 # chins
    j = 6 # bursting
    for y in range(j):
        for x in range(i):
            # run down
            click(1873,537)
            sleep(t)
            # run right
            click(1916,489)
            sleep(t)
        # pickup prayer potion
        click(1872,506)
        sleep(1.6)
        # move right
        click(1919,507)
        sleep(1.6)
        # drink prayer potion
        click(2092,600)

while True:
    # MONKEY JIGGLING
    click(1579,539), sleep(5.3) # run to bottom left spot
    click(2195,480), sleep(5.3) # run to chin right spot
    monkeyJiggler()
    click(1656,316), sleep(5.3) # run to top left spot
    click(2241,263), sleep(5.3) # run to chin right spot
    monkeyJiggler()