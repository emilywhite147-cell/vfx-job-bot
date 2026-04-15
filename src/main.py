import os
import requests

def send():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    print("TOKEN:", token)
    print("CHAT_ID:", chat_id)

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    r = requests.post(url, data={
        "chat_id": chat_id,
        "text": "🔥 TEST MESSAGE FROM GITHUB ACTIONS"
    })

    print(r.text)

if __name__ == "__main__":
    send()
