import speech_recognition as sr

r = sr.Recognizer()

try:
    while True:
        with sr.Microphone() as source:
            print('say something');
            audio = r.listen(source)
            print('---time over---')

        try:
            print('Text: ' + r.recognize_google(audio));
        except:
            pass

except:
    pass

