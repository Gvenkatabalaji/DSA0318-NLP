import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
def pos_tagging(text):    
    words = word_tokenize(text)
    tagged_words = nltk.pos_tag(words)
    return tagged_words
text = "This is a sample sentence for part-of-speech tagging using NLTK."
tagged_text = pos_tagging(text)
print(tagged_text)
