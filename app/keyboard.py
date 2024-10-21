from aiogram.types import ReplyKeyboardMarkup, keyboard_button, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, WebAppInfo

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='фудмоллы'), KeyboardButton(text='общественные пространства'), KeyboardButton(text='аниме магазины') ],
    [KeyboardButton(text='смотровые'), KeyboardButton(text='коворкинг'), KeyboardButton(text='назад') ],

],          resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню.')


foodmall_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='backyard'), KeyboardButton(text='фабрика'), KeyboardButton(text='balagan') ],
    [KeyboardButton(text='василеостровский рынок'), KeyboardButton(text='московский рынок')],
    [KeyboardButton(text='eat market'), KeyboardButton(text='vokzal 1853'),],

],          resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню.')



main_settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="zoom", web_app=WebAppInfo(url="https://reservationsteps.ru/rooms/index/5d33a60d-921b-4106-a099-698a659aa196?lang=ru&scroll_to_rooms=0&disable_block_scrolls=0&insidePopup=0"))],
])