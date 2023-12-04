import sys
from bs4 import BeautifulSoup
import requests
import re
from validate import validWikiArticleLinkString

"""
Validate command line arguments
"""
if len(sys.argv) < 2:
    print("No starting website specified")
    sys.exit()

website = sys.argv[1]

if "https://en.wikipedia.org/wiki/" not in website:
    print("Starting website must be of form https://en.wikipedia.org/wiki/[endpoint]")
    sys.exit()


"""
Define variables
"""
WIKI_LINK = "https://en.wikipedia.org"
counter = 0
MAX_HOPS = 100
visited = {website:1}

"""
Function to hop through websites till 
Philosophy or max hops has been exceeded
"""
while website != "https://en.wikipedia.org/wiki/Philosophy":

    """
    Get the current wiki page
    """
    html = requests.get(website).text
    parsed_html = BeautifulSoup(html, features="html.parser")
    body = parsed_html.find("div", {"id": "mw-content-text"})

    """
    Remove all italicized links
    """
    for italics in body.find_all("div", {'class':'hatnote'}):
        italics.decompose()

    """
    Find first link in main body that is not an invalid link and we have not visited already
    """
    link = None
    for p in body.find_all('p', limit=10):
        for l in p.find_all('a', attrs={'href': re.compile("^/wiki/")}):
            if validWikiArticleLinkString(l.get('href')) and WIKI_LINK+l.get('href') not in visited:
                link = l
                break
        if link is not None:
            break
    
    """
    Get next website to visit
    """
    if link is not None:
        visited[WIKI_LINK+link.get('href')] = 1
        website = WIKI_LINK+link.get('href')
    else:
        print("Did not find Philosophy due to a loop.")
        sys.exit()

    """
    Check if we went over max hops
    """
    if counter > MAX_HOPS:
        print("Max hops reached")
        sys.exit()

    print(website)
    counter += 1

print(str(counter) + " hops")







