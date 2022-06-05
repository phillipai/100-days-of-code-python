from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(1)
jumps = 0

def jump():
    global jumps
    win32api.keybd_event(38, 0, 0, 0)
    time.sleep(0.01)
    win32api.keybd_event(38, 0, win32con.KEYEVENTF_KEYUP, 0)
    jumps += 1


def duck():
    win32api.keybd_event(40, 0, 0, 0)
    time.sleep(0.4)
    win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
    print("I see a Pterodactyl")


# Press 'q' to stop running
while not keyboard.is_pressed('q'):
    if pyautogui.pixel(730, 468)[0] == 83:
        jump()
        print("I see a tall cactus!")
    elif pyautogui.pixel(715, 490)[0] == 83:
        jump()
        print("I see a short cactus!")
    if pyautogui.pixel(760, 460)[0] == 83:
        duck()
    # Speed increases
    if jumps > 3:
        if pyautogui.pixel(720, 468)[0] == 83:
            jump()
            print("I see a tall cactus!")
        elif pyautogui.pixel(705, 490)[0] == 83:
            jump()
        if pyautogui.pixel(750, 460)[0] == 83:
            duck()
