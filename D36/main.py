import requests
from datetime import datetime, timedelta
import smtplib
import os
ALPHA_VANTAGE_API_KEY = "HSG4O0PBU6ZIVI5S"
ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"
NEWSAPI_API_KEY = "88051ca9c9d24521a4a114348dc941ac"
NEWSAPI_URL = "https://newsapi.org/v2/everything"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_TO_SHOW = 3

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_PORT = 587
my_email = os.environ.get("ENV_MY_EMAIL")
my_password = os.environ.get("ENV_MY_PASSWORD")
receiver = "mek.chou@outlook.com"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_stock_data():
    parameter = {
        "function":"TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHA_VANTAGE_API_KEY, 
    }
    stock_request = requests.get(ALPHA_VANTAGE_URL, params=parameter)
    stock_request.raise_for_status()
    stock_data = stock_request.json()
    return stock_data

def check_stock_price(stock_data):
    today = datetime.now().date()
    yesterday = (today - timedelta(days=1)).isoformat()
    day_before_yesterday = (today - timedelta(days=2)).isoformat()
    yesterday_stock_price = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
    day_before_yesterday_stock_price = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])
    
    return (yesterday_stock_price, day_before_yesterday_stock_price)
    # return abs((yesterday_stock_price-day_before_yesterday_stock_price)/day_before_yesterday_stock_price) > 0.01

# if check_stock_price(get_stock_data()):
    # print("get news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_news():
    parameter = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAt", 
        "pageSize": NEWS_TO_SHOW,
        "apiKey": NEWSAPI_API_KEY,
    }
    request = requests.get(NEWSAPI_URL, params=parameter)
    request.raise_for_status()
    data = request.json()["articles"]
    return data

def parse_news(news):
    headline = news["title"]
    brief = news["description"]
    url = news["url"]
    return headline, brief, url
    
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def stock_performance(yesterday_stock_price, day_before_yesterday_stock_price):
    if yesterday_stock_price >= day_before_yesterday_stock_price:
        return f"UP {round(abs((yesterday_stock_price-day_before_yesterday_stock_price)/day_before_yesterday_stock_price)*100,2)}%"
    else:
        return f"DOWN{round(abs((yesterday_stock_price-day_before_yesterday_stock_price)/day_before_yesterday_stock_price)*100,2)}%"


def send_email(stock_performance, headline, brief, url):
    with smtplib.SMTP(host=GMAIL_SMTP, port=GMAIL_PORT) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver,
            # msg="test"
            msg=f"Subject: {STOCK} news:\n\n"\
            f"{stock_performance}\n"\
            f"Headline: {headline}\n"\
            f"Brief: {brief}\n"\
            f"Url: {url}"
        )

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

def main():
    stock_data = get_stock_data()
    (yesterday_price, day_before_yesterday_price) = check_stock_price(stock_data)
    if abs((yesterday_price-day_before_yesterday_price)/day_before_yesterday_price) >= 0.01:
        performance_text = f"{STOCK}: {stock_performance(yesterday_price, day_before_yesterday_price)}"
    # if True:
        for n in range(NEWS_TO_SHOW):
            (headline, brief, url) = (parse_news(get_news()[n]))
            send_email(performance_text, headline, brief, url)
            # send_email("performance_text", "headline", "brief", "url")
    # 
        # print(headline)
        # print(brief)
        
    # pass
    
if __name__ == "__main__":
    main()
    # check_stock_price(get_stock_data())
    # print(get_stock_data())

