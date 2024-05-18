y=eval(input("Enter the exponential power: "))

p=2**y
p2=p%100

print("\n2 raised to the power of ", y, " is ", p, ".", sep="")
print("The last two digits of ", p, " are ", p2, ".", sep="")