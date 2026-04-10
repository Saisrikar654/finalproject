import pyttsx3
import speech_recognition as sr
import eel
import time
from engine.notepad_logic import *
import re

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices= engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    engine.setProperty('rate', 174)
    # eel.DisplayMessage(text)
    # engine.say(text)
    eel.receiverText(text)
    # engine.runAndWait()
    try:
        eel.DisplayMessage(text)()  # note the parentheses
    except (AttributeError, RuntimeError):
        print("[SPEAK]:", text)  # fallback if JS not ready
    
    # engine.say(text)
    # engine.runAndWait()
    # --- ADDED: ESC INTERRUPT LOGIC ---
    # We import features inside to prevent circular import errors
    import engine.features as features 
    
    # Split the long response into small chunks to check the flag frequently
    parts = re.split(r'[,.!?]', text) 
    
    for part in parts:
        # Check if the global flag in features.py was toggled by the ESC key
        if hasattr(features, 'CHATBOT_INTERRUPTED') and features.CHATBOT_INTERRUPTED:
            print("🛑 Speech loop broken by ESC key.")
            engine.stop()
            return  # Stop execution immediately
        
        if part.strip():
            engine.say(part)
            engine.runAndWait() 
    # ----------------------------------

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.....')
        eel.DisplayMessage(' listening.....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

  
    try:
        print('recognizing')
        eel.DisplayMessage('recognizing.......' )
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}")
        # eel.DisplayMessage(query)
        time.sleep(3)
        
    except Exception as e:
        return ""
     
    return query.lower()

@eel.expose
def allCommands(message=1):
        
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:
        if "open notepad" in query:
            open_notepad()
            speak("Opened notepad for you, sir.")

        elif "write in notepad" in query:
            speak("What should I write?")
            content = takecommand()
            if content != "none":
                write_text(content)
                speak("Typed successfully.")

        elif "save the notepad file" in query or "save this file" in query:
            speak("What should I name the file?")
            filename = takecommand().lower().replace(" ", "_")
            if filename != "none":
                save_notepad(filename)
                speak(f"Saved as {filename} in your desktop folder.")

        elif "rename notepad file" in query:
            speak("What is the current name?")
            old_name = takecommand().lower().replace(" ", "_")
            if old_name != "none":
                speak("What is the new name?")
                new_name = takecommand().lower().replace(" ", "_")
            if rename_notepad_file(old_name, new_name):
                speak("File renamed successfully.")
            else:
                speak("I couldn't find the file to rename.")

        elif "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)

        else:
            from engine.features import chatBot
            chatBot(query)
            
    except:
        print("error")
    
    eel.ShowHood()

               
