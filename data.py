from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("[►Start Generating Session◄]", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="[►Return Home◄]", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("[►How to Use❔◄]", callback_data="help")],
        [
            InlineKeyboardButton("[►About◄]", callback_data="about"),
            InlineKeyboardButton("[►Support💬◄]", url="https://t.me/AerodynamicV1_Promotion")
        ],
        [InlineKeyboardButton("[►New Update Or More🔔◄]", url="https://t.me/AerodynamicV1_UPDATE")],
    ]

    START = """
💚Hey {}!

Welcome to {}

You can use me to generate pyrogram (even version 2) and telethon string session. Use below buttons to learn more !

Powered By [AerodynamicV1~🇮🇳](https://t.me/AerodynamicV1_OFFICIAL)
    """

    HELP = """
🔰 **Available Commands** 🔰

/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
/about - About The Bot

Powered By [AerodynamicV1~🇮🇳](https://t.me/AerodynamicV1_OFFICIAL)
"""

    ABOUT = """
🔰 **About This Bot** 🔰 

🤖Telegram Bot to generate Pyrogram and Telethon string session Powered By [AerodynamicV1~🇮🇳](https://t.me/AerodynamicV1_OFFICIAL)

▪️Source Code : [Click Here](https://github.com/AerodynamicV1Botz/String-Session-AeroBot)

▪️Framework : [Pyrogram](https://docs.pyrogram.org)

▪️Language : [Python](https://www.python.org)

▪️Developer : @AerodynamicV1_OFFICIAL
    """
