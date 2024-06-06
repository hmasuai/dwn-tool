#!/usr/bin/env zsh
python3 space_replace.py && sleep 1 # Run space_replace.py then pause for 1 second so final.txt can be created
# Delete spreadsheet header then add ytsearch: to the song title + artist name pipe that result to yt-dlp
sed 's/Track+Name+Artist+Name(s)//g;s/^/ytsearch:/' < final.txt | yt-dlp --batch-file - -x -P "$PWD/songs" -o "%(title)s.%(ext)s"
#yt-dlp options are audio only, create a folder, and name it based on title.
