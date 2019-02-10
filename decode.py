import sentencepiece as spm
from gtts import gTTS

sp = spm.SentencePieceProcessor()
sp.Load("./dataset/sp.en.model")
message = open("pred.txt", "r").read()

tts = gTTS(message)
#tts.lang('et')
tts.save('et.mp3')

#print(message)
#print(sp.DecodePieces(message))
