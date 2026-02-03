#Check whether the quadratic equation has real roots or imaginary roots. Display the roots.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b*b - 4*a*c

if d > 0:

    r1 = (-b + d**0.5) / (2*a)

    r2 = (-b - d**0.5) / (2*a)

    print("Roots are real")

    print("Root 1 =", r1)

    print("Root 2 =", r2)

elif d == 0:

    r = -b / (2*a)

    print("Roots are real and equal")

    print("Root =", r)

else:

    real = -b / (2*a)

    imag = (-d)**0.5 / (2*a)

    print("Roots are imaginary")

    print("Root 1 =", real, "+", imag, "i")

    print("Root 2 =", real, "-", imag, "i")
