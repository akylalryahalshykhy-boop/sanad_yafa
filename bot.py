from pyrogram import Client, filters
from groq import Groq
import config

app = Client(
    "Sanad_Yafa_Bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

client_groq = Groq(api_key=config.GROQ_API_KEY)

# ترحيب خاص
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "✨ **أهلاً بك في عالم يافا الذكي!**\n\n"
        "أنا هنا لمساعدتك، اسألني أي شيء.\n"
        "💡 [عالم يافا الرقمي](https://t.me/Yaffa_Digital_World)"
    )

# الكود الحاسم: الرد على أي نص غير الأوامر
@app.on_message(filters.text & ~filters.command(["start"]))
async def handle_all_messages(client, message):
    # إظهار حالة جاري الكتابة
    await client.send_chat_action(message.chat.id, "typing")
    
    try:
        # محاولة الحصول على رد من الذكاء الاصطناعي
        completion = client_groq.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": message.text}]
        )
        reply_text = completion.choices[0].message.content
        await message.reply_text(reply_text)
    except Exception as e:
        # إظهار الخطأ إذا حدث لتعرف السبب
        await message.reply_text(f"حدث خطأ في المعالجة: {str(e)}")

app.run()
