#!/usr/bin/env bash

set -x

VIDEO_URL_IN="$1"
AUDIO_IN="$2"
VIDEO_OUT="$3"

FFCONCAT_FILE_IN='ffconcat.txt'
FPS=5

usage() {
    echo "Usage: $0 VIDEO_URL MP3_AUDIO_FILE VIDEO_OUT"
}

if [ "$1" == "--help" ]; then
    usage
    exit
fi

# Defaults
if [ "$VIDEO_URL_IN" == "" ]; then
    VIDEO_URL_IN='https://www.infoq.com/presentations/Simple-Made-Easy'
fi

if [ "$AUDIO_IN" == "" ]; then
    AUDIO_IN='infoq-11-sep-simplemadeeasy.mp3'
fi

if [ "$VIDEO_OUT" == "" ]; then
    VIDEO_OUT='infoq-11-sep-simplemadeeasy.mp4'
fi

# Processing
mkdir -p data/slides
./download.py "$VIDEO_URL_IN" || exit 1
./process.py || exit 1
cd data
ffmpeg -i $FFCONCAT_FILE_IN -i $AUDIO_IN -c:a copy -vf fps=$FPS $VIDEO_OUT
