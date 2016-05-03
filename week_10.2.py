# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day
# for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below. Note that the auto-grader does not have support for the sorted() function.

fname = raw_input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhandle = open(fname)
HourDB = dict()

for lines in fhandle:
    line = lines.split()
    if line == [] or len(line) < 3 or line[0] != 'From' : continue
    position = lines.find(':')
    hour = lines[position - 2: position]
    HourDB[hour] = HourDB.get(hour, 0) + 1

Result = HourDB.items()
Result.sort()
for x, y in Result:
    print x, y