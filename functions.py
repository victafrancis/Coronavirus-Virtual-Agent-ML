from spellchecker import SpellChecker

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

