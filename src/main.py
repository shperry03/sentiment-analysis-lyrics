from scrape_lyrics import scrape_lyrics
from sentiment_analysis_cardiffnlp import sentiment_analysis_cardiffnlp

def main():

    song = input("Song: ")
    artist = input("Artist: ")

    lyrics = scrape_lyrics(song=song, artist=artist)
    sentiments = sentiment_analysis_cardiffnlp(lyrics=lyrics)

    for objects in zip(lyrics,sentiments):
        print(objects)


if __name__ == '__main__':
    main()