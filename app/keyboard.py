from aiogram.types import ReplyKeyboardMarkup, keyboard_button, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, WebAppInfo

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='фудмоллы'), KeyboardButton(text='общественные пространства'), KeyboardButton(text='pinterest') ],
    [KeyboardButton(text='музеи'), KeyboardButton(text='коворкинг')],

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
    [KeyboardButton(text='третье место'), KeyboardButton(text='флагшток') ],
    [KeyboardButton(text='никольские ряды'), KeyboardButton(text='лахта центр')],
    [KeyboardButton(text='назад')]
],          resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню.')

main_settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="zoom", web_app=WebAppInfo(url="https://reservationsteps.ru/rooms/index/5d33a60d-921b-4106-a099-698a659aa196?lang=ru&scroll_to_rooms=0&disable_block_scrolls=0&insidePopup=0"))],
])

pinterest_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='анненкирхе'), KeyboardButton(text='мираж cinema')],
    [KeyboardButton(text='назад')]
],          resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню.')

museum_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='советских игровых автоматов'), KeyboardButton(text='эрмитаж')],
    [KeyboardButton(text='назад')]
],          resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню.')


kovor_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='библиотека маяковского'), KeyboardButton(text='сообщество')],
    [KeyboardButton(text='назад')]
],          resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню.')


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

############# prostransvtva

sevkabel_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.240923,59.924126&mode=routes&rtext=~59.924126,30.240923&rtt=mt&ruri=~ymapsbm1://org?oid%3D105313507204&z=13.9")],
])

newhol_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.243660,59.924126&mode=routes&rtext=~59.929643,30.289633&rtt=mt&ruri=~ymapsbm1://org?oid%3D199688219277&z=13.81")],
])

seno_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.260251,59.924126&mode=routes&rtext=~59.926674,30.322860&rtt=mt&ruri=~ymapsbm1://org?oid%3D183226144612&z=13.37")],
])

bertgold_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.260251,59.924126&mode=routes&rtext=~59.928048,30.312368&rtt=mt&ruri=~ymapsbm1://org?oid%3D38306660659&z=13.37")],
])

brus_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.260251,59.924126&mode=routes&rtext=~59.922677,30.249571&rtt=mt&ruri=~ymapsbm1://org?oid%3D68217909330&z=13.37")],
])

etazhi_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.277094,59.924126&mode=routes&rtext=~59.921880,30.356367&rtt=mt&ruri=~ymapsbm1://org?oid%3D10865085335&z=13.03")],
])

thirdpalace_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.277094,59.924126&mode=routes&rtext=~59.933606,30.348339&rtt=mt&ruri=~ymapsbm1://org?oid%3D211313582405&z=13.03")],
])

flag_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.212658,59.970586&mode=routes&rtext=~59.970586,30.212658&rtt=mt&ruri=~ymapsbm1://org?oid%3D12216375577&z=16")],
])

nikol_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.301493,59.921014&mode=routes&rtext=~59.921014,30.301493&rtt=mt&ruri=~ymapsbm1://org?oid%3D1436376339&z=13.9")],
])

lahta_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.281294,59.954079&mode=routes&rtext=~59.987111,30.178101&rtt=mt&ruri=~ymapsbm1://org?oid%3D71693345624&z=12")],
])

### pinterest

mirage_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.302374,59.959620&mode=routes&rtext=~59.959620,30.302374&rtt=mt&ruri=~ymapsbm1://org?oid%3D1025545600&z=14")],
])

anne_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.307051,59.959617&mode=routes&rtext=~59.944718,30.352068&rtt=mt&ruri=~ymapsbm1://org?oid%3D1494386120&z=13.84")],
])

### museum

sov_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.326905,59.940084&mode=routes&rtext=~59.940084,30.326905&rtt=mt&ruri=~ymapsbm1://org?oid%3D1184371713&z=14.9")],
])

hermitage_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.314566,59.939864&mode=routes&rtext=~59.939864,30.314566&rtt=mt&ruri=~ymapsbm1://org?oid%3D1057721048&z=14.9")],
])

### kovor

maya_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.314688,59.930413&mode=routes&rtext=~59.931911,30.343424&rtt=mt&ruri=~ymapsbm1://org?oid%3D1022452273&z=14.49")],
])


soo_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Построить маршут", url="https://yandex.ru/maps/2/saint-petersburg/?indoorLevel=1&ll=30.291784,59.930413&mode=routes&rtext=~59.930556,30.291454&rtt=mt&ruri=~ymapsbm1://org?oid%3D81913438814&z=16.79")],
])
