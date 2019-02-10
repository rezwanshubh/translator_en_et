#!/usr/bin/env bash

echo "---initialize---"

python ./speech_to_text.py
echo "---speech to text---"

python ../OpenNMT-py/translate.py -model ./models/_step_350000.pt -src ./en.txt -output ./pred.txt -replace_unk -verbose
echo "---translated and data saved in pred.txt---"

python ./decode.py
echo "---decode and save as et.mp3---"

python ./play_audio.py
echo "play done"

