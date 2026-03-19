from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🛠 Наши услуги'), KeyboardButton(text='📂 Портфолио')],
    [KeyboardButton(text='💰 Прайс'), KeyboardButton(text='👤 О студии')],
    [KeyboardButton(text='🚀 Оставить заявку')]
], resize_keyboard=True, input_field_placeholder='Выберите интересующий раздел...')