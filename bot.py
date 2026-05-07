import os
import telebot
from openai import OpenAI

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENROUTER_KEY = os.environ.get("OPENROUTER_KEY")

client = OpenAI(
    api_key=OPENROUTER_KEY,
    base_url="https://openrouter.ai/api/v1"
)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda m: True)
def handle(message):
    try:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=[{"role": "user", "content": message.text}]
        )
        reply = response.choices[0].message.content
        if reply and reply.strip():
            bot.reply_to(message, reply)
        else:
            bot.reply_to(message, "Попробуйте ещё раз.")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")
bot.polling()