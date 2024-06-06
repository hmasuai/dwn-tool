#!/usr/bin/env python3
import csv

# Delete the irrelevant columns
# 1. Create parameters for the document
def delete_cols(file: str, cols_to_delete: list):
    # 2. Create list for the columns to be deleted
    cols_to_delete = set(cols_to_delete) # type: ignore
    # 3. Open file and write to CSV
    with open(file) as file, open('song.csv', 'w') as output: # type: ignore
        reader = list(csv.reader(file))
        headers = reader[0]

        indexes_to_delete = [idx for idx, elem in enumerate(headers) if elem in cols_to_delete]
        result = [[o for idx, o in enumerate(obj) if idx not in indexes_to_delete] for obj in reader]

        writer = csv.writer(output)
        writer.writerows(result)


delete_cols('songs.csv', ['Track URI', 'Artist URI(s)', 'Album URI', 'Album Name', 'Album Artist URI(s)', 'Album Artist Name(s)', 'Album Release Date', 'Album Image URL', 'Disc Number', 'Track Number', 'Track Duration (ms)', 'Track Preview URL', 'Explicit', 'Popularity', 'ISRC', 'Added By', 'Added At'])

# Convert CSV file to TXT and begin to add '+'
# 1. Open the CSV file in reading mode and the TXT file in writing mode
with open('song.csv', 'r') as f_in, open('song.txt', 'w') as f_out:

    # 2. Read the CSV file and store in variable
    content = f_in.read().replace(',','+')

    # 3. Write the content into the TXT file
    f_out.write(content)
    
# Add '+' to all song titles and artist names
# 1. Open above TXT file in read mode and final TXT file in writing mode
with open('song.txt', 'r') as p_in, open('final.txt', 'w') as p_out:
    # 2. Read TXT file and replace spaces with + and store in variable
    final = p_in.read().replace(' ', '+')
    # 3. Write contents into TXT file
    p_out.write(final)
