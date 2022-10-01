import sys  # to get the system parameter
import os   
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.util import ngrams
import pickle

def compute_prob(text, unigram_dict, bigram_dict, V):
    # N is the number of tokens in the training data
    # V is the vocabulary size in the training data (unique tokens)

    unigrams_test = word_tokenize(text)
    bigrams_test = list(ngrams(unigrams_test, 2))
    
    p_laplace = 1  # calculate p using Laplace smoothing

    for bigram in bigrams_test:
        b = bigram_dict[bigram] if bigram in bigram_dict else 0
        u = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        p_laplace = p_laplace * ((b + 1) / (u + V)) 
    return p_laplace

if __name__ == '__main__':
    sentenceList = []
    englishUni = pickle.load(open('englishUni.p', 'rb'))  # read binary
    englishBi = pickle.load(open('englishBi.p', 'rb'))
    frenchUni = pickle.load(open('frenchUni.p', 'rb'))
    frenchBi = pickle.load(open('frenchBi.p', 'rb'))
    italianUni = pickle.load(open('italianUni.p', 'rb'))
    italianBi = pickle.load(open('italianBi.p', 'rb'))
    V = len(englishUni) + len(frenchUni) + len(italianUni)
    test_text = 'ngram_files/ngram_files/LangId.test'
    f = open(test_text, "r", encoding='utf-8')
    text = f.read() 

    sentences = sent_tokenize(text)

    for i in sentences:
       sentenceList.append(i)

    englishCount = 0
    frenchCount = 0
    italianCount = 0
    lineNum = 0

    for sentence in sentenceList:
        english = compute_prob(sentence, englishUni, englishBi, V)
        french = compute_prob(sentence, frenchUni, frenchBi, V)
        italian = compute_prob(sentence, italianUni, italianBi, V)
        lineNum += 1
        if italian > english > french or italian > french > english:
            italianCount+=1
            print(lineNum, "Italian")
        elif english > italian > french or english > french > italian:
            englishCount+=1
            print(lineNum, "English")
        elif french > italian > english or french > english > italian:
            frenchCount+=1
            print(lineNum, "French")
    accuracy = ((italianCount + englishCount + frenchCount) / len(sentences)) * 100
    print(accuracy)
    
        

        











    
 
    
  
    
    
