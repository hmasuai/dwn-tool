# Yet another wacky download tool
***
Real simple python + bash script to download a playlist from Spotify. Should be simple but haven't been able to test this so let me know if something doesn't work out. 
#### Guide to use
1. Copy Spotify playlist and use [Exportify](https://watsonbox.github.io/exportify/) (not on firefox) and download the .csv file of the playlist. Don't change any of the settings or anything. **RENAME THE FILE TO songs.csv**
2. Create a folder and put the .csv file into it along with space_replace.py and grabsound.sh.
3. Open up command prompt and us `cd` to move into the folder. (Do `cd [destination]` until you arrive at the folder. i.e. `cd desktop` then `cd songs`)
4. Run the commands `chmod +x ./grabsound.sh` press enter and then `./grabsound.sh`
5. Voila you're done :)
