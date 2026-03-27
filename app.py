import warnings
import streamlit as st

warnings.filterwarnings("ignore")
from dotenv import load_dotenv
load_dotenv()
from src.core.planner import TravelPlanner
from src.utils.logger import get_logger
logger = get_logger(__name__)
st.set_page_config(page_title="AI Travel Planner", page_icon=":earth_americas:", layout="wide")
st.title("AI Travel Planner :earth_americas:")

with st.form("travel_form"):
    city = st.text_input("Enter the city you want to visit", "Paris")
    days = st.number_input("Number of days for the trip", min_value=1, max_value=30, value=5)
    interests = st.multiselect("Select your interests", ["Culture", "Food", "Nature", "History", "Nightlife"], default=["Culture", "Food"])
    style = st.selectbox("Select your travel style", ["Relaxed", "Balanced", "Active"], index=1)
    pace = st.selectbox("Select your preferred pace", ["Leisurely", "Moderate", "Fast-paced"], index=1)
    month = st.selectbox("Select your travel month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], index=0)
    submit_button = st.form_submit_button(label="Plan My Trip")
if submit_button:
    if city and interests:
        try:
            planner = TravelPlanner()
            itinerary = planner.create_itinerary(city, days, interests, style, pace, month)
            st.subheader("Your AI-Generated Itinerary:")
            st.write(itinerary)
            logger.info(f"Successfully created itinerary for {city} with interests {interests} and travel style {style}.")
        except Exception as e:
            logger.error(f"Error occurred while creating itinerary with error: {str(e)}")
            st.error("An error occurred while planning your trip. Please try again later.")