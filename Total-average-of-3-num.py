#Write a program that asks user to enter 3 numbers.
#Create variables total and average.
#Print values of total and average.

n1=eval(input("Enter the first number: "))
n2=eval(input("Enter the second number: "))
n3=eval(input("Enter the third number: "))

total=n1+n2+n3
average=total/3

print("\nThe total of the three numbers entered is", total)
print("\nThe average of the three numbers entered is", average)