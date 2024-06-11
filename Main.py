URL = "https://www.amazon.com.mx/Performance-Proteina-proteina-Inflamacion-Porciones/dp/B085WCH3D8/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.aPMvMOtUeWKcwmwD1Lfzi_mh1ITakjOsgWZTIisr3TLwH8xt2Oaicg4esUuES3BK7mbE4M-d-b7V0tQ3jcKcBhuJTnBN_egVv1oadY1Pio3ZveO5r9MnmwDbZV6rHPJ4fbfcSlZfDDeHL9jts195X53ldIt1LWfU0wrTZJ3-aNK3o6o8gaqHUHTWCceOcD5VgbZpoXJrerDNoJvZNwcYTHHgylgSNoN1c8MqrI_-tLBtXVer__B4z6dFpLFE2d5TTC9cNB4fTRZHjtXDtmWI6M_9kCEkMDMU667OEU-RAU8.nciWnaoiBwcFc91Mih-VvlQmEeE8qDt66EyKMxVexrk&dib_tag=se&keywords=creatina&qid=1718121408&sr=8-2-spons&ufe=app_do%3Aamzn1.fos.242f5c11-6cfd-40d6-91f6-be3d1974080c&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
from bs4 import BeautifulSoup
import requests
import smtplib

REGULAR_PRICE = 749

"""USE YOUR OWN CREDENCTIALS"""
PersonalEmail = "personalEmail.gmail"
Password = "XXXX XXXX XXXX XXXX"
Address = "addresemail.gmailoutlook.com"

"""SEND NOTIFICATION TO SMS or WHATSAPP??"""
from twilio.rest import Client
TWILIO_SID = "SID"
TWILIO_TOKEN = "TOKEN"

DataResponse = requests.get(URL)
"""LETS CHECK IF WE HAVE CONNECTION TO PAGE AMAZON"""
print(DataResponse.status_code)

"""PARSING HTML TO PYTHON"""
PriceTracker = DataResponse.text
NewPrice = BeautifulSoup(PriceTracker, 'html.parser')

"""WANT TO SEE ALL CODE FROM WEB PAGE??? Uncomment next line! """
#print(BeautifulSoup.prettify(NewPrice))

"""I WANT THE PRODUCT NAME SO WE SELECT THE ID TAG"""
TitleProduct = NewPrice.select_one("#productTitle").getText()

"""LETS COMPARE THR FINAL PRICE TO CHECK IF THERES ANY DISCOUNT OF IT"""
CurrentPrice = NewPrice.find(name="span",class_="a-offscreen")
DatePrice = CurrentPrice.getText().split("$")[1]
print(DatePrice)

if float(DatePrice) < REGULAR_PRICE:
    print("Enviando Mensaje")
    message = f"{TitleProduct} is now ${DatePrice}"
    Connection = smtplib.SMTP("smtp.gmail.com")
    Connection.starttls()
    Response = Connection.login(PersonalEmail, Password)
    Connection.sendmail(
        from_addr=PersonalEmail,
        to_addrs=Address,
        msg=f"Subject: Amazon Price Alert!!!\n\n{message}".encode("utf-8")
    )

    """SEND SMS"""
    NewClient = Client(TWILIO_SID, TWILIO_TOKEN)
    NewClient.messages.create(body=message,
                              from_="TWILIO NUMBER",
                              to="PERSONAL NUMBER")


