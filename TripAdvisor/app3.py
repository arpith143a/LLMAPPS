from dotenv import load_dotenv
load_dotenv() ## load all the environment variables from .env

import streamlit as st
import os
import google.generativeai as genai
from datetime import datetime,timedelta
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to make API call to Gemini model
def get_conversational_chain():

    prompt_template = """
    As a tripadvisor,Generate a personalized travel itinerary for {number_of_days} days trip to {destination} 
    from {start_date} to {end_date} having below preferences:
    1.{Interests}
    2.{Accomodation}
    3.{Budget}
    4.{Travel_style}
    5.{Dietary_preferences}
    6.{Transportation}
    7.{Must_visit_places}
    8.{optional_activities}
    9.{Time_Constraints}
    10.{Group_size}


Please generate a detailed itinerary that optimally utilizes the given preferences and ensures a memorable travel experience.

    Answer:
    """

    # model = ChatGoogleGenerativeAI(model="gemini-pro",
    #                          temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["number_of_days","destination","start_date","end_date","Interests","Accomodation","Budget","Travel_style","Dietary_preferences","Transportation","Must_visit_places","optional_activities","Time_Constraints","Group_size"])
    # chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([prompt])

    return response

# Streamlit app
# st.title("Travel Itinerary Generator")
st.set_page_config(page_title="Travel Itinerary Generator")
destination=st.text_input("Destination: ")

# Preferences
number_of_days = st.number_input("Enter the number of days", min_value=1, max_value=365)
start_date = st.date_input("Start date", min_value=datetime.today(), max_value=datetime.today() + timedelta(days=365))
end_date = st.date_input("End date", min_value=datetime.today(), max_value=datetime.today() + timedelta(days=365))
Interests = st.multiselect("Interests", ["Historical Sites", "Adventure Activities", "Culinary Exploration", "Cultural Events and Performances", "Nature and Scenic Views", "Relaxation and Leisure"])
Accommodation = st.selectbox("Accommodation", ["Hotels", "Hostels", "Vacation Rentals", "Boutique Inns", "Bed and Breakfast", "Luxury Resorts", "Camping", "Other"])
# specific_requirements = st.text_input("Specific Requirements")
Budget = st.selectbox("Budget", ["Economy", "Moderate", "High-end", "Luxury"])
Travel_style = st.multiselect("Travel Style", ["Slow-paced Exploration", "Adventure and Outdoor Activities", "Cultural Immersion", "City Exploration", "Relaxation and Wellness", "Backpacking", "Road Trip"])

dietary_preferences_options = ["Vegetarian", "Vegan", "Gluten-Free", "Local Cuisine", "Allergies", "Other Preferences"]

# Create a multi-checkbox for dietary preferences
Dietary_preferences = st.multiselect("Select Dietary Preferences", dietary_preferences_options)

# Check if "Allergies" or "Other Preferences" is selected
if "Allergies" in Dietary_preferences:
    allergies=st.text_area("Alergies", "")

if "Other Preferences" in Dietary_preferences:
    # Display a pop-up text input field for additional details
    other_preferences = st.text_area("other preferences", "")

transportation_options = [
        "Public Transportation",
        "Rental Car",
        "Walking/Biking",
        "Taxi/Uber",
        "Guided Tours",
        "Cruise",
        "Flights (if applicable)"
    ]

    # Create checkboxes for transportation preferences
Transportation = st.selectbox("Select Transportation Preferences", transportation_options)

must_visit_places_options = [
        "Specific Attractions",
        "Historical Landmarks",
        "Natural Wonders",
        "Local Markets",
        "Museums and Galleries",
        "Parks and Gardens",
        "Entertainment Venues",
        "Religious Sites"
    ]

    # Create checkboxes for must-visit places preferences
Must_visit_places = st.selectbox("Select Must-Visit Places Preferences", must_visit_places_options)


optional_activities_options = [
        "Adventure Sports",
        "Workshops or Classes",
        "Nightlife",
        "Shopping",
        "Spas and Wellness",
        "Festivals and Events",
        "Hidden Gems"
    ]

    # Create checkboxes for optional activities preferences
optional_activities = st.selectbox("Select Optional Activities Preferences", optional_activities_options)

group_size = st.radio("Select Group Size", ["Solo", "Couple", "Group"])



if group_size == "Group":
    # Display a pop-up text input field for group size
    group_size_input = st.text_input("Enter Group Size", "")

# Repeat the above for the remaining preferences...


# Button to Generate Itinerary
if st.button("Generate Itinerary"):
    preferences = { "number_of_days": number_of_days,
        "destination": destination,
        "start_date" : start_date,
        "end_date": end_date,
        "Interests":Interests,
        "Accomodation" : Accommodation,
        "Budget": Budget,
        "Travel_style": Travel_style,
        "Dietary_preferences": Dietary_preferences,
        "Transportation": Transportation,
        "Must_visit_places": Must_visit_places,
        "optional_activities": optional_activities,
        "Time_Constraints": optional_activities,
        "Group_size": group_size
        }

    # Call the Gemini model
    generated_itinerary = get_conversational_chain()

    # Display the generated itinerary
    if generated_itinerary:
        st.subheader("Generated Itinerary:")
        st.write(generated_itinerary)

    # chain = get_conversational_chain()
    # response = chain(
    #     { "number_of_days": number_of_days,
    #     "destination": destination,
    #     "start_date" : start_date,
    #     "end_date": end_date,
    #     "Interests":Interests,
    #     "Accomodation" : Accomodation,
    #     "Budget": Budget,
    #     "Travel_style": Travel_style,
    #     "Dietary_preferences": Dietary_preferences,
    #     "Transportation": Transportation,
    #     "Must_visit_places": Must_visit_places,
    #     "optional_activities": optional_activities,
    #     "Time_Constraints": optional_activities,
    #     "Group_size": Group_size
    #     }
    #     , return_only_outputs=True)

    # print(response)
    # st.write("Reply: ", response["output_text"])
