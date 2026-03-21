from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🛠 Наши услуги'), KeyboardButton(text='📂 Портфолио')],
    [KeyboardButton(text='🌐 Наш сайт'), KeyboardButton(text='👤 О студии')], # ТУТ ИЗМЕНЕНИЯ
    [KeyboardButton(text='🚀 Оставить заявку')]
], resize_keyboard=True, input_field_placeholder='Выберите нужный раздел...')