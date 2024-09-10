import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')

stemmer = PorterStemmer()

words = ['running', 'runs', 'ran', 'runner', 'easily', 'fairly']

stemmed_words = [stemmer.stem(word) for word in words]

for i in range(len(words)):
    print(f"Original: {words[i]}, Stemmed: {stemmed_words[i]}")
