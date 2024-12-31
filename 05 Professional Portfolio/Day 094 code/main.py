# Automate the Google Dinosaur Game

import pyautogui

while True:
    im = pyautogui.screenshot()
    for i in range(810, 900, 5):
        if im.getpixel((i, 246)) == (182, 182, 182, 255) or im.getpixel((i, 255)) == (182, 182, 182, 255): # Cactus detection
            pyautogui.keyUp("down")
            pyautogui.press("space")
            break
        elif im.getpixel((i, 224)) == (182, 182, 182, 255): # Bird detection
            pyautogui.keyDown("down")
            break
