import random

hang = ["""
    !!! W E L C O M E !!!
    
H A N G M A N - Animal Edition

   +---+
       |
       |
       |
       |
       |
=========""", """
H A N G M A N 

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |     H A N G E D
 / \  |
      |
========="""]


def getRandomWord():
    words = ['giraffe', 'fox', 'tiger', 'chimpanzee', 'squirrel', 'camel', 'lion', 'porcupine',
             'monkey', 'elephant', 'horse', 'kangaroo', 'rhinoceros', 'leopard', 'gorilla', 'hippopotamus', 'panda',
             'zebra', 'wolf', 'rabbit', 'koala']

    word = random.choice(words)
    return word


def displayBoard(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    # replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=' ')
    print("\n")


def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    return input("\nDo you want to play again?(y/n) ").lower().startswith('y')


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord()
gameIsDone = False

while True:
    displayBoard(hang, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The secret word is "' +
                  secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hang) - 1:
            displayBoard(hang, missedLetters,
                         correctLetters, secretWord)
            print('Game Over!!!\nYou have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord()
        else:
            break