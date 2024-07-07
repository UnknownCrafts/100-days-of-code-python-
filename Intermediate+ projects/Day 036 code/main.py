import requests
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
twilio_account_id = "" # Your twillio account id
twillio_auth_token = "" # Your twillio auth token
twillio_number = "+" # Your twillio number, numbers start with the country code, you could also use twillio whastapp number here
your_number = "+" # Your personal phone number, numbers start with the country code, you could also use your whastapp number here if twillio is sending via whatsapp


alphavantage_endpoint = "https://www.alphavantage.co/query"
alphavantage_api_key = "" # Put your api key here

newsapi_endpoint = "https://newsapi.org/v2/everything"
newsapi_key = "" # Put your api key here

alphavantage_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": alphavantage_api_key,
}

newsapi_params = {
    "q": COMPANY_NAME,
    "apiKey": newsapi_key,
    "sortBy": "popularity",
}

# Requesting for stock data
stock_request = requests.get(alphavantage_endpoint, params=alphavantage_params)
stock_request.raise_for_status()
stock_data = stock_request.json()["Time Series (Daily)"]
stock_data_dates = stock_data.keys()
yesterday_price = float(stock_data[stock_data_dates[0]]["5. adjusted close"])
day_before_yesterday_price = float(stock_data[stock_data_dates[1]]["5. adjusted close"])

percent_change = 0
arrow_type = "🔻"

if yesterday_price >= day_before_yesterday_price:
    percent_change = round(((yesterday_price - day_before_yesterday_price)/day_before_yesterday_price)*100, 3)
    arrow_type = "🔺"
else:
    percent_change = round(((day_before_yesterday_price - yesterday_price)/day_before_yesterday_price)*100, 3)

# Requesting for news data
news_request = requests.get(newsapi_endpoint, params=newsapi_params)
news_request.raise_for_status()
news_data = news_request.json()["articles"][0]
headline = news_data["title"]
brief =  news_data["description"]

# Sending sms
message = f"{STOCK}: {arrow_type}{percent_change}%\nHeadline: {headline}.\nBrief: {brief}."

client = Client(twilio_account_id, twillio_auth_token)
message = client.messages \
    .create(
        body=message,
        from=twillio_number,
        to=your_number
    )