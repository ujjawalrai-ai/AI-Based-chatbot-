from google import genai
client=genai.Client(api_key="API KEy")

command = '''[19:39, 26/7/2025] Ghost: Ok
[19:39, 26/7/2025] Ghost: I'll do this at first place     
[19:40, 26/7/2025] Samir EEE: 🥺🥺😂
[19:40, 26/7/2025] Ghost: Kr deta hu abhi kuch kr rha hu  
[19:53, 26/7/2025] Samir EEE: Ok
[02:26, 27/7/2025] Ghost: mene gemni add kr liya lekin    
[02:26, 27/7/2025] Ghost: response karne me time le rha h 
[09:31, 27/7/2025] Samir EEE: Acha
[09:31, 27/7/2025] Samir EEE: Main dekhta hu mere mein '''
messages ={"role":"system","content":"You're a person named ghost who speaks hindi as well as english. you're from india and you are a coder."
"you analyze chat history and respond like ghost. Output should be next chat response as ghost"}; 
#here we setup initial prompt based on that the ai will generate response to reply
{"role":"user","content":command}
response = client.models.generate_content(model="gemini-2.5-flash",contents =command)

print(response.text)
