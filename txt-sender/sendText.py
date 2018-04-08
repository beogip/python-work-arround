from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7c075270af40b12dabcafe4b86097c9b"
# Your Auth Token from twilio.com/console
auth_token = ""
# Your destination number
toNumber = ""
# Your Twilio number
fromNumber = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
    to=toNumber,
    from_=fromNumber,
    body="Hello from Python!")

print(message.sid)
