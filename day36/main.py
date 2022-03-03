import requests


STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_VANTAGE_APIKEY = "****************"
NEWS_APIKEY = "********************************"


def telegram_bot_send_text(bot_message):
    bot_token = "**********************************************"
    bot_chatID = "**********"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID \
                + '&parse_mode=Markdown&text=' + bot_message
    bot_response = requests.get(send_text)
    return bot_response.json()


def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        performance = round(abs(current - previous) / previous, 5) * 100.0
        print(performance)
        return performance
    except ZeroDivisionError:
        return 0


alpha_vantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_APIKEY,
}

news_api_parameters = {
    "q": f"{STOCK_NAME} Market Update",
    "pageSize": 3,
    "apiKey": NEWS_APIKEY,
}

alpha_vantage_response = requests.get(STOCK_ENDPOINT, params=alpha_vantage_parameters)
alpha_vantage_response.raise_for_status()
stock_data = alpha_vantage_response.json()

news_api_response = requests.get(NEWS_ENDPOINT, params=news_api_parameters)
news_api_response.raise_for_status()
news_data = news_api_response.json()

closing_prices = []
for _, date in zip(range(3), stock_data['Time Series (Daily)']):
    closing_prices.append(stock_data['Time Series (Daily)'][date]['4. close'])
yd_price = float(closing_prices[0])
dyd_price = float(closing_prices[1])

difference = yd_price - dyd_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if get_change(yd_price, dyd_price) >= 5:
    for article in range(3):
        market_performance = []
        news_headlines = []
        news_description = []
        market_performance.append(f"{STOCK_NAME}: {up_down} {get_change(yd_price, dyd_price)}% ")
        news_headlines.append(f"Headline: {news_data['articles'][article]['title']}")
        news_description.append(f"Description: {news_data['articles'][article]['description']}")
        news = (market_performance + news_headlines + news_description)
        joined_string = "\n".join(news)
        telegram_bot_send_text(f"{joined_string}")
