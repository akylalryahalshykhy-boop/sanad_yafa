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

# أمر البدء مع الترحيب
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "✨ **أهلاً بك في عالم يافا الذكي!**\n\n"
        "أنا هنا لمساعدتك في أي استفسار.\n"
        "💡 *تذكر: يرجى الاشتراك في قناتنا للاستفادة من كل جديد.*"
    )

# الرد الذكي على أي رسالة
@app.on_message(filters.text & ~filters.command(["start"]))
async def ai_chat(client, message):
    # إظهار حالة "جاري الكتابة..."
    await client.send_chat_action(message.chat.id, "typing")
    
    try:
        chat_completion = client_groq.chat.completions.create(
            messages=[{"role": "user", "content": message.text}],
            model="llama3-8b-8192",
        )
        reply = chat_completion.choices[0].message.content
        await message.reply_text(reply)
    except Exception as e:
        await message.reply_text("عذراً، حدث خطأ تقني بسيط في محرك الذكاء الاصطناعي. حاول مرة أخرى.")

app.run()
