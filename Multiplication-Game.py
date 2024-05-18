from random import randint

score=0

for i in range(10):
    num1=randint(1,10)
    num2=randint(1,10)
    answer=num1*num2
    
    question=eval(input("Question {}: {} x {} = ".format(i+1,num1,num2)))
    if question==answer:
        print("Right!")
        score=score+1
    else:
        print("Wrong. The answer is ", answer, ".", sep="")
        
print("Your score is {}/{}".format(score,10))
    
    