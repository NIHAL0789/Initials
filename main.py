print("Welcome to the rollercoaster!\U0001F600")

height =  int(input("What is your height in cms?"))

if height >= 120:
  print("Congrats, you can ride the rollercoaster.")
  age = int(input("What is your age?"))
  if age <= 12:
    print("Hurrah, you can only pay £10 with a children discount\U0001F601.")
  elif age <= 18:
    print("Hey you can pay only £12 as you are an underage\U0001F642.")
  else:
    print("You have to pay £15 as an adult price.\nThank you\U0001F642")

else:
 print("Sorry, you cannot ride the rollercoaster as the height requirement is not satisfied\U0001F612")
