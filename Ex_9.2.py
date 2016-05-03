fname = raw_input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhandle = open(fname)

days_if = dict()
days_get = dict()

#for lines in fhandle:
#    line = lines.split()
#    if line == [] or len(line) < 3 or line[0] != 'From' : continue
#    if line[2] not in days_if:
#        days_if[line[2]] = 1
#    else:
#        days_if[line[2]] += 1

for lines in fhandle:
    line = lines.split()
    if line == [] or len(line) < 3 or line[0] != 'From' : continue
    days_get[line[2]] = days_get.get(line[2],0) + 1

#print days_if
print days_get



