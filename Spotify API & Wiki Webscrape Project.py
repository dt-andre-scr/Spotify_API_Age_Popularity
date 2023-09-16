#packages and  Spotify API
import spotipy
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'get_your_client_id' # must get your own client_id for security purposes
client_secret = 'get_your_client_secret' # must get your own client_secret for secruity purposes

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Get name of artist
artist_name = input("Please enter the name of the artist: ")

#Search for artist, run this ONCE
results = sp.search(q='artist:' + artist_name, type='artist')

#digging through results variable to get the name and popularity of the first search result
first_artist_name = results['artists']['items'][0]['name']
first_artist_popularity = results['artists']['items'][0]['popularity']

#creating a dictionary and putting data into it
artist_info = {}
artist_info[first_artist_name] = first_artist_popularity

#creating lists and putting data into them
artist_name = []
artist_popularity = []

artist_name.append(first_artist_name)
artist_popularity.append(first_artist_popularity)

#checking the output
#print(artist_info)
#print(artist_name)
#print(artist_popularity)

artist_id = results['artists']['items'][0]['id']
similar_artists = sp.artist_related_artists(artist_id)

#looping through similar_artists_var, grabbing the 'name' and the 'popularity' and appending to the artist_info list
for similar in similar_artists['artists']:
    artist_info[similar['name']] = similar['popularity']
    artist_name.append(similar['name'])
    artist_popularity.append(similar['popularity'])
    print(similar['name'], similar['popularity'])

#checkpoint

print(artist_name)


#checkpoint


print(artist_popularity)


#gathering artist data from wikipedia and setting up groupings & exceptions

data_dict = {}
for name in artist_name:
    
    list_name = str(name).split()
    
    if len(list_name) == 1:

        #grabbing individual names from list
        name = list_name[0]   
        # create URL to Wikipedia
        wiki_url1 = f'https://en.wikipedia.org/wiki/{name}'
        
        # send the request and get the response
        response = requests.get(wiki_url1)
        
        # parse the response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # making variables for band_info and age_info for testing
        band_info = soup.find_all('th',{'class':'infobox-label'})
        age_info = soup.find('span', {'class':'noprint ForceAgeToShow'})
        
        #looping through band_info to find exceptions
        for x in band_info:
            
            if x.text == 'Members' or x.text =='Past members':
                members_var = x.text
                print(f'{name} is a band \n')
                break
                   
            elif x.text == 'Died':
                deceased_var = x.text
                print(f'{name} is deceased \n')
                      
        # after going through exceptions, checking for age_info         
        try:
            part_age = age_info.text
            #regex to get only numbers from age variable
            #search for all numbers that contain at least one digit from 0-9
            pattern = "[0-9]+"
            age = re.findall(pattern, part_age) #this will give us a list so to extract the number we will provide the position
            age = age[0]
            # print the results
            data_dict[name]=age
            print(f'{name} is {age} years old. \n')
        except:
            pass
############################################################################################################################
    elif len(list_name) == 2:    
        #grabbing individual names from list
        name = list_name[0]
        name2 =list_name[1]  
        # create URL to Wikipedia
        wiki_url4 = f'https://en.wikipedia.org/wiki/{name}_{name2}'
        
        # send the request and get the response
        response = requests.get(wiki_url4)
        
        # parse the response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # making variables for band_info and age_info for testing
        band_info = soup.find_all('th',{'class':'infobox-label'})
        age_info = soup.find('span', {'class':'noprint ForceAgeToShow'})
        
        #looping through band_info to find exceptions
        for x in band_info:
            
            if x.text == 'Members' or x.text =='Past members':
                members_var = x.text
                print(f'{name} {name2} is a band \n')
                break
                
                
            elif x.text == 'Died':
                deceased_var = x.text
                print(f'{name} {name2} is deceased \n')
                      
        # after going through exceptions, checking for age_info         
        try:
            part_age = age_info.text
            #regex to get only numbers from age variable
            #search for all numbers that contain at least one digit from 0-9
            pattern = "[0-9]+"
            age = re.findall(pattern, part_age) #this will give us a list so to extract the number we will provide the position
            age = age[0]
            # print the results
            data_dict[name+' '+name2]=age
            print(f'{name} {name2} is {age} years old. \n')
        except:
            pass
############################################################################################################################
    elif len(list_name) == 3:
        #grabbing individual names from list
        name = list_name[0]
        name2 = list_name[1]
        name3 = list_name[2]   
        # create URL to Wikipedia
        wiki_url5 = f'https://en.wikipedia.org/wiki/{name}_{name2}_{name3}'
        
        # send the request and get the response
        response = requests.get(wiki_url5)
        
        # parse the response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # making variables for band_info and age_info for testing
        band_info = soup.find_all('th',{'class':'infobox-label'})
        age_info = soup.find('span', {'class':'noprint ForceAgeToShow'})
        
        #looping through band_info to find exceptions
        for x in band_info:
            
            if x.text == 'Members' or x.text =='Past members':
                members_var = x.text
                print(f'{name} {name2} {name3} is a band \n')
                break
                
                
            elif x.text == 'Died':
                deceased_var = x.text
                print(f'{name} {name2} {name3} is deceased. \n')
                      
        # after going through exceptions, checking for age_info         
        try:
            part_age = age_info.text
            #regex to get only numbers from age variable
            #search for all numbers that contain at least one digit from 0-9
            pattern = "[0-9]+"
            age = re.findall(pattern, part_age) #this will give us a list so to extract the number we will provide the position
            age = age[0]
            # print the results
            data_dict[name+' '+name2+' '+name3]=age
            print(f'{name} {name2} {name3} is {age} years old.\n')
        except:
            pass
############################################################################################################################        
    else:
        print('UNKNOWN ERROR')


#checkpoint


print(artist_info) #contains names and popularity score of artists as dictionary

#creating empty lists to store data


names = []
ages = []
popularity = []

for name in data_dict:
    names.append(name)
    ages.append(data_dict[name])


#checkpoint

print(names)
print(ages)

#looping through values in names list and trying each value per position inside the artist_info dictionary to see
#if there's matches and if so, append it to the popularity list.. this essentially is a join to weed out null values

for pop_score in names:
    keys = artist_info[pop_score]
    popularity.append(keys)
print(popularity)


#checkpoint

print(data_dict) #contains names and ages of artists minus last as dictionary (MAIN)


# final dataframe with name, age, and popularity of artists from spotify & wikipedia

artist_name_age_pop = {'name': names, 'age': ages, 'popularity': popularity}
artist_info_df = pd.DataFrame(artist_name_age_pop)
artist_info_df


# importing data to .csv, type in your destination 

artist_info_df.to_csv("insert_your_destination")
