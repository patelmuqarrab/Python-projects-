#I am going to use an API called text belt 
#Steps
# >install schedule
# >install requests

phone_number = input("Phone_number: ")
import requests
import schedule
import time

def m_send():
    resp = requests.post('https://textbelt.com/text', {
    'phone': '5555555555',
    'message': 'Wake up to Reality',
    'key': 'textbelt',
    })
    print(resp.json())

# schedule.every().day.at.('08:00').do(m_send)
schedule.every(5).seconds.do(m_send)

while True:
    schedule.run_pending()
    time.sleep(2)

  
