import logging
from pyrogram import Client, filters
from groq import Groq
import config

# إعداد السجلات لنعرف أين يتوقف البوت
logging.basicConfig(level=logging.INFO)

app = Client(
    "Sanad_Yafa_Bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

client_groq = Groq(api_key=config.GROQ_API_KEY)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("✨ أهلاً بك في عالم يافا الذكي! أنا جاهز للرد على أسئلتك.")

@app.on_message(filters.text & ~filters.command(["start"]))
async def ai_chat(client, message):
    try:
        # إظهار حالة جاري الكتابة
        await client.send_chat_action(message.chat.id, "typing")
        
        # الاتصال بـ Groq
        chat_completion = client_groq.chat.completions.create(
            messages=[{"role": "user", "content": message.text}],
            model="llama3-8b-8192",
        )
        
        reply = chat_completion.choices[0].message.content
        await message.reply_text(reply)
    except Exception as e:
        # في حال فشل الاتصال، سيظهر لك الخطأ هنا
        await message.reply_text(f"خطأ في الاتصال بالذكاء الاصطناعي: {str(e)}")

app.run()
