import cmath

eq = input()
pa = cmath.phase(complex(eq))
r = abs(complex(eq))

print ("{}\n{}".format(r,pa))