import os
import struct
import time
import pyaudio
import pvporcupine
import pyautogui as autogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
from engine.helper import extract_yt_term

# =============================
# HOTWORD FUNCTION
# =============================
# def hotword():
#     porcupine = None
#     paud = None
#     audio_stream = None

#     try:
#         # Base directory for engine/features.py
#         base_dir = os.path.dirname(os.path.abspath(__file__))

#         # Correct hotword path
#         keyword_path = os.path.join(
#             base_dir,"engine" "hotword", "sunday_en_windows_v3_0_0.ppn"
#         )
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


# # =============================
# # ALLOW MODULE IMPORT WITHOUT EXECUTING
# # =============================
# if __name__ == "__main__":
#     hotword()
def hotword():
    # import pvporcupine, pyaudio, struct, time
    # import pyautogui as autogui
    # from engine.command import speak
    # import os

    porcupine = None
    paud = None
    audio_stream = None

    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        keyword_path = os.path.join(base_dir, "engine", "hotword", "sunday_en_windows_v3_0_0.ppn")
        keyword_path = os.path.abspath(keyword_path)

        print("Using keyword file:", keyword_path)
        print("Does file exist?:", os.path.exists(keyword_path))

        if not os.path.exists(keyword_path):
            raise FileNotFoundError("❌ Hotword file not found!")

        porcupine = pvporcupine.create(
            access_key="AHyqGTYq+h1ge88Hu/Cmod/QqJJH+yjpy+2qFT4JI2zjZcjs156G/Q==",
            keyword_paths=[keyword_path]
        )

        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        speak("Say 'SUNDAY' to activate...")

        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            if porcupine.process(pcm) >= 0:
                print("🎉 SUNDAY detected!")
                autogui.keyDown("win")
                autogui.press("o")
                time.sleep(1)
                autogui.keyUp("win")

    finally:
        if porcupine: porcupine.delete()
        if audio_stream: audio_stream.close()
        if paud: paud.terminate()


hotword()
