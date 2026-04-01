import requests
import time

# Your Render URL (without /whatsapp)
url = "https://your-bot-name.onrender.com"

while True:
    try:
        requests.get(url)
        print("Pinged bot to keep alive!")
    except Exception as e:
        print("Failed to ping:", e)
    time.sleep(60)  # wait 1 minute
