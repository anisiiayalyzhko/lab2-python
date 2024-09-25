def expression (m, n):
    z=(((m**0.5) - (n**0.5)) / m)
    return z

from pn import perfect_number

m = int(input("Enter m: "))
n = int(input("Enter n: "))
print ("Equalization z = ", expression(m, n) )

if perfect_number(n):
    print(f"{n} is perfect number.")
else:
    print(f"{n} is not perfect number.")
