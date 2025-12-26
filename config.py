import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8245953382:AAFH2MZPcXB9ExZA5Mjky7qK_lJN1S8v_XA")
    API_ID = int(os.environ.get("API_ID", "31193989"))
    API_HASH = os.environ.get("API_HASH", "9dbb821c39e6b0b8a6fe7d901666ecdf")
    AUTH_USER = os.environ.get('AUTH_USERS', '7348079600, 7368580476').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "꧁༒CHINTU❤️‍🔥༒꧂"#Here You Can Change with Your Name  or any custom name or title you prefer

