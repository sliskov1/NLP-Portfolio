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
    
    # count the number of correct predictions
    count = 0

    # list of languages to compare with LangId.sol
    langList = []

    # unigrams and bigrams being opened from pickle files
    englishUni = pickle.load(open('englishUni.p', 'rb'))  # read binary
    englishBi = pickle.load(open('englishBi.p', 'rb'))
    frenchUni = pickle.load(open('frenchUni.p', 'rb'))
    frenchBi = pickle.load(open('frenchBi.p', 'rb'))
    italianUni = pickle.load(open('italianUni.p', 'rb'))
    italianBi = pickle.load(open('italianBi.p', 'rb'))

    # total number of unigrams with each language 
    V = len(englishUni) + len(frenchUni) + len(italianUni)

    # opening test file
    test_text = 'ngram_files/ngram_files/LangId.test'
    f = open(test_text, "r", encoding='utf-8')
    text = f.read()

    # each sentence goes in a list called text_list
    text_list = text.splitlines()

    # computation of probabilities for each language
    for sentence in text_list:
        english = compute_prob(sentence, englishUni, englishBi, V)
        french = compute_prob(sentence, frenchUni, frenchBi, V)
        italian = compute_prob(sentence, italianUni, italianBi, V)

        # find the max probability for the most accurate language in that sentence
        prob_max = max(english, french, italian)

        if prob_max == english:
            langList.append("English")
        elif prob_max == french:
            langList.append("French")
        elif prob_max == italian:
            langList.append("Italian")

    # Use splitlines to have each element of the results in a list

    n = len(langList)
    predicted_list_str = '\n'.join([str(i) + ' ' + x for i, x in zip(range(1, n+1), langList)])
    predicted_list = predicted_list_str.splitlines()

    testsol_text = 'ngram_files/ngram_files/LangId.sol'
    linessol_list = open(testsol_text).read().splitlines()
    incorrectList = []

    print("Correctly Classified Items:")
    print()
    print("My Output : LangId Output")

    for line in linessol_list:
        force_break_loop = False
        for line2 in predicted_list:
            if line == line2:
               # count the number of times the predicted list has correct items 
               count+=1
               print(line, ":", line2)

               # if the item matches in the test file then turn boolean value true so when the item is never found the
               # line number of the item that is not found will go into the incorrect list 
               force_break_loop = True

               break
        if (force_break_loop):
            True
        # only output the incorrect line numbers into an incorrect list to be displayed
        else:
            incorrectList.append(line[:3])

    # calculate the accuracy of the percentage of correctly classified instances
    accuracy = ((count) / len(text_list)) * 100

    print("Line numbers of the incorrectly classified items: ", incorrectList)
    print("Accuracy: ", (int)(accuracy), "%")