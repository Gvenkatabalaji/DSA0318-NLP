import spacy
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Type: {ent.label_}")
example_text = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California."
perform_ner(example_text)
