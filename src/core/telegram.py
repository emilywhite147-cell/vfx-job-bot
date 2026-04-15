import os
import requests

def send_telegram_message(text: str):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Missing Telegram env vars")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    r = requests.post(url, data={
        "chat_id": chat_id,
        "text": text
    })

    print("TELEGRAM RESPONSE:", r.text)
