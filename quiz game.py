from itertools import count


print ("Welcome to a random quiz!!!")

playing = input ("Do you wanna play ? ")

if playing.lower() != "yes" :
    quit()

print("Lets play :) ")
score = 0
count = 0

answer = input("What is the capital of Finland? ")
count += 1
if answer.lower() == "helsinki" : 
    print ("you are correct! ")
    score += 1
else :
    print (" you are wrong!")

answer = input("What's the biggest animal in the world? ")
count += 1
if answer.lower() == "whale" : 
    print ("you are correct! ")
    score += 1
else :
    print (" you are wrong!")

answer = input("Which country is brie cheese originally from? ")
count += 1
if answer.lower() == "france" : 
    print ("you are correct! ")
    score += 1
else :
    print (" you are wrong !")

answer = input("What does IPA stand for?  ")
count += 1
if answer.lower() == "indian pale ale" : 
    print ("you are correct! ")
    score += 1
else :
    print (" you are wrong !")

if score == 1 :
    text = " question correct"
else :
    text = " questions correct"

print ("You got : " + str(score) + text)
print ("You got : " + str((score/count) * 100) + " %")