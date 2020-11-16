# importing all required libraries 
from telethon.sync import TelegramClient
from telethon import functions, types
from time import sleep

# app/account information

api_id = 'api_id'
api_hash = 'api_hash'
token = 'bot_token'
#or 
#phone = 'phone number'

# connect and send the message, sleep and repeat

with TelegramClient('session', api_id, api_hash) as client:
    while True:
        client.send_message("username", "message")
        
        #wait 24 hours / 86400
        
        sleep(number_of_seconds)
        
#printing results
#print(result.stringify())    
        
#disconnect
#client.disconnect() 
