from spellchecker import SpellChecker
from bs4 import BeautifulSoup
from urllib.request import urlopen

# spell checker
spellcheck = SpellChecker()

def check(question):
    question = removeSpecialCharacters(question)
    words = question.split()
    # mispelled = spellcheck.unknown(words)
    output = []

    for word in words:
        if word != spellcheck.correction(word):
            output.append(spellcheck.correction(word))
        else:
            output.append(word)

    return ' '.join(output)


def removeSpecialCharacters(sentence):
    unwanted = "!@#$%^&*()[]}{;:,./<>?\|`~-=_+"

    for char in unwanted:
        sentence = sentence.replace(char, "")
    
    return sentence


def getInfectedCount():
    url = 'https://www.worldometers.info/coronavirus/'
    
    html_page = urlopen(url).read()
    soup = BeautifulSoup(html_page, 'html.parser')

    count = soup.find("div", {"class": "maincounter-number"}).find("span", text=True)

    return count.string