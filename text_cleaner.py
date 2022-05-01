import re


def textCleaning(pathInput, pathOutput):
    with open(pathInput, encoding="utf-8") as fileIn:
        with open(pathOutput, 'a', encoding='utf-8') as fileOut:
            while True:
                title = fileIn.readline()
                if not title:
                    break

                title = title.lower()
                title = re.sub(r'\|(\s+)', ',', title)
                title = re.sub(r'#(\w+)|\(([^)]+)\)', '', title)
                title = re.sub(r'(best|of|twitch|fr)[^.]*(best|of|twitch|fr)', ' ', title)
                print(title)

                fileOut.write(title)


if __name__ == '__main__':
    textCleaning('data/titles.txt', 'data/titlesCleaned.txt')
