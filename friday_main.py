import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import threading
import spacy
import nltk
from nltk.tokenize import word_tokenize

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
nltk.download("punkt")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Service unavailable.")
        return ""

COMMANDS = {
    "open chrome": lambda: os.system("start chrome"),
    "search": lambda query: webbrowser.open(f"https://www.google.com/search?q={query}")
}

def process_command(command):
    doc = nlp(command)
    tokens = [token.text for token in doc if not token.is_stop]  # Remove stopwords
    processed_command = " ".join(tokens)
    return processed_command

def execute_commands(command):
    tasks = []
    command = process_command(command)
    words = word_tokenize(command)
    
    for key in COMMANDS:
        if key in command:
            if key == "search":
                search_index = words.index("search")
                query = " ".join(words[search_index + 1:])
                tasks.append(threading.Thread(target=COMMANDS[key], args=(query,)))
            else:
                tasks.append(threading.Thread(target=COMMANDS[key]))
    
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()

if __name__ == "__main__":
    speak("How can I assist you?")
    user_command = listen()
    if user_command:
        execute_commands(user_command)
