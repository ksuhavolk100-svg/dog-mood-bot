import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8787353448:AAHsnVDbN6B6IB_aVkuKdeeF-Jy9c1ym3uw"

moods = {
    "sad": ["sad1.gif", "sad2.gif", "sad3.gif"],
    "tired": ["tired1.gif", "tired2.gif"],
    "angry": ["angry1.gif", "angry2.gif"],
    "happy": ["happy1.gif", "happy2.gif", "happy3.gif"],
    "anxious": ["anxious1.gif", "anxious2.gif"]
}

async def handle_mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    sad_words = [
        "груст", "печаль", "плохо", "одинок", "плак", "слез",
        "тоск", "обид", "разбит", "уныл"
    ]

    tired_words = [
        "устал", "устала", "устало", "выгор", "нет сил", "измот",
        "спать", "сон", "вымот", "задолбал"
    ]

    angry_words = [
        "злю", "злость", "бесит", "раздраж", "ненавиж",
        "достал", "достало", "ярость", "кипит"
    ]

    happy_words = [
        "рад", "рада", "счаст", "класс", "кайф", "хорошо",
        "весело", "супер", "ура", "доволь"
    ]

    anxious_words = [
        "тревож", "страш", "боюсь", "пережив", "паник",
        "нерв", "волн", "стресс", "неспокойно"
    ]

    if any(word in text for word in sad_words):
        gif = random.choice(moods["sad"])
        message = "🐶 Собачка говорит: завтра будет лучше."

    elif any(word in text for word in tired_words):
        gif = random.choice(moods["tired"])
        message = "🐶 Срочно требуется сон и вкусняшка."

    elif any(word in text for word in angry_words):
        gif = random.choice(moods["angry"])
        message = "🐶 Одобрено ворчание в течение 15 минут."

    elif any(word in text for word in happy_words):
        gif = random.choice(moods["happy"])
        message = "🐶 Сегодня ты хорошая девочка."

    elif any(word in text for word in anxious_words):
        gif = random.choice(moods["anxious"])
        message = "🐶 Вдох. Выдох. Лапки на землю."

    else:
        gif = random.choice(moods["happy"])
        message = "🐶 Настроение не распознано, но собачка все равно пришла."

    await update.message.reply_text(message)

    with open(gif, "rb") as animation:
        await update.message.reply_animation(animation=animation)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, handle_mood))

print("Bot is running...")
app.run_polling()