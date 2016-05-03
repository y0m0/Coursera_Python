smallest = None
largest = None

while True:

    input = raw_input('Enter a number: ')
    
    # Special Cases
    if input == 'done' : break
    if len(input) < 1 : break
    
    # Conversion to integer number
    try:
        number = int(input)
    except:
        print 'Invalid input'
        continue
    
    # Find Smallest and Largest
    if smallest is None or smallest > number : smallest = number
    if largest is None or largest < number : largest = number

print 'Maximum is',largest
print 'Minimum is',smallest