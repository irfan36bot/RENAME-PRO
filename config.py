import os

class Config(object):
     # get a token from @BotFather
     TOKEN = os.environ.get("TOKEN", "5795235481:AAF2bQhLvG6q_m041GxgUIld5RhAX3V_ZcY")
     # The Telegram API things
     APP_ID = int(os.environ.get("APP_ID", "16784506"))
     API_HASH = os.environ.get("API_HASH", "562689b74bbd77c6baeceb097204c191")
     #Array to store users who are authorized to use the bot
     ADMIN = os.environ.get("ADMIN", "1125671241")
     #Your Mongo DB Database Name
     DB_NAME = os.environ.get("DB_NAME", "Cluster0")
     #Your Mongo DB URL Obtained From mongodb.com
     DB_URL = os.environ.get("DB_URL", "mongodb+srv://Irfan:786or786@cluster0.2jjhd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
