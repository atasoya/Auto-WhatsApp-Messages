import pyautogui
import time
import pyperclip as pc

# uses pyautogui magic to press searc logo
def pressSearch():
    pyautogui.click("assets/search.png")

# first enters the number to the search bar and then send the message
def enterNumber(number,message):
    pyautogui.write(number, interval=0.1)
    pyautogui.press("enter")
    time.sleep(1) # to make code more robust
    
    # copy paste operation
    pc.copy(message)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("v")
    pyautogui.press("enter")