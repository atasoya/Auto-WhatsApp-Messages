# imports
import cv2 as cv
import numpy as np
import pyautogui



# detect if image is on screen 
# filename is filename of photo we search
def isOnScreen(filename): # returns list that contains boolean , integer , integer ,  integer , integer

    # takes screenshot
    screenshot = pyautogui.screenshot("current_screen.png")  
    screenshot = np.array(screenshot)                   # saves current screen
    screenshot = screenshot[:, :, ::-1].copy()

    # reads current screen as haystack image to search for needle
    haystack_img = cv.imread("current_screen.png", cv.IMREAD_UNCHANGED) 
    haystack_img = cv.cvtColor(haystack_img, cv.COLOR_BGR2GRAY)  # changes it to grey scale to make searching faster and as they need to have same color gradient

    # loads needle image provided by function
    needle_img = cv.imread(f"assets/{filename}.png", cv.IMREAD_UNCHANGED)
    needle_img = cv.cvtColor(needle_img, cv.COLOR_BGR2GRAY)

    # image recognition part
    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # check confidence to decide if it is on the page
    if max_val > 0.7:
        return [True,min_loc,max_loc]
    else:
        return [False,min_loc,max_loc]




