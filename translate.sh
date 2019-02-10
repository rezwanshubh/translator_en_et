#!/usr/bin/env bash

echo "hello"
#python ./main.py
echo "hello_2"
#python ../OpenNMT-py/translate.py -model _step_350000.pt -src en.txt -output pred.txt -replace_unk -verbose
echo "hello_3"
gtts-cli '▁Tere ▁, ▁mina ▁olen ▁Re z wan ▁. ▁Ma ▁elan ▁Tal linnas ▁. ▁Mulle ▁meeldib ▁reisida ▁.' --lang et --output bonjour.mp3
gtts-cli 'Tere , mina olen Re z wan . Ma elan Tallinnas. Mulle meeldib reisida.' --lang et --output bonjour_2.mp3
#python ./decode.py