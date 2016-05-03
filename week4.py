def computepay(hrs, rate):
    if hrs <= 40:
        pay = hrs * rate
        return pay
    else:
        pay = (40 * rate) + ((hrs - 40) * rate * 1.5)
        return pay
try:
    hrs = float(raw_input("Enter Hours:"))
    rate = float(raw_input("Enter Rate:"))
except:
    print "wrong input"
    quit()
    
pay = computepay(hrs, rate)
print pay
