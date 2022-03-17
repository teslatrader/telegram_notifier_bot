# SIMPLE TELEGRAM NOTIFIER BOT

*Description*

Bot sends to particular telegram chat any message, which is previously processed
about specific symbols.

Main goal of that bot - easiest way to use it like telegram notifier in another
more complex bots.

**Instructions**

Make sure that you have installed python v.3.7+

Activate virtual environment (you have to have virtualenv installed)
or install packages from requirements.txt globally:

  for activating existing venv:
  ```
  . venv/bin/activate
  ```

  install requirements:
  ```
  pip3 install -r requirements.txt
  ```

**Usage**

    from bot import TelegramBot as tgb
    import bot_token, time

    tb = tgb(bot_token.TOKEN, bot_token.CHAT_ID)
    tb.send_msg(f'\n{time.ctime()}: initializing bot...')

***Notice that bots api token and chat id should be inserted in bot_token.py***