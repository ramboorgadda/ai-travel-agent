from langchain_community.utilities import GoogleSerperAPIWrapper
import os
from src.config.config import SERPER_API_KEY
from src.utils.logger import get_logger

logger = get_logger(__name__)

def google_serper_search_tool(query :str) -> str:
    """Performs a Google Serper search and returns the results as a string."""
    try:
        logger.info(f"Performing Google Serper search for query: {query}")
        serper = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)
        result = serper.run(query)
        logger.info(f"Google Serper search completed successfully for query: {query}")
        return result
    except Exception as e:
        logger.error(f"Error occurred during Google Serper search for query: {query} with error: {str(e)}")
        raise e