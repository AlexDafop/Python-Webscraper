Python-Webscraper
Some python code that scrapes a webpage using Selenium

Hello! I created this project initially to scrape website to try to find stock on the new 30 series graphics cards but I figured this code could be easily adopted to scrape any website.

There are currently two versions of this program. The first version "Bestbuy_Single_Item_Checker_With_Text_Notifications" only checks the stock availability of a single item from what ever BestBuy URL you give it. In this case its checking stock on a Nvidia 3060Ti Founders edition. The URL and class search can be changed for any item you wish to check stock for on the website.

If you wish to receive a SMS from the program when the item comes in stock you must register for a free Twilio account. Follow their python QuickStart guide here on how to get setup https://www.twilio.com/docs/sms/quickstart/python

You can also add an mp3 file of your choice to play when the program detects an item in stock.



My second version of the program is the one I’m currently working on and is very unfinished, but it does work. "Python_Webscraper_chrome" uses a headless chrome browser with Selenium to get the page information. In the current version it checks the BestBuy stock for all 3060Ti and 3070 models. It prints the name, price and availability status of the card and stops the program if it finds one in stock. With a couple of modifications this script could be changed to work for many different products. 

I'm currently in the process of updating this second program to make it run better but for now it does work as a proof of concept.

You must have the chromedriver installed. 



