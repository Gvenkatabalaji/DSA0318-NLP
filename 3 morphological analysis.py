import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
text = "The cats are chasing mice and playing in the garden."
words = word_tokenize(text)
lemmatizer = WordNetLemmatizer()
lemmas = []
for word in words:
    lemma = lemmatizer.lemmatize(word)
    lemmas.append(lemma)

print("Original words:", words)
print("Lemmatized words:", lemmas)
