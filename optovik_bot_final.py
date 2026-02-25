# ====================================================
# OPTOVIK SHOP BOTI - MUKAMMAL VERSIYA
# ====================================================

import telebot
from telebot import types
import random
import time
import os
from flask import Flask
import threading

# ====================================================
# 1️⃣ BOT TOKENI - @BotFather DAN OLING
# ====================================================
TOKEN = "8645017123:AAF8vaUtvHMaVrqiUs6NeyVf-__w4Sslxjw"
bot = telebot.TeleBot(TOKEN)

# ====================================================
# 2️⃣ ADMIN MA'LUMOTLARI - O'ZINGIZNI YOZING
# ====================================================
ADMIN_ISMI = "Zulhumor"
ADMIN_USERNAME = "@Zulxumor5900"
GURUH_NOMI = "OPTOVIK SHOP"
GURUH_LINKI = "https://t.me/Optovikshop_namangan"
TELEFON_RAQAM = "+998917585900"

# ====================================================
# 3️⃣ CHIROYLI MUROJAATLAR
# ====================================================
murojaatlar = [
    "💗 Hurmatli xonim", "🌺 Aziz xonim", "🌸 Muhtaram xonim", "💖 Qadrli xonim",
    "💝 Mehribon xonim", "🌷 Go'zal xonim", "✨ Dilbar xonim", "🎀 Shirin xonim",
    "💐 Malika xonim", "🌟 Zebo xonim", "🦋 Nozik xonim", "💞 Jonajon xonim"
]

maqtovlar = [
    "💗 Sizning didingiz juda zo'r ekan!", 
    "🌺 Ajoyib tanlov, sizga juda yarashadi!",
    "🌸 Sizga bu mahsulot aynan mos keladi!",
    "💖 Qanday go'zal didingiz bor!",
    "💝 Sizning tanlovingizdan hayratda qoldim!",
    "🌷 Eng yaxshi mahsulotlarni tanlaysiz!",
    "✨ Siz haqiqiy biluvchi ekanligingizni ko'rib turibman!",
    "🎀 Sizga mana shu rang aynan yarashadi!",
    "💐 Qoyil, ajoyib tanlov!",
    "🌟 Siz bilan gaplashish juda yoqimli!"
]

# ====================================================
# 4️⃣ SO'Z LUG'ATLARI
# ====================================================
narx_sozlar = ["narx", "narxi", "qancha", "puli", "so'm", "sum", "narhi", "narxlar", 
               "qancha turadi", "narxi qancha", "puli qancha", "baho", "chegirma", 
               "skidka", "arzon", "qimmat", "turibdi"]

admin_sozlar = ["admin", "boglanish", "bog'lanish", "aloqa", "telefon", "nomer", "raqam", 
                "username", "yordam", "savol", "muammo", "maslahat", "zulhumor", 
                "opa", "bog'lanmoqchi", "murojaat", "qo'ng'iroq"]

salom_sozlar = ["salom", "assalom", "assalomu alaykum", "alaykum assalom", "hayrli kun", 
                "hayrli tong", "hayrli kech"]

narx_javoblari = [
    "💗 Hurmatli xonim, narxlar haqida ma'lumotni faqat Zulhumor opa beradilar. Menga bu haqda gapirishga ruxsat berilmagan. Iltimos, admin bilan bog'laning! 👇",
    "🌸 Kechirasiz, aziz xonim. Narxlar o'zgaruvchan bo'lgani uchun, ularni faqat admin aytishi mumkin. Quyidagi tugma orqali bog'lanishingiz mumkin 👇",
    "✨ Qadrli xonim, mahsulotlarimiz juda sifatli! Ammo aniq narxni Zulhumor opa dan olishingiz kerak. Shu yerga bosing 👇",
    "💖 Go'zal xonim, narxlar haqida so'raganingiz uchun rahmat! Admin sizga eng yaxshi narxni taklif qiladilar. Bog'lanish uchun tugma 👇"
]

# ====================================================
# 5️⃣ /start KOMANDASI
# ====================================================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    maqtov = random.choice(maqtovlar)
    
    salom_matni = f"""
🌸 ASSALOMU ALAYKUM, {ism.upper()}! 🌸

{hurmat}, {GURUH_NOMI} NAMANGAN ga xush kelibsiz!

👩‍💼 Men {ADMIN_ISMI} opaning yordamchi botiman.
Siz bilan tanishganimdan xursandman! {maqtov}

━━━━━━━━━━━━━━━━━━━━━━━━
🏪 MAVJUD MAHSULOTLARIMIZ:
━━━━━━━━━━━━━━━━━━━━━━━━

💄 Kosmetika - yuz kremlari, penka, body loson
👗 Kiyim-kechak - ayollar uchun zamonaviy modellar
🧸 Bolalar mahsulotlari - kiyim va buyumlar
🏠 Uy-ro'zg'or - ko'rpa, choyshab, idishlar
💍 Aksesuarlar - ko'zoynak, sharf, hamyon
📱 Elektronika - quloqchin, powerbank

━━━━━━━━━━━━━━━━━━━━━━━━
📞 ADMIN BILAN BOG'LANISH:
━━━━━━━━━━━━━━━━━━━━━━━━

👩‍💼 Admin: {ADMIN_ISMI} opa
📱 Telefon: {TELEFON_RAQAM}
💬 Telegram: {ADMIN_USERNAME}
🌐 Guruh: {GURUH_LINKI}
━━━━━━━━━━━━━━━━━━━━━━━━

💬 {hurmat}, qanday mahsulot qiziqtiradi? 
Quyidagi tugmalardan birini tanlang 👇
    """
    
    # Tugmalar yaratish
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("💄 Kosmetika")
    btn2 = types.KeyboardButton("👗 Kiyim-kechak")
    btn3 = types.KeyboardButton("🧸 Bolalar uchun")
    btn4 = types.KeyboardButton("🏠 Uy-ro'zg'or")
    btn5 = types.KeyboardButton("💍 Aksesuarlar")
    btn6 = types.KeyboardButton("📱 Elektronika")
    btn7 = types.KeyboardButton("📞 Admin bilan bog'lanish")
    btn8 = types.KeyboardButton("ℹ️ Guruh haqida")
    btn9 = types.KeyboardButton("🌸 Ayollar maslahati")
    btn10 = types.KeyboardButton("❓ Savol-javob")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    
    bot.send_message(message.chat.id, salom_matni, reply_markup=markup)

# ====================================================
# 6️⃣ MAHSULOT TURLARI
# ====================================================
@bot.message_handler(func=lambda message: message.text == "💄 Kosmetika")
def kosmetika(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    matn = f"""
💄 {ism} XONIM, KOSMETIKA MAHSULOTLARIMIZ:

━━━━━━━━━━━━━━━━━━━━━━━━
🧴 Yuz kremi - terini namlaydi, oziqlantiradi
👁️ Ko'z atrofi kremi - shish va qorayishlarni ketkazadi
💆 Body loson - tanani namlaydi, mayin qiladi
🧼 Penka - yuzni tozalaydi, dog'larni ochartiradi
━━━━━━━━━━━━━━━━━━━━━━━━

✨ Barcha mahsulotlar ORIGINAL va SIFATLI!
✨ Namangan shahrida yetkazib berish bepul!

{hurmat}, qaysi mahsulot sizni qiziqtirdi? 
Narxlar va batafsil ma'lumotni admin bilan bog'lanib olasiz 👇
    """
    
    bot.send_message(message.chat.id, matn)
    admin_ga_ulash(message)

@bot.message_handler(func=lambda message: message.text == "👗 Kiyim-kechak")
def kiyim(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    matn = f"""
👗 {ism} XONIM, KIYIM-KECHAKLARIMIZ:

━━━━━━━━━━━━━━━━━━━━━━━━
👚 Ko'ylaklar - turli uslub va ranglarda
👕 Bluzkalar - ofis va kundalik hayot uchun
👖 Shimlar - klassik va sport uslubida
🧥 Kurtkalar - qishki va yozgi modellar
━━━━━━━━━━━━━━━━━━━━━━━━

✨ Barcha o'lchamlar mavjud (S, M, L, XL)!
✨ Sifatli materiallardan tayyorlangan

{hurmat}, o'zingizga yoqqan uslubni tanlang! 
Narxlar va rasmlar uchun admin bilan bog'lanishingiz mumkin 👇
    """
    
    bot.send_message(message.chat.id, matn)
    admin_ga_ulash(message)

@bot.message_handler(func=lambda message: message.text == "🧸 Bolalar uchun")
def bolalar(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    matn = f"""
🧸 {ism} XONIM, BOLALAR UCHUN MAHSULOTLAR:

━━━━━━━━━━━━━━━━━━━━━━━━
👶 Kombinezonlar - 0-6 oylik bolajonlar uchun
👕 Futbolkalar - 2-7 yosh, multfilm qahramonlari bilan
👖 Shimlar - 1-5 yosh, qulay va elastik
👗 Ko'ylaklar - qiz bolalar uchun chiroyli modellar
━━━━━━━━━━━━━━━━━━━━━━━━

👶 Farzandingizga eng yaxshisini tanlang!
✨ Bolalar terisiga mos, yumshoq materiallar

{hurmat}, farzandlaringiz uchun eng yaxshisini xohlaysizmi?
Narxlar va o'lchamlar haqida admin bilan bog'lanishingiz mumkin 👇
    """
    
    bot.send_message(message.chat.id, matn)
    admin_ga_ulash(message)

@bot.message_handler(func=lambda message: message.text == "🏠 Uy-ro'zg'or")
def uy_rozgor(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    matn = f"""
🏠 {ism} XONIM, UY-RO'ZG'OR BUYUMLARI:

━━━━━━━━━━━━━━━━━━━━━━━━
🛏️ Ko'rpalar - turli o'lcham va ranglarda
🛋️ Yostiqlar - ortopedik va oddiy
🧺 Choyshablar - paxta, ipak va atlas
🏺 Idish-tovoqlar - to'plam va alohida
━━━━━━━━━━━━━━━━━━━━━━━━

🏡 Uyingizni obod qiladigan mahsulotlar!
✨ Sifat va qulay narxlar

{hurmat}, uyingizni yanada chiroyli qiling!
Narxlar haqida admin bilan bog'lanishingiz mumkin 👇
    """
    
    bot.send_message(message.chat.id, matn)
    admin_ga_ulash(message)

@bot.message_handler(func=lambda message: message.text == "💍 Aksesuarlar")
def aksesuar(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    matn = f"""
💍 {ism} XONIM, AKSESUARLARIMIZ:

━━━━━━━━━━━━━━━━━━━━━━━━
🕶️ Ko'zoynaklar - quyoshdan saqlaydigan modellar
🧣 Sharflar - turli rang va o'lchamlarda
🧤 Qo'lqoplar - qishki va yozgi
👛 Hamyonlar - ayollar va erkaklar uchun
━━━━━━━━━━━━━━━━━━━━━━━━

✨ Kiyimingizga chiroyli qo'shimchalar!
✨ Har didga mos tanlov

{hurmat}, aksesuarlar sizni yanada go'zal qiladi!
Narxlar va rasmlar uchun admin bilan bog'lanishingiz mumkin 👇
    """
    
    bot.send_message(message.chat.id, matn)
    admin_ga_ulash(message)

@bot.message_handler(func=lambda message: message.text == "📱 Elektronika")
def elektronika(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    matn = f"""
📱 {ism} XONIM, ELEKTRONIKA MAHSULOTLARI:

━━━━━━━━━━━━━━━━━━━━━━━━
🎧 Quloqchinlar - bluetooth va simli
🔋 Powerbank - 10000, 20000 va 30000 mAh
📱 Telefon aksesuarlari - g'ilof, himoya oynasi
🔌 Zaryadlovchi kabellar - turli xil
━━━━━━━━━━━━━━━━━━━━━━━━

✨ Sifatli va ishonchli elektronika
✨ Arzon narxlar, kafolatli mahsulotlar

{hurmat}, zamonaviy texnologiyalardan foydalaning!
Narxlar haqida admin bilan bog'lanishingiz mumkin 👇
    """
    
    bot.send_message(message.chat.id, matn)
    admin_ga_ulash(message)

# ====================================================
# 7️⃣ GURUH HAQIDA
# ====================================================
@bot.message_handler(func=lambda message: message.text == "ℹ️ Guruh haqida")
def guruh_haqida(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    matn = f"""
ℹ️ {GURUH_NOMI} NAMANGAN HAQIDA

━━━━━━━━━━━━━━━━━━━━━━━━
👩‍💼 Admin: {ADMIN_ISMI} opa
📱 Telefon: {TELEFON_RAQAM}
💬 Telegram: {ADMIN_USERNAME}
📍 Shahar: Namangan
━━━━━━━━━━━━━━━━━━━━━━━━

🌟 MAHSULOT TURLARI:

💄 Kosmetika - yuz kremlari, penka, body loson
👗 Kiyim-kechak - ayollar uchun turli modellar
🧸 Bolalar mahsulotlari - kiyim va buyumlar
🏠 Uy-ro'zg'or - ko'rpa, choyshab, idishlar
💍 Aksesuarlar - ko'zoynak, sharf, hamyon
📱 Elektronika - quloqchin, powerbank

━━━━━━━━━━━━━━━━━━━━━━━━
✅ 100% SIFAT KAFOLATI
✅ ENG QULAY NARXLAR
✅ NAMANGAN BO'YLAB YETKAZIB BERISH
━━━━━━━━━━━━━━━━━━━━━━━━

🌐 Guruhga a'zo bo'ling: {GURUH_LINKI}

{hurmat}, savollar bo'lsa, bemalol murojaat qiling! 🤗
    """
    
    bot.send_message(message.chat.id, matn)
    admin_ga_ulash(message)

# ====================================================
# 8️⃣ AYOLLAR MASLAHATI
# ====================================================
@bot.message_handler(func=lambda message: message.text == "🌸 Ayollar maslahati")
def ayollar_maslahati(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    maslahatlar = [
        "Bilingki, har bir ayol go'zal va o'ziga xos! 🌸",
        "Teringizga g'amxo'rlik qilish - o'zingizga bo'lgan hurmat 💝",
        "Chiroyli kiyim kayfiyatingizni ko'taradi! 👗",
        "O'zingizni seving, o'zingizni qadrlang! 💖",
        "Har bir ona farzandlari bilan faxrlanadi! 👩‍👧",
        "Ayol kishi uyning ko'rki, oilaning ziynati! 🏡",
        "Tabassum sizga juda yarashadi! 😊",
        "Siz kuchlisiz, siz go'zalsiz, siz bebahosiz! 💎"
    ]
    
    maslahat = random.choice(maslahatlar)
    
    matn = f"""
🌸 {ism} XONIM, SIZGA MAXSUS MASLAHAT:

✨ {maslahat}

{hurmat}, o'zingizni asrang va seving! 
Siz dunyodagi eng go'zal ayollardan birisiz! 💝

Yana maslahat kerak bo'lsa, shu tugmani yana bosing!
    """
    
    bot.send_message(message.chat.id, matn)

# ====================================================
# 9️⃣ SAVOL-JAVOB
# ====================================================
@bot.message_handler(func=lambda message: message.text == "❓ Savol-javob")
def savol_javob(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    matn = f"""
❓ {ism} XONIM, SIZGA QANDAY YORDAM BERA OLAMAN?

━━━━━━━━━━━━━━━━━━━━━━━━
📌 TEZ-TEZ SO'RALADIGAN SAVOLLAR:
━━━━━━━━━━━━━━━━━━━━━━━━

🔹 Mahsulotlar qayerda ishlab chiqarilgan?
   → Xitoy, Turkiya va Koreya (sifatli!)

🔹 Yetkazib berish bormi?
   → Ha, Namangan shahri bo'ylab yetkazib berish BEPUL

🔹 To'lov qanday amalga oshiriladi?
   → Naqd, plastik karta yoki pul o'tkazmasi

🔹 Mahsulotni qaytarish mumkinmi?
   → Ha, nuqsoni bo'lsa 7 kun ichida almashtiramiz

🔹 Narxlar haqida qayerdan bilsam bo'ladi?
   → Narxlar uchun admin bilan bog'lanishingiz kerak

━━━━━━━━━━━━━━━━━━━━━━━━
📞 Boshqa savollar bo'lsa, admin bilan bog'lanishingiz mumkin
━━━━━━━━━━━━━━━━━━━━━━━━
    """
    
    bot.send_message(message.chat.id, matn)
    admin_ga_ulash(message)

# ====================================================
# 🔟 ADMIN BILAN BOG'LANISH TUGMASI
# ====================================================
@bot.message_handler(func=lambda message: message.text == "📞 Admin bilan bog'lanish")
def admin_bilan_boglanish(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    # INLINE TUGMALAR - TO'G'RI YOZILGAN
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("📞 Admin bilan bog'lanish", url=f"https://t.me/{ADMIN_USERNAME[1:]}")
    btn2 = types.InlineKeyboardButton("📱 Telefon raqam", callback_data="show_phone")
    btn3 = types.InlineKeyboardButton("🌐 Guruhga kirish", url=GURUH_LINKI)
    markup.add(btn1, btn2, btn3)
    
    matn = f"""
📞 {ism} XONIM, ADMIN BILAN BOG'LANISH:

━━━━━━━━━━━━━━━━━━━━━━━━
👩‍💼 Admin: {ADMIN_ISMI} opa
📱 Telefon: {TELEFON_RAQAM}
💬 Telegram: {ADMIN_USERNAME}
━━━━━━━━━━━━━━━━━━━━━━━━

{hurmat}, quyidagi tugmalardan birini tanlang 👇
    """
    
    bot.send_message(message.chat.id, matn, reply_markup=markup)

# ====================================================
# 1️⃣1️⃣ INLINE TUGMALAR UCHUN
# ====================================================
@bot.callback_query_handler(func=lambda call: True)
def inline_buttons(call):
    hurmat = random.choice(murojaatlar)
    
    if call.data == "show_phone":
        matn = f"""
📱 ADMIN TELEFON RAQAMI:

{TELEFON_RAQAM}

💬 Telegram: {ADMIN_USERNAME}

{hurmat}, qo'ng'iroq qilishingiz yoki Telegramdan yozishingiz mumkin!
        """
        bot.send_message(call.message.chat.id, matn)

# ====================================================
# 1️⃣2️⃣ NARX SO'RAGANDA
# ====================================================
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in narx_sozlar))
def narx_sorash(message):
    maqtov = random.choice(maqtovlar)
    bot.send_message(message.chat.id, maqtov)
    
    time.sleep(1)
    
    javob = random.choice(narx_javoblari)
    bot.reply_to(message, javob)
    
    admin_ga_ulash(message)

# ====================================================
# 1️⃣3️⃣ ADMIN SO'RAGANDA
# ====================================================
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in admin_sozlar))
def admin_sozlaganda(message):
    javob = random.choice([
        f"{ADMIN_ISMI} opa bilan bog'lanmoqchimisiz? 👇",
        "Admin bilan bog'lanish uchun quyidagi tugmani bosing 👇"
    ])
    bot.reply_to(message, javob)
    admin_ga_ulash(message)

# ====================================================
# 1️⃣4️⃣ SALOMLASHISH
# ====================================================
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in salom_sozlar))
def salom_javob(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    javoblar = [
        f"Va alaykum assalom, {hurmat} {ism}! Sizni ko'rganimdan xursandman! 😊 Qanday mahsulot qiziqtiradi?",
        f"Assalomu alaykum, {ism} xonim! {GURUH_NOMI} ga xush kelibsiz! Qanday yordam kerak?",
        f"Hayrli kun {ism} xonim! Sizni ko'rganimdan xursandman! Bugun sizga qanday yordam bera olaman? 🌸"
    ]
    bot.reply_to(message, random.choice(javoblar))

# ====================================================
# 1️⃣5️⃣ ADMINGA YO'NALTIRISH FUNKSIYASI
# ====================================================
def admin_ga_ulash(message):
    hurmat = random.choice(murojaatlar)
    
    javoblar = [
        f"{hurmat}, quyidagi tugma orqali {ADMIN_ISMI} opa bilan bog'lanishingiz mumkin 👇",
        f"Barcha savollaringizga {ADMIN_ISMI} opa javob beradi. Shu tugmani bosing 👇"
    ]
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(f"📞 {ADMIN_ISMI} opaga yozish", url=f"https://t.me/{ADMIN_USERNAME[1:]}")
    btn2 = types.InlineKeyboardButton("📱 Telefon raqam", callback_data="show_phone")
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id, random.choice(javoblar), reply_markup=markup)

# ====================================================
# 1️⃣6️⃣ GRUP XABARLARI
# ====================================================
@bot.message_handler(func=lambda message: message.chat.type in ['group', 'supergroup'])
def group_messages(message):
    text = message.text.lower() if message.text else ""
    
    # Botni tagiga yozishsa
    if message.text and f"@{bot.get_me().username}" in message.text:
        javob = random.choice([
            "Ha, men shu yerdaman! Qanday yordam kerak? 🤗",
            f"{ADMIN_ISMI} opaga murojaat qilmoqchimisiz? 👇"
        ])
        bot.reply_to(message, javob)
        admin_ga_ulash(message)
    
    # Narx so'ralgan bo'lsa
    elif any(soz in text for soz in narx_sozlar):
        javob = random.choice(narx_javoblari)
        bot.reply_to(message, javob)
        admin_ga_ulash(message)
    
    # Admin so'ralgan bo'lsa
    elif any(soz in text for soz in admin_sozlar):
        javob = random.choice([
            f"{ADMIN_ISMI} opa bilan bog'lanmoqchimisiz? 👇",
            "Admin bilan bog'lanish uchun quyidagi tugmani bosing 👇"
        ])
        bot.reply_to(message, javob)
        admin_ga_ulash(message)

# ====================================================
# 1️⃣7️⃣ BOSHQA XABARLAR (TUSHUNMAGANDA)
# ====================================================
@bot.message_handler(func=lambda message: True)
def boshqa_javob(message):
    ism = message.from_user.first_name
    hurmat = random.choice(murojaatlar)
    
    if random.random() > 0.5:
        maqtov = random.choice(maqtovlar)
        bot.send_message(message.chat.id, maqtov)
        time.sleep(1)
    
    javoblar = [
        f"{hurmat}, sizni to'liq tushunolmadim. Iltimos, yana bir bor yozib ko'ring yoki {ADMIN_ISMI} opaga murojaat qiling! 👇",
        f"Kechirasiz, {hurmat}. Savolingizni aniq tushunolmadim. Quyidagi tugma orqali admin bilan bog'lanishingiz mumkin 👇"
    ]
    
    bot.reply_to(message, random.choice(javoblar))
    admin_ga_ulash(message)

# ====================================================
# 1️⃣8️⃣ RENDER UCHUN
# ====================================================
app = Flask(__name__)

@app.route('/')
def home():
    return f"🌸 {GURUH_NOMI} BOTI ISHLAYAPTI! 🌸"

@app.route('/health')
def health():
    return "OK", 200

def run_flask():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# Flask-ni alohida threadda ishga tushirish
threading.Thread(target=run_flask).start()

# ====================================================
# 1️⃣9️⃣ BOTNI ISHGA TUSHIRISH
# ====================================================
print("=" * 70)
print(f"🌸 {GURUH_NOMI} BOTI ISHGA TUSHDI! 🌸")
print("=" * 70)
print(f"👩‍💼 Admin: {ADMIN_ISMI} {ADMIN_USERNAME}")
print(f"📞 Telefon: {TELEFON_RAQAM}")
print("=" * 70)
print("✅ HATOSIZ VERSIYA!")
print("✅ Narxlar FAQAT admin orqali!")
print("✅ Gruhda ishlaydi!")
print("=" * 70)

# Botni ishga tushirish
if __name__ == "__main__":
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"Xatolik: {e}")
        time.sleep(5)
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
