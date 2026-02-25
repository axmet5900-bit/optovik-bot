import telebot
from telebot import types
import random
import time
import os

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

# Ayollar uchun mehrli murojaatlar
mehrli_murojaatlar = [
    "azizaxon", "jahon", "gulim", "jonim", "opajon", "singiljon", 
    "malikam", "shirinjon", "mehribonim", "qizim", "xonimjon", "gulbahorim"
]

# Salomlashish so'zlari
salomlashish = ["salom", "assalom", "assalomu alaykum", "alaykum assalom", "salom alejkum",
                "hayrli kun", "hayrli tong", "hayrli kech", "xayrli kun"]

# Xayrlashish so'zlari
xayrlashish = ["xayr", "hayr", "xayr xayr", "rahmat", "katta rahmat", "ko'rishguncha", 
               "xayr salomat", "hozircha"]

# Hol-ahvol so'rash
hol_ahvol = ["qalay", "qalaysiz", "qanday", "qandaysiz", "yaxshimisiz", "ishlar qalay",
             "ahvollaringiz", "yuribsizmi"]

# Tashakkur so'zlari
tashakkur = ["rahmat", "tashakkur", "minnatdor", "katta rahmat", "rahmat sizga", "arzimaydi"]

# /start komandasi
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
    btn7 = types.KeyboardButton("📞 Zulhumor bilan bog'lanish")
    btn8 = types.KeyboardButton("ℹ️ Guruh haqida")
    btn9 = types.KeyboardButton("🌸 Ayollar maslahati")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    
    bot.send_message(message.chat.id, salom_matni, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup)

# Kosmetika haqida
@bot.message_handler(func=lambda message: message.text == "💄 Kosmetika")
def kosmetika(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    matn = f"""
💄 *{ism} XONIM, KOSMETIKA MAHSULOTLARI:*

━━━━━━━━━━━━━━━━━━━━━━━━
🧴 *Yuz kremi* - terini namlaydi, oziqlantiradi va mayinlik bag'ishlaydi
👁️ *Ko'z atrofi kremi* - shish va qorayishlarni ketkazadi, elastiklikni oshiradi
💆 *Body loson* - tanani namlaydi, mayin va yumshoq qiladi
🧼 *Penka* - qarishga qarshi, yuz dog'larini ochartiradi
❄️ *Ice Raw Puli* - muz terapiyasi, terini tetiklashtiradi
🌟 *Nabor (to'plam)* - barcha mahsulotlar bir joyda
━━━━━━━━━━━━━━━━━━━━━━━━

✨ *Barcha mahsulotlar ORIGINAL va SIFATLI!*
✨ *Namangan shahrida yetkazib berish tez va bepul!*

{mehrli}, bu mahsulotlar teringizni yanada go'zal qiladi! 
Narxlar va batafsil ma'lumot uchun Zulhumor opaga yozing!
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_yonalitirish(message)

# Kiyim-kechak
@bot.message_handler(func=lambda message: message.text == "👗 Kiyim-kechak")
def kiyim(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    matn = f"""
👗 *{ism} XONIM, KIYIM-KECHAK MAHSULOTLARI:*

━━━━━━━━━━━━━━━━━━━━━━━━
👚 *Ko'ylaklar* - turli uslub va ranglarda (S, M, L, XL)
👕 *Bluzkalar* - ofis va kundalik hayot uchun
👖 *Shimlar* - klassik va sport uslubida
🧥 *Kurtkalar* - qishki va yozgi modellar
👘 *Xalatlar* - uy uchun qulay va chiroyli
━━━━━━━━━━━━━━━━━━━━━━━━

✨ *Barcha o'lchamlar mavjud!*
✨ *Sifatli materiallardan tayyorlangan*

{mehrli}, o'zingizga yoqqan uslubni tanlang! 
Yangi kiyim har doim kayfiyatni ko'taradi! 👗
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_yonalitirish(message)

# Bolalar uchun
@bot.message_handler(func=lambda message: message.text == "🧸 Bolalar uchun")
def bolalar(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
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

{mehrli}, farzandlaringiz siz bilan faxrlanadi! 
Narxlar va mavjud o'lchamlar haqida Zulhumor opadan so'rang!
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_yonalitirish(message)

# Uy-ro'zg'or
@bot.message_handler(func=lambda message: message.text == "🏠 Uy-ro'zg'or")
def uy_rozgor(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
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

{mehrli}, uyingizni yanada chiroyli qiling! 
Qaysi mahsulot qiziqtiradi? Zulhumor opaga yozing!
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_yonalitirish(message)

# Aksesuarlar
@bot.message_handler(func=lambda message: message.text == "💍 Aksesuarlar")
def aksesuar(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    matn = f"""
💍 *{ism} XONIM, AKSESUARLAR:*

━━━━━━━━━━━━━━━━━━━━━━━━
🕶️ *Ko'zoynaklar* - quyoshdan saqlaydigan modellar
🧣 *Sharflar* - turli rang va o'lchamlarda
🧤 *Qo'lqoplar* - qishki va yozgi
👛 *Hamyonlar* - ayollar va erkaklar uchun
💎 *Zargarlik buyumlari* - original va chiroyli
━━━━━━━━━━━━━━━━━━━━━━━━

✨ *Kiyimingizga chiroyli qo'shimchalar!*
✨ *Har didga mos tanlov*

{mehrli}, aksesuarlar sizni yanada go'zal qiladi! 
Narxlar va rasmlar uchun Zulhumor opaga yozing!
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_yonalitirish(message)

# Elektronika
@bot.message_handler(func=lambda message: message.text == "📱 Elektronika")
def elektronika(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
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

{mehrli}, zamonaviy texnologiyalardan foydalaning!
Batafsil ma'lumot uchun Zulhumor opaga yozing!
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')
    admin_ga_yonalitirish(message)

# Ayollar maslahati
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
        "Kun yangi boshlangan, bugun ajoyib kun bo'ladi! ☀️"
    ]
    
    maslahat = random.choice(maslahatlar)
    
    matn = f"""
🌸 *{ism} XONIM, SIZGA MAXSUS MASLAHAT:*

*{maslahat}*

{mehrli}, o'zingizni asrang va seving! Siz dunyodagi eng go'zal ayollardan birisiz! 💝

*Yana maslahat kerak bo'lsa, shu tugmani yana bosing!*
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown')

# Guruh haqida
@bot.message_handler(func=lambda message: message.text == "ℹ️ Guruh haqida")
def guruh_haqida(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    matn = f"""
ℹ️ *{GURUH_NOMI} NAMANGAN HAQIDA*

━━━━━━━━━━━━━━━━━━━━━━━━
👩‍💼 *Admin:* {ADMIN_ISMI}
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

{mehrli}, savollar bo'lsa, bemalol murojaat qiling! 🤗
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown', disable_web_page_preview=True)
    admin_ga_yonalitirish(message)

# Zulhumor bilan bog'lanish
@bot.message_handler(func=lambda message: message.text == "📞 Zulhumor bilan bog'lanish")
def zulhumor_bilan_boglanish(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("📞 Zulhumorga yozish", url="https://t.me/Zulxumor5900")
    btn2 = types.InlineKeyboardButton("📱 Telefon raqam", callback_data="show_phone")
    markup.add(btn1, btn2)
    
    matn = f"""
📞 *{ism} XONIM, MEN BILAN BOG'LANISH UCHUN:*

━━━━━━━━━━━━━━━━━━━━━━━━
👩‍💼 *Admin:* {ADMIN_ISMI} opa
📱 *Telefon:* `{TELEFON_RAQAM}`
💬 *Telegram:* {ADMIN_USERNAME}
━━━━━━━━━━━━━━━━━━━━━━━━

*Quyidagi tugmalardan birini tanlang, {mehrli}!* 👇
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown', reply_markup=markup)

# Admin ga yo'naltirish funksiyasi
def admin_ga_yonalitirish(message):
    mehrli = random.choice(mehrli_murojaatlar)
    
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("📞 Zulhumorga yozish", url="https://t.me/Zulxumor5900")
    btn2 = types.InlineKeyboardButton("📱 Telefon raqam", callback_data="show_phone")
    markup.add(btn1, btn2)
    
    matn = f"""
💬 *BATAFSIL MA'LUMOT UCHUN*

{mehrli}, narxlar, rasmlar va barcha ma'lumotlarni 
Zulhumor opadan olishingiz mumkin!

👇 *Quyidagi tugmani bosib, yozing!*
    """
    
    bot.send_message(message.chat.id, matn, parse_mode='Markdown', reply_markup=markup)

# Inline tugmalar uchun
@bot.callback_query_handler(func=lambda call: True)
def inline_buttons(call):
    ism = call.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    if call.data == "show_phone":
        matn = f"""
📱 *ZULHUMOR OPANING TELEFON RAQAMI:*

`{TELEFON_RAQAM}`

💬 *Telegram:* {ADMIN_USERNAME}

{mehrli}, qo'ng'iroq qilishingiz yoki Telegramdan yozishingiz mumkin!
        """
        bot.send_message(call.message.chat.id, matn, parse_mode='Markdown')

# Narx so'raganda to'g'ridan-to'g'ri admin ga
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in ["narx", "qancha", "puli", "so'm", "sum", "narhi"]))
def narx_sorash(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    bot.reply_to(message, f"{mehrli}, narxlar haqida so'ragan ekansiz. Bu yerda narx yozish mumkin emas, Zulhumor opaga yozing!")
    
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("📞 Zulhumorga yozish", url="https://t.me/Zulxumor5900")
    markup.add(btn)
    bot.send_message(message.chat.id, "👇 Shu tugmani bosing!", reply_markup=markup)

# Salomlashish
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in salomlashish))
def salom_javob(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    javoblar = [
        f"Va alaykum assalom, {mehrli} {ism}! Qanday yaxshi odam bilan uchrashdim! 😊 Qaysi mahsulot qiziqtiradi?",
        f"Assalomu alaykum, azizaxon {ism}! OPTOVIK SHOP ga xush kelibsiz! Qanday yordam kerak?",
        f"Hayrli kun {ism} xonim! Sizni ko'rganimdan xursandman! Namanganning eng go'zal ayollaridan biriga xizmat ko'rsatish sharaf! 🌸"
    ]
    bot.reply_to(message, random.choice(javoblar))

# Hol-ahvol so'rash
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in hol_ahvol))
def qalay_javob(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    javoblar = [
        f"Rahmat so'raganingiz uchun, {mehrli}! Yaxshi, ishlar joyida. Sizning ahvollaringiz qalay?",
        f"Ajoyib, rahmat {ism}jon! Bugun kayfiyatingiz ko'tarinki ko'rinib turibdi. Biror yangilik bormi?",
        f"Yaxshi, rahmat! Siz bilan gaplashganimdan keyin kayfiyatim yanada yaxshilandi. Siz qalay, {mehrli}?"
    ]
    bot.reply_to(message, random.choice(javoblar))

# Tashakkur
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in tashakkur))
def rahmat_javob(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    javoblar = [
        f"Arzimaydi, {mehrli}! Sizga yordam berishdan xursandman! Yana savol bo'lsa, yozing.",
        f"Rahmat sizga ham, {ism}jon! OPTOVIK SHOP ni tanlaganingiz uchun tashakkur!",
        f"Marhamat, azizaxon! Doim sizni kutib qolamiz! 🌸"
    ]
    bot.reply_to(message, random.choice(javoblar))

# Xayrlashish
@bot.message_handler(func=lambda message: any(soz in message.text.lower() for soz in xayrlashish))
def xayr_javob(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    javoblar = [
        f"Xayr {mehrli}! Yana kelib turing, yangi mahsulotlar kelyapti!",
        f"Xayr xayr, {ism}jon! Sog'liq va omad tilayman!",
        f"Salomat bo'ling, azizaxon! OPTOVIK SHOP da yana ko'rishguncha! 🌸"
    ]
    bot.reply_to(message, random.choice(javoblar))

# Boshqa xabarlar
@bot.message_handler(func=lambda message: True)
def boshqa_javob(message):
    ism = message.from_user.first_name
    mehrli = random.choice(mehrli_murojaatlar)
    
    javoblar = [
        f"{mehrli}, tushunmadim biroz. Yana bir bor ayting-chi?",
        f"Ha, {ism}jon! Savolingiz bo'lsa, bemalol yozing. Qaysi mahsulot qiziqtiradi?",
        f"{mehrli}, sizga qanday yordam bera olaman? Kosmetika, kiyim yoki boshqa mahsulot?",
        f"Tushunishga harakat qilyapman, {ism}jon. Iltimos, yana bir bor yozing!"
    ]
    bot.reply_to(message, random.choice(javoblar))

print("=" * 50)
print("🌸 OPTOVIK SHOP BOTI ISHGA TUSHDI! 🌸")
print("=" * 50)
print(f"👩‍💼 Admin: {ADMIN_ISMI} {ADMIN_USERNAME}")
print(f"📞 Telefon: {TELEFON_RAQAM}")
print(f"🏪 Guruh: {GURUH_NOMI} NAMANGAN")
print("=" * 50)
print("✅ Bot muvaffaqiyatli ishga tushdi!")
print("📱 Telegramda botingizni ochib /start yozing")
print("=" * 50)

bot.infinity_polling()
