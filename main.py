import threading
import time
import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# 🔹 Your bot responses
demo_responses = {
    "hi": "👋 Hello! Welcome to CY.COM \n It is Easter! We have amazing deals for everyone of you. Hurry now and visit our stores. Offers ends soons!\n\Choose an option:\n1️⃣ Services\n2️⃣ Pricing\n3️⃣ Contact\n4️⃣ About Us",
    "1": "🚀 Our services include:\n• Phone Accesories\n• Phone Repairs\n• Latest Gadgets\n\nReply 0️⃣ to go back.",
    "2": "💼 Our pricing is flexible based on your needs.\n\nVisit our website at www.cygroup.ng\n\nReply 0️⃣ to go back.",
    "3": "📞 Contact us at:\nETAAGBO OFFICE: 07038323998\nETIM EDEM OFFICE: 08139252810\n\nReply 0️⃣ to go back.",
    "4": "🏆 CY.com is a leading phone accesories solution provider.We deliver nationwide\n\nReply 0️⃣ to go back.",
    "0": "🔁 Back to menu:\n1️⃣ Services\n2️⃣ Pricing\n3️⃣ Contact\n4️⃣ About Us"
}

# 🔹 WhatsApp webhook
@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()

    reply = demo_responses.get(
        incoming_msg,
        "❌ Sorry, I didn’t understand that.\n\nReply with 1, 2, 3, or 4."
    )

    resp.message(reply)
    return str(resp)

# 🔹 Home route (important for keep-alive)
@app.route("/")
def home():
    return "Bot is alive!"

# 🔹 Keep-alive function
def keep_alive():
    while True:
        try:
            requests.get("https://cy-whatsapp-bot.onrender.com")
            print("Pinged self to stay awake")
        except Exception as e:
            print("Ping failed:", e)
        time.sleep(60)  # every 1 minute

# 🔹 Start keep-alive in background
threading.Thread(target=keep_alive).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
