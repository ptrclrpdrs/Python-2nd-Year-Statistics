print("***Fin Restaurant***")
print("\n---MENU")
print("--Code/--Description/--Price")

A=input("\n   A     Spaghetti    P 90")
B=input("   B       Burger     P 80")
C=input("   C       Hotdog     P 70")


order_num=eval(input("\n\nHow many orders do you want to purchase? "))

for i in range(order_num):
    code=eval(input("\nType the Code of your choice: "))
    quantity=eval(input("\nType the quantity of your order: "))
    
p1=90*quantity
p2=80*quantity
p3=70*quantity

if code==A:
    print(quantity, "Spaghetti", p1)
    




    