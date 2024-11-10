from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram import Router
from app.keyboard import main_kb, foodmall_kb, main_settings, backyard_btn, vokzal_btn, eatmarket_btn, morynok_btn, vorynok_btn, balagan_btn, fabrika_btn
from app.handlers import Router

router = Router()

@router.message(F.text.contains('backyard'))
async def with_puree(message: types.Message, bot):
    caption = '*Backyard*: стильно оформлены корнеры, есть зона со столиками у камина.\n\nСовременная кухня на любой вкус - грузинская, корейская, итальянская, уйгурская и др.\n\n📍Херсонская ул., 43/12 '
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIGzGcvzC0u3xYr4z_TfvNmVM4P5wyzAAJCXwACv8eASd0qUM9XrzP4NgQ',
                         caption=caption, reply_markup=backyard_btn, parse_mode="Markdown")


@router.message(F.text.contains('фабрика'))
async def with_puree(message: types.Message, bot):
    caption = '*Фабрика*: фудхолл на 12 корнеров, или как их здесь называют - "цехов"; на втором этаже - коворкинг с общей рабочей зоной на 50 мест и отдельными офисами под аренду.\n\n📍 Кирочная, 67 '
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIIEWcwrGKXWY6RbDy2XbBnV5NveRfHAAK7XAACIM-JSQEcucWZluseNgQ',
                         caption=caption, reply_markup=fabrika_btn, parse_mode="Markdown")

@router.message(F.text.contains('balagan'))
async def with_puree(message: types.Message, bot):
    caption = '*balagan*: три этажа — каждый со своей концепцией: на первом уровне — фаст-кэжуал, быстрая отдача блюд и демократичные цены, на втором — оригинальные гастрономические проекты и бары с широким выбором вин, коктейлей, пива и закусок. Также здесь находится галерея Debosh,\n\n📍 Малый пр. ПС, 54-56'
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIG_mcv53cwDwmWu1YtxdNfWV0HK2qKAALCXwACv8eASS3-3Z7aTBJMNgQ',
                         caption=caption, reply_markup=balagan_btn, parse_mode="Markdown")

@router.message(F.text.contains('василеостровский рынок'))
async def with_puree(message: types.Message, bot):
    caption = '*василеостровский рынок*: современный фудхолл, создатели собрали внутри множество известных в городе гастропроектов, а также магазины и рыночные лавки.\n\n📍 Большой пр. ВО 16'
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIHw2cwi1uWRefhFZlglTGf1IIWAoSdAAL6bgACaY-ISSpKzR6JQNWPNgQ',
                         caption=caption, reply_markup=vorynok_btn, parse_mode="Markdown")

@router.message(F.text.contains('московский рынок'))
async def with_puree(message: types.Message, bot):
    caption = '*московский рынок*: гастромаркет расположился в здании советского рынка на улице Решетникова возле станции метро "Электросила"\n\n📍 ул. Решетникова, 12'
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIHC2cv72L9_woNpDHXAtSjVHHVSV6cAALaXwACv8eASV5SClnwQDvfNgQ',
                         caption=caption, reply_markup=morynok_btn, parse_mode="Markdown")

@router.message(F.text.contains('eat market'))
async def with_puree(message: types.Message, bot):
    caption = '*eat market*: представлены 40 ресторанных проектов. Каждый день здесь готовят каре ягненка, хумус и осьминогов, корейский пибимпаб, марокканский тажин, бургеры из лучшего российского мяса и кавказские лепешки. \n\n📍 Лиговский просп., 30'
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIB9GcQbwbTey_a4SIixt2HgawJvqXAAAKFYwACwsGBSC6LD37kK_oWNgQ',
                         caption=caption, reply_markup=eatmarket_btn, parse_mode="Markdown")

@router.message(F.text.contains('vokzal 1853'))
async def with_puree(message: types.Message, bot):
    caption = '*vokzal 1853*: самый большой фудмолл в Европе в историческом здании Варшавского вокзала. Три этажа объединят всю гастрономическую, развлекательную и деловую жизнь Петербурга. \n\n📍 наб. Обводного канала, 118С'
    await bot.send_video(chat_id=message.chat.id,
                         video='BAACAgIAAxkBAAIHNWcv8m15Od0YSZjuQDyULdeunxDrAALlXwACv8eASSwvupzg3UYNNgQ',
                         caption=caption, reply_markup=vokzal_btn, parse_mode="Markdown")