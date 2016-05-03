# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox-short.txt'
try:
    fh = open(fname)
except:
    print 'Impossible to open the file:', fname

text = "X-DSPAM-Confidence:"
totspam = 0
count = 0

for line in fh:
    if not line.startswith(text): continue
    start = line.find(':') + 1
    spam = float(line[start:])
    totspam += spam
    count += 1

print 'Average spam confidence:', totspam/count