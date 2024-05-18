grade=eval(input("Enter Grade: "))

if grade>=90 and grade<=100:
    print("A - Outstanding")    
elif grade<=89 and grade>=80:
    print("B - Good")
elif grade<=79 and grade>=70:
    print("C - Fair")
elif grade<=69 and grade>=60:
    print("D - Poor")
elif grade<=59:
    print("E - Failed")
elif grade>100:
    print("Invalid")              