import pandas as pd
import numpy as np

rhcp = pd.read_excel(r'C:\Users\Rumay-Paz\Desktop\Python Projects\RHCP\RHCP.xlsx')

#rhcp['Lyrics'] = rhcp['Lyrics'].str.replace('\n',' ').str.upper()

# I made a list of all cities and towns I could find in California and also a couple referrences, like the Lakers

#lst = ['Adelanto','Agoura Hills','Alameda','Albany','Alhambra','Aliso Viejo','Alturas','Amador City','American Canyon','Anaheim','Anderson','Angels Camp','Antioch','Apple Valley','Arcadia','Arcata','Arroyo Grande','Artesia','Atascadero','Atherton','Atwater','Auburn','Avalon','Avenal','Azusa','Bakersfield','Baldwin Park','Banning','Barstow','Beaumont','Bell Gardens','Bellflower','Belmont','Belvedere','Benicia','Berkeley','Beverly Hills','Big Bear Lake','Biggs','Bishop','Blue Lake','Blythe','Bradbury','Brawley','Brea ','Brentwood','Brisbane','Buellton','Buena Park','Burbank','Burlingame','Calabasas','Calexico','California City','Calimesa','Calipatria','Calistoga','Camarillo','Campbell','Canyon Lake','Capitola','Carlsbad','Carmel-by-the-Sea','Carpinteria','Carson','Cathedral City','Ceres','Cerritos','Chico','Chino','Chino Hills','Chowchilla','Chula Vista','Citrus Heights','Claremont','Clayton','Clearlake','Cloverdale','Clovis','Coachella','Coalinga','Colfax','Colma','Colton','Colusa','Commerce','Compton','Concord','Corcoran','Corning','Corona','Coronado','Corte Madera','Costa Mesa','Cotati','Covina','Crescent City','Cudahy','Culver City','Cupertino','Cypress','Daly City','Dana Point','Danville','Davis','Del Mar','Del Rey Oaks','Delano','Desert Hot Springs','Diamond Bar','Dinuba','Dixon','Dorris','Dos Palos','Downey','Duarte','Dublin','Dunsmuir','East Palo Alto','Eastvale','El Cajon','El Centro','El Cerrito','El Monte','El Segundo','Elk Grove','Emeryville','Encinitas','Escalon','Escondido','Etna','Eureka','Exeter','Fairfax','Fairfield','Farmersville','Ferndale','Fillmore','Firebaugh','Folsom','Fontana','Fort Bragg','Fort Jones','Fortuna','Foster City','Fountain Valley','Fowler','Fremont','Fresno','Fullerton','Galt','Garden Grove','Gardena','Gilroy','Glendale','Glendora','Goleta','Gonzales','Grand Terrace','Grass Valley','Greenfield','Gridley','Grover Beach','Guadalupe','Gustine','Half Moon Bay','Hanford','Hawaiian Gardens','Hawthorne','Hayward','Healdsburg','Hemet','Hercules','Hermosa Beach','Hesperia','Hidden Hills','Highland','Hillsborough','Hollister','Holtville','Hughson','Huntington Beach','Huntington Park','Huron','Imperial','Imperial Beach','Indian Wells','Indio','Inglewood','Ione','Irvine','Irwindale','Isleton','Jackson','Jurupa Valley','Kerman','King City','Kingsburg','La Cañada Flintridge','La Habra','La Habra Heights','La Mesa','La Mirada','La Palma','La Puente','La Quinta','La Verne','Lafayette','Laguna Beach','Laguna Hills','Laguna Niguel','Laguna Woods','Lake Elsinore','Lake Forest','Lakeport','Lakewood','Lancaster','Larkspur','Lathrop','Lawndale','Lemon Grove','Lemoore','Lincoln','Lindsay','Live Oak','Livermore','Livingston','Loma Linda','Lomita','Lompoc','Long Beach','Loomis','Los Alamitos','Los Altos','Los Altos Hills','Los Angeles','Los Banos','Los Gatos','Loyalton','Lynwood','Madera','Malibu','Mammoth Lakes','Manhattan Beach','Manteca','Maricopa','Marina','Martinez','Marysville','Maywood','McFarland','Mendota','Menifee','Menlo Park','Merced','Mill Valley','Millbrae','Milpitas','Mission Viejo','Modesto','Monrovia','Montague','Montclair','Monte Sereno','Montebello','Monterey','Monterey Park','Moorpark','Moraga','Moreno Valley','Morgan Hill','Morro Bay','Mount Shasta','Mountain View','Murrieta','Napa','National City','Needles','Nevada City','Newark','Newman','Newport Beach','Norco','Norwalk','Novato','Oakdale','Oakland','Oakley','Oceanside','Ojai','Ontario','Orange Cove','Orinda','Orland','Oroville','Oxnard','Pacific Grove','Pacifica','Palm Desert','Palm Springs','Palmdale','Palo Alto','Palos Verdes Estates','Paradise','Paramount','Parlier','Pasadena','Paso Robles','Patterson','Perris','Petaluma','Pico Rivera','Piedmont','Pinole','Pismo Beach','Pittsburg','Placentia','Placerville','Pleasant Hill','Pleasanton','Plymouth','Point Arena','Pomona','Port Hueneme','Porterville','Portola','Portola Valley','Poway','Rancho Cordova','Rancho Cucamonga','Rancho Mirage','Rancho Palos Verdes','Rancho Santa Margarita','Red Bluff','Redding','Redlands','Redondo Beach','Redwood City','Reedley','Rialto','Richmond','Ridgecrest','Rio Dell','Rio Vista','Ripon','Riverbank','Riverside','Rocklin','Rohnert Park','Rolling Hills','Rolling Hills Estates','Rosemead','Roseville','SacramentoCapital city','St. Helena','Salinas','San Anselmo','San Bernardino','San Bruno','San Carlos','San Clemente','San Diego','San Dimas','San Fernando','San Francisco','San Gabriel','San Jacinto','San Joaquin','San Jose','San Juan Bautista','San Juan Capistrano','San Leandro','San Luis Obispo','San Marcos','San Marino','San Mateo','San Pablo','San Rafael','San Ramon','Sand City','Sanger','Santa Ana','Santa Barbara','Santa Clara','Santa Clarita','Santa Cruz','Santa Fe Springs','Santa Maria','Santa Monica','Santa Paula','Santa Rosa','Santee','Saratoga','Sausalito','Scotts Valley','Seal Beach','Seaside','Sebastopol','Selma','Shafter','Shasta Lake','Sierra Madre','Signal Hill','Simi Valley','Solana Beach','Soledad','Solvang','Sonoma','Sonora','South El Monte','South Gate','South Lake Tahoe','South Pasadena','South San Francisco','Stanton','Stockton','Suisun City','Sunnyvale','Susanville','Sutter Creek','Taft','Tehachapi ', 'Tehama ', 'Temecula ', 'Temple City ', 'Thousand Oaks ', 'Tiburon ', 'Torrance ', 'Tracy ', 'Truckee ', 'Tulare ', 'Tulelake ', 'Turlock ', 'Tustin ', 'Twentynine Palms ', 'Ukiah ', 'Union City ', 'Upland ', 'Vacaville ', 'Vallejo ', 'Ventura ', 'Vernon ', 'Victorville ', 'Villa Park ', 'Visalia ', 'Vista ', 'Walnut ', 'Walnut Creek ', 'Wasco ', 'Waterford ', 'Watsonville ', 'West Covina ', 'West Hollywood ', 'West Sacramento ', 'Westlake Village ', 'Westminster ', 'Westmorland ', 'Wheatland ', 'Whittier ', 'Wildomar ', 'Willits ', 'Willows ', 'Windsor ', 'Winters ', 'Woodlake ', 'Woodland ', 'Woodside ', 'Yorba Linda ', 'Yountville ', 'Yreka ', 'Yuba City ', 'Yucaipa ', 'Yucca Valley ', 'Hollywood ', 'Cali', 'California ', 'Californication ', 'Laker', 'Angelin ', 'Venice ', 'L.A. ', 'East Side', 'West Side', 'West End', 'East End ', 'city ', 'Fax', 'Angelino', 'Golden Gate', 'Golden State']

# Then made a column for each of those items in my list

#lst = [x.upper() for x in lst]

#for i in lst:
#   print(f"{i} was found {rhcp['Lyrics'].str.upper().str.count(i).sum} times") # Fix this to show the amount of calis for each word


# Realized there were only a few of them:

found = ['CALEXICO','FAIRFAX','MALIBU','POMONA','SAN FRANCISCO','SANTA MONICA','HOLLYWOOD','CALI','CITY OF ANGEL','LAKER','VENICE','L.A. ','EAST SIDE', 'WEST SIDE', 'WEST END', 'EAST END', 'FAX', 'ANGELENO', 'GOLDEN GATE']

# I had to dig deeper to find which "city", they were talking about when the word "city" was found. :
# Cheked them all manually for context and 
    # in "Organic Anti-Beat Box Band" they refer to Fairfax as Fax
    # In "Deep kick" they talk about loving a Dirty City
    # "Tell me baby" is generally about people chasing Hollywood dreams, so I will count 1 California
    # and "Under the Bridge", they are talking about L.A., so I'm counting all those "city" as occurrences of California

# # IGNORED LOCATIONS DUE TO FAUX POSITIVES: Bell, Industry, Lodi, Orange, Williams, Arvin, Weed, Trinidad, Ross, Fortuna    


rhcp['Californias'] = rhcp['Lyrics'].str.upper().str.count('|'.join(found))



rhcp.to_excel(r'C:\Users\Rumay-Paz\Desktop\Python Projects\RHCP\CountedCalis.xlsx', index = False) 

#print(rhcp)

