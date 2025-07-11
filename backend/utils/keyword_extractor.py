import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(prompt):
    doc = nlp(prompt)
    keywords = set()
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop:
            keywords.add(token.lemma_.lower())
    return list(keywords)
