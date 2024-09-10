transitions = {
    'singular': {'s': 'plural', 'x': 'plural', 'y': 'plural'},
    'plural': {}
}
def generate_plural(noun):
    state = 'singular'
    plural_noun = noun    
    if noun.endswith('s') or noun.endswith('x') or noun.endswith('y'):
        state = 'plural'   
    if state == 'plural':
        plural_noun += 'es'
    else:
        plural_noun += 's' 
    return plural_noun
nouns = ['cat', 'dog', 'box', 'app', 'apple']
for noun in nouns:
    plural_form = generate_plural(noun)
    print(f"The plural form of '{noun}' is '{plural_form}'")
