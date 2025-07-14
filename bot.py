
import telebot

# توكن البوت الخاص بك
TOKEN = "8167724498:AA...1C1ao"

# إنشاء البوت
bot = telebot.TeleBot(TOKEN)

# قائمة كلمات والردود الخاصة بها
keywords = {
    "سجاد": "ها سجاد ☺️",
    "السلام": "وعليكم السلام 🌟",
    "شلونك": "تمام وانت؟ 😁",
    "بايثون": "لغة رائعة 🧑‍💻",
    "كود": "اكيد، اسألني أي شيء",
    "البرمجة": "فن وعلم 💡",
    "ترجمة": "هل تريد ترجمة كلمة؟",
    "الذكاء": "الذكاء الاصطناعي يتطور 🔍",
    "HTML": "لغة لبناء صفحات الويب 🌐",
    "CSS": "لتنسيق تصميم المواقع 🎨",
    "API": "وسيلة لتبادل البيانات بين الأنظمة 🔗",
    "PDF": "هل تريد إنشاء أو تعديل PDF؟",
    "ملف": "ارسل لي الملف وسأساعدك!",
    "تحويل": "هل تريد تحويل الملف إلى صيغة أخرى؟",
    "تعلم": "Practice makes perfect! 📘",
    "شكراً": "العفو ❤️"
    # أضف أكثر من 100 كلمة حسب ما تحتاج
}

# عند استقبال رسالة
@bot.message_handler(func=lambda message: True)
def reply_keywords(message):
    user_input = message.text.strip().lower()
    for keyword, response in keywords.items():
        if keyword in user_input:
            bot.reply_to(message, response)
            break

# تشغيل البوت
bot.polling()
