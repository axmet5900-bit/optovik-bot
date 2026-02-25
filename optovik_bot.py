import telebot
from telebot import types
import random
import time
import os
from flask import Flask
import threading

# ====================================================
# BOT TOKEN - @BotFather dan olingan
# ====================================================
TOKEN = "8645017123:AAF8vaUtvHMaVrqiUs6NeyVf-__w4Sslxjw"

bot = telebot.TeleBot(TOKEN)

# Admin va guruh ma'lumotlari
ADMIN_ISMI = "Zulhumor"
ADMIN_USERNAME = "@Zulxumor5900"
GURUH_NOMI = "OPTOVIK SHOP"
GURUH_LINKI = "https://t.me/Optovikshop_namangan"
TELEFON_RAQAM = "+998917585900"

# ====================================================
# HURMATLI MUROJAATLAR
# ====================================================
hurmatli_murojaatlar = [
    "Hurmatli xonim", "Aziz xonim", "Muhtaram xonim", "Hurmatli mijoz",
    "Qadrli xonim", "Aziz mijoz", "Muhtaram mijoz", "Hurmatli ayol",
    "Xonim", "Aziza xonim", "Mehribon xonim", "Qadrli ayol"
]

# ====================================================
# SALOMLASHISH
# ====================================================
salomlashish = [
    "salom", "assalom", "assalomu alaykum", "alaykum assalom", "hayrli kun",
    "hayrli tong", "hayrli kech", "xayrli kun", "xayrli tong", "xayrli kech"
]

# ====================================================
# XAYRLASHISH
# ====================================================
xayrlashish = [
    "xayr", "hayr", "xayr xayr", "rahmat", "katta rahmat", "ko'rishguncha", 
    "xayr salomat", "hozircha", "sog' bo'ling", "xayrli tun"
]

# ====================================================
# HOL-AHVOL
# ====================================================
hol_ahvol = [
    "qalay", "qalaysiz", "qanday", "qandaysiz", "yaxshimisiz", "ishlar qalay",
    "ahvollaringiz", "yuribsizmi", "nima gap", "nima yangilik"
]

# ====================================================
# TASHAKKUR
# ====================================================
tashakkur = [
    "rahmat", "tashakkur", "minnatdor", "katta rahmat", "rahmat sizga", 
    "arzimaydi", "minnatdorman"
]

# ====================================================
# ADMIN BILAN BOG'LANISH UCHUN SO'ZLAR
# ====================================================
admin_sozlar = [
    "admin", "boglanish", "bog'lanish", "aloqa", "telefon", "nomer", "raqam",
    "telegram", "username", "yordam", "savol", "muammo", "maslahat", "yozish",
    "gapirish", "murojaat", "zulhumor", "opa", "admin bilan", "bog'lanmoqchi"
]

# ====================================================
# NARX SO'RASH UCHUN SO'ZLAR
# ====================================================
narx_sozlar = [
    "narx", "narxi", "qancha", "puli", "so'm", "sum", "narhi", "narxlar",
    "qancha turadi", "narxi qancha", "puli qancha", "baxo", "baho",
    "chegirma", "skidka", "arzon", "qimmat", "turibdi", "sotiladi"
]

# ====================================================
# /start komandasi
# ====================================================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    salom_matni = f"""
🌸 *ASSALOMU ALAYKUM, {ism.upper()} XONIM!* 🌸

👩‍💼 Men *{ADMIN_ISMI}* opangiz, *{GURUH_NOMI}* guruhining adminiman.
Namangan shahridan barcha ayollarga salom!

🤗 *{hurmat}*, siz bilan tanishganimdan nihoyatda xursandman!

━━━━━━━━━━━━━━━━━━━━━━━━
🏪 *MAVJUD MAHSULOTLARIMIZ:*
━━━━━━━━━━━━━━━━━━━━━━━━

💄 *Kosmetika* - yuz kremlari, penka, body loson
👗 *Kiyim-kechak* - ayollar uchun zamonaviy modellar
🧸 *Bolalar mahsulotlari* - kiyim va buyumlar
🏠 *Uy-ro'zg'or* - ko'rpa, choyshab, idishlar
💍 *Aksesuarlar* - ko'zoynak, sharf, hamyon
📱 *Elektronika* - quloqchin, powerbank

━━━━━━━━━━━━━━━━━━━━━━━━
📞 *ADMIN BILAN BOG'LANISH:*
━━━━━━━━━━━━━━━━━━━━━━━━

👩‍💼 *Admin:* {ADMIN_ISMI} opa
📱 *Telefon:* `{TELEFON_RAQAM}`
💬 *Telegram:* {ADMIN_USERNAME}
🌐 *Guruh:* [OPTOVIK SHOP NAMANGAN]({GURUH_LINKI})
━━━━━━━━━━━━━━━━━━━━━━━━

💬 *{hurmat}, qanday mahsulot qiziqtiradi?* 
Quyidagi tugmalardan birini tanlang 👇
    """
    
    # Asosiy menyu tugmalari
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
    
    bot.send_message(message.chat.id, salom_matni, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup)

# ====================================================
# KOSMETIKA
# ====================================================
@bot.message_handler(func=lambda message: message.text == "💄 Kosmetika")
def kosmetika(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    matn = f"""
💄 *{ism} XONIM, KOSMETIKA MAHSULOTLARIMIZ:*

━━━━━━━━━━━━━━━━━━━━━━━━
🧴 *Yuz kremi* - terini namlaydi, oziqlantiradi
👁️ *Ko'z atrofi kremi* - shish va qorayishlarni ketkazadi
💆 *Body loson* - tanani namlaydi, mayin qiladi
🧼 *Penka* - yuzni tozalaydi, dog'larni ochartiradi
❄️ *Ice Raw Puli* - muz terapiyasi
🌟 *Nabor (to'plam)* - 5 mahsulot birga
━━━━━━━━━━━━━━━━━━━━━━━━

✨ *Barcha mahsulotlar ORIGINAL va SIFATLI!*
✨ *Namangan shahrida yetkazib berish bepul!*

{hurmat}, qaysi mahsulot sizni qiziqtirdi? 
Narxlar va batafsil ma'lumotni admin bilan bog'lanib olasiz 👇
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# KIYIM-KECHAK
# ====================================================
@bot.message_handler(func=lambda message: message.text == "👗 Kiyim-kechak")
def kiyim(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    matn = f"""
👗 *{ism} XONIM, KIYIM-KECHAKLARIMIZ:*

━━━━━━━━━━━━━━━━━━━━━━━━
👚 *Ko'ylaklar* - turli uslub va ranglarda (S, M, L, XL)
👕 *Bluzkalar* - ofis va kundalik hayot uchun
👖 *Shimlar* - klassik va sport uslubida
🧥 *Kurtkalar* - qishki va yozgi modellar
👘 *Xalatlar* - uy uchun qulay va chiroyli
━━━━━━━━━━━━━━━━━━━━━━━━

✨ *Barcha o'lchamlar mavjud!*
✨ *Sifatli materiallardan tayyorlangan*

{hurmat}, o'zingizga yoqqan uslubni tanlang! 
Narxlar va rasmlar uchun admin bilan bog'lanishingiz mumkin 👇
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# BOLALAR UCHUN
# ====================================================
@bot.message_handler(func=lambda message: message.text == "🧸 Bolalar uchun")
def bolalar(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    matn = f"""
🧸 *{ism} XONIM, BOLALAR UCHUN MAHSULOTLAR:*

━━━━━━━━━━━━━━━━━━━━━━━━
👶 *Kombinezonlar* - 0-6 oylik bolajonlar uchun
👕 *Futbolkalar* - 2-7 yosh, multfilm qahramonlari bilan
👖 *Shimlar* - 1-5 yosh, qulay va elastik
👗 *Ko'ylaklar* - qiz bolalar uchun chiroyli modellar
🛏️ *Bolalar ko'rpalari* - yumshoq va issiq
━━━━━━━━━━━━━━━━━━━━━━━━

👶 *Farzandingizga eng yaxshisini tanlang!*
✨ *Bolalar terisiga mos, yumshoq materiallar*

{hurmat}, farzandlaringiz uchun eng yaxshisini xohlaysizmi?
Narxlar va o'lchamlar haqida admin bilan bog'lanishingiz mumkin 👇
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# UY-RO'ZG'OR
# ====================================================
@bot.message_handler(func=lambda message: message.text == "🏠 Uy-ro'zg'or")
def uy_rozgor(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    matn = f"""
🏠 *{ism} XONIM, UY-RO'ZG'OR BUYUMLARI:*

━━━━━━━━━━━━━━━━━━━━━━━━
🛏️ *Ko'rpalar* - turli o'lcham va ranglarda
🛋️ *Yostiqlar* - ortopedik va oddiy
🧺 *Choyshablar* - paxta, ipak va atlas
🏺 *Idish-tovoqlar* - to'plam va alohida
🧹 *Tozalash vositalari* - sifatli va samarali
━━━━━━━━━━━━━━━━━━━━━━━━

🏡 *Uyingizni obod qiladigan mahsulotlar!*
✨ *Sifat va qulay narxlar*

{hurmat}, uyingizni yanada chiroyli qiling!
Narxlar haqida admin bilan bog'lanishingiz mumkin 👇
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# AKSESUARLAR
# ====================================================
@bot.message_handler(func=lambda message: message.text == "💍 Aksesuarlar")
def aksesuar(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    matn = f"""
💍 *{ism} XONIM, AKSESUARLARIMIZ:*

━━━━━━━━━━━━━━━━━━━━━━━━
🕶️ *Ko'zoynaklar* - quyoshdan saqlaydigan modellar
🧣 *Sharflar* - turli rang va o'lchamlarda
🧤 *Qo'lqoplar* - qishki va yozgi
👛 *Hamyonlar* - ayollar va erkaklar uchun
💎 *Zargarlik buyumlari* - original va chiroyli
━━━━━━━━━━━━━━━━━━━━━━━━

✨ *Kiyimingizga chiroyli qo'shimchalar!*
✨ *Har didga mos tanlov*

{hurmat}, aksesuarlar sizni yanada go'zal qiladi!
Narxlar va rasmlar uchun admin bilan bog'lanishingiz mumkin 👇
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# ELEKTRONIKA
# ====================================================
@bot.message_handler(func=lambda message: message.text == "📱 Elektronika")
def elektronika(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    matn = f"""
📱 *{ism} XONIM, ELEKTRONIKA MAHSULOTLARI:*

━━━━━━━━━━━━━━━━━━━━━━━━
🎧 *Quloqchinlar* - bluetooth va simli
🔋 *Powerbank* - 10000, 20000 va 30000 mAh
📱 *Telefon aksesuarlari* - g'ilof, himoya oynasi
💡 *Fonarlar* - kuchli yorug'likli
🔌 *Zaryadlovchi kabellar* - turli xil
━━━━━━━━━━━━━━━━━━━━━━━━

✨ *Sifatli va ishonchli elektronika*
✨ *Arzon narxlar, kafolatli mahsulotlar*

{hurmat}, zamonaviy texnologiyalardan foydalaning!
Narxlar haqida admin bilan bog'lanishingiz mumkin 👇
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# GURUH HAQIDA
# ====================================================
@bot.message_handler(func=lambda message: message.text == "ℹ️ Guruh haqida")
def guruh_haqida(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    matn = f"""
ℹ️ *{GURUH_NOMI} NAMANGAN HAQIDA*

━━━━━━━━━━━━━━━━━━━━━━━━
👩‍💼 *Admin:* {ADMIN_ISMI} opa
📱 *Telefon:* `{TELEFON_RAQAM}`
💬 *Telegram:* {ADMIN_USERNAME}
📍 *Shahar:* Namangan
━━━━━━━━━━━━━━━━━━━━━━━━

🌟 *MAHSULOT TURLARI:*

💄 *Kosmetika* - yuz kremlari, penka, body loson
👗 *Kiyim-kechak* - ayollar uchun turli modellar
🧸 *Bolalar mahsulotlari* - kiyim va buyumlar
🏠 *Uy-ro'zg'or* - ko'rpa, choyshab, idishlar
💍 *Aksesuarlar* - ko'zoynak, sharf, hamyon
📱 *Elektronika* - quloqchin, powerbank

━━━━━━━━━━━━━━━━━━━━━━━━
✅ *100% SIFAT KAFOLATI*
✅ *ENG QULAY NARXLAR*
✅ *NAMANGAN BO'YLAB YETKAZIB BERISH*
✅ *DO'STONA MUHIT VA SAMIMIY MULOQOT*
━━━━━━━━━━━━━━━━━━━━━━━━

🌐 *Guruhga a'zo bo'ling:* [OPTOVIK SHOP NAMANGAN]({GURUH_LINKI})

{hurmat}, savollar bo'lsa, bemalol murojaat qiling! 🤗
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown', disable_web_page_preview=True)
    admin_ga_ulash(message)

# ====================================================
# AYOLLAR MASLAHATI
# ====================================================
@bot.message_handler(func=lambda message: message.text == "🌸 Ayollar maslahati")
def ayollar_maslahati(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    maslahatlar = [
        "Bilingki, har bir ayol go'zal va o'ziga xos! 🌸",
        "Teringizga g'amxo'rlik qilish - o'zingizga bo'lgan hurmat 💝",
        "Chiroyli kiyim kayfiyatingizni ko'taradi! 👗",
        "O'zingizni seving, o'zingizni qadrlang! 💖",
        "Har bir ona farzandlari bilan faxrlanadi! 👩‍👧",
        "Ayol kishi uyning ko'rki, oilaning ziynati! 🏡",
        "Tabassum sizga juda yarashadi! 😊",
        "Kun yangi boshlangan, bugun ajoyib kun bo'ladi! ☀️",
        "Siz kuchlisiz, siz go'zalsiz, siz bebahosiz! 💎",
        "O'z sog'lig'ingizga e'tibor bering - bu eng muhim boylik!"
    ]
    
    maslahat = random.choice(maslahatlar)
    
    matn = f"""
🌸 *{ism} XONIM, SIZGA MAXSUS MASLAHAT:*

*✨ {maslahat} ✨*

{hurmat}, o'zingizni asrang va seving! 
Siz dunyodagi eng go'zal ayollardan birisiz! 💝

*Yana maslahat kerak bo'lsa, shu tugmani yana bosing!*
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')

# ====================================================
# SAVOL-JAVOB (TO'LIQ VERSIYA)
# ====================================================
@bot.message_handler(func=lambda message: message.text == "❓ Savol-javob")
def savol_javob(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    matn = f"""
❓ *{ism} XONIM, SIZGA QANDAY YORDAM BERA OLAMAN?*

━━━━━━━━━━━━━━━━━━━━━━━━
📌 *TEZ-TEZ SO'RALADIGAN SAVOLLAR:*
━━━━━━━━━━━━━━━━━━━━━━━━

🔹 *Mahsulotlar qayerda ishlab chiqarilgan?*
   → Xitoy, Turkiya va Koreya

🔹 *Yetkazib berish bormi?*
   → Ha, Namangan shahri bo'ylab yetkazib berish BEPUL

🔹 *To'lov qanday amalga oshiriladi?*
   → Naqd, plastik karta yoki pul o'tkazmasi

🔹 *Mahsulotni qaytarish mumkinmi?*
   → Ha, nuqsoni bo'lsa 7 kun ichida almashtiramiz

🔹 *Narxlar haqida qayerdan bilsam bo'ladi?*
   → Narxlar uchun admin bilan bog'lanishingiz kerak

━━━━━━━━━━━━━━━━━━━━━━━━
📞 *Boshqa savollar bo'lsa, admin bilan bog'lanishingiz mumkin*
━━━━━━━━━━━━━━━━━━━━━━━━
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# ADMIN BILAN BOG'LANISH TUGMASI
# ====================================================
@bot.message_handler(func=lambda message: message.text == "📞 Admin bilan bog'lanish")
def admin_bilan_boglanish(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("📞 Zulhumor opaga yozish", url="https://t.me/Zulxumor5900")
    btn2 = types.InlineKeyboardButton("📱 Telefon raqam", callback_data="show_phone")
    markup.add(btn1, btn2)
    
    matn = f"""
📞 *{ism} XONIM, ADMIN BILAN BOG'LANISH:*

━━━━━━━━━━━━━━━━━━━━━━━━
👩‍💼 *Admin:* {ADMIN_ISMI} opa
📱 *Telefon:* `{TELEFON_RAQAM}`
💬 *Telegram:* {ADMIN_USERNAME}
━━━━━━━━━━━━━━━━━━━━━━━━

{hurmat}, quyidagi tugmalardan birini tanlang 👇
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown', reply_markup=markup)

# ====================================================
# NARX SO'RAGANDA - ADMINGA YO'NALTIRISH
# ====================================================
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in narx_sozlar))
def narx_sorash(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    javoblar = [
        f"{hurmat}, men narxlarni bilmayman. Narxlar uchun Zulhumor opaga murojaat qiling! 👇",
        f"Kechirasiz {ism} xonim, narxlar haqida ma'lumot menda yo'q. Admin bilan bog'lanishingiz kerak 👇",
        f"{hurmat}, narxlar o'zgaruvchan. Aniq narxni admin dan olishingiz mumkin 👇",
        f"{ism} xonim, narxlar haqida Zulhumor opa ma'lumot beradi. Menga ruxsat berilmagan 👇",
        f"{hurmat}, men faqat mahsulotlar haqida umumiy ma'lumot bera olaman. Narxlar uchun admin bilan bog'lanishingizni so'rayman 👇"
    ]
    
    bot.reply_to(message, random.choice(javoblar))
    admin_ga_ulash(message)

# ====================================================
# ADMINGA YO'NALTIRISH FUNKSIYASI
# ====================================================
def admin_ga_ulash(message):
    hurmat = random.choice(hurmatli_murojaatlar)
    
    javoblar = [
        f"{hurmat}, quyidagi tugma orqali admin bilan bog'lanishingiz mumkin 👇",
        f"Barcha savollaringizga Zulhumor opa javob beradi. Shu tugmani bosing 👇",
        f"Admin bilan tezda bog'lanmoqchimisiz? Shu tugma sizga yordam beradi 👇",
        f"{hurmat}, admin sizni kutmoqda! 👇"
    ]
    
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("📞 Zulhumor opaga yozish", url="https://t.me/Zulxumor5900")
    btn2 = types.InlineKeyboardButton("📱 Telefon raqam", callback_data="show_phone")
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id, random.choice(javoblar), reply_markup=markup)

# ====================================================
# INLINE TUGMALAR UCHUN
# ====================================================
@bot.callback_query_handler(func=lambda call: True)
def inline_buttons(call):
    hurmat = random.choice(hurmatli_murojaatlar)
    
    if call.data == "show_phone":
        matn = f"""
📱 *ZULHUMOR OPANING TELEFON RAQAMI:*

`{TELEFON_RAQAM}`

💬 *Telegram:* {ADMIN_USERNAME}

{hurmat}, qo'ng'iroq qilishingiz yoki Telegramdan yozishingiz mumkin!
        """
        bot.send_message(call.message.chat.id, matn, parse_mode='Markdown')

# ====================================================
# SALOMLASHISH
# ====================================================
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in salomlashish))
def salom_javob(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    javoblar = [
        f"Va alaykum assalom, {hurmat} {ism}! Sizni ko'rganimdan xursandman! 😊 Qanday mahsulot qiziqtiradi?",
        f"Assalomu alaykum, {ism} xonim! OPTOVIK SHOP ga xush kelibsiz! Qanday yordam kerak?",
        f"Hayrli kun {ism} xonim! Sizni ko'rganimdan xursandman! Bugun sizga qanday yordam bera olaman? 🌸",
        f"Assalomu alaykum! {hurmat}, yaxshi kun tilayman! Qanday mahsulotlar bilan qiziqasiz?"
    ]
    bot.reply_to(message, random.choice(javoblar))

# ====================================================
# HOL-AHVOL SO'RASH
# ====================================================
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in hol_ahvol))
def qalay_javob(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    javoblar = [
        f"Rahmat so'raganingiz uchun, {hurmat}! Yaxshi, ishlar joyida. Sizning ahvollaringiz qalay?",
        f"Ajoyib, rahmat {ism} xonim! Bugun kayfiyatingiz ko'tarinki ko'rinib turibdi. Biror yangilik bormi?",
        f"Yaxshi, rahmat! Siz bilan gaplashganimdan keyin kayfiyatim yanada yaxshilandi. Siz qalay, {hurmat}?",
        f"Hammasi joyida, rahmat! Sizga qanday yordam bera olaman?"
    ]
    bot.reply_to(message, random.choice(javoblar))

# ====================================================
# TASHAKKUR
# ====================================================
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in tashakkur))
def rahmat_javob(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    javoblar = [
        f"Arzimaydi, {hurmat}! Sizga yordam berishdan xursandman!",
        f"Rahmat sizga ham, {ism} xonim! OPTOVIK SHOP ni tanlaganingiz uchun tashakkur!",
        f"Marhamat, {hurmat}! Doim sizni kutib qolamiz! 🌸",
        f"Bizning mijozimiz bo'lganingiz uchun rahmat! Yana savol bo'lsa, yozing."
    ]
    bot.reply_to(message, random.choice(javoblar))

# ====================================================
# XAYRLASHISH
# ====================================================
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in xayrlashish))
def xayr_javob(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    javoblar = [
        f"Xayr {hurmat}! Yana kelib turing, yangi mahsulotlar kelyapti!",
        f"Xayr xayr, {ism} xonim! Sog'liq va omad tilayman!",
        f"Salomat bo'ling, {hurmat}! OPTOVIK SHOP da yana ko'rishguncha! 🌸",
        f"Xayrli kun tilayman! Yana bizni tanlaganingizdan xursandmiz!"
    ]
    bot.reply_to(message, random.choice(javoblar))

# ====================================================
# ADMIN BILAN BOG'LANISHNI SO'RAGANDA
# ====================================================
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in admin_sozlar))
def admin_sozlari(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    javoblar = [
        f"{hurmat}, Zulhumor opa bilan bog'lanmoqchi bo'lsangiz, quyidagi tugmani bosing 👇",
        f"{ism} xonim, admin bilan bog'lanish uchun maxsus tugma tayyorladim 👇",
        f"Albatta {hurmat}, Zulhumor opa sizni kutmoqda! Shu tugma orqali yozishingiz mumkin 👇"
    ]
    
    bot.reply_to(message, random.choice(javoblar))
    
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("📞 Zulhumor opaga yozish", url="https://t.me/Zulxumor5900")
    btn2 = types.InlineKeyboardButton("📱 Telefon raqam", callback_data="show_phone")
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id, "👇 Shu tugmalardan birini tanlang:", reply_markup=markup)

# ====================================================
# BOSHQA XABARLAR (TUSHUNMADIM - ADMINGA YO'NALTIRISH)
# ====================================================
@bot.message_handler(func=lambda message: True)
def boshqa_javob(message):
    ism = message.from_user.first_name
    hurmat = random.choice(hurmatli_murojaatlar)
    
    javoblar = [
        f"{hurmat}, tushunmadim biroz. Iltimos, yana bir bor ayting yoki admin bilan bog'lanishingiz mumkin 👇",
        f"Kechirasiz {ism} xonim, savolingizni tushunolmadim. Yana boshqatdan yozib ko'ring yoki admin bilan bog'lanishingiz mumkin 👇",
        f"{hurmat}, men hali o'rganyapman. Aniqroq yozing yoki Zulhumor opaga murojaat qiling 👇",
        f"Savolingizni tushunmadim, {hurmat}. Iltimos, tugmalardan birini tanlang yoki admin bilan bog'laning 👇"
    ]
    
    bot.reply_to(message, random.choice(javoblar))
    admin_ga_ulash(message)

# ====================================================
# RENDER UCHUN PORT SOZLASH (MUHIM!)
# ====================================================
app = Flask(__name__)

@app.route('/')
def home():
    return "🌸 OPTOVIK SHOP BOTI ISHLAYAPTI! 🌸"

def run_flask():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# Flask-ni alohida threadda ishga tushirish
threading.Thread(target=run_flask).start()

print("=" * 60)
print("🌸 OPTOVIK SHOP BOTI ISHGA TUSHDI! 🌸")
print("=" * 60)
print(f"👩‍💼 Admin: {ADMIN_ISMI} {ADMIN_USERNAME}")
print(f"📞 Telefon: {TELEFON_RAQAM}")
print(f"🏪 Guruh: {GURUH_NOMI} NAMANGAN")
print("=" * 60)
print("✅ Bot muvaffaqiyatli ishga tushdi!")
print("📱 Telegramda botingizni ochib /start yozing")
print("=" * 60)

# Botni ishga tushirish
bot.infinity_polling()
# ====================================================
# RENDER UCHUN PORT SOZLASH (MUHIM!)
# ====================================================
import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "🌸 OPTOVIK SHOP BOTI ISHLAYAPTI! 🌸"

def run_flask():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# Flask-ni alohida threadda ishga tushirish
threading.Thread(target=run_flask).start()
