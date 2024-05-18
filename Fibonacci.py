#ask user how many fibonacci number and print
#1,1,2,3,5,8,13,21,34,55,89,....

fib=eval(input("Type the number of Fibonacci numbers to display: "))

n1, n2=0, 1
count=0

if fib <=0:
    print("Please enter positive integers.")
elif fib==1:
    print("Fibonacci sequence up to", fib, ":")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count <fib:
        print(n1)
        n=n1 + n2
        n1=n2
        n2=n
        count +=1