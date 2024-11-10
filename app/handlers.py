import asyncio
import logging
from codeop import compile_command
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram import Router
from app.keyboard import main_kb, foodmall_kb, prost_kb

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="места"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Какие места мы посетим сегодня?"
    )
    await message.answer("Привет!! Я так рад что ты зашел сюда :З Давай я тебе подскажу:", reply_markup=main_kb)

@router.message(F.video)
async def get_photo(message: types.Message):
    await message.answer(f'ID видео: {message.video.file_id}')

@router.message(F.photo)
async def get_photo(message: types.Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')



# @router.message(F.text.lower() == "назад")
# async def cmd_start(message: types.Message):
#     kb = [
#         [
#             types.KeyboardButton(text="места"),
#         ],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#         input_field_placeholder="Какие места мы посетим сегодня?"
#     )
#     await message.answer("Привет!! Я так рад что ты зашел сюда :З Давай я тебе подскажу:", reply_markup=keyboard)
#
#
# @router.message(F.text.lower() == "места")
# async def cmd_start(message: types.Message):
#     kb = [
#         [
#             types.KeyboardButton(text="полки"),
#             types.KeyboardButton(text="фуд-корты"),
#             types.KeyboardButton(text="общественные пространства"),
#             types.KeyboardButton(text="аниме магазины"),
#             types.KeyboardButton(text="смотровые"),
#             types.KeyboardButton(text="коворкинг"),
#             types.KeyboardButton(text="назад"),
#
#         ],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#         input_field_placeholder="Какие места мы посетим сегодня?"
#     )
#     await message.answer("Какие места мы посетим сегодня?", reply_markup=keyboard)

@router.message(F.text.lower() == "назад")
async def with_puree(message: types.Message):
    await message.reply("Куда мы в этот раз отправимся?)", reply_markup=main_kb)



@router.message(F.text.lower() == "полки")
async def with_puree(message: types.Message):
    await message.reply("https://yandex.ru/maps?bookmarks%5BpublicId%5D=54wrARBj&utm_source=share&utm_campaign=bookmarks")

@router.message(F.text.lower() == "фудмоллы")
async def without_puree(message: types.Message):
    await message.reply("Ты наверное очень любишь кушать ^_^\nВот подборка мест где суровый гурман может утешить свою душу:", reply_markup=foodmall_kb)

@router.message(F.text.lower() == "общественные пространства")
async def without_puree(message: types.Message):
    await message.reply("Отличный выбор для прогулки ^_^\nВот подборка мест где можно классно провести время:", reply_markup=prost_kb)





### фудмоллы

# @router.message(F.text.lower() == "backyard")
# async def without_puree(message: types.Message, bot):
#     await message.reply("Неплохой выбор, здесь и парвда можно перекусить. Много раличных кухонь, классный интерьер. Если ты будешь неподалёку, то советую тебе зайти сюда")
#     photo_ids = [
#         'BAACAgIAAxkBAAIBsGcQYElxeezp2AptBzIJAxbugoTDAAJ1YwACwsGBSFuahymrgfmLNgQ'
#
#     ]

    # media = [types.InputMediaVideo(media=video_id) for video_id in photo_ids]
    # await bot.send_media_group(chat_id=message.chat.id, media=media)
    # await message.reply("https://yandex.ru/maps/-/CDdEa41t")

# @router.message(F.text.lower() == "фабрика")
# async def without_puree(message: types.Message, bot):
#     await message.reply("Ооо,а это уже интереснее. Здесь проводят активности, можно сыграть в настольный теннис. Фабрика больше чем фудмолл, здесь можно отдохнуь")
#     photo_ids = [
#         'AgACAgIAAxkBAAIBxmcQZBVQMg5-zPVRfneNBJ1L0P2kAAKH5zEbwsGBSASa2ytWkqniAQADAgADeQADNgQ',
#         'AgACAgIAAxkBAAIBxWcQZBXMeSWbWkDRGBkP7pQpw_CdAAKG5zEbwsGBSApW2oUK20bgAQADAgADeQADNgQ',
#         'AgACAgIAAxkBAAIBxGcQZBVq-YG54ztBruqplx2BEIn4AAKF5zEbwsGBSB3aGRcEKjgNAQADAgADeQADNgQ'
#
#     ]
#
#     media = [types.InputMediaPhoto(media=photo_ids) for photo_ids in photo_ids]
#     await bot.send_media_group(chat_id=message.chat.id, media=media)
#     await message.reply("https://yandex.ru/maps/-/CDdEaKK4")
#
# @router.message(F.text.lower() == "balagan")
# async def without_puree(message: types.Message, bot):
#     await message.reply("Место для жителей города и туристов, для студентов и семейных пар, для белых воротничков и хипстеров, для девушек со стразами и парней со скейтами, для серьёзных и весёлых, для молодых и зрелых — для каждого… ")
#     await message.reply("Balagan — это трехуровневое гастрономическое пространство общей площадью более 2000 кв. м.")
#     photo_ids = [
#         'AgACAgIAAxkBAAIB2mcQaT0e2CE-o0fLHeovi_0VLBOhAAKK5zEbwsGBSLKp3j8EMM6fAQADAgADeAADNgQ',
#         'AgACAgIAAxkBAAIB3WcQaT3EYwVTSG7ZLhY9_ArMsWo9AAKN5zEbwsGBSPK2QI1jhyXQAQADAgADeAADNgQ',
#         'AgACAgIAAxkBAAIB3GcQaT27ri0Rh4VD0lzkDskk03Q6AAKM5zEbwsGBSIKmd3vGCAABmwEAAwIAA3kAAzYE',
#         'AgACAgIAAxkBAAIB22cQaT2OlYp-xL-X6yv_1WaA4cdbAAKL5zEbwsGBSJHo2pajc0-8AQADAgADeAADNgQ'
#     ]
#
#     media = [types.InputMediaPhoto(media=photo_ids) for photo_ids in photo_ids]
#     await bot.send_media_group(chat_id=message.chat.id, media=media)
#     await message.reply("https://yandex.ru/maps/-/CDdEa865")
#
# @router.message(F.text.lower() == "eat market")
# async def without_puree(message: types.Message, bot):
#     await message.reply("Описание: Eat Market — это гастрономический проект, который объединяет в одном месте ведущие ресторанные концепции столицы. На фуд-холле представлены 40 ресторанных проектов. Каждый день здесь готовят каре ягненка, хумус и осьминогов, корейский пибимпаб, марокканский тажин, бургеры из лучшего российского мяса и кавказские лепешки. В общем, вокруг света за 80 минут. И все под одним куполом!")
#     await message.reply("Мнение: Идеальное расположение, большой выбор кухонь, а если хочется что-нибудь поопроще, то можно спустится на этаж ниже.")
#     photo_ids = [
#         'BAACAgIAAxkBAAIB9GcQbwbTey_a4SIixt2HgawJvqXAAAKFYwACwsGBSC6LD37kK_oWNgQ',
#     ]
#
#     media = [types.InputMediaVideo(media=video_id) for video_id in photo_ids]
#     await bot.send_media_group(chat_id=message.chat.id, media=media)
#     await message.reply("https://yandex.ru/maps/-/CDdEeQZ8")
#
# @router.message(F.text.lower() == "vokzal 1853")
# async def without_puree(message: types.Message, bot):
#     await message.reply("Описание: Тематический ресторанный комплекс, самый большой фудмолл в Европе в историческом здании Варшавского вокзала. Три этажа объединят всю гастрономическую, развлекательную и деловую жизнь Петербурга.")
#     await message.reply("Мнение: ")
#     photo_ids = [
#         'AgACAgIAAxkBAAICGmcQdpdZNIh0A0wHWR-0skpYHrAqAAIV3jEbwsGJSIBmxjMvX_pWAQADAgADeAADNgQ',
#         'AgACAgIAAxkBAAICG2cQdpdtV3yhrHOpUydB-LvVjjc4AAIW3jEbwsGJSBJM96HbzIxYAQADAgADeQADNgQ',
#         'AgACAgIAAxkBAAICHGcQdpdTwMLV-O-2TTO28Zyf_-izAAIX3jEbwsGJSBGzAnO9pWrMAQADAgADeAADNgQ',
#         'AgACAgIAAxkBAAICHWcQdpfEaqyNTzoL5HwBkClMtYsNAAIY3jEbwsGJSGNdTyZdiRf3AQADAgADeQADNgQ'
#
#     ]
#
#     media = [types.InputMediaPhoto(media=photo_ids) for photo_ids in photo_ids]
#     await bot.send_media_group(chat_id=message.chat.id, media=media)
#     await message.reply("https://yandex.ru/maps/-/CDdEe020")
#
# @router.message(F.text.lower() == "василеостровский рынок")
# async def without_puree(message: types.Message, bot):
#     await message.reply("Описание: Атмосферное место в центре Петербурга по принципу фудкорт + рынок. Здорово, что можно прийти компанией и каждый выберет кухню по душе - индийскую, вьетнамскую, грузинскую, японскую, морепродукты, хот-доги и бургеры. Есть два этажа+дворик в летнее время")
#     await message.reply("Мнение: ")
#     photo_ids = [
#         'AgACAgIAAxkBAAICgmcQewqX96RVyAYIrp_9n28FzMX1AAIc3jEbwsGJSP0nYTSZDd_VAQADAgADeAADNgQ',
#         'AgACAgIAAxkBAAICgWcQewryQbaG2LCdN_E0FBDoCwLKAAIb3jEbwsGJSDNCkQHBUIzkAQADAgADeQADNgQ',
#         'AgACAgIAAxkBAAICg2cQewqRLpId8PAQgWUQqphYNCWEAAId3jEbwsGJSLQz05kgKJyAAQADAgADeAADNgQ',
#         'AgACAgIAAxkBAAIChGcQewosQmsInS8CltKTP1kMwi1mAAIe3jEbwsGJSBLBbh3ERF4BAQADAgADeAADNgQ'
#
#     ]
#
#     media = [types.InputMediaPhoto(media=photo_ids) for photo_ids in photo_ids]
#     await bot.send_media_group(chat_id=message.chat.id, media=media)
#     await message.reply("https://yandex.ru/maps/-/CDdEiFnK")
#
# @router.message(F.text.lower() == "московский рынок")
# async def without_puree(message: types.Message, bot):
#     await message.reply("Описание: Реконструированный рынок в Московском районе, куда стоит идти скорее на обед, чем за покупками. Например, чтобы съесть классный карри, фо бо или хот-дог. Впрочем, прилавки с красивыми фруктами, мясом и рыбой здесь тоже работают.")
#     await message.reply("Мнение: ")
#     photo_ids = [
#         'AgACAgIAAxkBAAICqWcQgU0Ef7Qk2HBcUjlEESfmD0R2AAIi3jEbwsGJSA31BIH2Q1xGAQADAgADeAADNgQ',
#         'AgACAgIAAxkBAAICq2cQgU1LfCxzSaEhkWI1prJ2KlAKAAIj3jEbwsGJSME2Ur2J6T3eAQADAgADeAADNgQ',
#         'AgACAgIAAxkBAAICqmcQgU13N8ZoUPyxR2NktyDXeJ8yAAIk3jEbwsGJSOmaRKtfyp1gAQADAgADeQADNgQ',
#
#     ]
#
#     media = [types.InputMediaPhoto(media=photo_ids) for photo_ids in photo_ids]
#     await bot.send_media_group(chat_id=message.chat.id, media=media)
#     await message.reply("https://yandex.ru/maps/-/CDdEi-oY")
#
#
#
#
# ###
#
#
# @router.message(F.text.lower() == "общественные пространства")
# async def without_puree(message: types.Message):
#     await message.reply("https://yandex.ru/maps?bookmarks%5BpublicId%5D=cNjx5wij&utm_source=share&utm_campaign=bookmarks")
#
# @router.message(F.text.lower() == "аниме магазины")
# async def without_puree(message: types.Message):
#     await message.reply("https://yandex.ru/maps?bookmarks%5BpublicId%5D=xEBlGhdW&utm_source=share&utm_campaign=bookmarks")
#
# @router.message(F.text.lower() == "смотровые")
# async def without_puree(message: types.Message):
#     await message.reply("https://yandex.ru/maps?bookmarks%5BpublicId%5D=RxoCp5rJ&utm_source=share&utm_campaign=bookmarks")
#
# @router.message(F.text.lower() == "коворкинг")
# async def without_puree(message: types.Message):
#     await message.reply("https://yandex.ru/maps?bookmarks%5BpublicId%5D=QWHt-V86&utm_source=share&utm_campaign=bookmarks")