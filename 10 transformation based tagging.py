import re
transformation_rules = [
    (r'\b[Aa]pple\b', 'NNP'),            
    (r'\bthe\b', 'DT'),                  
    (r'\b([0-9]+(\.[0-9]+)?)\b', 'CD'),  
    (r'\b([A-Z][a-z]*)\b', 'NNP'),        
    (r'\b\w+\b', 'NN')                    
]
def transform_tag(sentence, rules):
    tagged_sentence = []
    for word in sentence.split():
        for pattern, tag in rules:
            if re.match(pattern, word):
                tagged_sentence.append((word, tag))
                break
        else:
            tagged_sentence.append((word, 'NN')) 
    return tagged_sentence
sentence = "The Apple is $100."
tagged_sentence = transform_tag(sentence, transformation_rules)
print(tagged_sentence)
