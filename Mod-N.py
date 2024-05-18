z=eval(input("Enter the exponential power: "))
n=eval(input("Number of digits to find: "))

p=2**z
p2=p%(10**n)

print("\n2 raised to the power of ", z, " is ", p, ".", sep="")
print("The last ", n, " digits of ", p, " are ", p2, ".", sep="")