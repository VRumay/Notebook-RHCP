import os
import pandas as pd
import numpy as np

cwd = os.getcwd()
rhcp = pd.read_excel(fr'{cwd}\RHCP.xlsx', sheet_name="Studio Albums")
rhcp['Lyrics'] = rhcp['Lyrics'].str.upper().str.replace('\n',' ')

# #I made a list of all cities and towns I could find in California (total of 5775) and also a couple referrences, like the Lakers, Golden Gate, etc
# placesInCali = pd.read_excel(fr'{cwd}\PlacesInCali.xlsx', sheet_name="DISTINCT NAMES")["NAME"].to_list()
# placesInCali.append(r'L\.A\.') # Escape the Regex

# # I now needed to map those words to the lyrics, and find outliers or things that were out of place:
# checkGrid = rhcp['Lyrics'].str.extractall(f"({'|'.join(placesInCali)})").groupby(level=0)[0].value_counts().unstack(fill_value="")
# checkGrid.to_excel(f"{cwd}\griddedLocations.xlsx", index=False)

# # #Then processed the lyrics to count the ocurrence of each word and saved them to a dataframe:
# words = []
# wordCounts = []

# for i in placesInCali:
#    words.append(i)
#    wordCounts.append(rhcp['Lyrics'].str.upper().str.count(i.upper()).sum())

# wordDf = pd.DataFrame(list(zip(words, wordCounts)),columns =['word', 'count']) 

# wordDf.to_csv(fr'{cwd}\CountedWords.csv', index = False)

# # Realized there were only a few of them:

foundCalis =  ['HOLLYWOOD',
                'CALIFORNIA',
                'CALIFORNICATION',
                r'L\.A\.', # Escaping the Regex
                'CITY',
                'LAKER',
                'SUNSET',
                'ANGELS',
                'BAY',
                'BOULEVARD',
                'CALEXICO',
                'EAST SIDE',
                'SAN FRANCISCO',
                'VENICE',
                'WEST END',
                'TOWN',
                'BIG SUR',
                'DOGTOWN',
                'FAIRFAX',
                'HAIGHT',
                'MALIBU',
                'POMONA',
                'SANTA MONICA',
                'ANGELENO',
                'GOLDEN GATE',
                'CITY OF ANGEL',
                'BONNIE BRAE',
                'VINE',
                'STARWOOD',
                'CANTERS',
                'THE FAX',
                'BART']


rhcp['Californias'] = rhcp['Lyrics'].str.count('|'.join(foundCalis))
rhcp['Californias in Words'] = rhcp['Lyrics'].str.findall(f'({"|".join(foundCalis)})').apply(", ".join)            
rhcp.to_excel(f'{cwd}\Shortlist2.xlsx')

# I had to dig deeper to find which "city" or "town", they were talking about when those words were found, 
# so I went ahead and checked all the lyrics manually to get some more context and make sure I was getting the right results and make the proper adjustments to the count:

# -------- Positive Adjustments to Count ---------
    # Added +5: In "Hollywood (Africa)" Brotherland (appears 5 times) seems to be a nickname Anthony give to East L.A.
    # Added +14: The whole "Magic Johnson" song is an ode to the L.A. Lakers 
    #            "Magic Johnson" (6 times). 
    #            "M-A-G-I-C" (4 times). 
    #            Kareem Abdul Jabbar (1 time).
    #            Byron Scott (1 time).
    #            James Worthy (1 time). 
    #            A.C. Green (1 time).
    # Added +2: In "Mellowship Slinky in B Major", they mention the Forum and the LA Lakers.
    # Added +12: In "Under the Bridge", they talk about the city of LA as "she" (x5) and "her" (x3), plus 4 downtowns. 
    # Added +1: In "Deep kick" they talk about loving a Dirty City, L.A. is one of the most polluted and dirtiest cities in the US.
    # Added +1: In "One Big Mob", they say "We live in the city, we live in the jungle", added +1 to the count.
    # Added +3: In "Californication", California is the "Edge of the world and all of western civilization". 
    #           They also referrence San Andreas fault, through it's "Earthquakes". 
    #           I was torn about the "Good Vibrations" referrence because the Beach Boys are Californian after all, decided not to count it, because "Good Vibrations" is not about California.
    #           the "tidal waves" line is a referrence to Tool's song "AEnima", where Keenan wishes for Tidal waves to destroy California. 
    # Added +3: In "Road Trippin" they mention "the one" twice (x2), as in Highway 1, near the Pacific Ocean, and leaving "this town" (L.A.) once.
    # Added +3: In "Can't Stop" Anthony sings about "writing your message on the pavement", this is a referrence to Hollywood Boulevard. 
    #           "Ask the dust" is a novel set in L.A. 
    #           "J. Butterfly" is an environmentalist who lived in the treetop of a California Redwood to prevent a Lumber company fron cutting it down, the trees are (naturally) exclusive to California.
    # Added +1: "Old Rainbow" in "Warlocks" is a referrence to the "Rainbow Bar and Grill" in Sunset Strip, where Blackie used to sling drugs and bring Tony when he was a kid.
    # Added +4: "Tell me Baby" is about people chaing Hollywood dreams, so there are several referrences:
    #           "they come from every state", they come to California.
    #           "I'll take you to the broken sign", the Hollywood sign deteriorated over the decades and was later restored.
    #           "this town is made of many things", Hollywood is "this town".           
    #           "this place was made on you", Hollywood was made on "promising stars".

# -------- Negative Adjustments to Count ---------   
    # Substracted -1: "Readymade" brings two californias because of "The city of Pomona", counting just one.
    # Substracted -2: "Magic Johnson" contains 2 faux "town"
    # Substracted -2: In "Baby appeal", "The City" is mentioned twice, no city is specified, removed from count.
    # Substracted -1: "Green Heaven" gives a Faux positive on the "vine" of Diviner, removed from count.
    # Substracted -1: "Blackeyed blonde" contains Bay as part of Bayou, removed from count.
    # Substracted -1: "Catholic school Girls Rule" contains vine as part of Divine, removed from count.
    # Substracted -2: "Millionaires Against Hunger" contais Bay as a referrence to Chesapeake Bay (not in California) and "the city" as a generic city, removed from count.
    # Substracted -1: In "Walkabout", they talk about doing it "in the city", not a direct referrence, removed from count.
    # Substracted -1: In "Around the World" there's a faux "bay" in "Bombay", removed from count.
    # Substracted -1: The "Sunset" in "Charlie" is not a referrence to Sunset Blvd.
    # Substracted -1: "Even You Brutus?" mentions "Angels" but it's not a referrence.
    # Substracted -1: "Get Up and Jump" neither "town" or "city" are related to California.
    # Substracted -1: "By the way" the occurrence of "town" is counted twice because of "Dogtown".
    # Substracted -2: "What It Is (AKA Nina's Song)" neither "town" or "city" are related to California.
    # Substracted -1: "The Brothers Cup" neither "town" or "city" are related to California.
    # Substracted -1: "Backwoods" neither "town" or "city" are related to California.
    # Substracted -1: "Skinny Sweaty Man" neither "town" or "city" are related to California.
    # Substracted -1: "Death of a Martian" neither "town" or "city" are related to California.
    # Substracted -1: "Monarchy of Roses" neither "town" or "city" are related to California.
    # Substracted -1: "Look Around" neither "town" or "city" are related to California.
    # Substracted -1: "Goodbye Angels" neither "town" or "city" are related to California.
    # Substracted -1: "Detroit" neither "town" or "city" are related to California.
    # Substracted -1: "Happiness Loves Company" neither "town" or "city" are related to California.

# Then I applied these adjustments manually in Excel.

########### Purple Stain contains a refference to "Python power straight from Monty" #######
# MAYBE DO SOMETHING ABOUT DING DONG DINGS and AYO?
