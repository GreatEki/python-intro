import json
from difflib import get_close_matches

data = json.load(open('files/data.json'))

def translate(word):
    word = word.lower()
    if word in data:
       return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input('Did you mean %s if yes enter Y, or N for No: ' % get_close_matches(word, data.keys())[0])
        yn = yn.upper()
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return 'The word doesn= not exist. Please double check it'
        else: 
            return "Sorry we didn't understand your entry"

    else:
        return 'The word does not exist. Please double check the word'

        

theWord = input('Enter a word: ')

# print(translate(theWord))
output = translate(theWord)

if isinstance(output, list):
    for definition in output:
        print(definition)
elif isinstance(output, str):
    print(output)
else:
    print(output)