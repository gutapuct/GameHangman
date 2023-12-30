from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from game import Game


startButton = InlineKeyboardButton(text="Начать", callback_data="startGame")
startGame = InlineKeyboardMarkup(inline_keyboard=[[startButton]])

startAgainButton = InlineKeyboardButton(text="Начать заново", callback_data="startAgainGame")
startAgainGame = InlineKeyboardMarkup(inline_keyboard=[[startAgainButton]])


restartButton = InlineKeyboardButton(text="Рестарт", callback_data="restartGame")
continueButton = InlineKeyboardButton(text="Продолжить", callback_data="continueGame")
restartOrContinue = InlineKeyboardMarkup(inline_keyboard=[[ continueButton, restartButton ]])

alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def createLettersMarkup(game: Game) -> InlineKeyboardMarkup:
    buttons = list()
    lines = list()

    i = 1
    countInLine = 0

    for symbol in list(alphabet):
        if symbol not in game.successes and symbol not in game.failures:
            buttons.append(InlineKeyboardButton(text=symbol, callback_data="letter" + str(i)))
            countInLine += 1

            if (countInLine == 7):
                lines.append(buttons)
                buttons = list()
                countInLine = 0

        i += 1

    if (len(buttons) > 0):
        lines.append(buttons)

    return InlineKeyboardMarkup(inline_keyboard=lines)
