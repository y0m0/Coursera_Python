text = raw_input('Enter a word: ')
letter = raw_input('Which letter do you want to count?')


def count(string, search):
    x = 0
    for i in string:
        if i == search:
            x = x + 1
    print x

    
count(text, letter)       


    
    
