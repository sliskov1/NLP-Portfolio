import sys  # to get the system parameter
import os   # used by method 1 
from nltk import word_tokenize
from nltk import pos_tag
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import re
from random import randint

def preprocess(raw_text):
    """
        Preprocess raw tex.
        Arguments: a raw text string
        Output:
            text - raw_text with punctuation and numbers removed, lower cased
            tokens - tokens
            stemmed - stemmed words
            lemmas - lemmas
            content - tokens with stop words removed
    """

    # remove punctuation and numbers with a regular expression
    text = re.sub(r'[.?!,:;()\-\n\d]',' ', raw_text.lower())

    # tokenizing extracts words, not white space
    tokens = word_tokenize(text)

    #lowercase the text
    tokensLower = [t.lower() for t in tokens]

    #making unique tokens
    uniqueTokens = set(tokensLower)

    # Lexical diversity
    print("\nLexical diversity: %.2f" % (len(uniqueTokens) / len(tokens)))

    # get rid of punctuation and stopwords
    content = [t for t in tokensLower if t.isalpha() and
    t not in stopwords.words('english') and len(t) > 6]

    # lemmatization finds the root words
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in content]

    # make unique lemmas
    lemmas_unique = list(set(lemmas)) 

    # Use pos_tags on the unique lemmas & print out the first twenty
    tags = pos_tag(lemmas_unique)
    print(tags[:20])

    # Retrieves all the nouns
    nouns = [token for token, pos in tags if pos.startswith('N')]

    fdist = FreqDist(tokensLower)
    fdist2 = FreqDist(nouns)

    print("Number of tokens: ")
    print(fdist.N())
    print("Number of nouns: ")
    print(fdist2.N())

    return tokensLower, nouns

# Guessing game function
def runGame(words):
    score = 5
    guesses = ''
    word = words[randint(1, 50)] #randomly picks a word out of the 50 words in the list 
    print("Let's play a word guessing game!")

    # score starts off at 5 and will go down to zero if the player keeps incorrectly guessing the letter
    while score > 0:   

        failed = 0 

        # checks every letter in the word and checks if the letter that is inputted is in the guesses list 
        # when the game first starts the guesses will be empty
        for char in word:
            if char in guesses:
                print(char)
                score += 1
            else:
                print("_")
                failed += 1

        guess = input("Guess a character: ")

        # if the user inputs this symbol "!", then the program is terminated
        if guess == "!":
            break

        # the user input is stored in guesses list
        guesses += guess

        if failed == 0:
            print("You win!")
            break

        if guess not in word:

            # if the score is zero the game is done and program terminates
            if score == 0:
                print("You lose...")

            
            score = score - 1

            print("Sorry, guess again")
            print("Score is " + str(score))
        else:
            print("Right")
            print("Score is " + str(score))
        

                

    

    
        




if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
    else:
        fp = sys.argv[1]
        with open(os.path.join(os.getcwd(), fp), 'r+') as f: 

            # read the file
            raw_text = f.read()

            # call the preprocess function
            tokens, nouns = preprocess(raw_text)

            # intialize the word list for guessing game
            words = [] 

            # dictionary, key = noun & value = count for amount of nouns in tokens 
            counts = {t:tokens.count(t) for t in nouns}

            # sort the values in descending order
            sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

            # Save the first 50 words into the list named words and then print out those words
            for i in range(50):
                words.append(sorted_counts[i][0])
       
            runGame(words)
                
                
            

