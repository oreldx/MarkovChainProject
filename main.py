import random


def modelGenerator(order):
    with open('input_text.txt') as f:
        text = f.read()
    ngram = {}

    for i in range(len(text)-order):

        currentNgram = text[i:i+order]
        if not currentNgram in ngram:
            ngram[currentNgram] = [text[i+order]]
        else:
            ngram[currentNgram].append(text[i+order])
    return ngram


def textGenerator(order, ngrams):
    length = 100
    text = random.choice(list(ngrams))
    for i in range(length):
        if text[i:i+order] not in ngrams:
            break
        nextChar = random.choice(ngrams[text[i:i+order]])
        text += nextChar
    print(text)


def markovChainText():
    order = 6
    model = modelGenerator(order)
    textGenerator(order, model)


if __name__ == '__main__':
    markovChainText()
