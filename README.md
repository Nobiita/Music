<h1 align="centre">Rythm</h1>

### A bot that can play music on Telegram Group and Channel Voice Chats
#### POWERED BY [PYTGCALLS](https://github.com/pytgcalls/pytgcalls)
### Available on telegram as [@Rythm](https://t.me/RythmSupportGroup)

<p align="center">
  <img src="etc/tg_vc_bot.png">
</p>

<h2> Features 🔥 </h2>

- Thumbnail Support
- Playlist Support
- Current playback support
- Showing track names when skipping
- Zero downtime, Fully Stable
- Youtube playback support
- Settings panel
- Control with buttons
- Userbot auto join

## 🚀 Deployment

### 💜 Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/IrhamFadzillah/Rythm)

Get pyrogram (p)  `SESSION` from here:
[![Run on Repl.it](https://repl.it/badge/github/SpEcHiDe/GenerateStringSession)](https://repl.it/@SpEcHiDe/GenerateStringSession)

### ⚔ Self-hosting (For Devs) 
```sh
# Install Git First (apt-instll git)
$ git clone https://github.com/IrhamFadzillah/Rythm
$ cd Rythm
# Upgrade sources
# Install All Requirements 
$ pip(3) install -r requirements.txt
# Rename example.env to local.env and fill
$ npm i -g npm
# Start Bot 
$ python3 -m rythm
```

### Commands for Group 🛠
#### For all in group

- `/play <song name>` - play song you requested
- `/playlist` - Show now playing list
- `/current` - Show now playing
- `/song <song name>` - download songs you want quickly
- `/search <query>` - search videos on youtube with details
- `/video <song name>` - download videos you want quickly

#### Admins only.
- `/player` - open music player settings panel
- `/pause` - pause song play
- `/resume` - resume song play
- `/skip` - play next song
- `/end` - stop music play
- `/userbotjoin` - invite assistant to your chat
- `/userbotleave` - remove assistant from your chat
- `/reload` - Refresh admin list
- `/auth [reply to user]` - Authorize User
- `/deauth [reply to user]` - DeAuthorize user
Authorized users can execute admin commands in authorized group

### Commands for Sudo Users ⚔️
- `/userbotleaveall` - remove assistant from all chats
- `/pmpermit [on/off]` - enable/disable pmpermit message

#### Pmpermit
- `.a` - approove someone to pm you
- `.da` - disapproove someone to pm you
+ Sudo Users can execute any command in any groups

### Credits
Don't edit this part

#### Special Credits
- [Rojserbest](http://github.com/rojserbes): Callsmusic Developer

This bot is based on the original work done by [Rojserbest](http://github.com/rojserbest). Without his hardwork daisyxmusic won't exist. 
DaisyXmusic is a modified version of [Callsmusic](https://github.com/callsmusic/callsmusic) for fit the needs of @DaisyXbot users

#### Contribtors
- [InukaASiTH](https://github.com/InukaAsith): Dev
- [Rojserbest](http://github.com/rojserbes): Dev
- [Wrench](https://github.com/EverythingSuckz/): Dev
- [QueenArzoo](https://github.com/QueenArzoo): Dev
- [lucifeermorningstar](https://github.com/lucifeermorningstar): Dev
- [AuraXNetwork](https://github.com/AuraXNetwork/AuraXMusicBot)
- [Hamker Cat](https://github.com/thehamkercat/)
- [Anjana-Ma](https://github.com/Anjana-Ma): 
- [ImJanindu](https://github.com/ImJanindu): 
- [Laky](https://github.com/Laky-64) & [Andrew](https://github.com/AndrewLaneX): PyTgCalls
- [Original Repo owners](https://github.com/suprojects/CallsMusic)
