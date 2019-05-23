::!/usr/bin/env bash

rm ./pred.txt
rm ./en.txt
rm ./et.mp3

::"---initialize---"

python ./speech_to_text.py
::"---speech to text---"

python ../OpenNMT-py/translate.py -model ./models/_step_350000.pt -src ./en.txt -output ./pred.txt -replace_unk -verbose
::"---translated and data saved in pred.txt---"

python ./decode.py
::"---decode and save as et.mp3---"

python ./play_audio.py
::"---play done---"

::perl ../OpenNMT-py/tools/multi-bleu.perl pred.txt < human.pred.atok

::rm ./pred.txt
::rm ./en.txt
::rm ./et.mp3