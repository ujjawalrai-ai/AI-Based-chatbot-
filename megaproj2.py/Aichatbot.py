import pyautogui #lib is used to tell the position of mouse cursor or it's co ordinates
import pyperclip #helps us to take content from clipboard
import time
from google import genai

#here we'll define a funct to check the last msg from sender

def is_last_msg_from_sender(chat_log, sender_name="Arnav Gaur"): #here it will check whether the last msg is from sender
    messages = chat_log.strip().split("/2025]")[-1] #for multi line msg it will split the msg based on year as every 
    #msg get copied and paste with date we can see it in ai integrate file
    if sender_name in messages: #if sender name will be there for last msg then while loop will run
        return True
    return False
#--------------------------------------------------------------------------------------------------------------------------
'''now we have to run it manually so now we"ll set it up to
run by itself in loop so that we don't have to do it manually '''

# Click the chrome icon at given coordinates
pyautogui.click(1261, 296)
time.sleep(1)  # Wait for 1sec to ensure  the click is registered
#--------------------------------------------------------------------------------------------------------------------------

while(True):
    

    # Drag mouse to select text it will drag it for 1 sec
    pyautogui.moveTo(519, 240)
    pyautogui.dragTo(780, 985, duration=0.5, button='left')  # Adjust duration if needed[1][4][8]
    # Copy to clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(527,407) #will click at the positon and deselect the text
#when we run it in loop for automatically we will increase the timesleep or limit
    time.sleep(2)  # Ensure clipboard update is complete[2]

    # Get clipboard contents
    chat_history = pyperclip.paste()  #here the chat we got copy we will allocate it to chat history 
    print(chat_history)
    
#--------------------------------------------------------------------------------------------------------------------

    client=genai.Client(api_key="YOUR API KEY") #API integration

    msg =("You're a person named ghost who speaks hindi as well as english. you're from india and you are a college student."
    "you analyze chat history and respond like ghost. Output should be next chat response don't include my introduction to respond  " )

    prompt = f"{msg}\n\nChat History:\n{chat_history}\n\nReply:" #here we setup initial prompt based on that the ai will generate response to reply
    #means we're telling it that is the person and these are text(chat history) now respond accordingly
#------------------------------------------------------------------------------------------------------------------------------

    if is_last_msg_from_sender(chat_history): #calling the  function  if the last msg will from sender than it will generate the response
        # and do the following the copy and pasting the response
        
        #for below block of code it will generate reponse based on chat hisrtory from gemini for reply
        response = client.models.generate_content(model="gemini-2.5-flash",contents =prompt)
        sdk_http_response =response #defining sdk_http_response

        #here it's response has many hidden text words and many sign things but we want only the
        #  text(that includes reply) part means the part we want
        #to send as reply so we are selecting only that part

        text_output = sdk_http_response.candidates[0].content.parts[0].text # for SDK object selecting only the text portion for reply 

        pyperclip.copy(text_output) #will copy the text_output response to paste it in chatbox
#--------------------------------------------------------------------------------------------------------------------------------------------------------
        #we will use chatgpt and ask for code to click at the chat box and paste the 
        #response then click enter

        # Move to coordinates and click
        pyautogui.click(709, 1022) #cursor position where we will paste the text
        time.sleep(0.5)  # Optional: wait for app to focus 

        # Set your text
        
        pyperclip.copy(text_output)  #will paste the response in chat for sending

        # Paste the text (Ctrl+V on Windows)
        pyautogui.hotkey('ctrl', 'v')      
        time.sleep(0.1)
        pyautogui.press('enter')
    
