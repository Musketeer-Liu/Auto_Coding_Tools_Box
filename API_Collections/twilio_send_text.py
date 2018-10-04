from twilio import rest
from twilio.rest import TwilioRestClient

account_sid = "AC4710aacb5474f09a0995e65b5e00d2f7" # Your Account SID from www.twilio.com/console
auth_token  = "7a60c33324802c3a702390221f058ef0"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello, world! This is Yutong from Silicon Valley",
    to="+19795710648",    # Replace with your phone number
    from_="+14157874506") # Replace with your Twilio number

print(message.sid)
