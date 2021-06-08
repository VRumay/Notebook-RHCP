import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
import re
import os

# I didn't use the variable, maybe I'll work on extending this scraper late on. 
artist = "Red Hot Chili Peppers"         

# Manually looked for the album pages to iterate over them
albumURLs = {'The Red Hot Chili Peppers':'https://genius.com/albums/Red-hot-chili-peppers/The-red-hot-chili-peppers',
             'Freaky Styley':'https://genius.com/albums/Red-hot-chili-peppers/Freaky-styley',
             'The Uplift Mofo Party Plan':'https://genius.com/albums/Red-hot-chili-peppers/The-uplift-mofo-party-plan',
             "Mother's Milk":'https://genius.com/albums/Red-hot-chili-peppers/Mothers-milk',
             'Blood Sugar Sex Magik':'https://genius.com/albums/Red-hot-chili-peppers/Blood-sugar-sex-magik',
             'One Hot Minute':'https://genius.com/albums/Red-hot-chili-peppers/One-hot-minute',
             'Californication':'https://genius.com/albums/Red-hot-chili-peppers/Californication',
             'By the Way':'https://genius.com/albums/Red-hot-chili-peppers/By-the-way',
             'Stadium Arcadium':'https://genius.com/albums/Red-hot-chili-peppers/Stadium-arcadium',
             "I'm with You":'https://genius.com/albums/Red-hot-chili-peppers/Im-with-you',
             'The Getaway':'https://genius.com/albums/Red-hot-chili-peppers/The-getaway'}

# Dataframe to store data
column_names = ["songName", "songURL", "songLyrics"]
songDf = pd.DataFrame(columns = column_names)

# Iterate over the values in the URL dictionary
for url in albumURLs.values():
    hdr = {'User-Agent': 'Mozilla/5.0'} # Pretending to be a browser ;)
    albumWebsite = Request(url, headers=hdr)
    albumPage = urlopen(albumWebsite)
    pageSoup = soup(albumPage, "html.parser") 

    # After the HTML is saved, find the tables containing each song
    songInfo = pageSoup.findAll("div",{"class":"chart_row-content"}) # Find each row in the songs table
    
    for eachSong in songInfo:
        songName = (eachSong.find("h3", class_="chart_row-content-title").text).replace("Lyrics","").replace("\n","").replace("  ","") # find and save the song name to a variable, adding some format along the way
        a = eachSong.find("a", class_="u-display_block") # Find the a tag that contains the url
        songURL = a['href'] # Save the url to a variable
        
        # Create a variable that will contain the lyrics when they are scraped
        songLyrics = ""

        # As I was scraping, I started noticing that sometimes genius.com would return a different HTML, that did not contain any lyrics
        # I think that's a way for genius.com to stop scraping from happening, So I created a loop that would attempt to scrape lyrics for a particular song 
        # until the lyrics variable is not empty
        while songLyrics == "":      
            songWebsite = Request(songURL, headers=hdr)
            songPage = urlopen(songWebsite)
            lyricsSoup = soup(songPage, "html.parser")
            
            try: 
                htmlLyrics = lyricsSoup.find("div",class_="lyrics") # So when the website opens in chrome, the classname is "Lyrics__Container-sc-1ynbvzw-6 krDVEH", but when opened through BS4, the classname is "Lyrics"
                textLyrics = htmlLyrics.get_text(separator=" ").strip()
                songLyrics = re.sub("[\(\[].*?[\)\]]", '', textLyrics) # Genius has the Lyric structure inside every song, like [Chorus], I will remove that to keep the Lyrics clean
                # Some songs have empty lyrics because they are instrumental, so if the scrapers comes up with a situation like this, bue it didnt error out in the past 3 lines of code
                #  it will put "[Instrumental]"" in the lyrics variable
                if songLyrics == "":
                    songLyrics = "[Instrumental]"
            # However, if it does error out in the first 3 lines of the "try" (exception handler), it will keep the lyrics as an empty string and restart the while loop
            # Until it catches the                        
            except:
                songLyrics = ""
                print("Retrying...")
                
            time.sleep(5)

        songDf.loc[len(songDf)]=[songName, songURL, songLyrics]

cwd = os.getcwd()
songDf.to_csv(fr'{cwd}\Scraped Lyrics.csv', index=False) 
    


        
