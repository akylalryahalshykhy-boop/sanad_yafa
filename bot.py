import os
from pyrogram import Client, filters
from groq import Groq

# قراءة المفاتيح من متغيرات البيئة
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

app = Client("Sanad_Yafa_Bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
client_groq = Groq(api_key=GROQ_API_KEY)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("✨ أهلاً بك! أنا جاهز للرد على أسئلتك.")

@app.on_message(filters.text & ~filters.command(["start"]))
async def ai_chat(client, message):
    await client.send_chat_action(message.chat.id, "typing")
    try:
        chat_completion = client_groq.chat.completions.create(
            messages=[{"role": "user", "content": message.text}],
            model="llama3-8b-8192",
        )
        await message.reply_text(chat_completion.choices[0].message.content)
    except Exception as e:
        await message.reply_text(f"خطأ: {str(e)}")

app.run()
