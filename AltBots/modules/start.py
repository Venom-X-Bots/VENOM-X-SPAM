from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• 𝐶𝑂𝑀𝑀𝐴𝑁𝐷𝑆 •", data="help_back")
    ],
    [
        Button.url("• 𝐶𝐻𝐴𝑁𝑁𝐸𝐿 •", "https://t.me/Thecchub"),
        Button.url("• 𝑆𝑈𝑃𝑃𝑂𝑅𝑇 •", "https://t.me/+mBKAuzF9eP05ZTM1")
    ],
    [
        Button.url("• 𝑅𝐸𝑃𝑂 •", "https://t.me/+mBKAuzF9eP05ZTM1")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝐼'𝑀 [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ 𝐷𝐸𝑉𝐿𝑂𝑃𝐸𝑅​ : [𝑽𝑬𝑵𝑶𝑴](https://t.me/its_Aryaan)**\n\n"
        TEXT += f"» **𝐵𝑂𝑇 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :** `M3.3`\n"
        TEXT += f"» **𝑃𝑌𝑇𝐻𝑂𝑁 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :** `3.11.3`\n"
        TEXT += f"» **𝑇𝐸𝐿𝐸𝑇𝐻𝑂𝑁 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/8d771cd45a1bc53254501.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
