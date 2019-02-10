import speech_recognition as sr
import pyttsx3
import sentencepiece as spm


r = sr.Recognizer()

sp = spm.SentencePieceProcessor()
sp.Load("./dataset/sp.en.model")

def speak(message):
    engine=pyttsx3.init()
    engine.setProperty('voice', "estonian")
    engine.setProperty('rate', 150)
    engine.say('Tere! Minu nimi on Rezwan. Ma olen õpilane. Ma õpin Tartu Ülikoolis.')  #for testing
    engine.say('{}'.format(message))
    engine.runAndWait()

def encodeAndSaveAsText(message):
    file = open("en.txt", "w")
    encoded_text = sp.EncodeAsPieces(message)
    file.write(' '.join(encoded_text))
    file.close()
    print("--- encoded ---")

def translate(message):
    return True

def decode(message):
    sp.DecodePieces(message)


try:
    message = "Hello. I am Rezwan. I live in Tallinn. I like to travel. I eat rice, meat and coffee. Yesterday, I went to school."

    encodeAndSaveAsText(message)

except:
    pass



