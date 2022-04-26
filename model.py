# !python3 -m spacy download xx_ent_wiki_sm

from spacy.lang.xx import MultiLanguage
nlp = MultiLanguage()

def ent_pos(text):
  nlp = spacy.load('xx_ent_wiki_sm')
  doc = nlp(str(text))
  if doc.ents:    
    lang_list = []
    for ent in doc.ents:
        lang_list.append([ent.text, ent.label_, ent.start_char, ent.end_char])
    return lang_list
  else: 
    print('No named entities found.')

# examples for english sentence
print(ent_pos("Apple is looking at buying U.K. startup for $1 billion"))

# examples for hindi sentence
print(ent_pos("फ्रांस के राष्ट्रपति कौन हैं?"))
