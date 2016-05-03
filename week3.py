try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter Rate:")
    r = float(rate)
except:
    print "Wrong input"
    quit()
    
if h <= 40:
    pay = h * r
else :
    ext_h = h - 40
    ext_r = r * 1.5
    pay = 40 * r + ext_h * ext_r
print pay
    
    
