import requests

BOT_TOKEN = "********************************************"
BOT_CHATID = "*********"


class NotificationManager:

    def telegram_bot_send_text(self, bot_message):
        bot_token = BOT_TOKEN
        bot_chatID = BOT_CHATID
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID \
                    + '&parse_mode=Markdown&text=' + bot_message
        bot_response = requests.get(send_text)
        return bot_response.json()

