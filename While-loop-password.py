tries=5
while True:
  password=input("Enter password: ")
  if password=="wonderland":
        print("You have successfully logged in the system.")
        break
  elif password!="wonderland":
        print("Wrong. Please try again.")
        password=input("Enter password: ")
        
