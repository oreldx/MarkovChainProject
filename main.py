import random
from pprint import pprint

def getInputText(path):
    with open(path) as f:
        txt = f.read()
    return txt


def markovChainChar(order):
    text = getInputText('input_text.txt')
    ngrams = {}
    # Model creation
    for i in range(len(text)-order):
        currentNgram = text[i:i+order]
        if currentNgram not in ngrams:
            ngrams[currentNgram] = [text[i+order]]
        else:
            ngrams[currentNgram].append(text[i+order])

    pprint(ngrams)

    # Text generation
    length = 100
    text = random.choice(list(ngrams))
    for i in range(length):
        if text[i:i+order] not in ngrams:
            break
        nextChar = random.choice(ngrams[text[i:i+order]])
        text += nextChar
    print(text)

def findCursorWord(cursor, text):
    i = cursor
    endText = False
    while text[i] != ' ':
        i += 1
        if i + 1 > len(text):
            endText = True

    return cursor, i, endText

def markovChainWord():
    text = getInputText('input_text.txt')
    words = {}

    cursor = 0
    endText = False
    while cursor < len(text):
        cursor, i, endText = findCursorWord(cursor, text)
        if not endText:
            currentWord = text[cursor:i]
            cursor = i + 1
            cursor, i, endText = findCursorWord(cursor, text)
            nextWord = text[cursor:i]
            if currentWord not in words:
                words[currentWord] = [nextWord]
            print(currentWord)


if __name__ == '__main__':
    markovChainWord()
