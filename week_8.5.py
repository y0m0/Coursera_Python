fname = raw_input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhandle = open(fname)
count = 0

for line in fhandle:
    words = line.split()
    if len(words) == 0 or words[0] != 'From' : continue
    print words[1]
    count += 1

print "There were", count, "lines in the file with From as the first word"
