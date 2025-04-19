import colorama  # lib for colors
from colorama import Style, Fore # lib for import main parts of lib

import random # random generator 
import threading # lib for multiple process on cpu
import sys


# output print
start = """                                        
@@@       @@@   @@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@   
@@@       @@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!       @@!  !@@         @@!    @@!       @@!  @@@  
!@!       !@!  !@!         !@!    !@!       !@!  @!@  
@!!       !!@  !!@@!!      @!!    @!!!:!    @!@!!@!   
!!!       !!!   !!@!!!     !!!    !!!!!:    !!@!@!    
!!:       !!:       !:!    !!:    !!:       !!: :!!   
 :!:      :!:      !:!     :!:    :!:       :!:  !:!  
 :: ::::   ::  :::: ::      ::     :: ::::  ::   :::  
: :: : :  :    :: : :       :     : :: ::    :   : :  
                                                      

written by FEx0

for help CTRL + C and run python3 lister.py help


"""

map = """


LISTER EXTRA FUNCTIONS 
+------------------------------------------+
| 1. 🔀 Random                             |
| 2. 💣 Rockyou included                   |
| 3. 📂 Include my own list file (.txt)    |
| 4. 🔣 Input special charakters           |
|                                          |
| If none pres ENTER                       |
+------------------------------------------+

"""

class ColorPrinter: # coloring text easy
    def __init__(self):
        self.colors = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'blue': Fore.BLUE,
            'yellow': Fore.YELLOW,
            'cyan': Fore.CYAN,
            'magenta': Fore.MAGENTA,
            'white': Fore.WHITE,
            'black': Fore.BLACK
        }

    def print(self, text, color):
        color = color.lower()
        if color in self.colors:
            print(self.colors[color] + text + Style.RESET_ALL)
        else:
            print(Style.RESET_ALL + text)  # fallback: default color
cp = ColorPrinter()

def showHelp():
    cp.print("\n\nThis tool is only for education purposes \n\n", "yellow")
    cp.print("""
This tool helps you with making password lists.

        Usage:
             1. Run this script (python3 lister.py)
             2. It will automatically ask on your words
             3. Insert info about person (more is better), like this: tool;lists;5000;education;python;2025;%;! (the sequence doesn't matter)
             4. Pres ENTER
             5. Write name for future password list
             6. Pres ENTER
             7. Tool will show you options
             8. Write all numbers if you want to use the option, like this: 4;1;3 (the sequence doesn't matter)
             9. Press ENTER
            10. Now you can decide if you want to create the file
            11. If yes pres y or Y otherwise pres n or N
            12. Wait and enjoy
             

         Bonus: If you want to exit earlier pres CTRL + C 
             

Thanks for using FEx0

""", "blue")

def importWords():

    importedWords = []
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(" , ")", "-", "_", "+", "="]


    wordsInput = input(str("Write all words including numbers separated by ;  "))
    fileName = input("File name: ")

    
    for words in wordsInput.split(";"): # insert words in importedWords list
        importedWords.append(words.strip())



    return importedWords, symbols, fileName

def decomposition(listWords): # from given words creates list with letters


    maxLenght = max(len(lenght) for lenght in listWords)

    letters = [] # first x letters
    lettersInvertBack = [] # last x letters backwards
    lettersBack = [] # last x letters 
    lettersInvert = [] # first x letters backwards
    lettersList = [letters, lettersInvertBack, lettersBack, lettersInvert]
    lettersListLowerUpper = []

    for x in range(1, maxLenght + 1):

        for words in listWords: # outputs first x letters/numbers from strings in importedWords
            if len(words) >= x: # if word has more then x letters
            
                letters.append(words[:x])

    ####################################################################           

    for x in range(1, maxLenght + 1):

        for words in listWords: # outputs last x letters/numbers from strings in importedWords backwards
            if len(words) >= x: # if word has more then x letters
            
                lettersInvertBack.append(words[-x:][::-1])

    ###################################################################

    for x in range(1, maxLenght + 1):

        for words in listWords: # outputs last x letters/numbers from strings in importedWords
            if len(words) >= x: # if word has more then x letters
            
                lettersBack.append(words[-x:])

    ####################################################################           

    for x in range(1, maxLenght + 1):

        for words in listWords: # outputs last x letters/numbers from strings in importedWords
            if len(words) >= x: # if word has more then x letters
            
                lettersInvert.append(words[:x][::-1])


    for i in lettersList: # in list takes every before created chrakter and 
        for x in i:
            x = "".join(x)
            lettersListLowerUpper.append(x)
            x = x.upper()
            lettersListLowerUpper.append(x)


    for words in listWords: # words to letters
        for letter in words:
            lettersListLowerUpper.append(letter)

        for letter in words.upper():
            lettersListLowerUpper.append(letter)
            

    lettersListLowerUpper = list(set(lettersListLowerUpper)) # deleting repeating charakters

    return lettersListLowerUpper




if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            if sys.argv[1].lower() == "help":
                showHelp()
                sys.exit()  # ends help


        cp.print(start, "red")
        importedWords, symbols, fileName = importWords() # loading inputed words and symbols
        lettersListLowerUpper = decomposition(importedWords)

    except KeyboardInterrupt:
        sys.exit(0)

    