import os
from dotenv import load_dotenv
from src.utils.logger import get_logger


logger = get_logger(__name__)

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
if not GROQ_API_KEY:
    logger.error("GROQ_API_KEY is not set in the environment variables.")
    raise ValueError("GROQ_API_KEY is required but not set.")
if not TAVILY_API_KEY:
    logger.error("TAVILY_API_KEY is not set in the environment variables.")
    raise ValueError("TAVILY_API_KEY is required but not set.")
if not SERPER_API_KEY:
    logger.error("SERPER_API_KEY is not set in the environment variables.")
    raise ValueError("SERPER_API_KEY is required but not set.")
logger.info("All API keys loaded successfully and config initialized.")