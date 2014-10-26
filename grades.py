grade = raw_input("input grade between 0.0 and 1.0: ")
g = float(grade)
if g > 1.0:
    print "input grade between 0.0 and 1.0"
elif g >= .9:
    print "A"
elif g >= .8:
    print "B"
elif g >= .7:
    print "C"
elif g >= .6:
    print "D"
else:
    print "F"
