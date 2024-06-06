#!/usr/bin/env zsh
python3 space_replace.py && sleep 1
sed 's/Track+Name+Artist+Name(s)//g;s/^/ytsearch:/' < final.txt | yt-dlp --batch-file - -x -P "$PWD/songs" -o "%(title)s.%(ext)s"
