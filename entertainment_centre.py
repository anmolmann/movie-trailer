import fresh_tomatoes
import json
import urllib
from bs4 import BeautifulSoup
import string
from recordtype import recordtype

url = "http://api.themoviedb.org/3/movie/upcoming?api_key=2824ef0048b9cf1ffbba8902600c5d2d&page=1"
response = urllib.urlopen(url)

# movie data(response => in json format to be converted into an array "data")
data = json.loads(response.read())

# create a video class with several instance variables
Video = recordtype('Video', 'poster_path adult overview release_date genre_ids id original_title original_language title backdrop_path popularity vote_count video vote_average')

# create instances of Video class and save these instances in an array "results"
results = [Video(**k) for k in data["results"]]

# generate a youtube movie trailer link for each movie using recordtype as it is mutable
for res in results:
    url = "http://youtube.com/results?search_query="+res.title+"official_trailer"
    response2 = urllib.urlopen(url) 
    html = response2.read()
    soup = BeautifulSoup(html)
    vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
    new_trailer_url = "http://www.youtube.com"+vid['href']
    res.original_title = new_trailer_url

fresh_tomatoes.open_movies_page(results)
