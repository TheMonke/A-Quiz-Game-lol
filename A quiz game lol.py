# This is a Quiz Game...
score = 0

user = input("Do you want to play this Quiz Game I made? ")
if user == ("Yes"):
    print("Ok, lets play!")

elif user == ("No"):
    quit()

question = input("Can Visual Studio Code be classifed as an IDE? ")
if question == ("Yes"):
    print("Correct!")
    score += 1

elif question == ("What's an IDE?"):
    print("LEAVE THIS PROGRAM RIGHT NOW!!")
else:
    print("Incorrect idiot!")


question = input("Is PyCharm a good IDE for Python? ")
if question == ("Yes"):
    print("Incorrect idiot!")


question = input("What is an IDE? ")
if question == ("Integrated Development Environment"):
    print("Correct!")
    score += 1
else:
    print("Incorrect idiot!")


question = input("What was the first programming language ever made? ")
if question == ("FORTRAN"):
    print("Correct!")
    score += 1
else:
    print("Incorrect idiot!")


question = input("Should everyone learn to code? ")
if question == ("No"):
    print("Correct!")
    score += 1
else:
    print("Incorrect idiot!")


question = input("What is the best programming language for beginners?? ")
if question == ("Python"):
    print("Correct!")
    score += 1
else:
    print("Incorrect idiot!")


question = input("What is the best programming language for making games? ")
if question == ("C#"):
    print("Correct!")
    score += 1
else:
    print("Incorrect idiot!")


question = input("What is the best Game Engine? ")
if question == ("Unity"):
    print("Correct!")
    score += 1
else:
    print("Incorrect idiot!")


question = input("What is a string? ")
if question == ("Sequence of characters"):
    print("Correct!")
    score += 1
else:
    print("Incorrect idiot!")


question = input("What is a comment? ")
if question == ("Ignored lines of code"):
    print("Correct!")
    score += 1
else:
    print("Incorrect idiot!")

question = input("What is the terminal? ")
if question == ("command lines or console"):
    print("Correct!")
    score += 1
else:
    print("Incorrect idiot!")


print("You have finished the Quiz, lets get your score")

print("Your final score was " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%")
if score == 0:
    print("Congratulations, you're a complete idiot!")