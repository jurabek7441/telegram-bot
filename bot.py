import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = "8526653860:AAEX8ROTNpbRnFVYHiD9_yROP2DZtp27Hpg"
GEMINI_KEY = "AIzaSyD6Kxtb2JH6Z99Q-ewjS--5CnHQ1I5r0eQ"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-3-flash-preview")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda m: True)
def handle(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

bot.polling()