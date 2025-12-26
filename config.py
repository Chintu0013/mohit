import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7926246903:AAFN9-lgq6zVdQPX7baq4Iww8mLZdjvPsVk")
    API_ID = int(os.environ.get("API_ID", "21567814"))
    API_HASH = os.environ.get("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
    AUTH_USER = os.environ.get('AUTH_USERS', '6126688051, 7324794111').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "〖ᴷⁱⁿᴳ Ⱥʂʂìցղҽɾ 🔰❌️🔰♡▪︎•Å𝑁𝐈𐌑À𝐿•▪︎♡ ⱽᵉʳⁱᶠⁱᵉᵈ"#Here You Can Change with Your Name  or any custom name or title you prefer
