import sys
import twitchio
import insertMSG
from twitchio.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...

        super().__init__(
            token="TOKEN",
            prefix="?",
            initial_channels=["CHANNEL"],
        )
        self.yt = insertMSG.auth()
        self.chatID = (
            self.yt.videos()
            .list(part="liveStreamingDetails", id=sys.argv[1])
            .execute()["items"][0]["liveStreamingDetails"]["activeLiveChatId"]
        )

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f"Hello {ctx.author.name}!")

    async def event_message(self, message: twitchio.Message) -> None:
        strmsg = message.author.name + " : " + message.content.__str__()
        self.yt.liveChatMessages().insert(
            part="snippet",
            body={
                "snippet": {
                    "liveChatId": self.chatID,
                    "type": "textMessageEvent",
                    "textMessageDetails": {"messageText": strmsg},
                }
            },
        ).execute()
        return await super().event_message(message)


bot = Bot()
bot.run()
