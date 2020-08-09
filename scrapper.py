# pull out data from a url (similar to request)
import requests
from bs4 import BeautifulSoup
import time

# Enables to send emails
import smtplib


URL = "https://www.amazon.in/WeCool-X2-Innovative-Bluetooth-Waterproof/dp/B07ZFTP69L/ref=sr_1_1_sspa?crid=1FY68HZC62ALM&dchild=1&keywords=bluetooth+earpods+wireless&qid=1596978394&sprefix=bluetooth+earpods%2Caps%2C781&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFEQVlRSjBVWlZJNTUmZW5jcnlwdGVkSWQ9QTA2Njk0Njg5SjNaRllUSjFWOEsmZW5jcnlwdGVkQWRJZD1BMDAxMzMxODNRMFZDVDQzVllSOUYmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)

    # to establish connection between two email servers => ehlo
    server.ehlo()

    server.starttls()
    server.ehlo()
    server.login("meemusiri@gmail.com", "wxvnxppoldikelew")

    subject = "Price fell down"
    body = "Check the amazon link: https://www.amazon.in/WeCool-X2-Innovative-Bluetooth-Waterproof/dp/B07ZFTP69L/ref=sr_1_1_sspa?crid=1FY68HZC62ALM&dchild=1&keywords=bluetooth+earpods+wireless&qid=1596978394&sprefix=bluetooth+earpods%2Caps%2C781&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFEQVlRSjBVWlZJNTUmZW5jcnlwdGVkSWQ9QTA2Njk0Njg5SjNaRllUSjFWOEsmZW5jcnlwdGVkQWRJZD1BMDAxMzMxODNRMFZDVDQzVllSOUYmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail("meemusiri@gmail.com", "meera.mukundrao@gmail.com", msg)

    print("HEY EMAIL HAS BEEN SENT!!!")
    server.quit()


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html5lib")

    title = soup.find(id="titleSection").get_text(strip=True)
    converted_price = soup.find(id="priceblock_ourprice").get_text(strip=True)

    # Getting rid of , in string
    converted_price = converted_price.replace(",", "")
    # Getting rid of rupee symbol and and extra space
    converted_price = converted_price.replace(converted_price[0], "")
    converted_price = converted_price.replace(converted_price[0], "")

    # converting final reduced string to float
    price = float(converted_price)

    if price < 3000.00:
        send_mail()


# print(title)
while True:
    check_price()
    time.sleep(3600 * 7)
