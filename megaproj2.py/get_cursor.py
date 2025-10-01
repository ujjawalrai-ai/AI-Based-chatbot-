import pyautogui
#pip install pyautogui -> will install pyautogui libraries
import pyperclip #pip install pyperclip ->helps use to take content from clipboard
while True:
    a = pyautogui.position() #funct pf pyautogui from pyautogui docs website
    #returns the position of mouse or cordinates of mouse cursor x and y
    print(a) #will give position of cursor 
    # 1261,296 #position of cursor at a in print funct
    # 566,237 to 901,958  #position of cusor at top left corner point in the chat