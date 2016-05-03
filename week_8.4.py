#open file
fname = raw_input("Enter file name: ")
#auto open correct file on blank input
if fname == '':
    fname = 'romeo.txt'

fh = open(fname)
lst = list()


for line in fh:
    strings = line.split()
    print strings
    #check if word is already present inside the list and if not add it to it
    for words in strings:
        if lst is [] or words not in lst:
            lst.append(words)

lst.sort()
print lst
