import pyautogui
import time
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0
time.sleep(5)

#write text using pyautogui
#pyautogui.write('Hello, this is a test message!', interval=0.1)  # Type with a slight delay between each character
#pyautogui.press('enter')  # Press the Enter key
#pyautogui.typewrite('Hello, this is a test message!', interval=0.1)  # Type with a slight delay between each character



#shift +a
pyautogui.keyDown('shift')  # Hold down the Shift key
pyautogui.press('a')  # Press the 'a' key while Shift is held down
pyautogui.keyUp('shift')  # Release the Shift key

pyautogui.hotkey('ctrl', 'a')  # Select all text
pyautogui.hotkey('ctrl', 'c')  # Copy the selected text
#paste text using ctrl + v
pyautogui.hotkey('ctrl', 'v')  # Paste the copied text