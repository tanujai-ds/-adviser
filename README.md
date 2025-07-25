# -adviser
# 💼 Career Advisor with AI & Live Job API Integration

An intelligent career recommendation system that analyzes your inputs (skills, interests, goals, education, etc.) and suggests a career path, with real-time job openings shown using the JSearch API.

---

## 🚀 Features

- Predicts best-fit careers based on 10 user-selected attributes
- Pulls real-time job listings using the **JSearch API**
- Simple UI using **Streamlit**
- Customizable & extensible
- No paid services required — 100% free to use

---

## 📊 Attributes Used in Career Prediction

This app uses these 10 detailed attributes:

1. ✅ Strongest Skill  
2. 🎯 Primary Interest Area  
3. 🎓 Education Level  
4. 💼 Preferred Work Style  
5. 📈 Career Goal Type  
6. 👨‍💻 Coding/Tech Experience Level  
7. 🧠 Preferred Learning Style  
8. 🧰 Known Tools/Technologies  
9. 📍 Preferred Job Location  
10. 💰 Income Expectation  

---

## 📥 How to Run This App

### 1. Clone This Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

2. Set Up Environment (Recommended)

python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux


3. Install Required Packages

pip install -r requirements.txt

4. 📌 Get Your Free JSearch API Key
Go to: https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch

Sign in or create a free account

Subscribe to the Free Plan (100 requests/day)

Copy your API key (X-RapidAPI-Key)

Create a file called apikey.txt in your project root folder

Paste your API key inside apikey.txt


▶️ Run the App

streamlit run app.py


🧠 Technologies Used
Python 3.x

Streamlit

scikit-learn (ML model)

Pandas

JSearch API (via RapidAPI)







