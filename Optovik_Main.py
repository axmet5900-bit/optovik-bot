import telebot
from telebot import types
import sqlite3
import re
import google.generativeai as genai
from flask import Flask
import threading
import os

# ====================================================
# 1. SOZLAMALAR
# ====================================================
TOKEN = "8645017123:AAF8vaUtvHMaVrqiUs6NeyVf-__w4Sslxjw"
GEMINI_API_KEY = "SIZNING_TOLIQ_API_KEYINGIZ" # O'sha ...bTWQ bilan tugaydigan kalit

bot = telebot.TeleBot(TOKEN)
genai.configure(api_key=GEMINI_API_KEY)
ai_model = genai.GenerativeModel('gemini-pro')

SHOP_INFO = {
    "admin_ismi": "Zulhumor",
    "username": "@Zulxumor5900",
    "tel": "+998917585900",
    "nomi": "OPTOVIK SHOP NAMANGAN"
}

# ====================================================
# 2. BAZA BILAN ISHLASH
# ====================================================
def init_db():
    conn = sqlite3.connect('shop_data.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stats 
                 (user_id INTEGER PRIMARY KEY, name TEXT, count INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

def update_user_count(user_id, name, add_count):
    conn = sqlite3.connect('shop_data.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO stats (user_id, name, count) VALUES (?, ?, 0)", (user_id, name))
    c.execute("UPDATE stats SET count = count + ?, name = ? WHERE user_id = ?", (add_count, name, user_id))
    conn.commit()
    conn.close()

# ====================================================
# 3. AQLLI AI YORDAMCHI (PROMPT)
# ====================================================
def get_ai_response(text, user_name):
    prompt = f"""
    Sen {SHOP_INFO['nomi']} do'konining yordamchisisan. Admin - {SHOP_INFO['admin_ismi']} opa.
    Mijoz ismi: {user_name}.
    
    SENING XARAKTERING:
    1. O'ta muloyim, xushmuomala va samimiy Namanganlik yordamchi qizsan.
    2. Mijozlarga 'asalkinam', 'go'zalim', 'xonimjon' deb murojaat qil.
    3. Hech qachon 'tushunmadim' yoki 'robotman' dema.
    4. Namangan bo'ylab dostavka tekin va tezligini maqta (24 soatda!).
    5. Agar narx so'rashsa, {SHOP_INFO['username']} ga yo'naltir, lekin buni ham shirin gap bilan ayt.
    6. Har bir xabarda kamida 3-4 ta emoji ishlat (🌸, ✨, 💄,🛍).
    """
    try:
        response = ai_model.generate_content(f"{prompt}\nMijoz: {text}")
        return response.text
    except:
        return f"Assalomu alaykum {user_name} xonim! Zulhumor opamiz hozirgina sizga javob beradilar, birozgina kutib turing asalkinam. 🌸"

# ====================================================
# 4. KLAVIATURA
# ====================================================
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("💄 Katalog", "🚚 Dostavka")
    markup.add("📊 Mening natijam", "🏆 Top faollar")
    markup.add("📞 Admin bilan aloqa")
    return markup

# ====================================================
# 5. ASOSIY HANDLERLAR
# ====================================================

@bot.message_handler(commands=['start'])
def start(message):
    init_db()
    text = f"Assalomu alaykum, {message.from_user.first_name} go'zalim! ✨\n{SHOP_INFO['nomi']}ga xush kelibsiz! Sizga qanday yordam bera olaman? 🌸"
    bot.send_message(message.chat.id, text, reply_markup=main_menu())

@bot.message_handler(content_types=['new_chat_members'])
def member_added(message):
    inviter = message.from_user
    for member in message.new_chat_members:
        if inviter.id != member.id:
            update_user_count(inviter.id, inviter.first_name, 1)
            bot.send_message(message.chat.id, f"🌟 Barakalla {inviter.first_name} xonim! Guruhga yangi dugonamizni qo'shdingiz. Sovg'alarga yaqinlashyapsiz! 🎁")

@bot.message_handler(func=lambda m: True)
def chat_handler(message):
    # Reklama filtri
    if message.chat.type in ['group', 'supergroup']:
        if re.search(r'http[s]?://|t\.me/|@', message.text or ""):
            status = bot.get_chat_member(message.chat.id, message.from_user.id).status
            if status not in ['creator', 'administrator']:
                bot.delete_message(message.chat.id, message.message_id)
                return

    # AI Javobi (Faqat shaxsiyda yoki botga murojaat bo'lsa)
    if message.chat.type == "private" or f"@{bot.get_me().username}" in (message.text or ""):
        bot.send_chat_action(message.chat.id, 'typing')
        response = get_ai_response(message.text, message.from_user.first_name)
        bot.reply_to(message, response)

# ====================================================
# 6. SERVER
# ====================================================
app = Flask(__name__)
@app.route('/')
def home(): return "Bot Online ✨"

if __name__ == "__main__":
    init_db()
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000)).start()
    bot.infinity_polling()
