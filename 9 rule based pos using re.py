import re

def rule_based_pos_tagging(sentence):
    tagged_sentence = []
    for word in sentence.split():
        
        if re.match(r'\b(?:is|am|are|was|were)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'VERB'))
        elif re.match(r'\b(?:a|an|the)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'DET'))
        elif re.match(r'\b(?:I|you|he|she|it|we|they)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'PRON'))
        elif re.match(r'\b(?:dog|cat|bird)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'NOUN'))
        elif re.match(r'\b(?:runs|jumps|eats)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'VERB'))
        elif re.match(r'\b(?:quick|lazy|brown|black)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'ADJ'))
        elif re.match(r'\b(?:in|on|at|under|over)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'ADP'))
        elif re.match(r'\b(?:and|but|or)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'CONJ'))
        else:
            tagged_sentence.append((word, 'UNK'))  
    
    return tagged_sentence


sentence = "The quick brown fox jumps over the lazy dog"
tagged_sentence = rule_based_pos_tagging(sentence)
print(tagged_sentence)
