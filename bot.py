import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🌟 Welcome to MotivateMe Quotes! 🌟\n\n"
        "💪 Your daily source of motivation, inspiration, and positive energy.\n\n"
        "✨ Stay inspired.\n"
        "🚀 Keep growing.\n\n"
        "Use /quote to get a motivational quote!"
    )


@bot.message_handler(commands=["quote"])
def quote(message):
    bot.reply_to(
        message,
        "🔥 Believe in yourself. Every small step you take today "
        "brings you closer to the person you want to become. 💪"
    )


@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "🤖 MotivateMe Quotes\n\n"
        "/start - Start the bot\n"
        "/quote - Get a motivational quote\n"
        "/help - Show this help message"
    )


print("MotivateMe Quotes bot is running...")

bot.infinity_polling()
