'''
 GOAL: 
    - Ask for artist and song
    - go to genius and get lyrics
    - write lyrics to a new text file (for now)

 TO-DO:
    - Ask for artist and song
    - go to genius and get lyrics
    - write lyrics to a new text file (for now)
'''
import api_key
import requests
import lyricsgenius as lg
# client access token for the genius API, I have mine in an api_key.py folder for security
# my_client_access_key = 'KEYKEYKEY'
client_access_token = api_key.my_client_access_key

def scrape_lyrics(song: str, artist: str) -> None:

   # take what the user input and search for the closest match
   search_term = song + ' ' + artist
   search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"

   # get the actual title and artist from the search
   response = requests.get(search_url).json()
   song, artist = response['response']['hits'][0]['result']['title'], response['response']['hits'][0]['result']['primary_artist']['name']

   # set my access key with lyrics genius
   genius = lg.Genius(client_access_token)

   # get the lyrics and print them                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
   song_search = genius.search_song(title=song, artist=artist)
   lyrics=song_search.lyrics

   # clean the lyrics to just be an array of lines
   lyrics = clean_lyrics(lyrics)

   return lyrics

'''
makes the lyrics usable
sorts the lyrics into the lines they are sung
'''
def clean_lyrics(lyrics):
   line = ""
   new_lyrics = []

   # lyrics comes in as a long string sadly
   for letter in lyrics:
      # separate lines by the new line character
      if letter == '\n'and line != '':
         # remove everything that is not lyrics
         if '[' not in line:
            new_lyrics.append(line)
         line = ''
      else:
         line = line + letter
         
   # append the last line
   new_lyrics.append(line)

   return new_lyrics
