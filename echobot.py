
import logging
import telegram
from telegram import Bot
from telegram.error import NetworkError, Unauthorized
from time import sleep
from telegram.utils.request import Request
import logging
import urllib3
urllib3.disable_warnings()
from urllib3.contrib.socks import SOCKSProxyManager
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)



update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('798593629:AAFrNj9zSciSFB_BRryQ36hfDnXWeCxS5RE')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            update.message.reply_text(update.message.text)


if __name__ == '__main__':
    #main()
    # SOCKS_URL = 'socks5://77.247.94.153:8888/'
    # SOCKS_USER = ''
    # SOCKS_PASS = ''
    # bot = Bot(
    #     '798593629:AAFrNj9zSciSFB_BRryQ36hfDnXWeCxS5RE',
    #     request=Request(
    #         proxy_url=SOCKS_URL,
    #         urllib3_proxy_kwargs={
    #             'username': SOCKS_USER,
    #             'password': SOCKS_PASS,
    #         },
    #     )
    # )
    # print(str(bot.get_me().id))
    import requests

    url = "http://api.telegram.org/bot798593629:AAFrNj9zSciSFB_BRryQ36hfDnXWeCxS5RE/getMe"



    response = requests.request("GET", url)

    print(response.text)
