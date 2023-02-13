print("Welcome to the computer quiz!")

play = input("Do you want to play? " )

if play != ("yes"):
  quit()

print("Ok, lets play\U0001F600")
score = 0

answer = input("1.What is the colour of sky? ")
if answer.lower() == "blue":
    print("Your answer is correct!")
    score += 1
else:
    print("Your answer isn't correct.")

answer = input("2.What country has the highest life expectancy? ")
if answer.lower() == "hongkong":
    print("Your answer is correct!")
    score += 1
else:
    print("Your answer isn't correct.")  


answer = input("3.What year was the United Nations established? ")
if answer.lower() == "1945":
    print("Your answer is correct!")
    score += 1
else:
    print("Your answer isn't correct.")
  

  
answer = input("4.When did India got it's Independence? ")
if answer.lower() == "1947":
    print("Your answer is correct!")
    score += 1
else:
    print("Your answer isn't correct.")


answer = input("5.What artist has the most streams on Spotify? ")
if answer.lower() == "drake":
    print("Your answer is correct!")
    score += 1
else:
    print("Your answer isn't correct.")


answer = input("6.What company was originally called 'Cadabra'? ")
if answer.lower() == "amazon":
    print("Your answer is correct!")
    score += 1
else:
    print("Your answer isn't correct.")


answer = input("7.What sports car company manufactures the 911? ")
if answer.lower() == "porsche":
    print("Your answer is correct!")
    score += 1
else:
    print("Your answer isn't correct.")


answer = input("8.What city is known as 'The Eternal City'? ")
if answer.lower() == "rome":
    print("Your answer is correct!")
    score += 1
else:
    print("Your answer isn't correct.")


answer = input("9.How many bones do we have in an ear? ")
if answer.lower() == "3":
    print("Your answer is correct!")
    score += 1
else:
    print("Your answer isn't correct.")


answer1 = input("10.Which company was initially known as 'Blue Ribbon Sports'? ")
if answer.lower() == "nike":
    print("Your answer is correct!")
    score += 1
else:
    print("Your answer isn't correct.")


print("You got "  +str(score)+  " right answers")
print("Your total score is "  +str((score/10) * 100)+  "%.")
