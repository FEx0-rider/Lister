import colorama  # lib for colors
from colorama import Style, Fore # lib for import main parts of lib

import random # random generator 
import threading # lib for multiple process on cpu



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



def inportWords():

    inportedWords = []
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(" , ")", "-", "_", "+", "="]


    wordsInput = input(str("Write all words including numbers separated by ;  "))
    fileName = input("File name: ")

    
    for words in wordsInput.split(";"): # insert words in inportedWords list
        inportedWords.append(words.strip())



    return inportedWords, symbols, fileName


def decomposition(listWords):


    maxLenght = max(len(lenght) for lenght in listWords)

    letters = [] # first x letters
    lettersInvertBack = [] # last x letters backwards
    lettersBack = [] # last x letters 
    lettersInvert = [] # first x letters backwards
    lettersList = [letters, lettersInvertBack, lettersBack, lettersInvert]
    lettersListLowerUpper = []

    for x in range(1, maxLenght + 1):

        for words in listWords: # outputs first x letters/numbers from strings in inportedWords
            if len(words) >= x: # if word has more then x letters
            
                letters.append(words[:x])

    ####################################################################           

    for x in range(1, maxLenght + 1):

        for words in listWords: # outputs last x letters/numbers from strings in inportedWords backwards
            if len(words) >= x: # if word has more then x letters
            
                lettersInvertBack.append(words[-x:][::-1])

    ###################################################################

    for x in range(1, maxLenght + 1):

        for words in listWords: # outputs last x letters/numbers from strings in inportedWords
            if len(words) >= x: # if word has more then x letters
            
                lettersBack.append(words[-x:])

    ####################################################################           

    for x in range(1, maxLenght + 1):

        for words in listWords: # outputs last x letters/numbers from strings in inportedWords
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
    print(lettersListLowerUpper)


    return lettersListLowerUpper

    



if __name__ == "__main__":
    
    cp.print(start, "red")
    inportedWords, symbols, fileName = inportWords() # loading inputed words and symbols

    print("\nDone!")

    decomposition(inportedWords)