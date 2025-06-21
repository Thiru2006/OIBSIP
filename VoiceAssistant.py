import speech_recognition as sr
import datetime
import webbrowser

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        return query.lower()

def respond_to_command(command):
    if "hello" in command:
        print("Hi there! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.date.today().strftime("%B %d, %Y")
        print(f"Today's date is {current_date}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        print(f"Searching for {query}...")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    else:
        print("Sorry, I don't understand that command.")

print("Voice Assistant is ready. Speak now!")
while True:
    command = take_command()
    if "exit" in command or "stop" in command:
        print("Goodbye!")
        break
    respond_to_command(command)
