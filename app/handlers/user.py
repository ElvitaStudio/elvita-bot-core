import os
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import app.keyboards.reply as kb
import app.keyboards.inline as inv

router = Router()

class Order(StatesGroup):
    description = State()
    budget = State()

# --- СТАРТ И ОБ СТУДИИ ---
@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Добро пожаловать в **Elvita Studio**, {message.from_user.first_name}! 🚀\n"
        "Мы создаем профессиональные IT-решения для вашего бизнеса.\n\n"
        "Выберите раздел в меню ниже 👇", 
        reply_markup=kb.main
    )

@router.message(F.text == '👤 О студии')
async def about_us(message: types.Message):
    await message.answer(
        "**Мы — команда профессионалов с 5-летним опытом работы в сфере IT-разработки и автоматизации бизнеса.**\n\n"
        "**Elvita Studio** — это эксперты в области создания сложных Telegram-систем, Web-приложений и интеграции искусственного интеллекта.\n\n"
        "✅ **Наш путь:** За 5 лет мы реализовали более 100 проектов: от высоконагруженных торговых систем до инновационных Mini Apps.\n"
        "✅ **Наш стек:** Python (Aiogram, FastAPI), Node.js, React, Next.js, OpenAI API, PostgreSQL.\n"
        "✅ **Наш подход:** Мы не просто пишем код, а создаем продукт, который приносит прибыль вашему бизнесу."
    )

@router.message(F.text == '🌐 Наш сайт')
async def our_website(message: types.Message):
    await message.answer(
        "🌐 **Наш официальный сайт**\n\n"
        "Там вы можете более подробно ознакомиться с нашими кейсами, узнать о нашей команде и подходе к работе.\n\n"
        "🔗 **[ССЫЛКА БУДЕТ ЗДЕСЬ]**"
    )

# --- РАЗДЕЛ УСЛУГИ (ПОДРОБНО) ---
@router.message(F.text == '🛠 Наши услуги')
async def services_menu(message: types.Message):
    await message.answer("💎 **Наши компетенции:**\n\nВыберите категорию для подробностей 👇", reply_markup=inv.services)

@router.callback_query(F.data.startswith('service_'))
async def service_details(callback: types.CallbackQuery):
    service_type = callback.data.split('_')[1]
    
    descriptions = {
        'bots': "🤖 **Telegram Боты**\n\n● ERP/CRM системы управления бизнесом.\n● Парсеры любой сложности (OLX, Work.ua).\n● Стек: Python (Aiogram 3.x), PostgreSQL.",
        'apps': "📱 **Mini Apps (WebApps)**\n\n● Полноценные интерфейсы внутри TG.\n● Корзина, оплата, сложные анимации.\n● Стек: React / Node.js Backend.",
        'trading': "📈 **Trading Systems**\n\n● Боты для Binance/Bybit на Websockets.\n● Скринеры объемов, плотностей и волатильности.\n● DEX/Web3 автоматизация.",
        'sites': "🌐 **Сайты & Лендинги**\n\n● Высококонверсионные страницы.\n● SEO-оптимизация и скорость.\n● Стек: Next.js, Tailwind CSS.",
        'ai': "🧠 **AI Ассистенты**\n\n● Интеграция GPT-консультантов 24/7.\n● Обучение нейросети на ваших данных (RAG).\n● Автоматизация поддержки на 80%."
    }
    
    text = descriptions.get(service_type, "Описание скоро будет.")
    try:
        await callback.message.edit_text(text, reply_markup=inv.services)
    except:
        pass
    await callback.answer()

# --- ПОРТФОЛИО (ИСПРАВЛЕННОЕ) ---
@router.message(F.text == '📂 Портфолио')
async def portfolio_menu(message: types.Message):
    await message.answer("📂 **Наши выполненные проекты:**\nВыберите кейс для изучения деталей 👇", reply_markup=inv.portfolio)

@router.callback_query(F.data.startswith('port_'))
async def portfolio_details(callback: types.CallbackQuery):
    project = callback.data.split('_')[1]
    
    # Ссылки (Замени на свои реальные, чтобы не было ошибки "Пользователя не существует")
    links = {
        'crypto': 'https://t.me/mybodt',
        'olx': 'https://t.me/dnepr_rent_test',
        'work': 'https://t.me/workua_jobs_Ukraine',
        'fuel': 'https://t.me/Aishop2_bot',
        'nodeshop': 'https://t.me/UX_Shop_Bot',
        'beauty': 'https://t.me/feybeauty_bot'
    }

    descriptions = {
        'crypto': "📊 **Crypto Screener Pro**\n\n● Мониторинг 200+ пар Binance/Bybit.\n● Отслеживание плотностей и объемов.\n● Уведомления за 0.3-0.5 сек.",
        'olx': "🏠 **OLX Parser**\n\n● Авто-мониторинг недвижимости.\n● Фильтрация и обход блокировок.\n● Данные быстрее общего поиска.",
        'work': "💼 **Work.ua Parser**\n\n● Сбор вакансий по ключевым словам.\n● Удаление дублей, экспорт в Sheets.\n● Автоматизация рекрутинга.",
        'fuel': "⛽ **Магазин талонов с AI**\n\n● GPT-консультант для клиентов.\n● Продажа талонов WOG/OKKO.\n● Прием оплат Mono/Crypto.",
        'nodeshop': "🛍️ **Mini App Shop**\n\n● Магазин на Node.js + React.\n● Корзина и оплата внутри Telegram.",
        'beauty': "💇 **Booking System**\n\n● Запись в салон на Next.js.\n● Календарь окон и напоминания.\n● Стек: PostgreSQL, Prisma.",
        'dev': "🛠 **В разработке**\n\nПроект на стадии полировки. Скоро здесь будет описание!"
    }

    text = descriptions.get(project, "Описание скоро будет.")
    
    kb_to_show = inv.portfolio
    if project in links:
        link_btn = InlineKeyboardButton(text='🔗 Открыть проект', url=links[project])
        kb_to_show = InlineKeyboardMarkup(inline_keyboard=[[link_btn]] + inv.portfolio.inline_keyboard)

    try:
        await callback.message.edit_text(text, reply_markup=kb_to_show)
    except:
        pass
    await callback.answer()

# --- ЗАЯВКА (FSM) ---
@router.message(F.text == '🚀 Оставить заявку')
async def start_order(message: types.Message, state: FSMContext):
    await state.set_state(Order.description)
    await message.answer("Опишите вашу задачу: что именно нужно разработать? 📝", reply_markup=types.ReplyKeyboardRemove())

@router.message(Order.description)
async def get_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(Order.budget)
    await message.answer("Ваш примерный бюджет на проект? 💰")

@router.message(Order.budget)
async def get_budget(message: types.Message, state: FSMContext):
    await state.update_data(budget=message.text)
    data = await state.get_data()
    await message.answer("✅ Заявка принята! Менеджер свяжется с вами.", reply_markup=kb.main)
    admin_id = os.getenv('ADMIN_ID')
    if admin_id:
        await message.bot.send_message(admin_id, f"🔔 **ЗАЯВКА!**\n👤 @{message.from_user.username}\n📝 {data['description']}\n💰 {data['budget']}")
    await state.clear()