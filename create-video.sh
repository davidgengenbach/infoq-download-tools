#!/usr/bin/env bash

set -x

VIDEO_URL_IN="$1"
FFCONCAT_FILE_IN='ffconcat.txt'
AUDIO_IN='infoq-11-sep-simplemadeeasy.mp3'
VIDEO_OUT='infoq-11-sep-simplemadeeasy.mp4'
FPS=5

if [ $VIDEO_URL_IN == "" ]; then
    VIDEO_URL_IN='https://www.infoq.com/presentations/Simple-Made-Easy'
fi

mkdir -p data/slides

cd data
../download.py "$VIDEO_URL_IN" || exit 1
../process.py || exit 1
ffmpeg -i $FFCONCAT_FILE_IN -i $AUDIO_IN -c:a copy -vf fps=$FPS $VIDEO_OUT
