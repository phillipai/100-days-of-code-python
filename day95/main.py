import requests
import json
from datetime import datetime
import time
from random import randint

product_name = "RTX 3080 FE"
URL = "https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.standardproduct.v1%2Bjson&accept-language=en-CA&locations=938%7C202%7C617%7C203%7C57%7C926%7C977%7C233%7C930%7C927%7C62%7C622%7C931%7C245%7C207%7C954%7C795%7C916%7C910%7C544%7C932%7C237%7C200%7C965%7C990%7C956%7C943%7C937%7C942%7C223%7C985%7C925&postalCode=M8W&skus=15463567"

headers = {
    'authority': 'www.bestbuy.ca',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4159.2 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/15463567',
    'accept-language': 'en-US,en;q=0.9'
}


def main():
    quantity = 0
    attempt = 0

    while quantity < 1:
        response = requests.get(URL, headers=headers)
        response_formatted = json.loads(response.content.decode('utf-8-sig').encode('utf-8'))

        quantity = response_formatted['availabilities'][0]['shipping']['quantityRemaining']

        if quantity < 1:
            print(f"Time: {datetime.now()} | Attempt: {attempt}")
            attempt += 1
            # time.sleep(randint(0, 5))
        else:
            print(f"🚨 {product_name} available to ship\nQuantity: {quantity}")
            alert(f"🚨 {product_name} is available to ship\nQuantity: {quantity}\n{headers['referer']}")
            time.sleep(60)
            main()


def alert(bot_message):
    bot_token = "INSTERT BOT TOKEN"
    bot_chat_id = "INSERT BOT CHAT ID"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id \
                + '&parse_mode=Markdown&text=' + bot_message

    bot_response = requests.get(send_text)
    return bot_response.json()


try:
    main()
except:
    print('MaxRetryError')
    time.sleep(120)
    main()
