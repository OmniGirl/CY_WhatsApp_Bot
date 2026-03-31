import time
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

demo_responses = {
    "hi": "Hello! Welcome to CY.com demo. Choose an option:\n1. Services\n2. Pricing\n3. Contact\n4. About Us",
    "1": "Our services include Phone Repairs, Phone Accessories, and Latest Gadgets. Reply 0 to go back.",
    "2": "Our pricing is flexible based on your needs Visit www.cygroup.ng. Reply 0 to go back.",
    "3": "You can contact us on ETAAGBOR OFFICE 07038323998 ETIM EDEM OFFICE 08139252810. Reply 0 to go back.",
    "4": "CY.com is a leading phone accesories solution provider. Reply 0 to go back.",
    "0": "Choose an option:\n1. Services\n2. Pricing\n3. Contact\n4. About Us"
}

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    
    # Simulate "typing" delay
    time.sleep(1.5)
    
    reply = demo_responses.get(incoming_msg, "Sorry, I didn't understand that. Reply 0 to go back.")
    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
