import os

print("TOKEN RAW:", repr(os.getenv("TELEGRAM_BOT_TOKEN")))
print("CHAT ID:", repr(os.getenv("TELEGRAM_CHAT_ID")))
