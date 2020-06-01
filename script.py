from twilio.rest import Client 
 
account_sid = 'Your account_sid here' 
auth_token = 'Your auth_token here' 
client = Client(account_sid, auth_token) 
 
def msg():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Your appointment is coming up on July 21 at 3PM',      
                                to='whatsapp:+918285671810' 
                            ) 
        
    print(message.sid)
