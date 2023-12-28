import random
from words import words
from aiogram.types import FSInputFile

class Game:
    def __init__(self, word) -> None:
        self.word = word
        self.successes = list()
        self.failures = list()

    def __str__(self) -> str:
        return f"Word is {self.word}, successes is {self.successes}, failures is {self.failures}"
    
    def getImage(self) -> FSInputFile:
        match len(self.failures):
            case 0:
                return FSInputFile('0.png')
            case 1:
                return FSInputFile('1.png')
            case 2:
                return FSInputFile('2.png')
            case 3:
                return FSInputFile('3.png')
            case 4:
                return FSInputFile('4.png')
            case 5:
                return FSInputFile('5.png')
            case _:
                return FSInputFile('6.png')

    def getUnguessedWord(self) -> str:
        result = list()

        for char in list(self.word):
            if (char not in self.successes):
                char = result.append("_")
            else:
                char = result.append(char)

        return " ".join(result)
    
def createGame() -> Game:
    randomWord = random.choice(words)
    print(f'word: {randomWord}')
    return Game(randomWord)

