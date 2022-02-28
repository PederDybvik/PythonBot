from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.008)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.008)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixelMatchesColor(600,551,(2,2,2)):
        click(600,551)
    if pyautogui.pixelMatchesColor(700,551,(2,2,2)):
        click(700,551)
    if pyautogui.pixelMatchesColor(800,551,(2,2,2)):
        click(800,551)
    if pyautogui.pixelMatchesColor(900,551,(2,2,2)):
        click(900,551)