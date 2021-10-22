import pyttsx3
import speech_recognition as sr
import Wiki
import weathe_speech
import Yt
import datetime as dt
import randfacts
# import snakeGame
# import covidCases
# import Calculator
speaker = pyttsx3.init()
speaker.setProperty("rate",140)
voices = speaker.getProperty("voices")
speaker.setProperty("voice",voices[1].id)
r = sr.Recognizer()
def speak(text):
    speaker.say(text)
    speaker.runAndWait()
def hour():
    hour = int(dt.datetime.now().hour)
    if hour > 0 and hour<12:
        return ("Good Morning")
    elif hour > 12 and hour < 16:
        return ("Good afternoon")
    else:
        return ("Good night")
speak(hour()+"mam slash sir, I am your voice assistent Beeling. What should i call you?")
with sr.Microphone() as source:
    print("listening")
    r.adjust_for_ambient_noise(source, 1.2)
    audio = r.listen(source)
    text = r.recognize_google(audio)
speak("Hey! "+text+" here are the list of commands you can say")
print ("Open YouTube\nOpen Wikipedia\nWhat's the weather?\nI am bored\nWhat is the time\nOpen Calculator\nI want to play a game\nHow many ")
while True:
    speak("listening")
    with sr.Microphone() as source:
        print("listening")
        r.adjust_for_ambient_noise(source, 1.2)
        audio1 = r.listen(source)
        text1 = r.recognize_google(audio1)
        text1 = text1.lower()
    print(text1)
    if "youtube" in text1:
        speak("What would you like to search on youtube")
        with sr.Microphone() as source:
            print("listening")
            r.adjust_for_ambient_noise(source, 1.2)
            audio2 = r.listen(source)
            text2 = r.recognize_google(audio2)
        Yt.getYt(text2)
    elif "wikipedia" in text1:
        speak("What would you like to search on wikipedia")
        with sr.Microphone() as source:
            print("listening")
            r.adjust_for_ambient_noise(source, 1.2)
            audio2 = r.listen(source)
            text2 = r.recognize_google(audio2)
        Wiki.getWiki(text2)
    elif "weather" in text1:
        speak("Which place?")
        with sr.Microphone() as source:
            print("listening")
            r.adjust_for_ambient_noise(source, 1.2)
            audio2 = r.listen(source)
            text2 = r.recognize_google(audio2)
        print("getting results....")
        print(text2)
        print(weathe_speech.getWeather(text2))
        speak(weathe_speech.getWeather(text2))
    elif "time" in text1:
        print("It is "+str(dt.datetime.now())+" right now")
        speak("It is "+str(dt.datetime.now())+" right now")
    elif "bored" or "fact" in text1:
        x = randfacts.get_fact()
        print(x)
        speak(x)

