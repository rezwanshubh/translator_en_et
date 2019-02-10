import speech_recognition as sr
import sentencepiece as spm

r = sr.Recognizer()


def encodeAndSaveAsText(message):
    file = open("en.txt", "w")
    sp = spm.SentencePieceProcessor()
    sp.Load("./dataset/sp.en.model")
    encoded_text = sp.EncodeAsPieces(message)
    file.write(' '.join(encoded_text))
    file.close()

with sr.Microphone() as source:
    print('--- say something ---');
    audio = r.listen(source)

try:
    message = r.recognize_google(audio)
    print('Text: ' + message);
    encodeAndSaveAsText(message)
except:
    pass




