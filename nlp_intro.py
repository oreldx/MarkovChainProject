import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import re


def introNLP():
    """
    La suppression des stops words permet de retirer les mots qui n'apportent aucune valeur d'analyse globale au texte
    """
    frenchStopWords = set(stopwords.words('french'))
    filterStopFr = lambda text: [token for token in text if token.lower() not in frenchStopWords]
    # filterStopFr(word_tokenize(title, language='french'))

    with open('data/titlesCleaned.txt', encoding='utf-8') as file:
        titles = file.read()

        """
        La tokenisation est le processus de découper mot par mot ou phrase par phrase notre texte
        """
        # word_tokenize(title, language="french")
        titleTokenised = filterStopFr(word_tokenize(titles, language="french"))
        print(titleTokenised)

        frequenceDistribution = nltk.FreqDist(titleTokenised)
        print(frequenceDistribution.most_common())

        """
        La stemmatisation consiste à regrouper les mots de même racine synthaxique
        """
        stemmer = nltk.stem.SnowballStemmer('french')

        for w in titleTokenised:
            print(stemmer.stem(w))


if __name__ == '__main__':
    introNLP()
