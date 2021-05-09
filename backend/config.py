import os
from dotenv import load_dotenv


class Config(object):
    """
    Get the configurations.
    """
    dotenv_path = './.env'
    load_dotenv(dotenv_path)
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")