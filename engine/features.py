import json
import os
import re
from shlex import quote
import struct
import subprocess
import time
from playsound import playsound
import eel
import pyaudio
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import webbrowser
import sqlite3
import pvporcupine
import pyautogui as autogui
import pyautogui

from engine.helper import extract_yt_term, remove_words
from hugchat import hugchat

con = sqlite3.connect("sunday.db")

cursor = con.cursor()

@eel.expose
def playAssistantSound():
    music_dri="www\\assets\\audio\\iron-man-repulsor-157371.mp3"
    playsound(music_dri)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    app_name = query.strip()
     
    if app_name != "":
        
        
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")



def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)


# def hotword():
#     porcupine=None
#     paud=None
#     audio_stream=None
#     try:
       
#         # pre trained keywords    
#         porcupine=pvporcupine.create(keywords=["sunday","alexa"]) 
#         paud=pyaudio.PyAudio()
#         audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
#         # loop for streaming
#         while True:
#             keyword=audio_stream.read(porcupine.frame_length)
#             keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

#             # processing keyword comes from mic 
#             keyword_index=porcupine.process(keyword)

#             # checking first keyword detetcted for not
#             if keyword_index>=0:
#                 print("hotword detected")

#                 # pressing shorcut key win+j
#                 import pyautogui as autogui
#                 autogui.keyDown("win")
#                 autogui.press("o")
#                 time.sleep(2)
#                 autogui.keyUp("win")
                
#     except:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()
# def hotword():
#     porcupine = None
#     paud = None
#     audio_stream = None

#     try:
#         base_dir = os.path.dirname(os.path.abspath(__file__))
#         keyword_path = os.path.join(base_dir, "hotwords", "sunday_en_windows_v4_0_0.ppn")

#         print("Using keyword file:", keyword_path)
#         print("Does file exist?:", os.path.exists(keyword_path))

#         porcupine = pvporcupine.create(
#             access_key="AHyqGTYq+h1ge88Hu/Cmod/QqJJH+yjpy+2qFT4JI2zjZcjs156G/Q==",  # Replace with your real key
#             keyword_paths=[keyword_path]
#         )

#         paud = pyaudio.PyAudio()
#         audio_stream = paud.open(
#             rate=porcupine.sample_rate,
#             channels=1,
#             format=pyaudio.paInt16,
#             input=True,
#             frames_per_buffer=porcupine.frame_length
#         )

#         speak("Say 'SUNDAY' to activate...")

#         while True:
#             keyword = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
#             keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
#             keyword_index = porcupine.process(keyword)

#             if keyword_index >= 0:
#                 print("🎉 SUNDAY detected!")
#                 autogui.keyDown("win")
#                 autogui.press("o")
#                 time.sleep(1)
#                 autogui.keyUp("win")

#     except Exception as e:
#         print("Error during hotword setup or processing:", e)

#     finally:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()
# hotword()
# def hotword():
#     # import pvporcupine, pyaudio, struct, time
#     # import pyautogui as autogui
#     # from engine.command import speak
#     # import os

#     porcupine = None
#     paud = None
#     audio_stream = None

#     try:
#         base_dir = os.path.dirname(os.path.abspath(__file__))
#         keyword_path = os.path.join(base_dir, "engine", "hotword", "sunday_en_windows_v3_0_0.ppn")
#         keyword_path = os.path.abspath(keyword_path)

#         print("Using keyword file:", keyword_path)
#         print("Does file exist?:", os.path.exists(keyword_path))

#         if not os.path.exists(keyword_path):
#             raise FileNotFoundError("❌ Hotword file not found!")

#         porcupine = pvporcupine.create(
#             access_key="AHyqGTYq+h1ge88Hu/Cmod/QqJJH+yjpy+2qFT4JI2zjZcjs156G/Q==",
#             keyword_paths=[keyword_path]
#         )

#         paud = pyaudio.PyAudio()
#         audio_stream = paud.open(
#             rate=porcupine.sample_rate,
#             channels=1,
#             format=pyaudio.paInt16,
#             input=True,
#             frames_per_buffer=porcupine.frame_length
#         )

#         speak("Say 'SUNDAY' to activate...")

#         while True:
#             pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
#             pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

#             if porcupine.process(pcm) >= 0:
#                 print("🎉 SUNDAY detected!")
#                 autogui.keyDown("win")
#                 autogui.press("o")
#                 time.sleep(1)
#                 autogui.keyUp("win")

#     finally:
#         if porcupine: porcupine.delete()
#         if audio_stream: audio_stream.close()
#         if paud: paud.terminate()
# hotword()

# -------------------------------
# Hotword detection function
# -------------------------------
def hotword():
    porcupine = None
    paud = None
    audio_stream = None

    try:
        # -------------------------------
        # Correct project root path
        # -------------------------------
        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        KEYWORD_PATH = os.path.join(PROJECT_ROOT, "engine", "hotword", "sunday_en_windows_v3_0_0.ppn")
        KEYWORD_PATH = os.path.abspath(KEYWORD_PATH)

        print("Using keyword file:", KEYWORD_PATH)
        print("Does file exist?:", os.path.exists(KEYWORD_PATH))

        if not os.path.exists(KEYWORD_PATH):
            raise FileNotFoundError("❌ Hotword file not found!")

        # -------------------------------
        # Initialize Porcupine
        # -------------------------------
        porcupine = pvporcupine.create(
            access_key="AHyqGTYq+h1ge88Hu/Cmod/QqJJH+yjpy+2qFT4JI2zjZcjs156G/Q==",  # Replace with your Picovoice AccessKey
            keyword_paths=[KEYWORD_PATH]
        )

        # -------------------------------
        # Initialize PyAudio
        # -------------------------------
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("Say 'SUNDAY' to activate...")
        # print("Say 'SUNDAY' to activate...")
        # -------------------------------
        # Listening loop
        # -------------------------------
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            if porcupine.process(pcm) >= 0:
                print("🎉 SUNDAY detected!")
                # Example action on detection
                autogui.keyDown("win")
                autogui.press("o")
                time.sleep(1)
                autogui.keyUp("win")

    except Exception as e:
        print("Error during hotword setup or processing:", e)

    finally:
        # -------------------------------
        # Cleanup
        # -------------------------------
        if porcupine:
            porcupine.delete()
        if audio_stream:
            audio_stream.close()
        if paud:
            paud.terminate()


# -------------------------------
# Run hotword directly for testing
# -------------------------------
if __name__ == "__main__":
    hotword()
# from engine.command import speak

# def hotword():
#     porcupine = None
#     paud = None
#     audio_stream = None

#     try:
#         # ✅ BASE DIRECTORY (engine/features.py location)
#         base_dir = os.path.dirname(os.path.abspath(__file__))

#         # ✅ CORRECT PATH (matches your verified working setup)
#         keyword_path = os.path.join(
#             base_dir,
#             "..",            # go from features → engine
#             "hotword",       # correct folder name
#             "sunday_en_windows_v3_0_0.ppn"  # verified working file
#         )
#         keyword_path = os.path.abspath(keyword_path)

#         print("Using keyword file:", keyword_path)
#         print("Does file exist?:", os.path.exists(keyword_path))

#         if not os.path.exists(keyword_path):
#             raise FileNotFoundError("❌ Hotword file not found")

#         porcupine = pvporcupine.create(
#             access_key="PASTE_YOUR_VALID_ACCESS_KEY_HERE",
#             keyword_paths=[keyword_path]
#         )

#         paud = pyaudio.PyAudio()
#         audio_stream = paud.open(
#             rate=porcupine.sample_rate,
#             channels=1,
#             format=pyaudio.paInt16,
#             input=True,
#             frames_per_buffer=porcupine.frame_length
#         )

#         speak("Say 'SUNDAY' to activate...")

#         while True:
#             pcm = audio_stream.read(
#                 porcupine.frame_length,
#                 exception_on_overflow=False
#             )
#             pcm = struct.unpack_from(
#                 "h" * porcupine.frame_length,
#                 pcm
#             )

#             keyword_index = porcupine.process(pcm)

#             if keyword_index >= 0:
#                 print("🎉 SUNDAY detected!")
#                 autogui.keyDown("win")
#                 autogui.press("o")
#                 time.sleep(1)
#                 autogui.keyUp("win")

#     except Exception as e:
#         print("Error during hotword setup or processing:", e)

#     finally:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()
# def  extract_yt_term(command):
#     pattern = r'paly\s+(.*?)\s+on\s+youtube'
#     match = re.search(pattern, command, re.IGNORECASE)
#     return match.group(1) if match else None
# def extract_yt_term(command):
#     pattern = r'play\s+(.*?)\s+(on\s+youtube)?$'
#     match = re.search(pattern, command, re.IGNORECASE)
#     return match.group(1).strip() if match else None

# find contacts
def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call','send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    

def whatsApp(mobile_no, message, flag, name):
    

    if flag == 'message':
        target_tab = 12 
        sunday_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 6
        message = ''
        sunday_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        sunday_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    # print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(sunday_message)

# chat bot 
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    # print(response)
    speak(response)
    return response

# android automation

def makeCall(name, mobileNo):
    mobileNo =mobileNo.replace(" ", "")
    speak("Calling "+name)
    command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(command)

# to send message
def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open sms app
    tapEvents(136, 2220)
    #start chat
    tapEvents(819, 2192)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(601, 574)
    # tap on input
    tapEvents(390, 2270)
    #message
    adbInput(message)
    #send
    tapEvents(957, 1397)
    speak("message send successfully to "+name)
    

    # Assistant name
@eel.expose
def assistantName():
    name = ASSISTANT_NAME
    return name


@eel.expose
def personalInfo():
    try:
        cursor.execute("SELECT * FROM info")
        results = cursor.fetchall()
        jsonArr = json.dumps(results[0])
        eel.getData(jsonArr)
        return 1    
    except:
        print("no data")


@eel.expose
def updatePersonalInfo(name, designation, mobileno, email, city):
    cursor.execute("SELECT COUNT(*) FROM info")
    count = cursor.fetchone()[0]

    if count > 0:
        # Update existing record
        cursor.execute(
            '''UPDATE info 
               SET name=?, designation=?, mobileno=?, email=?, city=?''',
            (name, designation, mobileno, email, city)
        )
    else:
        # Insert new record if no data exists
        cursor.execute(
            '''INSERT INTO info (name, designation, mobileno, email, city) 
               VALUES (?, ?, ?, ?, ?)''',
            (name, designation, mobileno, email, city)
        )

    con.commit()
    personalInfo()
    return 1



@eel.expose
def displaySysCommand():
    cursor.execute("SELECT * FROM sys_command")
    results = cursor.fetchall()
    jsonArr = json.dumps(results)
    eel.displaySysCommand(jsonArr)
    return 1


@eel.expose
def deleteSysCommand(id):
    cursor.execute("DELETE FROM sys_command WHERE id = ?", (id,))
    con.commit()


@eel.expose
def addSysCommand(key, value):
    cursor.execute(
        '''INSERT INTO sys_command VALUES (?, ?, ?)''', (None,key, value))
    con.commit()


@eel.expose
def displayWebCommand():
    cursor.execute("SELECT * FROM web_command")
    results = cursor.fetchall()
    jsonArr = json.dumps(results)
    eel.displayWebCommand(jsonArr)
    return 1


@eel.expose
def addWebCommand(key, value):
    cursor.execute(
        '''INSERT INTO web_command VALUES (?, ?, ?)''', (None, key, value))
    con.commit()


@eel.expose
def deleteWebCommand(id):
    cursor.execute("DELETE FROM web_command WHERE Id = ?", (id,))
    con.commit()


@eel.expose
def displayPhoneBookCommand():
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    jsonArr = json.dumps(results)
    eel.displayPhoneBookCommand(jsonArr)
    return 1


@eel.expose
def deletePhoneBookCommand(id):
    cursor.execute("DELETE FROM contacts WHERE Id = ?", (id,))
    con.commit()


@eel.expose
def InsertContacts(Name, MobileNo, Email, City):
    cursor.execute(
        '''INSERT INTO contacts VALUES (?, ?, ?, ?, ?)''', (None,Name, MobileNo, Email, City))
    con.commit()
