from pyrogram import Client, filters
import config

# إنشاء البوت مباشرة بدون أي إضافات مخفية
app = Client(
    "Sanad_Yafa_Bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# أمر الترحيب المباشر
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("أهلاً بك في بوت سناد يافا! البوت يعمل الآن بنجاح.")

print("البوت يعمل الآن..")
app.run()
