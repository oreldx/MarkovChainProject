import random
from pprint import pprint


def getInputText(path):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    return txt


def markovChainChar(order):
    text = getInputText('input_text.txt')
    ngrams = {}
    # Model creation
    for i in range(len(text)-order):
        currentNgram = text[i:i+order]
        if text[i+order] != '\n':
            if currentNgram not in ngrams:
                ngrams[currentNgram] = [text[i+order]]
            else:
                ngrams[currentNgram].append(text[i+order])

    pprint(ngrams)

    # Text generation
    length = 300
    text = random.choice(list(ngrams))
    # text = text[:order]
    for i in range(length):
        if text[i:i+order] not in ngrams:
            break
        nextChar = random.choice(ngrams[text[i:i+order]])
        text += nextChar
    print(text)


def textCleaner(path):
    text = getInputText(path)
    for index, char in enumerate(text):
        print(index, char)
        if index+1 < len(text):
            if char in '.:,;?!' and text[index+1] != '\n':
                text = text[index:] + '\n' + text[:index]
    return text


def findCursorWord(cursor, text):
    i = cursor
    endText = False
    while text[i] != ' ' and not endText:
        i += 1
        if i + 1 >= len(text):
            endText = True
    return cursor, i, endText


def markovChainWord():
    text = getInputText('input_text.txt')
    words = {}

    cursor = 0
    endText = False
    while not endText:
        cursor, i, endText = findCursorWord(cursor, text)
        if not endText:
            currentWord = text[cursor:i]
            cursor = i + 1
            cursor, i, endText = findCursorWord(cursor, text)
            nextWord = text[cursor:i]
            if currentWord not in words:
                words[currentWord] = [nextWord]
            # print(currentWord)
    # pprint(words)


if __name__ == '__main__':
    # print(textCleaner('input_text.txt'))
    # markovChainWord()
    markovChainChar(7)