import sentencepiece as spm
from gtts import gTTS

sp = spm.SentencePieceProcessor()
sp.Load("./dataset/sp.et.model")
message = open("pred.txt", "r").read()
message_decoded = sp.DecodePieces(message.split())

print(message_decoded)
tts = gTTS(message_decoded)
tts.save('et.mp3')

#print(message)
#print(sp.DecodePieces(message))
