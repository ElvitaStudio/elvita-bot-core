from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Раздел "Наши услуги"
services = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='🤖 Telegram Боты', callback_data='service_bots'),
        InlineKeyboardButton(text='📱 Mini Apps (WebApps)', callback_data='service_apps')
    ],
    [
        InlineKeyboardButton(text='📈 Trading Systems', callback_data='service_trading'),
        InlineKeyboardButton(text='🌐 Сайты & Лендинги', callback_data='service_sites')
    ],
    [
        InlineKeyboardButton(text='🧠 AI Ассистенты', callback_data='service_ai')
    ]
])

# Раздел "Портфолио" (8 проектов, названия кнопок исправлены под код)
portfolio = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='📈 Crypto Bot', callback_data='port_crypto'),
        InlineKeyboardButton(text='🏠 OLX Parser', callback_data='port_olx')
    ],
    [
        InlineKeyboardButton(text='💼 Work.ua Bot', callback_data='port_work'),
        InlineKeyboardButton(text='⛽ Топливные талоны', callback_data='port_fuel')
    ],
    [
        InlineKeyboardButton(text='🛍️ Node.js Shop', callback_data='port_nodeshop'),
        InlineKeyboardButton(text='💇 Салон (Next.js)', callback_data='port_beauty')
    ],
    [
        InlineKeyboardButton(text='📄 Лендинги', callback_data='port_dev'),
        InlineKeyboardButton(text='🌐 Сайты', callback_data='port_dev')
    ],
    [InlineKeyboardButton(text='🔗 Весь код на GitHub Студии', url='https://github.com/ElvitaStudio')]
])