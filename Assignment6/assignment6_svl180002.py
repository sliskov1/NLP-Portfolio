from bs4 import BeautifulSoup
from urllib.request import Request
import requests
from urllib import request
import re
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
import math

def webcrawler(starter_url):

    r = requests.get(starter_url)

    data = r.text
    soup = BeautifulSoup(data, features="html.parser")

    # write urls to a file
    with open('urls.txt', 'w') as f:
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            print(link_str)
            if 'Eddie' in link_str or 'eddie' in link_str:
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                    print('MOD:', link_str)
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str:
                    f.write(link_str + '\n')

def scrapeAndCleanText():
    with open('urls.txt', 'r') as f:
        urls = f.read().splitlines()
        for i, line in enumerate(urls):
            req = Request(line , headers={'User-Agent': 'XYZ/3.0'})
            html = request.urlopen(req).read().decode('utf8')
            soup = BeautifulSoup(html, features="html.parser")
            f = open("url_%i.txt" %i,'w')
            lol = soup.get_text()
            string_encode = lol.encode("ascii", "ignore")
            string_decode = string_encode.decode()
            text_chunks = [chunk for chunk in string_decode.splitlines() if not re.match(r'^\s*$', chunk)]
            for chunk in text_chunks:
                f.write(chunk)

def tokenizeSent():
    for i in range(17):
        with open("url_%i.txt" %i,'r')as f:
            line = f.read()
            text_list = sent_tokenize(line)
            f = open("url_%i_new.txt" %i,'w')
            for sent in text_list:
                f.write(sent)
    
def extractImportantTerms():
    num_docs = 4
    for i in range(17):
        with open("url_%i.txt" %i,'r')as f:
            line = f.read()
            vocab = set()  # set of words
            tf_dict = {}
            tokens = word_tokenize(line)
            tokens = [token.lower() for token in tokens]
            stopword = stopwords.words('english')
            tokens = [w for w in tokens if w.isalpha() and w not in stopword]
            for t in tokens:
                if t in tf_dict:
                    tf_dict[t] += 1
                else:
                    tf_dict[t] = 1
            token_set = set(tokens)
            tf_dict = {t:tokens.count(t) for t in token_set}
            for t in tf_dict.keys():
                tf_dict[t] = tf_dict[t] / len(tokens)

            vocab = set(tf_dict.keys())

            idf_dict = {}

            vocab_by_topic = [tf_dict.keys()]

            for term in vocab:
                temp = ['x' for voc in vocab_by_topic if term in voc]
                idf_dict[term] = math.log((1+num_docs) / (1+len(temp))) 

            tf_idf = create_tfidf(tf_dict, idf_dict)

            term_weights = sorted(tf_idf.items(), key=lambda x:x[1], reverse=True)
            print("\nurl_%i:" %i, term_weights[:30])


def create_tfidf(tf, idf):
    tf_idf = {}
    for t in tf.keys():
        tf_idf[t] = tf[t] * idf[t] 
        
    return tf_idf
    
def knowledgeBase():
    topTenList = ["eddie", "murphy", "film", "new", "york", "daughter", "saturday", "night", "live", "actor"]
    for i in range(17):
        with open("url_%i.txt" %i,'r')as f:
            line = f.read()
            text_list = sent_tokenize(line)
            for sent in text_list:
                for word in topTenList:
                    if word in sent:
                        dict = {word: sent}
                        print(dict)
                        break


                



            
if __name__ == '__main__':
    starter_url = 'https://www.google.com/search?q=eddie+murphy&sxsrf=ALiCzsaTlZaOIl99l0IRirYbVynhLZAX6A%3A1664994971029&ei=m849Y6ClAYO2qtsP7K-foAE&ved=0ahUKEwjg3rPO3cn6AhUDm2oFHezXBxQQ4dUDCA4&uact=5&oq=eddie+murphy&gs_lp=Egdnd3Mtd2l6uAED-AEBMgQQIxgnMggQABiABBixAzIIEC4YgAQYsQMyBRAAGIAEMgcQABixAxhDMgUQABiABDIHEAAYsQMYQzIIEC4YgAQYsQMyCBAuGIAEGLEDMgUQLhiABMICChAAGEcY1gQYsAOQBgJIrQdQmQJY1gNwAXgByAEAkAEAmAGBAaABxgGqAQMxLjHiAwQgQRgA4gMEIEYYAIgGAQ&sclient=gws-wiz'
    webcrawler(starter_url)
    scrapeAndCleanText()
    tokenizeSent()
    extractImportantTerms()
    knowledgeBase()