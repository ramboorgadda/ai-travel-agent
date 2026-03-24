from langchain_tavily import TavilySearch
import os
from src.config.config import TAVILTY_API_KEY
from src.utils.logger import get_logger
logger = get_logger(__name__)


def tavily_search(query :str) -> str:
    """Performs a search using the Tavily API and returns the results as a string."""
    try:
        logger.info(f"Performing Tavily search for query: {query}")
        tavily = TavilySearch(max_results = 5,
                            topic = "general",
                            tavily_api_key=TAVILTY_API_KEY)
        result = tavily.invoke({"query":query})
        logger.info(f"Tavily search completed successfully for query: {query}")
        return result
    except Exception as e:
        logger.error(f"Error occurred during Tavily search for query: {query} with error: {str(e)}")
        raise e 