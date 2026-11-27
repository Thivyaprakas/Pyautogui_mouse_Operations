import pyautogui
import time
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0
time.sleep(2)  # Wait for 4 seconds before taking the screenshot
import pyscreeze


#screenshot operation
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')  # Save the screenshot to a file