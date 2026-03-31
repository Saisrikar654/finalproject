# import os
# import eel

# from engine.features import *
# from engine.command import *

# def start():
#     eel.init("www")
  
# playAssistantSound()

# os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# eel.start('index.html', mode=None, host='localhost', block=True)

import os
import eel
from engine.features import *
from engine.command import *
from engine.auth import recoganize


def start():
    WWW_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www")
    eel.init(WWW_FOLDER)
    playAssistantSound() 

    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready for face authentication")
        # optional startup sound
        flag = recoganize.AuthenticateFace()

        if flag ==1:
            eel.hideFaceAuth()
            speak("Face authentication verified user")
            eel.hideFaceAuthSuccess()
            speak("welcome")
            eel.hideStart()
            playAssistantSound() 

        else:
             speak("Face authentication failed ")

    # Open browser manually (Edge app mode)
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    # Start Eel server
    eel.start('index.html', mode=None, host='localhost', block=True)

# import json
# import sounddevice as sd
# from vosk import Model, KaldiRecognizer
# import pyttsx3
# import eel

# # Initialize Eel
# eel.init(".")

# # Load Vosk models for Telugu, Hindi, and English
# models = {
#     "en": Model("model-en"),  # English
#     "hi": Model("model-hi"),  # Hindi
#     "te": Model("model-te")   # Telugu
# }

# # Speak function
# def speak(text):
#     engine = pyttsx3.init('sapi5')
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id)
#     engine.setProperty('rate', 174)
#     engine.say(text)
#     engine.runAndWait()

# @eel.expose
# def takecommand(language="en"):
#     print(f"Listening in: {language.upper()}")
#     model = models.get(language, models["en"])  # default to English if invalid

#     rec = KaldiRecognizer(model, 16000)

#     with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
#                            channels=1, callback=lambda indata, frames, time, status: rec.AcceptWaveform(indata)):
#         print("Say something...")

#         result = {}
#         while True:
#             if rec.AcceptWaveform(sd.rec(4000, samplerate=16000, channels=1, dtype='int16')):
#                 result = json.loads(rec.Result())
#                 break

#     query = result.get("text", "")
#     print("Recognized:", query)
#     return query.lower()

# # Optional testing on launch
# # speak("Welcome to Sunday Assistant")

# eel.start("index.html", size=(800, 600))  # Or use mode='chrome' if needed
