from  pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(1270, 875)[0] == 0:
        click(1270, 875)
        
    if pyautogui.pixel(1430, 875)[0] == 0:
        click(1430, 875)
        
    if pyautogui.pixel(1585, 875)[0] == 0:
        click(1585, 875)
        
    if pyautogui.pixel(1725, 875)[0] == 0:
        click(1725, 875)