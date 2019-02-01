import speech_recognition as sr
import pyttsx3

def speak(message):
    engine=pyttsx3.init()
    engine.setProperty('voice', "estonian")
    engine.setProperty('rate', 150)
    engine.say('Tere! Minu nimi on Rezwan. Ma olen õpilane. Ma õpin Tartu Ülikoolis.')  #for testing
    engine.say('{}'.format(message))
    engine.runAndWait()

r = sr.Recognizer()

try:
    while True:
        with sr.Microphone() as source:
            print('say something');
            audio = r.listen(source)
            print('---time over---')

        try:
            print('Text: ' + r.recognize_google(audio));
            speak(r.recognize_google(audio))
        except:
            pass

except:
    pass



