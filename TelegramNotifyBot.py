import requests.adapters


class TelegramNotifyBot:
    def __init__(self, token, user_id):
        """
        Telegram Notify Bat is the main class for sending notifications via telegram.

        :param token: Your bot's access token in telegram.
        :param user_id: Your id in the telegram.
        """
        self.token = token
        self.user_id = user_id
        self.url = f'https://api.telegram.org/bot{token}'
        self.params = {'chat_id': user_id, 'text': ''}

    def send_message(self, message):
        self.params['text'] = message
        return requests.get(self.url + '/sendMessage', params=self.params)
