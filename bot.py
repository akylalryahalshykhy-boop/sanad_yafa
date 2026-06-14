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

client_groq = Groq(api_key=config.GROQ_API_KEY)

# 1. الاستجابة للأوامر (مثل /start)
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "✨ **أهلاً بك في عالم يافا الذكي!**\n\n"
        "أنا جاهز لمساعدتك. اكتب لي أي سؤال وسأجيبك.\n"
        "💡 [اشترك في قناة عالم يافا الرقمي](https://t.me/Yaffa_Digital_World)"
    )

# 2. الاستجابة لأي رسالة نصية (هذا هو الجزء الذي كان ينقصك)
@app.on_message(filters.text & ~filters.command(["start"]))
async def ai_responder(client, message):
    # إظهار حالة "جاري الكتابة" ليعرف المستخدم أن البوت يعمل
    await client.send_chat_action(message.chat.id, "typing")
    
    try:
        # إرسال الرسالة لمحرك الذكاء الاصطناعي
        chat_completion = client_groq.chat.completions.create(
            messages=[{"role": "user", "content": message.text}],
            model="llama3-8b-8192",
        )
        # إرسال الرد للمستخدم
        await message.reply_text(chat_completion.choices[0].message.content)
    except Exception as e:
        # إذا فشل الاتصال بـ Groq، البوت سيخبرك بالسبب
        await message.reply_text(f"⚠️ خطأ تقني: {str(e)}")

app.run()
