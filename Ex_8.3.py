#Exercise 8.3

fhand = open('mbox-short.txt')
count = 0

for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        print words[2]

