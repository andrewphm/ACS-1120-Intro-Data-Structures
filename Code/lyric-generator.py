import lyricsgenius
import os
from dotenv import load_dotenv
# generate an api key and paste it
# https://genius.com/api-clients
load_dotenv()

genius_access_token = os.getenv('GENIUS_ACCESS_TOKEN')
genius = lyricsgenius.Genius(genius_access_token)

def save_lyrics(songs, artist_name, album_name):
    for i in range(len(songs
    )):
        song_title = songs[i]
        song = genius.search_song(song_title, artist_name)
        lyrics = song.lyrics
        lyrics_lines = lyrics.split('\\n')[1:]  # Skip the first line
        with open('data/songs/{}/{}_{}_{}.txt'.format('_'.join(artist_name.split(' ')), i+1, album_name, '-'.join(''.join(song_title.split('\'')).split(' '))), 'w') as f:
            f.writelines('\n'.join(lyrics_lines))  # Write the remaining lines to the file


if __name__ == '__main__':
    songs = ["Love Story", "You Belong With Me", "Shake It Off", "Blank Space", "Bad Blood"]
    save_lyrics(songs, 'taylor swift', '')
