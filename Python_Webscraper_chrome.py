from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#Loops program untill an item is found in stock
while True:
    # Set config options for chrome webdriver
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    # Specify path to driver on your local machine
    DRIVER_PATH = 'PATH_TO_DRIVER_ON_YOUR_MACHINE'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

    # Set URL that you wish to scrape here
    driver.get('URL')

    time.sleep(15)
    a = 0

    # set xpath of general element you are searching for
    cards = driver.find_elements_by_xpath('//xpath')

    for each_card in cards:

        # Search for specific elements here
        card_name = each_card.find_elements_by_xpath('//xpath')[a]
        card_price = each_card.find_elements_by_xpath('//xpath')[a]
        card_available = each_card.find_elements_by_xpath('//xpath')[a]
        card_is_available = card_available.text

        # Check if item is available and print output
        if card_is_available != "Coming soon" and card_is_available != "Sold out online":
            print(card_name.text)
            print('Is In Stock!!!')
            driver.quit()
            quit()

        else:
            print(card_name.text)
            print(card_price.text)
            print(card_available.text, '\n')

        a = a + 1

    driver.quit()


