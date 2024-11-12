from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram import Router
from app.keyboard import sevkabel_btn
from app.handlers import Router

router = Router()

@router.message(F.text.contains('мираж cinema'))
async def with_puree(message: types.Message, bot):
    caption = '*мираж cinema*: креативное пространство, расположенное на берегу Финского залива. Здесь можно найти множество кафе, ресторанов, художественных галерей и концертных площадок\n\n📍Кожевенная линия, 40Б '
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIHlGcwAAFjO5pas7f1GK-gJCwShHt8lAACkWgAAmmPgElyQPrTRIgUyTYE',
                         caption=caption, reply_markup=sevkabel_btn, parse_mode="Markdown")
