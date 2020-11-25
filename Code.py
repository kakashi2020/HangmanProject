word = "papaya"
game_over = "exit"
letter = input("You have 10 tries to guess the 6 letter word. Enter a character or word ")
print()
guesses = 1
while letter != word.casefold():
    if letter.casefold() == game_over:
        print("Game Over")
        break
    elif letter in word.casefold():
        if word.count(letter) == 1:
            print("There is 1 letter '{}' in the word you are guessing".format(letter))
        else:
            print("There are {} letters '{}' in the word you are guessing".format(word.count(letter), letter))
        #print("There is one or more letters {} in the word you are guessing".format(letter))
    elif letter != word and guesses == 10:
        print("In your 10th try you did not guess the word. You lose!")
        break
    else:
        print("There's no letter '{}' in the word you are guessing".format(letter))
    letter = input("This was your {} try out of 10. Try another another letter or word, or write 'Exit' to end the game ".format(guesses))
    guesses += 1
    print("*" * 80)
else:
    print("You guest right! The word you are looking for is '{}'".format(word))


#Changes to make:
  #- Get random word 
  
