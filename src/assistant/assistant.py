# src/assistant.py
import speech_recognition as sr
import pyttsx3
from commands import execute_command

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""

def run_assistant():
    speak("How can I help you?")
    while True:
        command = listen()
        if "exit" in command:
            speak("Goodbye")
            break
        execute_command(command)

if __name__ == "__main__":
    run_assistant()