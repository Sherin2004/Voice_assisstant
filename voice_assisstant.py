import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Helper function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        try:
            # Listen for up to 10 seconds
            audio = recognizer.listen(source, timeout=10)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out, no input detected.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None

# Core functions to handle various commands
def respond(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        speak("What do you want to search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")
    elif "thank you" in command:
        speak("You're welcome! Have a great day!")
        return False  # Stop the loop if user says "thank you"
    else:
        speak("I'm sorry, I didn't understand that command.")
    return True  # Continue listening for further commands

# Main loop
if __name__ == "__main__":
    speak("Voice assistant activated. How can I help you?")
    while True:
        user_command = listen()
        if user_command:
            if not respond(user_command):
                break  # Exit the loop if "thank you" is detected
