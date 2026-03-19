from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import app.keyboards.reply as kb

router = Router()

# Создаем состояния для анкеты
class Order(StatesGroup):
    description = State()  # Описание задачи
    budget = State()       # Бюджет

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Добро пожаловать в **Elvita Studio**, {message.from_user.first_name}! 🚀\n\n"
        "Выберите нужный раздел в меню ниже 👇",
        reply_markup=kb.main
    )

# --- ЛОГИКА АНКЕТЫ ---

@router.message(F.text == '🚀 Оставить заявку')
async def start_order(message: types.Message, state: FSMContext):
    await state.set_state(Order.description)
    await message.answer("Опишите вкратце вашу задачу: что именно нужно разработать? 📝", 
                         reply_markup=types.ReplyKeyboardRemove()) # Убираем меню на время опроса

@router.message(Order.description)
async def get_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text) # Сохраняем описание
    await state.set_state(Order.budget)
    await message.answer("Ваш примерный бюджет на проект? 💰")

@router.message(Order.budget)
async def get_budget(message: types.Message, state: FSMContext):
    await state.update_data(budget=message.text)
    data = await state.get_data()
    
    # 1. Отвечаем клиенту
    await message.answer(
        "✅ **Заявка принята!**\n\n"
        "Наш менеджер свяжется с вами в ближайшее время. Спасибо!",
        reply_markup=kb.main
    )
    
    # 2. Отправляем уведомление ТЕБЕ (админу)
    admin_id = os.getenv('ADMIN_ID')
    if admin_id:
        await message.bot.send_message(
            chat_id=admin_id,
            text=f"🔔 **НОВАЯ ЗАЯВКА!**\n\n"
                 f"👤 **От кого:** @{message.from_user.username or 'скрыт'}\n"
                 f"📝 **Задача:** {data['description']}\n"
                 f"💰 **Бюджет:** {data['budget']}"
        )
    
    await state.clear()