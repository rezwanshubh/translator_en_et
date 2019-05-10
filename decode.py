import sentencepiece as spm
from gtts import gTTS

sp = spm.SentencePieceProcessor()
sp.Load("./dataset/sp.et.model")
message = open("pred.txt", "r", encoding="utf8").read()
message_decoded = sp.DecodePieces(message.split())

print(message_decoded)
tts = gTTS(message_decoded, lang='et')
tts.save('et.mp3')

