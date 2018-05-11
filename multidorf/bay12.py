from bs4 import BeautifulSoup
import urllib.request


def list_df():
    f = urllib.request.urlopen('http://bay12games.com/dwarves/older_versions.html')
    soup = BeautifulSoup(f.read(), 'html.parser')
    return soup.body.find('p', attrs={'class':'menu'}).text