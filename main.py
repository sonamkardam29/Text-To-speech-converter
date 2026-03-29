
# main.py
import pyttsx3
from gtts import gTTS
from playsound import playsound
import os

def pyttsx3_tts(text):
    """Offline TTS using pyttsx3"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def gtts_tts(text):
    """Online TTS using gTTS"""
    tts = gTTS(text=text, lang='en')
    filename = "gtts_audio.mp3"
    tts.save(filename)
    print(f"Audio saved as {filename}")
    playsound(filename)

def main():
    print("Welcome to Dual TTS Converter!")
    text = input("Enter text to convert to speech: ")

    print("\nChoose TTS Engine:")
    print("1. Offline (pyttsx3)")
    print("2. Online (gTTS)")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        pyttsx3_tts(text)
    elif choice == '2':
        gtts_tts(text)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()