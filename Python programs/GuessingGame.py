# code to build a guessing game

secret_word = "Giraffe"
guess = ""
count = 1
count_limit = 3
correctGuess = False

while guess!=secret_word and count<=count_limit :
    guess = input("Input your guess "+str(count)+" : ")
    if guess == secret_word:
        correctGuess = True
    count+=1

if correctGuess :
    print("You Win!!")

else :
    print("You didn't win")