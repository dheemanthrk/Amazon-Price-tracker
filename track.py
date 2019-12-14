import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/Apple-MR972HN-15-4-inch-i7-8850H-Integrated/dp/B07G49GQ56/ref=sr_1_4?keywords=macbook+pro&qid=1576257615&sr=8-4"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}

page = requests.get(URL,headers=headers)

soup = BeautifulSoup(page.content,'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
convert=float(price[1:])

if(convert < 220000.00):
        send_mail()
print(convert)
print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.echlo()
    server.startlist()
    server.ehlo()

    server.login('youremail@gmail.com','Two_step_authentication_password')

    subject = 'Price fell down !!'
    body = "Here's the link https://www.amazon.in/Apple-MR972HN-15-4-inch-i7-8850H-Integrated/dp/B07G49GQ56/ref=sr_1_4?keywords=macbook+pro&qid=1576257615&sr=8-4"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('dheemanthkumawat22@gmail.com','dheemanthkumawat22@gmail.com',msg)#The from and to emails are same in this case

    print("Check your email !!")

    server.quit()
