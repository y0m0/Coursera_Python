fname = raw_input("Enter file name: ")
if len(fname) < 1:
    fname = "words.txt"

fhandle = open(fname)
word = dict()


for line in fhandle:
    words = line.split()
    for x in words:
        if x not in word:
            word[x] = 1

while True:
    search = raw_input('Search a word:')
    if search == 'done' or search == "" : break
    if search in word:
        print 'Found It!'
    else:
        print 'Try Again..'




