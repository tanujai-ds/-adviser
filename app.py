import streamlit as st
import pandas as pd
import pickle
import requests

# Load trained model
with open("career_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🚀 Career Recommendation System with Job Info")

# --- Collect user input ---
st.header("🧠 Tell Us About Yourself")

skill = st.selectbox("Strongest Skill", [
    "Coding", "Data Analysis", "Design", "Writing", "Management", "Marketing",
    "Problem Solving", "Public Speaking", "Leadership", "Customer Service"
])

interest = st.selectbox("Primary Interest Area", [
    "Technology", "Art", "Science", "Business", "Media", "Finance",
    "Healthcare", "Education", "Engineering", "Law"
])

education = st.selectbox("Education Level", [
    "High School", "Bachelor", "Master", "PhD", "Diploma", "Associate Degree",
    "Self-Taught", "Online Certification", "Bootcamp", "Other"
])

work_style = st.selectbox("Preferred Work Style", [
    "Independent", "Team", "Remote", "On-site", "Hybrid", "Flexible",
    "Structured", "Creative", "Leadership", "Supportive"
])

goal_type = st.selectbox("Career Goal Type", [
    "Entrepreneurial", "Executive", "Creative", "Analytical", "Research-Oriented",
    "Helping Others", "Stable", "Adventurous", "High Income", "Academic"
])

coding_level = st.selectbox("Coding/Tech Experience Level", [
    "Beginner", "Intermediate", "Advanced", "None", "Learning",
    "Expert", "Basic HTML/CSS", "Python Only", "Frontend", "Backend"
])

learning_style = st.selectbox("Preferred Learning Style", [
    "Visual", "Auditory", "Reading/Writing", "Kinesthetic", "Group Learning",
    "Solo Learning", "Online", "Offline", "Project-Based", "Lectures"
])

tools = st.selectbox("Known Tools/Technologies", [
    "Python", "Photoshop", "Excel", "JavaScript", "AutoCAD", "WordPress",
    "SQL", "Google Analytics", "Figma", "None"
])

location = st.selectbox("Preferred Job Location", [
    "Mumbai", "Delhi", "Bangalore", "Pune", "Hyderabad", "Chennai",
    "Remote", "USA", "UK", "Europe"
])

income = st.selectbox("Income Expectation", [
    "Below 5 LPA", "5-10 LPA", "10-20 LPA", "20-30 LPA", "30-50 LPA",
    "50+ LPA", "Hourly Freelance", "Equity Based", "Commission", "Flexible"
])

# --- Predict ---
if st.button("🔍 Recommend My Career"):
    input_data = pd.DataFrame([{
        'Skill': skill,
        'Interest': interest,
        'Education': education,
        'WorkStyle': work_style,
        'GoalType': goal_type,
        'CodingLevel': coding_level,
        'LearningStyle': learning_style,
        'Tools': tools,
        'Location': location,     # ✅ Fixed: included this
        'Income': income
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"✅ Recommended Career: {prediction}")

    # --- API Integration ---
    st.header("🌐 Real-Time Job Info")
    st.write("Fetching job roles and info based on recommendation...")

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": prediction,
        "page": "1",
        "num_pages": "1",
        "country": "in"
    }

    headers = {
       "X-RapidAPI-Key": st.secrets["RAPIDAPI_KEY"],  # 🔐 Replace here if needed
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        jobs = response.json().get("data", [])

        if not jobs:
            st.warning("No job info found. Try another role or check API limits.")
        else:
            for i, job in enumerate(jobs[:3]):
                st.subheader(f"🔹 {i+1}. {job.get('job_title', 'N/A')} at {job.get('employer_name', 'N/A')}")
                st.markdown(f"📍 Location: {job.get('job_city', 'Unknown')}, {job.get('job_state', '')}")
                st.markdown(f"🕒 Posted: {job.get('posted_at', 'N/A')}")
                st.markdown(f"🔗 [View Job Posting]({job.get('job_apply_link', '#')})")
                st.markdown("---")

    except Exception as e:
        st.error(f"❌ Failed to fetch job data: {str(e)}")
