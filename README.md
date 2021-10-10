#Web Scraping with Python - Beautiful Soup Crash

##Installation
___Requests___
      
    pip install requests

___BeautifulSoup___

    pip install beautifulsoup4

##Usage
    import requests  
    from bs4 import BeautifulSoup 
    bs = BeautifulSoup()

##Examples
__Making web requests__

With Python's ___requests___ (___pip install requests___) library we're getting a web page by using ___get()___ on the URL. The response ___r___ contains many things, but using ___r.content___ will give us the HTML. Once we have the HTML we can then parse it for the data we're interested in analyzing.
    
    import requests
    url = 'https://www.coingecko.com/en'
    r = requests.get(url)
    print(r.content[:100])    

__Parsing HTML with BeautifulSoup__

We used ___requests___ to get the page from the Cryptocurrency server, but now we need the BeautifulSoup library (___pip install beautifulsoup4___) to parse HTML and XML. When we pass our HTML to the BeautifulSoup constructor we get an object in return that we can then navigate like the original tree structure of the DOM.

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.content, 'html.parser')

This ___soup___ object defines a bunch of methods — many of which can achieve the same result — that we can use to extract data from the HTML. 

