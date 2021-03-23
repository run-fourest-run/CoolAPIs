import lyricsgenius
import json



access_token = r'FDpcY8Ai8OwxzTnlfzZA0W_Wyyh71nsGX6t6Cto1g7NrxaRDKSiOejkPGMjjoDs4'
genius = lyricsgenius.Genius(access_token)


def create_artist_object(artist_name):
    artist = genius.search_artist(artist_name,max_songs=1)
    return artist

def create_song(artist,song_name):
    song = artist.song(song_name)
    return song


def save_song(song):
    song.save_lyrics()

def get_lyrics(input_file):
    with open(input_file) as f:
        song = []
        data = json.load(f)
        for key, value in data.items():
            if key == 'lyrics':
                song.append(value)
        return song


input_file = r'C:\Users\afournier\PycharmProjects\ZillowAPI\GeniusAPI\CUsersafournierPycharmProjectsZillowAPIoutputjesus_walks.json'
lines = get_lyrics(input_file)

def word_count(lines):
    count = dict()
    for line in lines:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] +=1
    return(count)



word_count = word_count(lines)
sorted_word_count = max(word_count)
