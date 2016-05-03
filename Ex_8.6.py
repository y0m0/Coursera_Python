memory = list()


while True:
    number = raw_input('Enter a number:')
    if number == 'done' or number == '' : break
    memory.append(float(number))


print min(memory)
print max(memory)