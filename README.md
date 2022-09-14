# TelegramNotify
Telegram Notify is needed to send notifications in telegram. Just create a Telegram Notify Bot class using your telegram user ID and an access token to the telegram bot, which should send you notifications. To create a bot, you need to register and get its unique id, which is also a token. To do this, there is a special bot in Telegram — @BotFather. We write to him /start and get a list of all his commands. The first and main one is /newbot — we send it to him and the bot asks him to come up with a name for our new bot. The only restriction on the name is that it must end in "bot". If successful, BotFather returns the bot token and a link to quickly add the bot to contacts, otherwise you will have to puzzle over the name. Don't forget to check the received token using the link api.telegram.org/bot /getMe, they say, does not always work the first time.
