import sys  # to get the system parameter
import os   
from nltk import word_tokenize
from nltk.util import ngrams
import pickle

def generateModel(fp):
    with open(os.path.join(os.getcwd(), fp), 'r+', encoding='utf-8') as f: 

            # read the file
            raw_text = f.read()

            text = raw_text.replace('\n', '')

            tokens = word_tokenize(text)

            unigrams = [t.lower() for t in tokens]

            bigrams = list(ngrams(tokens, 2))

            unigram_dict = {t:unigrams.count(t) for t in set(unigrams)}

            bigram_dict = {b:bigrams.count(b) for b in set(bigrams)}

            return unigram_dict, bigram_dict



if __name__ == '__main__':
    fnEnglish = 'ngram_files/ngram_files/LangId.train.English'
    fnFrench = 'ngram_files/ngram_files/LangId.train.French'
    fnItalian = 'ngram_files/ngram_files/LangId.train.Italian'
    englishUni, englishBi = generateModel(fnEnglish)
    frenchUni, frenchBi = generateModel(fnFrench)
    italianUni, italianBi = generateModel(fnItalian)
    pickle.dump(englishUni, open('englishUni.p', 'wb'))  # write binary
    pickle.dump(englishBi, open('englishBi.p', 'wb'))  # write binary
    pickle.dump(frenchUni, open('frenchUni.p', 'wb'))  # write binary
    pickle.dump(frenchBi, open('frenchBi.p', 'wb'))  # write binary
    pickle.dump(italianUni, open('italianUni.p', 'wb'))  # write binary
    pickle.dump(italianBi, open('italianBi.p', 'wb'))  # write binary
