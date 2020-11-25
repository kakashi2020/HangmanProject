word = "papaya"
game_over = "exit"
letter = input("Guess the 6 letter word. Enter a character or word ")

while letter != word.casefold():
    if letter.casefold() == game_over:
        print("Game Over")
        break
    elif letter in word.casefold():
        print("There are {} letter(s) {} in the word you are guessing".format(word.count(letter), letter))
    else:
        print("There's no letter {} in the word you are guessing".format(letter))
    letter = input("Guess another letter or word, or write 'Exit' to end the game ")
else:
    print("You guest right! The word you are looking for is {}".format(word))


#Changes to make:
  #- Provide position of the letter - CHECK
  #- Display answer of amount of letters in singular if there's only 1 of the chosen letter in the word. Else display anser in plural   
  #- Random Words
