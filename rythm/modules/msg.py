# rythm (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from rythm.config import ASSISTANT_NAME, PROJECT_NAME


class Messages:
    START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\n✅ Send me /help for more info."
    HELP_MSG = [
        ".",
        f"""
**Hey Welcome back to {PROJECT_NAME}

 {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

 Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",
        f"""
**Commands**

**=>> Song Playing **

- /play: Play song using youtube music
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio


**=>> Playback ⏯**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        f"""
**=>> More tools **

- /reload: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
- /auth [reply to user] - Authorize User
- /deauth [reply to user] - DeAuthorize user
Authorized users can execute admin commands in authorized group

**=>> Commands for Sudo Users **

 - /userbotleaveall - remove assistant from all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

""",
    ]
