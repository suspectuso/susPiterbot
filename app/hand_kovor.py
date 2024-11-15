from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram import Router
from app.keyboard import maya_btn, soo_btn
from app.handlers import Router

router = Router()

@router.message(F.text.contains('библиотека маяковского'))
async def with_puree(message: types.Message, bot):
    caption = '*библиотека маяковского*: бесплатный вход, стильное просторное место \n\n📍наб. реки Фонтанки, 44'
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIMxmc3MsOgPl3bAAGmXTx4r23ZHwABUtMAAr9fAAKXu7hJjSMNaP2QHgE2BA',
                         caption=caption, reply_markup=maya_btn, parse_mode="Markdown")


@router.message(F.text.contains('сообщество'))
async def with_puree(message: types.Message, bot):
    caption = '*сообщество*: стильно, модно, молодёжно, да ещё и в самом сердце Питера. Платишь 150₽ и сидишь хоть до закрытия \n\n📍 Новая голландия'
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAINBWc3NclwEWAYB0N8XHmVYQNaThROAAL2XwACl7u4SXxgrl3bJqCwNgQ',
                         caption=caption, reply_markup=soo_btn, parse_mode="Markdown")