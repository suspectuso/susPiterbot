from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram import Router
from app.keyboard import sov_btn, hermitage_btn
from app.handlers import Router

router = Router()

@router.message(F.text.contains('советских игровых автоматов'))
async def with_puree(message: types.Message, bot):
    caption = '*музей советских игровых автоматов*: уникальная коллекция музея включает в себя более 50 действующих советских игровых автоматов, можно поиграть, попробовать советскую газировку. \n\n📍Конюшенная пл., д. 2В '
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAILuGc3ItDAl3sbL_b8naiFrNHbd5vYAALmXgACl7u4SdNKqCt4siz_NgQ',
                         caption=caption, reply_markup=sov_btn, parse_mode="Markdown")

@router.message(F.text.contains('эрмитаж'))
async def with_puree(message: types.Message, bot):
    caption = '*эрмитаж*: крупнейший музей России и один из величайших музеев мира \n\n📍Дворцовая пл., 2'
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIMQmc3LOIEt7Vwz1_kMrjph9O-oQ1HAAKIXwACl7u4SV7Hfr7Uwg80NgQ',
                         caption=caption, reply_markup=hermitage_btn, parse_mode="Markdown")




