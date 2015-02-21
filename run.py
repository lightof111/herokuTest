from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml
app = Flask(__name__)
 
# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route('/abcd')
def caller():
	response = 'hi'
	return str(response) 

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

@app.route('/twilio')
def sendMessage():
	account_sid = "ACd9ea80cb5247395f43f6b1eea438b8dc"
	auth_token = "10736f5b33ef8e1855961379b2cb67b3"
	client = TwilioRestClient(account_sid, auth_token)
 	body = "sup"
 	cem = "+14152983952"
 	alan = "+17329252682"
	message = client.messages.create(to=alan, from_="+17324791835",
                                     body=body)
	return "message sent " + body

if __name__ == "__main__":
    app.run(debug=True)

