#!/usr/bin/env bash

cd static
ffmpeg -y -i android-chrome-512x512.png -vf scale=192:192 android-chrome-192x192.png
ffmpeg -y -i android-chrome-512x512.png -vf scale=32:32 apple-touch-icon.png
ffmpeg -y -i android-chrome-512x512.png -vf scale=16:16 favicon-16x16.png
ffmpeg -y -i android-chrome-512x512.png -vf scale=32:32 favicon-32x32.png
ffmpeg -y -i android-chrome-512x512.png -vf scale=32:32 favicon.ico