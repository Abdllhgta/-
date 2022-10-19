import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = int(os.getenv("API_ID", "19886814"))
API_HASH = os.getenv("API_HASH", "b21f92291415ac8e777532f10443f69e")
SESSION = os.getenv("SESSION", "BABD0n1pxXnEnG5rNlrr4OrrxJaVPhrKiT0sYL0ymbzLc-bPaT8T_YDx5rOEgwOhfNGt3GSjdtmo9udFr_grkddR0nZ1OIoOqNmVuYRhQXqgHJRwR9uaQQJ7KXRqC_hjwNz4QowBBbSopIA-rBQZR8Utqm00igpjuRNpSjf-zKrChbuM7dSm9gY2-Gs-iGH8Qq8N8ALdCZGI0vRma8XRezjeYDVp4iUIONZnKP-d7V-0Vm7bhR1ZmNQAr8925zdwS1gSeaMUolgVf0gw_CvrF0dtOM3LbntL3kOzJaObRazFS7Xlr6893egFOtEAK0H1wT8oaecjRbbLBWFfSBraku8RAAAAASyURo0A")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTelethon"))
call_py = PyTgCalls(bot)
