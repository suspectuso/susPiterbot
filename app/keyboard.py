from aiogram.types import ReplyKeyboardMarkup, keyboard_button, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, WebAppInfo

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='фудмоллы'), KeyboardButton(text='общественные пространства'), KeyboardButton(text='аниме магазины') ],
    [KeyboardButton(text='смотровые'), KeyboardButton(text='коворкинг')],

],          resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню.')


foodmall_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='backyard'), KeyboardButton(text='фабрика'), KeyboardButton(text='balagan') ],
    [KeyboardButton(text='василеостровский рынок'), KeyboardButton(text='московский рынок')],
    [KeyboardButton(text='eat market'), KeyboardButton(text='vokzal 1853')],
    [KeyboardButton(text='назад')]

],          resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню.')

prost_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='севкабель порт'), KeyboardButton(text='новая голладния')],
    [KeyboardButton(text='seno'), KeyboardButton(text='бертгольд центр')],
    [KeyboardButton(text='брусницын двор'), KeyboardButton(text='этажи')],
    [KeyboardButton(text='третье место')]
],          resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню.')

main_settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="zoom", web_app=WebAppInfo(url="https://reservationsteps.ru/rooms/index/5d33a60d-921b-4106-a099-698a659aa196?lang=ru&scroll_to_rooms=0&disable_block_scrolls=0&insidePopup=0"))],
])


##### foodmals


backyard_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.com/maps/2/saint-petersburg/?ll=30.384823,59.926783&mode=routes&rtext=~59.926843,30.384833&rtt=auto&ruri=~ymapsbm1://org?oid%3D65512785735&z=17")],
])

fabrika_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.390194,59.938802&mode=routes&rtext=~59.939050,30.390134&rtt=mt&ruri=~ymapsbm1://org?oid%3D80963524983&z=17.12")],
])

balagan_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.347692,59.948950&mode=routes&rtext=~59.961253,30.298180&rtt=mt&ruri=~ymapsbm1://org?oid%3D147021361953&z=14.3")],
])

vorynok_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.341381,59.948950&mode=routes&rtext=~59.939385,30.285572&rtt=mt&ruri=~ymapsbm1://org?oid%3D230888383637&z=14.13")],
])

morynok_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.341381,59.922676&mode=routes&rtext=~59.879196,30.323972&rtt=mt&ruri=~ymapsbm1://org?oid%3D137305570564&z=12.79")],
])

eatmarket_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.341381,59.922676&mode=routes&rtext=~59.927622,30.360492&rtt=mt&ruri=~ymapsbm1://org?oid%3D2151546385&z=12.79")],
])

vokzal_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.341381,59.922676&mode=routes&rtext=~59.907193,30.307371&rtt=mt&ruri=~ymapsbm1://org?oid%3D1058429273&z=12.79")],
])

#############

