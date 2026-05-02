import os
import telebot
from google import genai

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_KEY = os.environ.get("GEMINI_KEY")

client = genai.Client(api_key=GEMINI_KEY)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda m: True)
def handle(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=message.text
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

bot.polling()