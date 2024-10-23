# CI=P*(1+R/100).N    P=PRINCIPAL AMOUNT  N=TIME PERIOD    R=RATE OF INTREST
import math
p=float(input("please enter the principal amount:"))
r=float(input("please enter the rate of intrest:"))
n=float(input("please enter the time period:"))
total=p*((1+r/100)**n)
print("total is:",total)
intrest=total-p
print(intrest)