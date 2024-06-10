import logging
import config, discord
# These three main libraries MUST be set up first before anything.
discord.utils.setup_logging()
config.setup_config()

import datetime, auth, psycopg2
from config import bot_config
from discord.ext import commands
connection = psycopg2.connect(
    user=bot_config['db']['username'],
    password=bot_config['db']['password'],
    host=bot_config['db']['host'],
    port=bot_config['db']['port'],
    database=bot_config['db']['database']
)
cursor = connection.cursor()

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
    try:
        x = auth.User.from_username(username)
        await ctx.send(f"The user ID of {username} is `{x.user_id}`")
        query = """INSERT INTO whitelist (USER_ID) VALUES (%s)"""
        cursor.execute(query, (x.user_id))
    except auth.NotRealUserException:
        await ctx.send(f"`{username}` is not a real valid username.")


client.run(bot_config['bot']['token'])