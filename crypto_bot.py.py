from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import logging
# flake8: noqa

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен Telegram
TOKEN = '7677377155:AAGBKSjEErriozRHxoCyWd69XNn5STa-Wj8'  # <-- ВСТАВЬ СВОЙ ТОКЕН

# Сообщения на двух языках
MESSAGES = {
    "ru": {
        "welcome": "🌍 Выберите язык:\n🇷🇺 Русский — /ru\n🇺🇦 Українский — /ua",
        "menu": "Выберите, что вас интересует:",
        "about": """
🚀 Добро пожаловать!

Мы делимся настоящими, проверенными инсайдами крипторынка. 🔐
Наша команда — это опытные трейдеры и аналитики, которые прошли путь от новичков до профессионалов. 📊

Если ты хочешь узнать, как зарабатывать на крипте осознанно — ты по адресу. 💡
""",
        "payment": """
🔥 Наш путь — это знания, практика и победы. И теперь мы готовы передать этот опыт вам.

Мы верим, что крипта — это возможность изменить свою жизнь. С нами ты получишь доступ к стратегиям, которые действительно работают. 🚀
""",
        "contacts": """
📩 Для подписки и оплаты:

👉 Напишите в Telegram: @Wasabi9876  
Мы подскажем и поможем на каждом этапе!
"""
    },
    "ua": {
        "welcome": "🌍 Оберіть мову:\n🇷🇺 Російська — /ru\n🇺🇦 Українська — /ua",
        "menu": "Оберіть, що вас цікавить:",
        "about": """
🚀 Ласкаво просимо!

Ми ділимося справжніми, перевіреними інсайдами крипторинку. 🔐
Наша команда — це досвідчені трейдери й аналітики, які пройшли шлях від новачків до професіоналів. 📊

Якщо ти хочеш дізнатися, як заробляти на крипті свідомо — ти за адресою. 💡
""",
        "payment": """
🔥 Наш шлях — це знання, практика і перемоги. І тепер ми готові передати цей досвід вам.

Ми віримо, що крипта — це можливість змінити своє життя. З нами ти отримаєш доступ до стратегій, які справді працюють. 🚀
""",
        "contacts": """
📩 Для підписки та оплати:

👉 Напишіть у Telegram: @Wasabi9876  
Ми підкажемо та допоможемо на кожному етапі!
"""
    }
}

# Кнопки
keyboard = [
    [KeyboardButton("📖 Про нас"), KeyboardButton("💰 Умови")],
    [KeyboardButton("📩 Контакти")]
]

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(MESSAGES["ru"]["welcome"])

# /ru и /ua
async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = update.message.text[1:].lower()
    if lang in MESSAGES:
        context.user_data["lang"] = lang
        await update.message.reply_text(
            MESSAGES[lang]["menu"],
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )
    else:
        await update.message.reply_text("Неверный выбор. Используйте /ru или /ua.")

# Обработка кнопок
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = context.user_data.get("lang", "ru")
    text = update.message.text

    if text == "📖 О нас":
        await update.message.reply_text(MESSAGES[lang]["about"])
    elif text == "💰 Условия":
        await update.message.reply_text(MESSAGES[lang]["payment"])
    elif text == "📩 Контакты":
        await update.message.reply_text(MESSAGES[lang]["contacts"])
    else:
        await update.message.reply_text("Выберите вариант из меню.")

# Главная функция
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ru", set_language))
    app.add_handler(CommandHandler("ua", set_language))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
