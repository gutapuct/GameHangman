import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from game import Game
from KeyboardMarkups import startGame, restartOrContinue, startAgainGame, createLettersMarkup

TOKEN = os.environ.get('TELEGRAM_GAMEHANGMAN_TOKEN')

if TOKEN is None:
    raise Exception("Телеграм Токен не найден. Положите токен в Environments по имени TELEGRAM_GAMEHANGMAN_TOKEN3")

dp = Dispatcher()

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
    await callback.message.answer_photo(game.getImage(), caption=game.getUnguessedWord(), reply_markup=createLettersMarkup(game))

@dp.callback_query(F.data == "restartGame")
async def go(callback: types.CallbackQuery) -> None:
    game = setGame(callback.from_user.id)
    await callback.message.answer_photo(game.getImage(), caption=game.getUnguessedWord(), reply_markup=createLettersMarkup(game))

@dp.callback_query(F.data == "continueGame")
async def go(callback: types.CallbackQuery) -> None:
    game = getOrCreate(callback.from_user.id)
    await callback.message.answer_photo(game.getImage(), caption=game.getUnguessedWord(), reply_markup=createLettersMarkup(game))

@dp.callback_query(F.data == "startAgainGame")
async def go(callback: types.CallbackQuery) -> None:
    game = setGame(callback.from_user.id)
    await callback.message.answer_photo(game.getImage(), caption=game.getUnguessedWord(), reply_markup=createLettersMarkup(game))

async def callbackForLetter(callback: types.CallbackQuery, game: Game) -> None:
    if (game.finished()):
        await callback.message.answer_photo(game.getImage(), caption=f"{hbold("Это победа!")} :-) Ты молодец!!!", reply_markup=startAgainGame)
    elif (game.failed()):
        await callback.message.answer_photo(game.getImage(), caption=f"{hbold("Это поражение!")} :-( Попробуй снова", reply_markup=startAgainGame)
    else:
        await callback.message.answer_photo(game.getImage(), caption=game.getUnguessedWord(), reply_markup=createLettersMarkup(game))

@dp.message()
async def echo_handler(message: types.Message) -> None:
    game = getGame(message.from_user.id)
    if (game is None):
        await message.answer(f"Для начала игры нажмите кнопку!", reply_markup=startGame)
    else:
        await message.answer(f"Хотите начать заново?", reply_markup=restartOrContinue)

def getGame(id) -> Game:
    return games.get(id)

def getOrCreate(id) -> Game:
    game = getGame(id)
    if (game is None):
        game = setGame(id)

    return game

def setGame(id) -> Game:
    games[id] = Game()
    return getGame(id)

@dp.callback_query(F.data == "letter1")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("А")
    await callbackForLetter(callback, game)
    
@dp.callback_query(F.data == "letter2")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Б")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter3")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("В")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter4")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Г")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter5")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Д")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter6")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Е")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter7")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Ж")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter8")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("З")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter9")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("И")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter10")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Й")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter11")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("К")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter12")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Л")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter13")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("М")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter14")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Н")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter15")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("О")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter16")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("П")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter17")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Р")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter18")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("С")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter19")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Т")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter20")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("У")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter21")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Ф")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter22")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Х")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter23")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Ц")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter24")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Ч")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter25")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Ш")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter26")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Щ")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter27")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Ъ")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter28")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Ы")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter29")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Ь")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter30")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Э")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter31")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Ю")
    await callbackForLetter(callback, game)

@dp.callback_query(F.data == "letter32")
async def go(callback: types.CallbackQuery) -> None:
    game = getGame(callback.from_user.id)
    game.checkLetter("Я")
    await callbackForLetter(callback, game)

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
