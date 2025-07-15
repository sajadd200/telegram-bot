import smtplib
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
from flask import Flask
import threading

EMAIL = 'your_email@gmail.com'
PASSWORD = 'your_email_password'
SUBJECT = 'بلاغ تلقائي'
VICTIMS = [
    'stopCA@telegram.org',
    'abuse@telegram.org',
    'Support@telegram.org',
    'dmca@telegram.org'
]

def send_emails(count):
    message = f"""Subject  :  {SUBJECT}\n\nبلاغ لمجموعة تخالف سياسات تيليجرام، نرجو التعامل معها."""
    success = 0
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        for _ in range(count):
            for victim in VICTIMS:
                server.sendmail(EMAIL, victim, message)
                success += 1
        server.quit()
        return f"تم إرسال {success} رسالة بنجاح."
    except Exception as e:
        return f"حدث خطأ: {str(e)}"

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        count = int(context.args[0])
        await update.message.reply_text("يتم الآن إرسال البلاغات...")
        result = send_emails(count)
        await update.message.reply_text(result)
    except:
        await update.message.reply_text("يرجى استخدام الأمر هكذا: /report 5")

def start_bot():
    TOKEN = "8167724498:AAFvvWUjh2EbB9fIksHw4VVYo0ylT39C1ao"
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("report", report))
    print("تم تشغيل البوت.")
    app.run_polling()

# Flask endpoint لمنع إيقاف التطبيق على Render
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "البوت يعمل على Render!"

def run_web():
    web_app.run(host="0.0.0.0", port=10000)

def main():
    threading.Thread(target=start_bot).start()
    run_web()

if __name__ == "__main__":
    main()
