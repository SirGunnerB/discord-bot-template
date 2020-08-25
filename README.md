# Discord Bot Template (Python)

A discord bot template that includes an example "cog" that you can use to quickly stand up your own bots!

## How do I use this?
1) You'll want to first clone the repository or download the ZIP to your PC
2) Make a copy of the `auth.ini.example` file and call it `auth.ini`.
    - If you are putting this bot on github for code versioning make sure you DO NOT commit this `auth.ini` file as it will contain your bot token. Exposiing this token will allow anyone to hijack your bot!
 3) Create a new application [in the Discord Develop Portal](https://discord.com/developers/applications)
 4) Under the "Bot" tab click the "Add Bot" button
5) Copy the token under the "Build-A-Bot" section and paste it in the new `auth.ini` file.
6) Lastly to invite your bot goto the "OAuth2" tab and select "bot" under "SCOPES" then all the relevant permissions you want your bot to have initially (don't worry this can be adjusted with roles inside your server). Copy the link that it generates and paste that in your browser.
7) Profit???

