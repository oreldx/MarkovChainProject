from pprint import pprint
import random


def findCursorWord(cursor, text):
    i = cursor
    while text[i] != ' ' and text[i] != '\n':
        i += 1
        print(cursor, i, text[cursor:i])
    return cursor, i


def markovChainWord(textSample):
    with open(textSample, encoding="utf-8") as file:
        words = {}
        while True:
            title = file.readline()
            if not title:
                break

            wordsTitle = title.split()

            for index, currentWord in enumerate(wordsTitle):
                if index != 0:
                    backWord = wordsTitle[index-1]
                    if backWord not in words:
                        words[backWord] = [currentWord]
                    else:
                        words[backWord].append(currentWord)
    pprint(words)

    # Text generation
    length = 100
    titleGenerated = random.choice(list(words))
    nextWord = titleGenerated
    while len(titleGenerated) < length:
        print(nextWord)
        if nextWord not in words:
            break
        nextWord = random.choice(words[nextWord])
        titleGenerated += ' ' + nextWord
    print(titleGenerated)


if __name__ == '__main__':
    markovChainWord('data/titlesCleaned.txt')
