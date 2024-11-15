from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram import Router
from app.keyboard import mirage_btn, anne_btn
from app.handlers import Router

router = Router()

@router.message(F.text.contains('анненкирхе'))
async def with_puree(message: types.Message, bot):
    caption = '*лютеранская церковь Святой Анны*: популярное место, где можно посетить богослужения, выставки, органные концерты, выпить кофе и купить христианский мерч.\n\n📍Кирочная 8 '
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIK_mc3FjaBpjyAsLNqAxzOuVLPO_ExAAIhXgACl7u4SRgo0PgELeXXNgQ',
                         caption=caption, reply_markup=anne_btn, parse_mode="Markdown")

@router.message(F.text.contains('мираж cinema'))
async def with_puree(message: types.Message, bot):
    caption = '*мираж cinema*: атмосферное место, необычные дизайнерские решения , супер комфортабельный зал\n\n📍 Большой просп. Петроградской стороны, 35 '
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAILEmc3GWme50tt4U6AzQFlpEjhVeQ0AAJUXgACl7u4SYoW3aOaKm4kNgQ',
                         caption=caption, reply_markup=mirage_btn, parse_mode="Markdown")