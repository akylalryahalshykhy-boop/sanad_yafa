from pyrogram import Client, filters
from groq import Groq
import config

# إعداد البوت
app = Client(
    "Sanad_Yafa_Bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# إعداد محرك الذكاء الاصطناعي
client_groq = Groq(api_key=config.GROQ_API_KEY)

# أمر البدء مع رابط قناتك
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "✨ **أهلاً بك في عالم يافا الذكي!**\n\n"
        "أنا هنا لمساعدتك في أي استفسار تقني أو عام.\n"
        "💡 **اشترك في قناتنا ليصلك كل جديد:** [عالم يافا الرقمي](https://t.me/Yaffa_Digital_World)"
    )

# الرد الذكي على الرسائل
@app.on_message(filters.text & ~filters.command(["start"]))
async def ai_chat(client, message):
    # إظهار حالة "جاري الكتابة..." للمستخدم
    await client.send_chat_action(message.chat.id, "typing")
    
    try:
        # إرسال النص إلى نموذج Llama 3 عبر Groq
        chat_completion = client_groq.chat.completions.create(
            messages=[{"role": "user", "content": message.text}],
            model="llama3-8b-8192",
        )
        # إرسال الرد الذكي
        await message.reply_text(chat_completion.choices[0].message.content)
    except Exception as e:
        # في حال وجود خطأ تقني
        print(f"Error: {e}")
        await message.reply_text("عذراً، المحرك الذكي يحتاج لحظة للراحة. حاول مجدداً بعد قليل.")

# تشغيل البوت
app.run()
