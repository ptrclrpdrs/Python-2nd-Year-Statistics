x=eval(input("Enter the exponential power: "))

p=2**x
p2=p%10

print("\n2 raised to the power of ", x, " is ", p, ".", sep="")
print("The last digit of ", p, " is ", p2, ".", sep="")