from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from src.tools.tavily_tool import tavily_search
from src.tools.serper_tool import google_serper_search_tool
from src.utils.logger import get_logger
from src.config.config import GROQ_API_KEY

logger = get_logger(__name__)

model = init_chat_model(
    model="groq:llama-3.3-70b-versatile",
    temperature = 0.3,
    api_key=GROQ_API_KEY
)

SYSTEM_PROMPT = """You are an expert AI travel planner.

Rules:
- Always use web search tools for real-world accuracy
- Create a detailed day-wise itinerary
- Include food suggestions, local tips, and travel advice

User Inputs:
City, Number of days, Interests, Travel style, Pace"""

agent = create_agent(model=model, 
            tools=[tavily_search, google_serper_search_tool],
            system_prompt=SYSTEM_PROMPT.strip())

logger.info("Travel agent created successfully with the specified model and tools.")