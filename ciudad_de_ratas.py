#  determinar segun el crecimineto poblacional cuando a con un crecimineto poblacional del 7% sera menor que b con un crecimiento poblacional de 5%

print("-------------------------------------------")
print("---determinar el crecimiento poblacional---")
print("-------------------------------------------")

#input

A=3500000
B=5000000
n=1980

#processing

while A<=B:
    A=A+(A*0.07)
    B=B+(B*0.05)
    n=n+1

#output

print("el año es:"+str(n))

