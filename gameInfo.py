import re, urllib.request
from bs4 import BeautifulSoup

updateRegex =   re.compile(r'(?<=<p>).*?(?=<p>)')
versionRegex =  re.compile(r'^.(\S)+')
dateRegex =     re.compile(r'(?<=\().*?(?=\))')
noteRegex =     re.compile(r'(?<=\<li\>).*?(?=\<\/li\>)')

def getGameInfo():
    url = "https://devforum.roblox.com/t/retail-tycoon-2-changelog/858524"

    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.HTTPError:
        return "HTTP error. Unable to connect."

    soup = BeautifulSoup(html, "html5lib")
    soup = str(soup)
    soup = soup.replace("\n", " ")

    allUpdates =    updateRegex.findall(soup)
    lastUpdate =    allUpdates[1]
    lastVersion =   (versionRegex.search(lastUpdate)).group()
    lastDate =      (dateRegex.search(lastUpdate)).group()
    notes =         noteRegex.findall(lastUpdate)
    notes =         ' '.join([("\n→ " + elem) for elem in notes])
    infoString =    "Last update: " + lastDate + "\nVersion: " + lastVersion + notes

    return infoString

if __name__ == '__main__':
    print(getGameInfo())