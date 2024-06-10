import logging
import config, discord
# These three main libraries MUST be set up first before anything.
discord.utils.setup_logging()
config.setup_config()

import datetime, sqlite3, auth
from config import bot_config
from discord.ext import commands

conn = sqlite3.connect("main.db")
cur = conn.cursor()
# Create DB tables
cur.execute("""CREATE TABLE IF NOT EXISTS test_db (text BLOB NOT NULL UNIQUE);""")
conn.commit()

intents = discord.Intents.all()
client = commands.Bot(command_prefix="%", intents=intents)

@client.event
async def on_ready():
    logging.info(f"Bot started at {datetime.datetime.now()}")

@client.command(name="hello")
async def hello_command(ctx: commands.Context):
    await ctx.reply("hello, world!")

@client.command(name="whitelist", aliases=['wl'])
async def whitelist_command(ctx: commands.Context, username: str):
    x = auth.User.from_username(username)
    await ctx.send(f"The user ID of {username} is `{x.user_id}`")

client.run(bot_config['bot']['token'])