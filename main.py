import speech_recognition as sr
import pyttsx3

def speak(message):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-20)
    engine.say('{}'.format(message))
    # engine.say("Selleks et valijakaart saada mugavalt oma e-postkasti")
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



