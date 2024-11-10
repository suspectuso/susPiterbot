from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram import Router
from app.keyboard import main_kb, foodmall_kb, main_settings, backyard_btn, vokzal_btn, eatmarket_btn, morynok_btn, vorynok_btn, balagan_btn, fabrika_btn
from app.handlers import Router

router = Router()

@router.message(F.text.contains('севкабель порт'))
async def with_puree(message: types.Message, bot):
    caption = '*севкабель порт*: креативное пространство, расположенное на берегу Финского залива. Здесь можно найти множество кафе, ресторанов, художественных галерей и концертных площадок\n\n📍Кожевенная линия, 40Б '
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIHlGcwAAFjO5pas7f1GK-gJCwShHt8lAACkWgAAmmPgElyQPrTRIgUyTYE',
                         caption=caption, reply_markup=backyard_btn, parse_mode="Markdown")

@router.message(F.text.contains('новая голладния'))
async def with_puree(message: types.Message, bot):
    caption = '*новая голладния*: общественное пространство и парк с отреставрированными зданиями, липовой аллеей, большим публичным газоном, ресторанами, террасами, магазинами, павильонами и детской площадкой\n\n📍наб. Адмиралтейского канала, 2,'
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIIQmcw0vyL-z3sqIG3vUnK2vU6XEUtAAIBdAACaY-ISd8Z1SH4EnPSNgQ',
                         caption=caption, reply_markup=backyard_btn, parse_mode="Markdown")

@router.message(F.text.contains('seno'))
async def with_puree(message: types.Message, bot):
    caption = '*seno*: пространство совместило в себе множество направлений бизнеса: рестораны, бары, спорт, ритейл, услуги и коворкинг\n\n📍Гороховая улица, 49Б'
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIIRGcw0zEfcvTAbI0Rei6yIRmD7N4pAAIDdAACaY-ISaUWqCSM6Z5XNgQ',
                         caption=caption, reply_markup=backyard_btn, parse_mode="Markdown")

@router.message(F.text.contains('бертгольд центр'))
async def with_puree(message: types.Message, bot):
    caption = '*бертгольд центр*: креативное пространство с барами, магазинами и фестивалями\n\n📍Кожевенная линия, 30 '
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIIb2cw5gHSHIC9LPM6NMDFYBNcs4i1AAKFYQACv8eISeXDnsrb22QTNgQ',
                         caption=caption, reply_markup=backyard_btn, parse_mode="Markdown")


@router.message(F.text.contains('брусницын двор'))
async def with_puree(message: types.Message, bot):
    caption = '*бертгольд центр*: креативное пространство с барами, магазинами и фестивалями\n\n📍Кожевенная линия, 30 '
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIIbWcw5aLL1JwV07DioQhDmDWvze0MAAKAYQACv8eIScTj1AkvqrP-NgQ',
                         caption=caption, reply_markup=backyard_btn, parse_mode="Markdown")

@router.message(F.text.contains('этажи'))
async def with_puree(message: types.Message, bot):
    caption = '*этажи*: каждый этаж здания имеет свою тематику, например, на предпоследнем этаже находится небольшая картинная галерея и фуд-корт, а на остальных этажах — магазины одежды и украшений.\n\n📍Кожевенная линия, 30 '
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIIrGcw6vuyLUERQN0pYuVVqQ3DNrcFAAIGdgACaY-ISWSKLZJUlKJMNgQ',
                         caption=caption, reply_markup=backyard_btn, parse_mode="Markdown")

@router.message(F.text.contains('третье место'))
async def with_puree(message: types.Message, bot):
    caption = '*третье место*: общественное pinterest место, сюда классно приходить вечером и пить вино. \n\n📍Кожевенная линия, 30 '
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIIs2cw7N9oLauRAkTgdAfYyZkR_AnFAALRYQACv8eISaT7a1VplqInNgQ',
                         caption=caption, reply_markup=backyard_btn, parse_mode="Markdown")