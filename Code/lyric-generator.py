import lyricsgenius
import os
from dotenv import load_dotenv
import re
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
        if song is not None:
            lyrics = song.lyrics
            lyrics_lines = lyrics.split('\n')[1:]  # Skip the first line
            lyrics_lines = [re.sub(r'\d+Embed$', '', line) for line in lyrics_lines]  # Remove trailing xxEmbed
            lyrics_lines = [line for line in lyrics_lines if not line.startswith('[')]  # Remove lines starting with [

            with open('data/songs/{}/{}_{}_{}.txt'.format('_'.join(artist_name.split(' ')), i+1, album_name, '-'.join(''.join(song_title.split('\'')).split(' '))), 'w') as f:
                f.writelines('\n'.join(lyrics_lines))  # Write the remaining lines to the file
        else:
            print(f"Song {song_title} not found!")


if __name__ == '__main__':
    taylor_swift_songs = [
    "Blank Space",
    "Style",
    "Out of The Woods",
    "All You Had To Do Was Stay",
    "Shake It Off",
    "I Wish You Would",
    "Bad Blood",
    "Wildest Dreams",
    "How You Get The Girl",
    "This Love",
    "I Know Places",
    "Clean",
    "Wonderland",
    "You Are In Love",
    "New Romantics",
    "I Forgot That You Existed",
    "Cruel Summer",
    "Lover",
    "The Man",
    "The Archer",
    "I Think He Knows",
    "Miss Americana & The Heartbreak Prince",
    "Paper Rings",
    "Cornelia Street",
    "Death By A Thousand Cuts",
    "London Boy",
    "Soon You'll Get Better",
    "False God",
    "You Need To Calm Down",
    "Afterglow",
    "ME!",
    "It's Nice To Have A Friend",
    "Daylight",
    "Christmas Tree Farm",
    "Only The Young",
    "Beautiful Ghosts",
    "The Lakes",
    "Right Where You Left Me",
    "It's Time To Go",
    "willow",
    "champagne problems",
    "gold rush",
    "tis the damn season",
    "tolerate it",
    "no body, no crime",
    "happiness",
    "dorothea",
    "coney island",
    "ivy",
    "cowboy like me",
    "long story short",
    "marjorie",
    "closure",
    "evermore",
    ]

    # remove duplicate songs
    taylor_swift_songs = list(dict.fromkeys(taylor_swift_songs))


    save_lyrics(taylor_swift_songs, 'taylor swift', '')
