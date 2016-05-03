fname = raw_input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhandle = open(fname)

mail = dict()

for lines in fhandle:
    line = lines.split()
    if line == [] or len(line) < 3 or line[0] != 'From' : continue
    mail[line[1]] = mail.get(line[1],0) + 1

for x in mail:
    print x, mail[x]
