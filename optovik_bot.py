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
# AYOLLAR UCHUN MEHRLI MUROJAATLAR (40 xil)
# ====================================================
mehrli_murojaatlar = [
    "azizaxon", "jahon", "gulim", "jonim", "opajon", "singiljon", 
    "malikam", "shirinjon", "mehribonim", "qizim", "xonimjon", "gulbahorim",
    "dilbarim", "sadoqatim", "farzandim", "onajon", "opa", "singil",
    "go'zalim", "malikam", "shahzodam", "parizod", "bebahom", "aslim",
    "muhabbatim", "orzuim", "maftunim", "dildorim", "sog'inchim", "omonim",
    "javlonim", "niholim", "lolaxon", "nargiz", "durdona", "gavhar",
    "marvarid", "zumrad", "qimmatim", "bahorim"
]

# ====================================================
# SALOMLASHISH SO'ZLARI (20 xil)
# ====================================================
salomlashish = [
    "salom", "assalom", "assalomu alaykum", "alaykum assalom", "salom alejkum",
    "hayrli kun", "hayrli tong", "hayrli kech", "xayrli kun", "xayrli tong",
    "xayrli kech", "salom qalay", "salom ishlar", "salom berdim", "salom opa",
    "salom singil", "salom jon", "salom azizaxon", "salom gulim", "salom dunyo"
]

# ====================================================
# XAYRLASHISH SO'ZLARI (15 xil)
# ====================================================
xayrlashish = [
    "xayr", "hayr", "xayr xayr", "rahmat", "katta rahmat", "ko'rishguncha", 
    "xayr salomat", "hozircha", "sog' bo'ling", "omad", "xayr endi", 
    "ketdim", "boring", "xayr xudo hafsiz", "xayrli tun"
]

# ====================================================
# HOL-AHVOL SO'RASH (15 xil)
# ====================================================
hol_ahvol = [
    "qalay", "qalaysiz", "qanday", "qandaysiz", "yaxshimisiz", "ishlar qalay",
    "ahvollaringiz", "yuribsizmi", "nima gap", "nima yangilik", "ishlar joyidami",
    "tinchmisiz", "sog'lik", "yaxshi yuribsizmi", "hayot qalay"
]

# ====================================================
# TASHAKKUR SO'ZLARI (12 xil)
# ====================================================
tashakkur = [
    "rahmat", "tashakkur", "minnatdor", "katta rahmat", "rahmat sizga", 
    "arzimaydi", "rahma", "tashakkur sizga", "minnatdorman", "rahmat opa",
    "rahmat singil", "borakalla"
]

# ====================================================
# SAVOL SO'ZLARI (narx, qayer, qachon, qanaqa)
# ====================================================
savol_sozlar = [
    "narx", "qancha", "puli", "so'm", "sum", "narhi", "narxi",
    "qayerda", "qayerdan", "qachon", "qachon keladi", "bormi", 
    "qanaqa", "qanday", "qaysi", "necha", "nechchi"
]

# ====================================================
# /start komandasi
# ====================================================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    salom_matni = f"""
🌸 *ASSALOMU ALAYKUM, {ism.upper()} XONIM!* 🌸

Men *{ADMIN_ISMI}* opangiz, *{GURUH_NOMI}* guruhining adminiman. 
Namangan shahridan barcha ayollarga salom! 🤗

Siz bilan tanishganimdan nihoyatda xursandman, {mehrli}!

━━━━━━━━━━━━━━━━━━━━━━━━
🏪 *MAVJUD MAHSULOTLAR:*
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

👩‍💼 *Admin:* {ADMIN_ISMI}
📱 *Telefon:* `{TELEFON_RAQAM}`
💬 *Telegram:* {ADMIN_USERNAME}
🌐 *Guruh:* [OPTOVIK SHOP NAMANGAN]({GURUH_LINKI})
━━━━━━━━━━━━━━━━━━━━━━━━

💬 *Qanday mahsulot qiziqtiradi, {mehrli}?* 
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
    mehrli = random.choice(mehrli_murojaatlar)
    
    matn = f"""
💄 *{ism} XONIM, KOSMETIKA MAHSULOTLARIMIZ:*

━━━━━━━━━━━━━━━━━━━━━━━━
🧴 *Yuz kremi* - terini namlaydi, oziqlantiradi
   *Narxi:* 45.000 - 85.000 so'm

👁️ *Ko'z atrofi kremi* - shish va qorayishlarni ketkazadi
   *Narxi:* 55.000 so'm

💆 *Body loson* - tanani namlaydi, mayin qiladi
   *Narxi:* 65.000 so'm

🧼 *Penka* - yuzni tozalaydi, dog'larni ochartiradi
   *Narxi:* 75.000 so'm

❄️ *Ice Raw Puli* - muz terapiyasi
   *Narxi:* 95.000 so'm

🌟 *Nabor (to'plam)* - 5 mahsulot
   *Narxi:* 350.000 so'm
━━━━━━━━━━━━━━━━━━━━━━━━

✨ *Barcha mahsulotlar ORIGINAL va SIFATLI!*
✨ *Namangan shahrida yetkazib berish bepul!*

{mehrli}, qaysi mahsulot sizni qiziqtirdi? 
Batafsil ma'lumot uchun admin bilan bog'lanishingiz mumkin.
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# KIYIM-KECHAK
# ====================================================
@bot.message_handler(func=lambda message: message.text == "👗 Kiyim-kechak")
def kiyim(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    matn = f"""
👗 *{ism} XONIM, KIYIM-KECHAKLARIMIZ:*

━━━━━━━━━━━━━━━━━━━━━━━━
👚 *Ko'ylaklar* - turli uslub va ranglarda
   *Narxi:* 120.000 - 250.000 so'm
   *O'lchamlar:* S, M, L, XL

👕 *Bluzkalar* - ofis va kundalik hayot uchun
   *Narxi:* 80.000 - 150.000 so'm

👖 *Shimlar* - klassik va sport uslubida
   *Narxi:* 100.000 - 180.000 so'm

🧥 *Kurtkalar* - qishki va yozgi modellar
   *Narxi:* 250.000 - 450.000 so'm

👘 *Xalatlar* - uy uchun qulay va chiroyli
   *Narxi:* 150.000 - 220.000 so'm
━━━━━━━━━━━━━━━━━━━━━━━━

✨ *Barcha o'lchamlar mavjud!*
✨ *Sifatli materiallardan tayyorlangan*

{mehrli}, o'zingizga yoqqan uslubni tanlang! 
Rasmlar va batafsil ma'lumot uchun admin bilan bog'lanishingiz mumkin.
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# BOLALAR UCHUN
# ====================================================
@bot.message_handler(func=lambda message: message.text == "🧸 Bolalar uchun")
def bolalar(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    matn = f"""
🧸 *{ism} XONIM, BOLALAR UCHUN MAHSULOTLAR:*

━━━━━━━━━━━━━━━━━━━━━━━━
👶 *Kombinezonlar* - 0-6 oylik bolajonlar uchun
   *Narxi:* 80.000 - 120.000 so'm

👕 *Futbolkalar* - 2-7 yosh, multfilm qahramonlari bilan
   *Narxi:* 45.000 - 65.000 so'm

👖 *Shimlar* - 1-5 yosh, qulay va elastik
   *Narxi:* 55.000 - 75.000 so'm

👗 *Ko'ylaklar* - qiz bolalar uchun chiroyli modellar
   *Narxi:* 70.000 - 110.000 so'm

🛏️ *Bolalar ko'rpalari* - yumshoq va issiq
   *Narxi:* 150.000 - 250.000 so'm
━━━━━━━━━━━━━━━━━━━━━━━━

👶 *Farzandingizga eng yaxshisini tanlang!*
✨ *Bolalar terisiga mos, yumshoq materiallar*

{mehrli}, farzandlaringiz siz bilan faxrlanadi! 
Narxlar va mavjud o'lchamlar haqida admin bilan bog'lanishingiz mumkin.
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# UY-RO'ZG'OR
# ====================================================
@bot.message_handler(func=lambda message: message.text == "🏠 Uy-ro'zg'or")
def uy_rozgor(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    matn = f"""
🏠 *{ism} XONIM, UY-RO'ZG'OR BUYUMLARI:*

━━━━━━━━━━━━━━━━━━━━━━━━
🛏️ *Ko'rpalar* - turli o'lcham va ranglarda
   *Narxi:* 200.000 - 400.000 so'm

🛋️ *Yostiqlar* - ortopedik va oddiy
   *Narxi:* 50.000 - 120.000 so'm

🧺 *Choyshablar* - paxta, ipak va atlas
   *Narxi:* 150.000 - 350.000 so'm

🏺 *Idish-tovoqlar* - to'plam va alohida
   *Narxi:* 80.000 - 300.000 so'm

🧹 *Tozalash vositalari* - sifatli va samarali
   *Narxi:* 30.000 - 90.000 so'm
━━━━━━━━━━━━━━━━━━━━━━━━

🏡 *Uyingizni obod qiladigan mahsulotlar!*
✨ *Sifat va qulay narxlar*

{mehrli}, uyingizni yanada chiroyli qiling! 
Qaysi mahsulot qiziqtiradi? Admin bilan bog'lanishingiz mumkin.
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# AKSESUARLAR
# ====================================================
@bot.message_handler(func=lambda message: message.text == "💍 Aksesuarlar")
def aksesuar(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    matn = f"""
💍 *{ism} XONIM, AKSESUARLARIMIZ:*

━━━━━━━━━━━━━━━━━━━━━━━━
🕶️ *Ko'zoynaklar* - quyoshdan saqlaydigan modellar
   *Narxi:* 80.000 - 200.000 so'm

🧣 *Sharflar* - turli rang va o'lchamlarda
   *Narxi:* 40.000 - 90.000 so'm

🧤 *Qo'lqoplar* - qishki va yozgi
   *Narxi:* 30.000 - 70.000 so'm

👛 *Hamyonlar* - ayollar va erkaklar uchun
   *Narxi:* 60.000 - 150.000 so'm

💎 *Zargarlik buyumlari* - original va chiroyli
   *Narxi:* 100.000 - 500.000 so'm
━━━━━━━━━━━━━━━━━━━━━━━━

✨ *Kiyimingizga chiroyli qo'shimchalar!*
✨ *Har didga mos tanlov*

{mehrli}, aksesuarlar sizni yanada go'zal qiladi! 
Rasmlar uchun admin bilan bog'lanishingiz mumkin.
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# ELEKTRONIKA
# ====================================================
@bot.message_handler(func=lambda message: message.text == "📱 Elektronika")
def elektronika(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    matn = f"""
📱 *{ism} XONIM, ELEKTRONIKA MAHSULOTLARI:*

━━━━━━━━━━━━━━━━━━━━━━━━
🎧 *Quloqchinlar* - bluetooth va simli
   *Narxi:* 70.000 - 250.000 so'm

🔋 *Powerbank* - 10000, 20000 va 30000 mAh
   *Narxi:* 150.000 - 350.000 so'm

📱 *Telefon aksesuarlari* - g'ilof, himoya oynasi
   *Narxi:* 30.000 - 120.000 so'm

💡 *Fonarlar* - kuchli yorug'likli
   *Narxi:* 50.000 - 150.000 so'm

🔌 *Zaryadlovchi kabellar* - turli xil
   *Narxi:* 25.000 - 60.000 so'm
━━━━━━━━━━━━━━━━━━━━━━━━

✨ *Sifatli va ishonchli elektronika*
✨ *Arzon narxlar, kafolatli mahsulotlar*

{mehrli}, zamonaviy texnologiyalardan foydalaning!
Batafsil ma'lumot uchun admin bilan bog'lanishingiz mumkin.
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_ulash(message)

# ====================================================
# AYOLLAR MASLAHATI
# ====================================================
@bot.message_handler(func=lambda message: message.text == "🌸 Ayollar maslahati")
def ayollar_maslahati(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
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
        "O'z sog'lig'ingizga e'tibor bering - bu eng muhim boylik!",
        "Farzandlaringiz sizning eng katta boyligingiz! 👶",
        "Bir piyona choy iching va dam oling! ☕",
        "Do'stlaringiz bilan ko'proq vaqt o'tkazing! 👯‍♀️",
        "Orzularingiz sari intiling! ✨",
        "Bugun o'zingiz uchun yaxshilik qiling! 🎁"
    ]
    
    maslahat = random.choice(maslahatlar)
    
    matn = f"""
🌸 *{ism} XONIM, SIZGA MAXSUS MASLAHAT:*

*✨ {maslahat} ✨*

{mehrli}, o'zingizni asrang va seving! 
Siz dunyodagi eng go'zal ayollardan birisiz! 💝

*Yana maslahat kerak bo'lsa, shu tugmani yana bosing!*
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')

# ====================================================
# SAVOL-JAVOB
# ====================================================
@bot.message_handler(func=lambda message: message.text == "❓ Savol-javob")
def savol_javob(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    matn = f"""
❓ *{ism} XONIM, SIZGA QANDAY YORDAM BERA OLAMAN?*

━━━━━━━━━━━━━━━━━━━━━━━━
📌 *TEZ-TEZ SO'RALADIGAN SAVOLLAR:*
━━━━━━━━━━━━━━━━━━━━━━━━

🔹 *Mahsulotlar qayerda ishlab chiqarilgan?*
   - Barcha mahsulotlar Xitoy, Turkiya va Koreyadan keltiriladi

🔹 *Yetkazib berish bormi?*
   - Ha, Namangan shahri bo'ylab yetkazib berish BEPUL

🔹 *To'lov qanday amalga oshiriladi?*
   - Naqd, plastik karta yoki pul o'tkazmasi orqali

🔹 *Mahsulotni qaytarish mumkinmi?*
   - Ha, agar nuqsoni bo'lsa 7 kun ichida almashtirib beramiz

🔹 *Chegirmalar bormi?*
   - Doimiy mijozlarimizga 5-15% chegirma mavjud

━━━━━━━━━━━━━━━━━━━━━━━━
📞 *Boshqa savollar bo'lsa, admin bilan bog'lanishingiz mumkin:*
━━━━━━━━━━━━━━━━━━━━━━━━

👩‍💼 *Admin:* {ADMIN_ISMI}
📱 *Telefon:* {TELEFON
