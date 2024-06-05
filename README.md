# Yet another wacky download tool
Real simple python + shell script to download a playlist from Spotify. Should be simple but haven't been able to test this so let me know if something doesn't work out. 
#### Guide to use
###### Pre-Installation
You'll need python3 and zsh installed before being able to use this.
Do `brew install python3` in the terminal and then do `brew install zsh`
###### Installation
1. Copy Spotify playlist and use [Exportify](https://watsonbox.github.io/exportify/) (not on firefox) and download the .csv file of the playlist. Don't change any of the settings or anything. **RENAME THE FILE TO songs.csv**
2. Create a folder(or use whatever one you want) and put the .csv file into it along with space_replace.py and grabsound.sh.
3. Open up command prompt and us `cd` to move into the folder. (Do `cd [destination]` until you arrive at the folder. i.e. `cd desktop` then `cd songs`)
4. Run the commands `chmod +x ./grabsound.sh` press enter and then `./grabsound.sh`
5. yt-dlp will start to download all of the songs into a new folder called songs.
6. Voila you're done :)
