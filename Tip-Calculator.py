#Tip Calculator
#Ask user for price of meal and percent tip
#Print tip amount and total bill

price=eval(input("Price of the meal: "))
tip=eval(input("Tip %: "))

tip_amount=tip/100*price
total_bill=price+tip_amount

print("Tip Amount: ", tip_amount)
print("Total Bill: ", total_bill)