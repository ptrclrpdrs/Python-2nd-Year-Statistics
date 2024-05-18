while True:
    print("\nEnter two numbers and an operator to perform calculation (or any symbol to exit): ")
    num1=eval(input("\nEnter first number: "))
    num2=eval(input("Enter second number: "))
    op=input('Enter operator (+, -, *, **, /): ')
    if op=='+':
        print('\n', num1, "+", num2, "=", num1+num2)
    elif op=='-':
        print('\n', num1, "-", num2, "=", num1-num2)
    elif op=='*':
        print('\n', num1, "*", num2, "=", num1*num2)
    elif op=='**':
        print('\n', num1, "**", num2, "=", num1**num2)
    elif op=='/':
        print('\n', num1, "/", num2, "=", num1/num2)
    elif op!='+,-,*,**,/':
        print('\n\nThank you for using the calculator. \n\nExiting calculator...')
        break