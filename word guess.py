import random
words=["hello","hai","how","you"]
turns=12
guesses=""
word=random.choice(words)
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1
    if failed==0:
        print("you win")
        print("word is:",word)
    guess=input("enter a charcter:")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("your remaining turns are",turns)
        if turns==0:
            print("you loose")
