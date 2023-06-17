import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            #print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',180)
    engine.say(x)
    engine.runAndWait()

if __name__ ==  "__main__":

    while True:

        data1 = sptext().lower()

        if "your name" in data1:
            name = "my name is bro"
            speechtx(name)

        elif "old are you" in data1:
            age = "i am 20 years old"
            speechtx(age)

        elif "time" in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)

        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")

        elif 'joke' in data1:
            jock_1 = pyjokes.get_joke(language="en", category="neutral")
            speechtx(jock_1)

        elif "exit" in data1:
            speechtx("thank you")
            break










