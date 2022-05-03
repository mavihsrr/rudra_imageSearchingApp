import requests 
from bs4 import BeautifulSoup

def getdata(url): 
    r = requests.get(url) 
    return r.text 

GOOGLE="http://google.com/"
google_query_to_images="&tbm=isch"

def get_images(query):
    images=[]
    htmldata = getdata(GOOGLE+"search?q="+query+google_query_to_images) 
    soup = BeautifulSoup(htmldata, 'html.parser')
    for item in soup.find_all('img'):
        images.append(item['src'])
    return images

    