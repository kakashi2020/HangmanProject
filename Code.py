word = "papaya"
game_over = "exit"
letter = input("Guess the 6 letter word. Enter a character or word ")

while letter != word.casefold():
    if letter.casefold() == game_over:
        print("Game Over")
        break
    elif letter in word.casefold():
        if word.count(letter) == 1:
            print("There is 1 letter {} in the word you are guessing".format(letter))
        else:
            print("There are {} letter(s) {} in the word you are guessing".format(word.count(letter), letter))
    else:
        print("There's no letter {} in the word you are guessing".format(letter))
    letter = input("Guess another letter or word, or write 'Exit' to end the game ")
else:
    print("You guest right! The word you are looking for is {}".format(word))


#Changes to make:
  #- Get random word 
  #- Insert a limited amount of tries
