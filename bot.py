# الرد الذكي مع كشف الأخطاء
@app.on_message(filters.text & ~filters.command(["start"]))
async def ai_chat(client, message):
    await client.send_chat_action(message.chat.id, "typing")
    
    try:
        # إضافة طباعة للتأكد من أن الرسالة وصلت للكود
        print(f"User message: {message.text}")
        
        chat_completion = client_groq.chat.completions.create(
            messages=[{"role": "user", "content": message.text}],
            model="llama3-8b-8192",
        )
        reply = chat_completion.choices[0].message.content
        await message.reply_text(reply)
        
    except Exception as e:
        # إذا حدث خطأ، سيرسله البوت لك في المحادثة مباشرة
        await message.reply_text(f"⚠️ خطأ تقني: {str(e)}")
