# imports
import webbrowser
import time
import computer_vision
import automate

def main(message):
    counter = 0 # usefull variable

    # open https://web.whatsapp.com/ in default browser
    webbrowser.open("https://web.whatsapp.com/")

    # check if https://web.whatsapp.com/ loaded using image recognition

    while True:
        if counter == 100:
            print("page didnt loaded")
            quit()
        time.sleep(1) # make code sleep 1 sec to make it more stable
        if computer_vision.isOnScreen("loaded_mark")[0] == True:
            counter = 0
            break
        else:
            counter += 1

    
    numbersFile = open("numbers.txt","r") # assuming we have 1 number per line
    # first presses search logo and then enters number to send the message
    for line in numbersFile:
        automate.pressSearch()
        automate.enterNumber(line[0:len(line)-2],message)
    numbersFile.close()







