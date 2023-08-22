# Named Entity Recognition using SpaCy

This repository contains code for performing Named Entity Recognition (NER) using SpaCy's `MultiLanguage` module. The `ent_pos` function in the code utilizes the `spacy.lang.xx` library to perform NER on input text. The code is written in Python and supports multiple languages for entity recognition.

## Getting Started

### Prerequisites

- Python 3.x
- SpaCy library (`spacy`) (https://spacy.io/models/xx)

You can install the required dependencies using the following command:

```bash
pip install spacy
```

## Installation
Clone this repository to your local machine using:
```bash
git clone https://github.com/your-username/your-repo.git
```

Navigate to the repository directory:
```bash
cd your-repo
```

## Usage
Import the required modules:
```python
from spacy.lang.xx import MultiLanguage
import spacy
```
Create an instance of MultiLanguage:
```python
nlp = MultiLanguage()
```

Define the ent_pos function for performing Named Entity Recognition:
```python
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
```

Examples for English and Hindi sentences:
```python
# Example for an English sentence
english_text = "Apple is looking at buying U.K. startup for $1 billion"
print(ent_pos(english_text))

# Example for a Hindi sentence
hindi_text = "फ्रांस के राष्ट्रपति कौन हैं?"
print(ent_pos(hindi_text))
```

## Contributing
If you'd like to contribute to this project, feel free to open an issue or submit a pull request. We welcome any improvements or additional features!

Hit a Like:thumbsup:
