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
# Rasmingizdagi AIzaSy...bTWQ kalitini shu yerga qo'ying:
GEMINI_API_KEY = "SIZNING_API_KALITINGIZ" 

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
# 2. BAZA BILAN ISHLASH (Yaxshilangan)
# ====================================================
def init_db():
    with sqlite3.connect('shop_data.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS stats 
                     (user_id INTEGER PRIMARY KEY, name TEXT, count INTEGER DEFAULT 0)''')
        conn.commit()

def update_user_count(user_id, name, add_count):
    with sqlite3.connect('shop_data.db') as conn:
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO stats (user_id, name, count) VALUES (?, ?, 0)", (user_id, name))
        c.execute("UPDATE stats SET count = count + ?, name = ? WHERE user_id = ?", (add_count, name, user_id))
        conn.commit()

# ====================================================
# 3. AQLLI AI YORDAMCHI
# ====================================================
def get_ai_response(text, user_name):
    prompt = f"""
    Sen {SHOP_INFO['nomi']} do'konining yordamchisisan. Admin: {SHOP_INFO['admin_ismi']} opa.
    Mijoz ismi: {user_name}. 
    Namanganlik ayollarga xos, o'ta muloyim va shirinso'z bo'l. 
    'Asalkinam', 'go'zalim' deb murojaat qil. Dostavka Namangan bo'ylab tekin.
    Narx so'rashsa {SHOP_INFO['username']} ga yo'naltir.
    Emoji ishlat: 🌸, ✨, 🛍.
    """
    try:
        response = ai_model.generate_content(f"{prompt}\nMijoz: {text}")
        return response.text
    except:
        return f"Assalomu alaykum {user_name} xonim! Hozir biroz bandman, Zulhumor opaga yozib turing asalkinam. 🌸"

# ====================================================
# 4. KLAVIATURA
# ====================================================
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("💄 Katalog", "🚚 Dostavka")
    markup.add("📊 Mening natijam", "📞 Admin bilan aloqa")
    return markup

# ====================================================
# 5. HANDLERLAR
# ====================================================

@bot.message_handler(commands=['start'])
def start(message):
    init_db()
    text = f"Xush kelibsiz {message.from_user.first_name} go'zalim! ✨\nSizga qanday yordam bera olaman? 🌸"
    bot.send_message(message.chat.id, text, reply_markup=main_menu())

@bot.message_handler(content_types=['new_chat_members'])
def member_added(message):
    inviter = message.from_user
    for member in message.new_chat_members:
        if inviter.id != member.id:
            update_user_count(inviter.id, inviter.first_name, 1)
            bot.send_message(message.chat.id, f"🌟 Barakalla {inviter.first_name}! Dugonangizni qo'shib, sovg'aga yaqinlashyapsiz! 🎁")

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
    is_private = message.chat.type == "private"
    is_mentioned = f"@{bot.get_me().username}" in (message.text or "")
    
    if is_private or is_mentioned:
        bot.send_chat_action(message.chat.id, 'typing')
        clean_text = message.text.replace(f"@{bot.get_me().username}", "").strip()
        response = get_ai_response(clean_text, message.from_user.first_name)
        bot.reply_to(message, response)

# ====================================================
# 6. SERVER (Render uchun optimallashgan)
# ====================================================
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive! ✨"

def run_flask():
    # Render PORT muhitini avtomatik aniqlaydi
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    init_db()
    # Flaskni alohida thread'da ishga tushiramiz
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()
    # Botni asosiy thread'da ishga tushiramiz
    bot.infinity_polling()
