import logging, datetime, yaml, sqlite3, requests
from discord.ext import commands
import discord
discord.utils.setup_logging()

config = {}
with open("config.yml") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        raise Exception(exc)

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

@client.command()
async def hello_command(ctx: commands.Context):
    await ctx.reply("hello, world!")

client.run(config['bot']['token'])