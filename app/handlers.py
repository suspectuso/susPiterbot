import asyncio
import logging
from codeop import compile_command
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram import Router
from app.keyboard import main_kb, foodmall_kb, prost_kb, pinterest_kb, museum_kb

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

@router.message(F.text.lower() == "pinterest")
async def without_puree(message: types.Message):
    await message.reply("Любищь делать фотографии? Великолепно! Подборка для тебя:", reply_markup=pinterest_kb)

@router.message(F.text.lower() == "музеи")
async def without_puree(message: types.Message):
    await message.reply("Любищь делать фотографии? Великолепно! Подборка для тебя:", reply_markup=museum_kb)