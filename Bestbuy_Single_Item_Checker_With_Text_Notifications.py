from requests_html import  HTMLSession
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
from playsound import playsound

def get_page_html(url):
    session = HTMLSession()
    page = session.get(url)
    page.html.render(timeout=60)
    html_text = page.text
    return html_text

def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    results = soup.find('span', class_='availabilityMessage_ig-s5 container_3LC03')
    stock = results.text
    return stock

def setup_twilio_client():
    account_sid = 'AC0df6e81b84bbe66ff871892117138002'
    auth_token = 'dd1d15020a019eaf19b1b299ebe469c6'
    return Client(account_sid, auth_token)

def send_notification():
    twilio_client = setup_twilio_client()
    twilio_client.messages.create(
        body="3060ti Back in Stock Hurry!",
        from_='########',
        to='#########'
    )
    while True:
        playsound('buy.mp3')

def check_inventory():
    url = "https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3060-ti-8gb-gddr6-video-card/15166285"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html) == "Available to ship":
        send_notification()
    else:
        print("out of stock")

while True:
    check_inventory()
    time.sleep(30)





