import os
from dotenv import load_dotenv
from src.utils.logger import get_logger


logger = get_logger(__name__)

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILTY_API_KEY = os.getenv("TAVILTY_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY")
if not GROQ_API_KEY:
    logger.error("GROQ_API_KEY is not set in the environment variables.")
    raise ValueError("GROQ_API_KEY is required but not set.")
if not TAVILTY_API_KEY:
    logger.error("TAVILTY_API_KEY is not set in the environment variables.")
    raise ValueError("TAVILTY_API_KEY is required but not set.")
if not SERP_API_KEY:
    logger.error("SERP_API_KEY is not set in the environment variables.")
    raise ValueError("SERP_API_KEY is required but not set.")
logger.info("All API keys loaded successfully and config initialized.")