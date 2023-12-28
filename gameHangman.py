import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import hbold
from game import createGame, Game

TOKEN = os.environ.get('TELEGRAM_GAMEHANGMAN_TOKEN3')

if TOKEN is None:
    raise Exception("Телеграм Токен не найден. Положите токен в Environments по имени TELEGRAM_GAMEHANGMAN_TOKEN3")

dp = Dispatcher()

startButton = InlineKeyboardButton(text="Начать", callback_data="startGame")
restartButton = InlineKeyboardButton(text="Рестарт", callback_data="restartGame")
continueButton = InlineKeyboardButton(text="Продолжить", callback_data="continueGame")
startGame = InlineKeyboardMarkup(inline_keyboard=[[startButton]])
restartOrContinue = InlineKeyboardMarkup(inline_keyboard=[[ continueButton, restartButton ]])

games = {}

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!")
    
    game = getGame(message.from_user.id)
    
    if (game is not None):
        await message.answer(f"Есть незаконченная партия. Продолжить или начать заново?", reply_markup=restartOrContinue)
    else:
        await message.answer(f"Давай сыграем в игру \"Виселица\"!", reply_markup=startGame)

@dp.callback_query(F.data == "startGame")
async def go(callback: types.CallbackQuery) -> None:
    game = getOrCreate(callback.from_user.id)
    await callback.message.answer_photo(game.getImage(), caption=game.getUnguessedWord())

@dp.callback_query(F.data == "restartGame")
async def go(callback: types.CallbackQuery) -> None:
    game = setGame(callback.from_user.id)
    await callback.message.answer_photo(game.getImage(), caption=game.getUnguessedWord())

@dp.callback_query(F.data == "continueGame")
async def go(callback: types.CallbackQuery) -> None:
    game = getOrCreate(callback.from_user.id)
    await callback.message.answer_photo(game.getImage(), caption=game.getUnguessedWord())

@dp.message()
async def echo_handler(message: types.Message) -> None:
    game = games.get(message.from_user.id)
    print(f'game from message: {game}')
    
    await message.answer_photo(game.getImage(), caption=game.getUnguessedWord())

def getGame(id) -> Game:
    return games.get(id)

def getOrCreate(id) -> Game:
    game = getGame(id)
    if (game is None):
        game = setGame(id)

    return game

def setGame(id) -> Game:
    games[id] = createGame()
    return getGame(id)

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
