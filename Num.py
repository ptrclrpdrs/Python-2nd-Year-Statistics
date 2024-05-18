num=eval(input("Enter a number: "))
smallest=num
largest=num
while num!=0:
    num=eval(input("Enter a number: "))
    if num>largest:
        largest=num
    if num<smallest and num!=0:
        smallest=num
    else:
        smallest=smallest

