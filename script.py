from twilio.rest import Client 
 
account_sid = 'ACa1fe3d0103fcb468cbb0e3153b74c69e' 
auth_token = '7dcba0e469f5c62df14d503d3a6d0420' 
client = Client(account_sid, auth_token) 
 
def msg():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Your appointment is coming up on July 21 at 3PM',      
                                to='whatsapp:+918285671810' 
                            ) 
        
    print(message.sid)