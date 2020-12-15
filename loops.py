
def test():
    entries = []
    while True:
        user_input = input('Enter something: ') 
        # capitalize user input 
        capitalized = user_input.capitalize()
        textToSave = None 
        # We declare this is None so we can reassign the variable textToSave

        # Check if user input is a question or not
        if user_input.startswith(('how' 'How', 'what', 'What', 'Where', 'where', 'when', 'When', 'Why', 'why')):
            textToSave = '{}?'.format(capitalized)
        else:
            textToSave = '{}.'.format(capitalized)

        if(user_input == 'end'):
            results = " ".join(entries)
            print(results)
            # length = len(entries)
            # for entry in entries:
            # print(entries[:length])
            break
        else:
            entries.append(textToSave)
            continue

test()


# while True:
#     username = input('Enter username:')
#     if username == 'pypy':
#         break
#     else:
#         continue
