from requests_html import  HTMLSession
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
from playsound import playsound

#Get the HTML of the defined page here and return it
def get_page_html(url):
    session = HTMLSession()
    page = session.get(url)
    html_text = page.text
    return html_text

#Parse the HTML, search for which ever class you wish and return text results inside class
def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    results = soup.find('span', class_='availabilityMessage_ig-s5 container_3LC03')
    stock = results.text
    return stock

#Setup Twilio notifications here. Only if you want to be texted a notification or alerted by a song
def setup_twilio_client():
    account_sid = 'account_sid here'
    auth_token = 'Auth_token here'
    return Client(account_sid, auth_token)

def send_notification():
    twilio_client = setup_twilio_client()
    twilio_client.messages.create(
        body="3060ti Back in Stock Hurry!",
        from_='########',
        to='#########'
    )
    while True:
        playsound('.mp3 file of your choice')

#Define URL to search here
def check_inventory():
    url = "https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3060-ti-8gb-gddr6-video-card/15166285"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html) == "Available to ship":
        send_notification()
        print("Item is in stock!")
        quit()
    else:
        print("out of stock")

#Loop through program every 5 seconds
while True:
    check_inventory()
    time.sleep(5)





