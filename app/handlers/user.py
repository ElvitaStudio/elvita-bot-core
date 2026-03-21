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

# --- СТАРТ И О СТУДИИ ---
@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Добро пожаловать в **Elvita Studio**, {message.from_user.first_name}! 🚀\n\nВыберите раздел в меню 👇", reply_markup=kb.main)

@router.message(F.text == '👤 О студии')
async def about_us(message: types.Message):
    await message.answer("**Elvita Studio** — ваш партнер в IT.\n\n✅ Опыт разработки 2+ года.\n✅ Стек: Python, Aiogram, React.")

# --- РАЗДЕЛ УСЛУГИ ---
@router.message(F.text == '🛠 Наши услуги')
async def services_menu(message: types.Message):
    await message.answer("💎 **Наши услуги:**\nВыберите категорию 👇", reply_markup=inv.services)

@router.callback_query(F.data.startswith('service_'))
async def service_details(callback: types.CallbackQuery):
    service_type = callback.data.split('_')[1]
    if service_type == 'bots':
        text = "🤖 **Telegram Боты**\n\nСоздаем всё: от автоответчиков до сложных ERP-систем."
    elif service_type == 'apps':
        text = "📱 **Mini Apps**\n\nПолноценные Web-интерфейсы внутри Telegram."
    elif service_type == 'trading':
        text = "📈 **Трейдинг системы**\n\nСкринеры, торговые боты (Binance/Bybit) и DEX."
    await callback.message.edit_text(text, reply_markup=inv.services)
    await callback.answer()

# --- РАЗДЕЛ ПОРТФОЛИО (ВСТАВЛЯЕМ СЮДА) ---
@router.message(F.text == '📂 Портфолио')
async def portfolio_menu(message: types.Message):
    await message.answer("📂 **Наши кейсы:**\nВыберите проект, чтобы узнать подробности 👇", reply_markup=inv.portfolio)

@router.callback_query(F.data.startswith('port_'))
async def portfolio_details(callback: types.CallbackQuery):
    project = callback.data.split('_')[1]
    
    # Сюда вставляй свои ссылки
    links = {
        'crypto': 'https://t.me/mybodt',
        'olx': 'https://t.me/dnepr_rent_test',
        'work': 'https://t.me/workua_jobs_Ukraine',
        'fuel': 'https://t.me/Aishop2_bot',
        'nodeshop': 'https://t.me/UX_Shop_Bot',
        'beauty': 'https://t.me/feybeauty_bot'
    }

    # Тексты описаний
    descriptions = {
        'crypto': (
            "📊 **Crypto Screener Pro**\n\n"
            "● **Функционал:** Мониторинг 200+ торговых пар на Binance и Bybit в реальном времени.\n"
            "● **Возможности:** Отслеживание крупных лимитных заявок (плотностей), резких всплесков объема и волатильности.\n"
            "● **Технологии:** Python (Asyncio), Websockets, API бирж.\n"
            "● **Скорость:** Уведомление приходит в Telegram через 0.3-0.5 сек после события."
        ),
        'olx': (
            "🏠 **OLX Parser (Недвижимость)**\n\n"
            "● **Функционал:** Автоматический мониторинг новых объявлений об аренде/продаже.\n"
            "● **Возможности:** Фильтрация по цене за м², району, этажности. Обход блокировок OLX и защита от капчи.\n"
            "● **Результат:** Клиент получает объявление раньше, чем оно появляется в общем поиске.\n"
            "● **Стек:** BS4, Selenium, Proxy-rotation."
        ),
        'work': (
            "💼 **Work.ua Job Scraper**\n\n"
            "● **Функционал:** Сбор вакансий по заданным ключевым словам и зарплате.\n"
            "● **Возможности:** Автоматическое удаление дублей, фильтрация сетевого маркетинга, экспорт данных в Google Таблицы.\n"
            "● **Применение:** Идеально для HR-агентств и автоматизации поиска работы."
        ),
        'fuel': (
            "⛽ **Магазин топливных талонов с AI-ассистентом**\n\n"
            "● **AI-технологии:** В бот интегрирован умный помощник на базе GPT. Он отвечает на вопросы клиентов, помогает выбрать тип топлива и рассчитывает выгоду в реальном времени.\n"
            "● **Функционал:** Полный цикл продажи талонов (WOG, OKKO, SOCAR). Автоматический прием платежей (Mono/LiqPay/Crypto).\n"
            "● **Возможности:** Генерация QR-кодов, проверка лимитов, система лояльности и реферальная программа.\n"
            "● **Результат:** Снижение нагрузки на поддержку на 80% за счет AI-консультанта."
        ),
        'nodeshop': (
            "🛍️ **Mini App Shop (Node.js)**\n\n"
            "● **Интерфейс:** Полноценное Web-приложение внутри Telegram (как нативный сайт).\n"
            "● **Возможности:** Плавная анимация, корзина с сохранением товаров, удобный выбор категорий.\n"
            "● **Технологии:** Node.js (Backend), React (Frontend).\n"
            "● **Плюс:** Высокая скорость работы и современный UX/UI."
        ),
        'beauty': (
            "💇 **Service Booking System (Next.js)**\n\n"
            "● **Функционал:** Система онлайн-записи для салонов красоты.\n"
            "● **Возможности:** Выбор мастера и услуги, интерактивный календарь свободных окон, SMS/Telegram напоминания клиентам.\n"
            "● **Админка:** Удобная панель для владельца для управления графиком и базой клиентов.\n"
            "● **Стек:** Next.js, PostgreSQL, Prisma."
        ),
        'dev': (
            "🛠 **В разработке (Лендинги и Сайты)**\n\n"
            "Сейчас мы работаем над созданием высококонверсионных посадочных страниц и корпоративных сайтов.\n"
            "Скоро здесь появятся кейсы с крутым дизайном и чистым кодом!"
        )
    }

    # Создаем кнопку "Открыть", если ссылка есть в списке выше
    current_kb = inv.portfolio # Оставляем основное меню портфолио
    
    if project in links:
        # Создаем временную кнопку для перехода на проект
        link_btn = InlineKeyboardButton(text='🔗 Открыть проект', url=links[project])
        # Генерируем новую клавиатуру: кнопка "Открыть" + старое меню портфолио
        current_kb = InlineKeyboardMarkup(inline_keyboard=[
            [link_btn], 
            *inv.portfolio.inline_keyboard # Распаковываем старые кнопки под новую
        ])

    text = descriptions.get(project, "Описание не найдено")
    
    await callback.message.edit_text(text, reply_markup=current_kb)
    await callback.answer()

# --- ФОРМА ЗАЯВКИ ---
@router.message(F.text == '🚀 Оставить заявку')
async def start_order(message: types.Message, state: FSMContext):
    await state.set_state(Order.description)
    await message.answer("Опишите вашу задачу 📝", reply_markup=types.ReplyKeyboardRemove())

@router.message(Order.description)
async def get_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(Order.budget)
    await message.answer("Ваш бюджет? 💰")

@router.message(Order.budget)
async def get_budget(message: types.Message, state: FSMContext):
    await state.update_data(budget=message.text)
    data = await state.get_data()
    await message.answer("✅ Заявка принята!", reply_markup=kb.main)
    admin_id = os.getenv('ADMIN_ID')
    if admin_id:
        await message.bot.send_message(admin_id, f"🔔 **ЗАЯВКА!**\n\n👤 @{message.from_user.username}\n📝 {data['description']}\n💰 {data['budget']}")
    await state.clear()

# Заглушка для Прайса
@router.message(F.text == '💰 Прайс')
async def price_info(message: types.Message):
    await message.answer("Раздел **Прайс** в разработке. Примерная стоимость бота — от $100. 💵")