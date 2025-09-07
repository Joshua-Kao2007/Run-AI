import streamlit as st
import openai
from config import OPENAI_API_KEY
from utils.prompts import generate_training_prompt

# Configure OpenAI API key
openai.api_key = OPENAI_API_KEY

# Streamlit UI
st.title("🏃 RunAI – Adaptive Training Plan (MVP)")
st.write("Generate a simple 1-week running plan based on your goals.")

# Input fields
age = st.number_input("Age", min_value=10, max_value=80, value=18)
gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
weekly_mileage = st.number_input("Current Weekly Mileage (miles)", min_value=0, max_value=200, value=10)
race_goal = st.text_input("Race Goal (e.g. 5K, Half Marathon, Finish First Race)")
goal_time = st.text_input("Goal Time (optional, e.g. sub-20 5K)")
fitness_level = st.selectbox("How do you feel today?", ["Normal", "Tired", "Sore", "Energized"])

if st.button("Generate Training Plan"):
    with st.spinner("Generating your training plan..."):
        # Build prompt
        prompt = generate_training_prompt(
            age=age,
            gender=gender,
            mileage=weekly_mileage,
            race_goal=race_goal,
            goal_time=goal_time,
            fitness_level=fitness_level,
        )

        # Call GPT
        client = openai.OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a certified running coach AI."},
                {"role": "user", "content": prompt},
            ],
        )

        plan = response.choices[0].message.content

        st.success("Here’s your 1-week plan:")
        st.markdown(plan)
