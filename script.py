from twilio.rest import Client

account_sid = 'AC68dd6fb818a70751f9f8a5af3235'       #Replace with your account_sid
auth_token = '0d9c4274fea8fc95aXXXXXXXX'          #Replace with your auth_token

client = Client(account_sid, auth_token)

def callmsg():    
    call = client.calls.create(
          from_='+17146604658',     #Replace with the phone number that you got from Twilio
          twiml='<Response><Say>Reminder to take your Pill at 7:17 P.M.</Say></Response>',
          to='+918285XXXXXX'    #Phone number that you add on Twilio
    )
  
print(call.sid)
