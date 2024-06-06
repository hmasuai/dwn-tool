# Yet another wacky download tool
Real simple python + shell script to download a playlist from Spotify. Should be simple but haven't been able to test this so let me know if something doesn't work out. 
#### Guide to use
###### Pre-Installation
You'll need python3 and zsh installed before being able to use this.
Do `brew install python3` in the terminal and then do `brew install zsh`
###### Installation
1. Press the code and download zip button in github then extract the folder.
2. Copy Spotify playlist and use [Exportify](https://watsonbox.github.io/exportify/) (not on firefox) and download the .csv file of the playlist. Don't change any of the settings or anything. **RENAME THE FILE TO songs.csv**
3. Create a folder(or use whatever one you want) and put the .csv file into it along with space_replace.py and grabsound.sh.
4. Open up command prompt and us `cd` to move into the folder. (Do `cd [destination]` until you arrive at the folder. i.e. `cd desktop` then `cd songs`)
5. Run the commands `chmod +x ./grabsound.sh` press enter and then `./grabsound.sh`
6. yt-dlp will start to download all of the songs into a new folder called songs.
7. Voila you're done :)
8. To run again simply replace the songs.csv and delete the other created files.

#### Limitations
- Downloads through a youtube search of title + artist which could fail
- No way to specify song besides the title or artist (specific releases could be challenging)

#### To Do
- Need to fix running another csv through without deletion
- Import metadata?
- Look at if theres a better way to ensure correct download
