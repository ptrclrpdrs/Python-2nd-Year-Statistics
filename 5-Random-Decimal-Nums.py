#Program that generates 5 random decimal numbers between 1-100 w/ 2 decimal places accuracy.
#Compute average.

from random import uniform

a=uniform(1,100)
b=uniform(1,100)
c=uniform(1,100)
d=uniform(1,100)
e=uniform(1,100)

a=round(a,2)
b=round(b,2)
c=round(c,2)
d=round(d,2)
e=round(e,2)

ave=(a+b+c+d+e)/5
ave=round(ave,2)

print(a,b,c,d,e, sep="\n")
print("\nAverage:", ave)
