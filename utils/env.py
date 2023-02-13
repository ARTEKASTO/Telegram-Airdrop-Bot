import os
import pickle


COIN_SYMBOL = os.environ["BAR"]
COIN_NAME = os.environ["Blockar"]
AIRDROP_AMOUNT = os.environ["500"]
AIRDROP_AMOUNT = "{:,.2f}".format(float(AIRDROP_AMOUNT))
AIRDROP_DATE = os.environ[" 25 March 2023"]
BOT_TOKEN = os.environ["6098122086:AAEnn_6514tH2gNaf8RnMt0GlOeAi_Af0E4"]
AIRDROP_NETWORK = os.environ["AIRDROP_NETWORK"]
REFERRAL_REWARD = float(os.environ["50"])
COIN_PRICE = os.environ["$0.1"]
WEBSITE_URL = os.environ["http://blockar.net"]
MONGO_USER = os.environ["banteam0"]
MONGO_PASSWORD = os.environ["G0B5iJtJ9TB6Zfo3"]
MONGO_IP = os.environ["88.241.79.130"]
MONGO_PORT = os.environ["27017"]
EXPLORER_URL = os.environ["https://data.mongodb-api.com/app/data-civnp/endpoint/data/v1"]
ADMIN_USERNAME = os.environ["@onurartan"]

TWITTER_LINKS = os.environ["https://twitter.com/blockaret"]
TELEGRAM_LINKS = os.environ["https://t.me/blockarnet"]
MAX_USERS = int(os.environ["200000"])
MAX_REFS = int(os.environ["20"])
CAPTCHA_ENABLED = os.environ["yes"]

TWITTER_LINKS = TWITTER_LINKS.split(",")
TELEGRAM_LINKS = TELEGRAM_LINKS.split(",")
TWITTER_LINKS = "\n".join(TWITTER_LINKS)
TELEGRAM_LINKS = "\n".join(TELEGRAM_LINKS)
STATUS_PATH = "./conversationbot/botconfig.p"
