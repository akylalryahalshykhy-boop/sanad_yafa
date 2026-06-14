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

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "✨ **أهلاً بك في عالم يافا الذكي!**\n\n"
        "أنا جاهز للرد على أسئلتك.\n"
        "💡 [اشترك في قناة عالم يافا الرقمي](https://t.me/Yaffa_Digital_World)"
    )

@app.on_message(filters.text & ~filters.command(["start"]))
async def ai_chat(client, message):
    await client.send_chat_action(message.chat.id, "typing")
    
    try:
        # الصيغة الصحيحة لاستدعاء مكتبة groq
        chat_completion = client_groq.chat.completions.create(
            messages=[{"role": "user", "content": message.text}],
            model="llama3-8b-8192",
        )
        
        # استخراج النص بشكل آمن
        reply = chat_completion.choices[0].message.content
        await message.reply_text(reply)
        
    except Exception as e:
        # في حال حدوث أي خطأ، سنعرفه من هنا
        await message.reply_text(f"خطأ برمجي: {str(e)}")

app.run()
