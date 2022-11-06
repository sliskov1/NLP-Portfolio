from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

def knowledgeBase():
    list = ["mario", "nintendo"]
    with open("text1.txt",'r') as f:
        line = f.read().lower().splitlines()
        for sent in line:
            for word in list:
                if word in sent:
                    dict = {word : sent}
                    list.pop(0)
                    print(dict)
                    break
                

if __name__ == '__main__':
    knowledgeBase()