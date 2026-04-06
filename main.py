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

