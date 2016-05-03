fname = raw_input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhandle = open(fname)
mail = dict()
big = None
address = None

for lines in fhandle:
    line = lines.split()
    if line == [] or len(line) < 3 or line[0] != 'From' : continue
    mail[line[1]] = mail.get(line[1],0) + 1
    if big is None or big < mail[line[1]] :
        big = mail[line[1]]

print address