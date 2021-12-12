import yfinance as fy
import pandas as import pd
import os
from twilio.rest import Client



df = pd.read_csv('companylist.csv')

print(df['Symbol'])

upSymbols = []

for stock in df['Symbol']:
    stock = stock.upper()
    if '^' in stock: #ignoring formatting problems in the .csv file
        pass
    else:
        try:
            stock_info = yf.Ticker(stock)

            history = stock_info.history(period="5d")

            prevAverageVol = history['Volume'].iloc[1:4:1].mean()

            today_vol = history['Volume'][-1]

            if today_vol > prevAverageVol * 3 :

                upSymbols.append(stock)

            except:

                pass
                AC265bd9d2ca73e357c8c04625f8939c18
                AC7d88d0d26a1146dc0f61f67c22d65550

print(upSymbols)

str1 = ''.join(upSymbols)

MY_PHONE_NUMBER= #redacted

TWILIO_AUTH_TOKEN= #redacted

TWILIO_ACCOUNT_SID= #redacted


account_sid = os.environ["TWILIO_ACCOUNT_SID"]

auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

client.messages.create(

    to=os.environ["MY_PHONE_NUMBER"]

    from_="+16728001634"

    body=str1


)
