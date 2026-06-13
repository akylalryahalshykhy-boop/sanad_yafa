from pyrogram import Client, filters
import config

app = Client(
    "Sanad_Yafa_Bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("أهلاً بك في بوت سند يافع! البوت يعمل الآن بنجاح.")

print("سند يافع يعمل الآن..")
app.run()
