# 💘 VivahScope — India’s Smart Matchmaking Estimator

---

<img width="1536" height="1024" alt="image_vivascope" src="https://github.com/user-attachments/assets/6b7ae483-02e0-4c1b-9cce-89703d57b635" />

VivahScope is a data-driven matchmaking web app built with **Streamlit**, designed to help individuals and families estimate compatible marriage prospects using real-world demographic data, personalized filters, and **astrological compatibility**.

## 🔮 Features

### 🎯 Matchmaking Estimator
Estimate the number of eligible matches based on:

- Gender preference
- Age range
- Region (North, South, East, West India)
- Caste
- Income (₹50K+ to ₹3L+ monthly)
- Marital status
- Gotra, Rashi, Nakshatra
- Current city (Delhi, Mumbai, Bangalore, etc.)

### 🧮 Compatibility Calculator
- Checks **Gotra compatibility**
- Evaluates **Rashi** and **Nakshatra** match
- Displays result instantly

### 🎓 Advanced Filters
Refine match estimation with:

- Education Level (Graduate, Postgraduate, PhD, IIT/NIT, etc.)
- Profession / Industry
- Family Background (Affluent, Liberal, Conservative, etc.)
- Horoscope Exceptions (Manglik / Non-Manglik)

## 🧠 How it Works

The app uses population-level estimates, logical filters, and match reduction factors to provide an approximate count of compatible individuals in a chosen city.

### Example Calculation:
> “How many single North Indian Brahmin women aged 22–27 earning ₹1L+ live in Bangalore?”

```
## 🚀 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Visualization:** Streamlit widgets + Matplotlib/Plotly (optional)
- **Astro Filters:** Custom logic (Gotra/Rashi/Nakshatra compatibility)
```
---

## 📦 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/vivahscope.git
cd vivahscope

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run matchmaking_webapp.py
