print("Welcome to my computer quiz")

play = input("Do you want to play? ")
if play !="yes":
    quit()

print("okay let's play")
score = 0


answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score+=1

else:
    print("incorrect!")    



answer = input("What does GPU stands for? ")
if answer.lower() == "graphical processing unit":
    print('correct!')
    score+=1
    
else:
    print("incorrect!")   



answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score+=1
    
else:
    print("incorrect!")   




answer = input("What does www stands for? ")
if answer.lower() == "world wide web":
    print('correct!')
    score+=1


else:
    print("incorrect!")   

print("you got " + str(score) + " questions correct!")  

print("you got " + str((score/4)*100) + "%")   




