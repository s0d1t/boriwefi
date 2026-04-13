from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards import get_main_menu, get_back_menu

router = Router()

# --- Тексты инструкций ---

TEXT_SETUP = """
➕ <b>Как добавить бота-модератора в группу:</b>

1️⃣ Добавьте бота (которого вы создаете для модерации) в вашу группу.
2️⃣ Зайдите в настройки группы -> Администраторы.
3️⃣ Найдите бота и назначьте его администратором.
4️⃣ <b>Обязательно выдайте права:</b>
   • Бан пользователей
   • Удаление сообщений
   • Закрепление сообщений (опционально)

После этого бот сможет выполнять команды, описанные ниже!
"""

TEXT_ROLES = """
👮 <b>Уровни доступа и возможности:</b>

🔹 <b>МОДЕРАТОР</b>
<i>Доступные команды:</i>
• <code>/mute</code> — замутить пользователя (ограничить право писать).
• <code>/info</code> — получить краткую информацию о юзере.

🔸 <b>АДМИНИСТРАТОР</b>
<i>Все команды Модератора +</i>
• <code>/ban</code> — забанить пользователя навсегда.
• <code>/warn</code> — выдать предупреждение. 
  ⚠️ <i>3 предупреждения = автоматический кик/бан.</i>
• <code>/history</code> — посмотреть историю нарушений юзера.

👑 <b>ВЛАДЕЛЕЦ</b>
• Полный доступ ко всем командам.
• Настройка фильтров (ссылки, мат).
• Назначение и снятие Модераторов/Админов.
"""

TEXT_COMMANDS = """
🛡️ <b>Шпаргалка по командам (писать в чате):</b>

<code>/warn @user причина</code> — Выдать предупреждение.
<code>/ban @user причина</code> — Забанить пользователя.
<code>/mute @user 1h причина</code> — Замутить (1h - час, 10m - мин).
<code>/info @user</code> — Карточка пользователя (варны/статус).
<code>/history @user</code> — История всех наказаний.

<i>💡 Совет: Для удобства можно отвечать командой на сообщение нарушителя.</i>
"""

TEXT_FAQ = """
❓ <b>Частые вопросы:</b>

<b>П: Бот не реагирует на команды в чате!</b>
О: Убедитесь, что бот добавлен в администраторы группы с правами на бан и удаление сообщений.

<b>П: Как изменить список запрещенных слов?</b>
О: Это может сделать только Владелец через специальные команды настройки (в разработке).

<b>П: Можно ли разбанить пользователя?</b>
О: Да, это можно сделать через стандартное меню Telegram (правой кнопкой по юзеру -> Разбанить).
"""

# --- Обработчики ---

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 <b>Привет! Я помощник администратора.</b>\n\n"
        "Здесь ты найдешь инструкции по настройке и использованию бота-модератора.\n"
        "Выбери раздел:",
        reply_markup=get_main_menu(),
        parse_mode="HTML"
    )

@router.callback_query(F.data == "start")
async def callback_start(callback: CallbackQuery):
    await callback.message.edit_text(
        "👋 <b>Привет! Я помощник администратора.</b>\n\n"
        "Здесь ты найдешь инструкции по настройке и использованию бота-модератора.\n"
        "Выбери раздел:",
        reply_markup=get_main_menu(),
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "guide_setup")
async def callback_setup(callback: CallbackQuery):
    await callback.message.edit_text(
        TEXT_SETUP,
        reply_markup=get_back_menu(),
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "guide_roles")
async def callback_roles(callback: CallbackQuery):
    await callback.message.edit_text(
        TEXT_ROLES,
        reply_markup=get_back_menu(),
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "guide_commands")
async def callback_commands(callback: CallbackQuery):
    await callback.message.edit_text(
        TEXT_COMMANDS,
        reply_markup=get_back_menu(),
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "guide_faq")
async def callback_faq(callback: CallbackQuery):
    await callback.message.edit_text(
        TEXT_FAQ,
        reply_markup=get_back_menu(),
        parse_mode="HTML"
    )
    await callback.answer()