import json
import webbrowser
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#Car Criteria
MAKES = ["Mercedes-Benz","Porsche","BMW"]
MAX_YEAR = 1999
MAX_PRICE = 20000

#Website URL
my_url = "https://bringatrailer.com/auctions/"

#Opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML soup
page_soup = soup(page_html, "html.parser")

#Grabs all cars objects
containers = page_soup.findAll("div",{"class":"auctions-item-container"})
containers.pop(0)

#Creating csv file
filename = "Older German Cars On Bring A Trailer.csv"
f = open(filename, "w")

headers = "Title, Price,,Link\n"
f.write(headers)

for container in containers:
    try:
        make = json.loads(container["data-searchable"])["make"]
        title = json.loads(container["data-searchable"])["title"]
        year = int(float(json.loads(container["data-searchable"])["year"]))
        price = int(float(container["data-price"]))
        link = container.find("a","auctions-item-image-link")["href"]
    except:
        continue

    if(make in MAKES and year <= MAX_YEAR and price <= MAX_PRICE):
        print("Title: " + title)
        print("Price: " + str(price))
        print("Link: " + link)

        f.write(title +"," + str(price) + "," + " " + "," + link + '\n')
        #opens link in browser
        webbrowser.open(link) 

f.close()