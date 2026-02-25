import telebot
from telebot import types
import random
import time
import os
import re
import sqlite3
from flask import Flask
import threading
import google.generativeai as genai

# ====================================================
# 1. SOZLAMALAR (TOKEN VA API KALITLAR)
# ====================================================
TOKEN = "8645017123:AAF8vaUtvHMaVrqiUs6NeyVf-__w4Sslxjw"
# Rasmdagi API kalitingizni shu yerga to'liq holda qo'ying:
GEMINI_API_KEY = "SIZ_RASMDA_OLGAN_TOLIQ_API_KEY_SHU_YERGA" 

bot = telebot.TeleBot(TOKEN)

# Gemini AI sozlamasi
genai.configure(api_key=GEMINI_API_KEY)
ai_model = genai.GenerativeModel('gemini-pro')

# Admin va Do'kon ma'lumotlari
SHOP_INFO = {
    "admin_ismi": "Zulhumor",
    "username": "@Zulxumor5900",
    "guruh_linki": "https://t.me/Optovikshop_namangan",
    "tel": "+998917585900",
    "nomi": "OPTOVIK SHOP NAMANGAN"
}

# ====================================================
# 2. MA'LUMOTLAR BAZASI (SQLITE)
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

def get_user_stats(user_id):
    conn = sqlite3.connect('shop_data.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT count FROM stats WHERE user_id = ?", (user_id,))
    res = c.fetchone()
    conn.close()
    return res[0] if res else 0

def get_top_users():
    conn = sqlite3.connect('shop_data.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT name, count FROM stats WHERE count > 0 ORDER BY count DESC LIMIT 10")
    res = c.fetchall()
    conn.close()
    return res

# ====================================================
# 3. YORDAMCHI FUNKSIYALAR
# ====================================================
def get_ai_response(text, user_name):
    prompt = f"""
    Sen {SHOP_INFO['nomi']} yordamchisisan. Admin: {SHOP_INFO['admin_ismi']} opa.
    Mijoz ismi: {user_name}. 
    Qoidalar: 
    1. O'zbek tilida, ayollarga xos juda muloyim gapir. 
    2. Narx so'rashsa, {SHOP_INFO['username']} ga murojaat qilishni ayt. 
    3. Namangan bo'ylab dostavka xizmati juda tezligini ta'kidla.
    """
    try:
        response = ai_model.generate_content(f"{prompt}\nMijoz: {text}")
        return response.text
    except:
        return f"Assalomu alaykum {user_name} xonim! Hozir biroz bandman, savolingizni Zulhumor opaga yozib turing. 🌸"

LINK_PATTERN = r'http[s]?://|t\.me/|@'

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("💄 Katalog", "🚚 Dostavka")
    markup.add("📊 Mening natijam", "🏆 Top faollar")
    markup.add("📝 Buyurtma berish", "📞 Admin bilan aloqa")
    return markup

# ====================================================
# 4. BOT HANDLERLARI (MANTIQ)
# ====================================================

@bot.message_handler(commands=['start'])
def start_cmd(message):
    init_db()
    bot.send_message(message.chat.id, f"Assalomu alaykum! 🌸\n{SHOP_INFO['nomi']} botiga xush kelibsiz!", reply_markup=main_menu())

@bot.message_handler(content_types=['new_chat_members'])
def member_added(message):
    inviter = message.from_user
    for member in message.new_chat_members:
        if inviter.id != member.id:
            update_user_count(inviter.id, inviter.first_name, 1)
            count = get_user_stats(inviter.id)
            bot.send_message(message.chat.id, f"🌟 Rahmat {inviter.first_name}! Siz guruhga {member.first_name}ni qo'shdingiz. Jami natijangiz: {count} ta. 🎁")
        else:
            bot.send_message(message.chat.id, f"Xush kelibsiz! 🌸 Biz bilan go'zallik olamiga sho'ng'ing!")

@bot.message_handler(func=lambda m: m.text == "📊 Mening natijam")
def show_my_stats(message):
    count = get_user_stats(message.from_user.id)
    bot.reply_to(message, f"📊 Siz qo'shgan a'zolar soni: **{count} ta**. Faollik uchun rahmat! ✨")

@bot.message_handler(func=lambda m: m.text == "🏆 Top faollar")
def show_leaderboard(message):
    tops = get_top_users()
    if not tops:
        bot.send_message(message.chat.id, "Hozircha faollar ro'yxati bo'sh.")
        return
    msg = "🏆 **ENG KO'P ODAM QO'SHGAN FAOL XONIMLAR:**\n\n"
    for i, (name, count) in enumerate(tops, 1):
        msg += f"{i}. {name} — {count} ta a'zo\n"
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda m: m.text == "🚚 Dostavka")
def delivery_info(message):
    bot.send_message(message.chat.id, "🚚 Namangan shahar ichida dostavka tekin! Tumanlarga kelishilgan holda tezda yetkazamiz. ✨")

@bot.message_handler(func=lambda m: m.text == "📞 Admin bilan aloqa")
def admin_contact(message):
    bot.send_message(message.chat.id, f"👩‍💼 Admin: {SHOP_INFO['admin_ismi']} opa\n✈️ Telegram: {SHOP_INFO['username']}\n📞 Tel: {SHOP_INFO['tel']}")

@bot.message_handler(func=lambda m: True)
def main_handler(message):
    # Reklama o'chiruvchi filtr
    if message.chat.type in ['group', 'supergroup']:
        if re.search(LINK_PATTERN, message.text or ""):
            status = bot.get_chat_member(message.chat.id, message.from_user.id).status
            if status not in ['creator', 'administrator']:
                bot.delete_message(message.chat.id, message.message_id)
                return

    # Gemini AI javobi
    if message.chat.type == "private" or f"@{bot.get_me().username}" in (message.text or ""):
        bot.send_chat_action(message.chat.id, 'typing')
        ai_msg = get_ai_response(message.text, message.from_user.first_name)
        bot.reply_to(message, ai_msg)

# ====================================================
# 5. SERVER (RENDER/HEROKU UCHUN)
# ====================================================
app = Flask(__name__)
@app.route('/')
def index(): return "Bot ishlamoqda..."

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

if __name__ == "__main__":
    init_db()
    threading.Thread(target=run_flask).start()
    print("Bot Namangan vaqti bilan ishga tushdi! 🚀")
    bot.infinity_polling()
