count = 0
total = 0
avg = None
while True:

    try:
        inp = raw_input('Enter a number: ')
        if inp == 'done': break
        if len(inp) < 1 : break
        num = float(inp)
        count = count + 1
        total = total + num
        avg = total / count 
    except:
        print 'Invalid input'
        continue

	
print 'Count = ',count
print 'Total = ',total
print 'Average = ',avg
