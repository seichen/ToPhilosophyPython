from bs4 import BeautifulSoup
"""
from: https://stackoverflow.com/questions/10634278/get-the-first-link-in-a-wikipedia-article-not-inside-parentheses
"""
def validWikiArticleLinkString(href):
    """ Takes a string and returns True if it contains the substring
        '/wiki/' in the beginning and does not contain any of the
        "special" wiki pages. 
    """
    return (href.find("/wiki/") == 0
            and href.find("(disambiguation)") == -1 
            and href.find("File:") == -1 
            and href.find("Wikipedia:") == -1
            and href.find("Portal:") == -1
            and href.find("Special:") == -1
            and href.find("Help:") == -1
            and href.find("Template_talk:") == -1
            and href.find("Template:") == -1
            and href.find("Talk:") == -1
            and href.find("Category:") == -1
            and href.find("Bibcode") == -1
            and href.find("Main_Page") == -1
            and href.find("#") == -1
            and href.find("%") == -1
            and href.find(":") == -1
            and href.find(",") == -1
            and href.find("(") == -1)