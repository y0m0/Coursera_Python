# Exercise 8.1

numbers = [1, 2, 3, 4, 5, 6]


def chop(x):
    x = x[1:len(x)-1]


def middle(y):
    return y[1:len(y)-1]


print chop(numbers)
print middle(numbers)
