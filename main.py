import requests
import os
import random
import string
import json


url= 'https://dpd.package-id.com/main/final.action.php'

Chars= string.ascii_letters + string.digits + '!@£$%&()'
random.seed = (os.urandom(1024))

CreditCards= json.loads (open('Card no.json').read())

FirstNames = json.loads (open('FirstName.json').read())
LastNames = json.loads (open('LastNames.JSON').read())

for CreditCard in CreditCards:
    #Fetch Credit card information
    CreditCardNo = str(CreditCard['CreditCard']['CardNumber'])
    CardIssuer = CreditCard['CreditCard']['IssuingNetwork']
    CreditCardNo_Formatted = ' - '.join(CreditCardNo[i:i+4]for i in range (0,len(CreditCardNo),4))
    #Create Account Holder Info:
    FirstName = random.choice(FirstNames)
    LastName = random.choice(LastNames)

    #build csv code
    if CardIssuer == "American Express":
        csv_floor = 1000
        csv_cap = 9999
    else:
        csv_floor= 100
        csv_cap = 999
    csv_code = (random.sample(range(csv_floor,csv_cap),1))[0]
    #build Card Expiry
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    month = random.choice(months)
    year= (random.sample(range(22,27),1))[0]
    cardexpiry = str(month) +'/'+ str(year)
    #build email address
    domains = ['@outlook.com','@yahoo.com','@aol.com','@gmail.com','@msn.com','@hotmail.com']
    user_extra = ''.join(random.choices(Chars, k=2))
    mail= FirstName.lower()+user_extra+random.choice(domains)

    payload = {
        'fullname': f'{FirstName}  {LastName}',
        'email': f'{mail}',
        'phone': '',
        'address': '',
        'postcode': '',
        'dob': '',
        'town': '',
        'county': '',
        'cardname': f'{FirstName}  {LastName}',
        'cardnumber': f'{CreditCardNo_Formatted}',
        'cardexpiry': f'{cardexpiry}',
        'cardsecurity': f'{csv_code}',
        'account': '',
        'sortcode': '',
    }

    response = requests.post (url, data=payload)
    print(FirstName,LastName)
    print(mail)
    print ('Card Issuer:', CardIssuer )
    print('Credit Card Number:', CreditCardNo_Formatted)
    print('csv code is:', csv_code)
    print("card expiry date is:", cardexpiry )
    print ('-------------------------------------------------------------')
    print(response)