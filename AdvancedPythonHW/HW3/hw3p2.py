count = 0
dictionary_words = dict()   
            
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        dictionary_words[word] = 1

word = input('Enter a word: ')
if word in dictionary_words:
    print(word, 'was found')
else:
    print(word, 'was not found')
