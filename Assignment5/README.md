N-grams are a set of co-occuring words much like a continuous sequence of words, symbols, or tokens within a given corpus. To estimate the probability of the last word of an n-gram given the previous words, the language model determines whether or not the next word goes with what we think will go next considering only the previous words, an n-gram model assigns a probability score to each option.
The n-grams are widely used in many fields such as commuinication thoery, computational linguistics, computational biology, and data compression. Fun applications include, spelling error detection and correction, query expansion, information retrieval with serial, inverted and signature files, dictionary look‐up, text compression, and language identification. 
The way probabilities are calculated with unigrams and bigrams is the process finding the likelihood estimate of a sequence of words. The best technique is laplace smoothing which is to add one to all the counts in the bigram or unigram which results to better accuracy.   
It's important to find a corpus that makes sense for the application and is in the right language. If the text that is being tested on isn't in the right language, then the percentage of the probability will probably be zero. 
In training to generate text in the language model we first prepare the train data from the corpus. Then, the language model learns the conditional probability distribution of the next token for a sequence (prompt) generated from the corpus. The LM calculates the conditional probability of each vocabulary token to be the next token. We sample the next token using this conditional probability distribution. We concatenate this token to the seed and provide this sequence as the new seed to LM. 
Traditionally, language model performance is measured by perplexity, cross entropy, and bits-per-character (BPC). As language models are increasingly being used as pre-trained models for other NLP tasks, they are often also evaluated based on how well they perform on downstream tasks.
Google N-Gram viewer is new and cool way of seeing if sequence of words have a better probability than other sequence of words. 

![alt text](Assignment5\google_n-gram.png)

References:

Karakaya, Murat. “Fundamentals of Text Generation.” Medium, Deep Learning Tutorials with Keras, 29 May 2021, https://medium.com/deep-learning-with-keras/fundamentals-of-text-generation-745d66238a1f.

Huyen, Chip. “Evaluation Metrics for Language Modeling.” The Gradient, The Gradient, 5 Dec. 2021, https://thegradient.pub/understanding-evaluation-metrics-for-language-models/#:~:text=Traditionally,%20language%20model%20performance%20is,they%20perform%20on%20downstream%20tasks. 