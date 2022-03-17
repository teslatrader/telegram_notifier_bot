# -*- coding: utf-8 -*-
import requests, datetime, time

class TelegramBot:
    def __init__(self, token, chat_address):
        self.token = token
        self.message = ''
        self.chat_id = chat_address
        self.send_msg_temp = f'/sendMessage?chat_id={self.chat_id}'
        self.parse_mode = '&parse_mode=MarkdownV2&text='
        self.bot_url = f'https://api.telegram.org/bot{self.token}{self.send_msg_temp}{self.parse_mode}'


    def send_msg(self, message):
        # print(message)
        self.message = self.msg_cast(f'{datetime.datetime.fromtimestamp(time.time())}: {message}')
        self.send_it()
        return


    def send_it(self):
        url = f'{self.bot_url}{self.message}'
        r = requests.get(url)
        return


    def msg_cast(self, message: str):
        message = str(message)
        for char in ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!' ]:
            if char in message:
                message = message.replace(char, "\\"+char)
        return message