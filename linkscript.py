import json
import random

from urllib.error import HTTPError
from urllib.request import urlretrieve
import urllib.request
import tweepy

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


#keys go here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def finalScript():
    linksFile = open('/home/franky/links.txt', 'r')
    suffixFile = open('/home/franky/suffixfile.txt','r')
    numFile = open('/home/franky/prodnum.txt','r')

    links = linksFile.readlines()
    suffixes = suffixFile.readlines()
    numrange = numFile.readlines()


    randnum = random.randint(0,165)
    selectedLink = links[randnum]
    tempcategory = suffixes[randnum]
    category = tempcategory.strip('\n')

    maxprodnum = int(numrange[randnum])
    productnumber = random.randint(0,maxprodnum)

    print(selectedLink)
    print(category)
    print(maxprodnum)
    print(productnumber)

    newlink = "https://sik.search.blue.cdtapps.com/us/en/product-list-page/more-products?sessionId=23796da1-2e66-4be2-9052-5ab044285263&category=" + category + "&sort=RELEVANCE&start=" + str(productnumber -1) + "&end=" + str(productnumber) + "&c=lf&v=20200709"

    print(newlink)

    with urllib.request.urlopen(newlink) as url:
        data = json.loads(url.read().decode())
        print(json.dumps(data, indent=4, sort_keys=True))

    print(json.dumps(data["moreProducts"]["productWindow"][0]["name"], indent=4, sort_keys=True))

    text = str(data["moreProducts"]["productWindow"][0]["name"])
    tempfilepath = str(data["moreProducts"]["productWindow"][0]["mainImageUrl"])

    itemdescription = str(data["moreProducts"]["productWindow"][0]["typeName"])
    numprice = data["moreProducts"]["productWindow"][0]["priceNumeral"]
    price = '{0:.2f}'.format(numprice)
    producturl = str(data["moreProducts"]["productWindow"][0]["pipUrl"])
    
    
    #tweet
    newtext = text+"\n\n"+itemdescription+". $"+price
    photofile = downloadImage(tempfilepath)

    media_ids = []

    res = api.media_upload(photofile)
    media_ids.append(res.media_id)

    api.update_status(newtext, media_ids=media_ids)


    linksFile.close()
    suffixFile.close()
    numFile.close()

def downloadImage(url):
    print(url)

    filepath = "/home/franky/developer/ikeapic.JPG"
    print(filepath)

    try:
        urlretrieve(url, filepath)
        print("success")
        return filepath

    except FileNotFoundError as err:
        print("path error")   # something wrong with local path
    except HTTPError as err:
        print("url error")  # something wrong with url


if __name__ == '__main__':
    finalScript()

