from langchain_core.messages import HumanMessage, AIMessage
from src.agents.travel_agent import agent
from src.utils import logger
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages = []
        logger.info("TravelPlanner initialized successfully with the travel agent.")

    def create_itinerary(self,
                        city: str,
                        days: int,
                        interests: list[str],
                        style: str,
                        pace: str,
                        month: str|None = None) -> str:
        try:
            user_prompt = f"""Plan a {days}-day trip to {city} for me.
                        I am interested in {', '.join(interests)}.
                        My travel style is {style} and I prefer a {pace} pace.
                        I will be traveling in {month}.
                        Provide detailed itinerary including activities, accommodations, and dining options."""
            self.messages.append(HumanMessage(content=user_prompt))
            agent_response = agent.invoke({"messages": self.messages})
            final_answer = agent_response["messages"][-1].content
            return final_answer
        except Exception as e:
            logger.error(f"Error occurred while creating user prompt for itinerary creation with error: {str(e)}")
            raise CustomException("Failed to create user prompt for itinerary creation", e)
