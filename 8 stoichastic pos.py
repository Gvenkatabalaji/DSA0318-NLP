import random
training_data = [
    ("The", "DT"),
    ("dog", "NN"),
    ("runs", "VBZ"),
    ("in", "IN"),
    ("the", "DT"),
    ("park", "NN")
]
def create_probabilistic_model(training_data):
    word_tag_counts = {}
    tag_transitions = {}
    prev_tag = None    
    for word, tag in training_data:
        word_tag_counts[(word, tag)] = word_tag_counts.get((word, tag), 0) + 1
        
        if prev_tag is not None:
            tag_transitions[(prev_tag, tag)] = tag_transitions.get((prev_tag, tag), 0) + 1
        
        prev_tag = tag
    
    word_tag_probs = {pair: count / sum(word_tag_counts.values()) for pair, count in word_tag_counts.items()}
    tag_transition_probs = {pair: count / sum(tag_transitions.values()) for pair, count in tag_transitions.items()}    
    return word_tag_probs, tag_transition_probs
def stochastic_pos_tagging(sentence, word_tag_probs, tag_transition_probs):
    tagged_sentence = []
    prev_tag = None
    
    for word in sentence.split():
        possible_tags = [tag for (w, tag), _ in word_tag_probs.items() if w == word]
        if not possible_tags:
            tagged_sentence.append((word, 'NN'))
            continue
        
        if prev_tag is None:
            tag = random.choices(possible_tags, weights=[word_tag_probs[(word, tag)] for tag in possible_tags])[0]
        else:
            possible_transitions = [(prev_tag, tag) for tag in possible_tags]
            tag = random.choices(possible_tags, weights=[tag_transition_probs[(prev_tag, tag)] for tag in possible_tags])[0]
        
        tagged_sentence.append((word, tag))
        prev_tag = tag
    
    return tagged_sentence


word_tag_probs, tag_transition_probs = create_probabilistic_model(training_data)


sentence = "The dog runs in the park"
tagged_sentence = stochastic_pos_tagging(sentence, word_tag_probs, tag_transition_probs)
print(tagged_sentence)
