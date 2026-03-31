from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

demo_responses = {
    "hi": "Hello! Welcome to CY.com demo. Choose an option:\n1. Services\n2. Pricing\n3. Contact\n4. About Us",
    "1": "Our services include A, B, and C. Reply 0 to go back.",
    "2": "Our pricing is flexible based on your needs. Reply 0 to go back.",
    "3": "You can contact us at contact@cy.com. Reply 0 to go back.",
    "4": "CY.com is a leading phone accesories solution provider. Reply 0 to go back.",
    "0": "Choose an option:\n1. Services\n2. Pricing\n3. Contact\n4. About Us"
}

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    reply = demo_responses.get(incoming_msg, "Sorry, I didn't understand that. Reply 0 to go back.")
    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
