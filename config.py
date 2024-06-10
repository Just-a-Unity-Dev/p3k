import yaml, logging

bot_config = {}
config_setup = False

def setup_config():
    global bot_config, config_setup
    if config_setup:
        raise Exception("")
    with open("config.yml") as stream:
        try:
            bot_config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise Exception(exc)
    config_setup = True
    logging.info("Bot configuration initialized")