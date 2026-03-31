# import struct
# import time
# import pvporcupine
# import pyaudio
# import pyautogui as autogui
# import os

# def hotword():
#     porcupine = None
#     paud = None
#     audio_stream = None

#     try:
#         base_dir = os.path.dirname(os.path.abspath(__file__))
#         keyword_path = os.path.join(base_dir, "hotword", "sunday_en_windows_v3_0_0.ppn")

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

#         print("Say 'SUNDAY' to activate...")

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
import os
import struct
import pvporcupine
import pyaudio

# ==============================
# CONFIGURATION
# ==============================
ACCESS_KEY = "AHyqGTYq+h1ge88Hu/Cmod/QqJJH+yjpy+2qFT4JI2zjZcjs156G/Q=="
KEYWORD_PATH = r"C:\Users\sSs\Desktop\sunday1\engine\hotword\sunday_en_windows_v3_0_0.ppn"

# ==============================
# FILE CHECK
# ==============================

print("=" * 40)
print("Using keyword file:", KEYWORD_PATH)
print("Does file exist?:", os.path.exists(KEYWORD_PATH))
print("=" * 40)

if not os.path.exists(KEYWORD_PATH):
    raise FileNotFoundError("❌ Hotword file not found! Check path and filename.")

# ==============================
# INIT PORCUPINE
# ==============================

porcupine = pvporcupine.create(
    access_key=ACCESS_KEY,
    keyword_paths=[KEYWORD_PATH]
)

pa = pyaudio.PyAudio()

stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

print("🎙️ Listening for wake word: 'Sunday'...")

# ==============================
# LISTEN LOOP
# ==============================

try:
    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from(
            "h" * porcupine.frame_length,
            pcm
        )

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print("🚀 Wake word 'Sunday' detected!")
            break

except KeyboardInterrupt:
    print("🛑 Stopped by user")

finally:
    stream.stop_stream()
    stream.close()
    pa.terminate()
    porcupine.delete()
    print("🔚 Hotword engine closed.")


