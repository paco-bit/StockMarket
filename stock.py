import requests
API_ENDPOINT="https://www.alphavantage.co/query"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#Parameters for this file
STOCK_PARAMETERS = {
        "function": 'TIME_SERIES_DAILY_ADJUSTED',
        "symbol": STOCK,
        "apikey": 'OAW8Z8C8ATTGK8PF',
}

r = requests.get(API_ENDPOINT, STOCK_PARAMETERS)
data = r.json()

print(data)


## replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=OAW8Z8C8ATTGK8PF'
#
#with requests.Session() as s:
#    download = s.get(CSV_URL)
#    decoded_content = download.content.decode('utf-8')
#    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#    my_list = list(cr)
#    for row in my_list:
#        print(row)
#
## My VARIABLES
#
#
#

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
