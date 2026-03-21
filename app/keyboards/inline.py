from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки услуг остаются прежними
services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🤖 Telegram Боты', callback_data='service_bots')],
    [InlineKeyboardButton(text='📱 Mini Apps (WebApps)', callback_data='service_apps')],
    [InlineKeyboardButton(text='📈 Трейдинг системы', callback_data='service_trading')]
])

# ПОЛНОЕ ПОРТФОЛИО (8 проектов)
portfolio = InlineKeyboardMarkup(inline_keyboard=[
    # Ряд 1: Трейдинг и Парсинг
    [
        InlineKeyboardButton(text='📈 Crypto Bot', callback_data='port_crypto'),
        InlineKeyboardButton(text='🏠 OLX Parser', callback_data='port_olx')
    ],
    # Ряд 2: Работа и Топливо
    [
        InlineKeyboardButton(text='💼 Work.ua Bot', callback_data='port_work'),
        InlineKeyboardButton(text='⛽ Топливные талоны', callback_data='port_fuel')
    ],
    # Ряд 3: Магазины и Сервисы
    [
        InlineKeyboardButton(text='🛍️ Node.js Shop', callback_data='port_nodeshop'),
        InlineKeyboardButton(text='💇 Салон (Next.js)', callback_data='port_beauty')
    ],
    # Ряд 4: Сайты (В работе)
    [
        InlineKeyboardButton(text='📄 Лендинги (In dev)', callback_data='port_dev'),
        InlineKeyboardButton(text='🌐 Сайты (In dev)', callback_data='port_dev')
    ],
    # Ссылка на GitHub
    [InlineKeyboardButton(text='🔗 Посмотреть весь код на GitHub', url='https://github.com/ElvitaStudio')]
])