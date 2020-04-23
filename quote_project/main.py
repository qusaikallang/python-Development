#!/usr/bin/python
from twilio.rest import Client
import requests

def sendmsg():
    id = "ACa494d07d504d5e436f1de3bba4fbb72e"
    token = "7e742551fc1d446c09b15f9f2816b0ca"
    Quote = ''
    By = ''
    proxies = {'https':'178.128.93.68:44344'}
    try:
        url = 'https://quotes.rest/qod'
        response = requests.get(url,proxies=proxies).json()
        Quote = response['contents']['quotes'][0]['quote']
        By = response['contents']['quotes'][0]['author']
    except Exception:
        exit(0)

    client = Client(id,token)

    sms = client.messages.create(body='Quote: '+Quote+'\nBy: '+By,from_="+12058505361",to='+919370480627')


sendmsg()
