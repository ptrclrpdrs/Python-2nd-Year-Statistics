from random import randint

score=0

for i in range(10):
    num1=randint(1,10)
    num2=randint(1,10)
    answer=num1*num2
    
    guess=eval(input(f"What is {num1} times {num2}? "))
    if guess==answer:
        print("Right!")
        score+=1
    else:
        print("Wrong. The answer is ", answer, ".", sep="")
        
print("Your score is", score, "out of 10.")