# matchmaking_webapp.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="India Matchmaking Estimator", layout="wide")

st.title("💘 VivahScope:Matchmaking Insights Estimator")

st.sidebar.header("🔍 Input Preferences")

gender = st.sidebar.selectbox("Looking for", ["Female", "Male"])
age_min, age_max = st.sidebar.slider("Preferred Age Range", 18, 45, (22, 27))
regions = st.sidebar.multiselect("Preferred Regions", ["North India", "South India", "East India", "West India", "All India"], default=["North India"])
caste = st.sidebar.selectbox("Preferred Caste", ["Brahmin", "Kayastha", "Vaishya", "Any"])
marital_status = st.sidebar.radio("Looking for: ", ["Single", "Married", "Any"], index=0)
income_range = st.sidebar.selectbox("Minimum Income/month (₹)", ["50K", "80K", "1L", "1.5L", "2L", "3L+"], index=2)

cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Noida", "Gurgaon", "Kolkata"]
current_city = st.sidebar.selectbox("Current Living City of Matches", cities)

user_gotra = st.sidebar.text_input("Your Gotra", "Bhardwaj")
preferred_gotra = st.sidebar.text_input("Preferred Gotra", "Kashyap")

rashis = ["Any", "Mesh", "Vrishabh", "Mithun", "Karka", "Simha", "Kanya", "Tula", "Vrischika", "Dhanu", "Makar", "Kumbha", "Meen"]
nakshatras = ["Any", "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshta", "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"]

user_rashi = st.sidebar.selectbox("Your Rashi", rashis[1:])
preferred_rashi = st.sidebar.selectbox("Preferred Rashi", rashis)
user_nakshatra = st.sidebar.selectbox("Your Nakshatra", nakshatras[1:])
preferred_nakshatra = st.sidebar.selectbox("Preferred Nakshatra", nakshatras)

preferred_location = st.sidebar.selectbox("Preferred Match Location", cities)

# Advanced Filters
st.sidebar.header("🎓 Advanced Filters")
education = st.sidebar.selectbox("Minimum Education Level", ["Any", "Graduate", "Postgraduate", "PhD", "IIT/NIT/IIM/Top Tier"])
profession = st.sidebar.selectbox("Preferred Profession/Industry", ["Any", "Software/Tech", "Finance", "Consulting", "Startup", "Government", "Other"])
family_background = st.sidebar.selectbox("Family Background Preference", ["Any", "Upper Middle Class", "Affluent", "Conservative", "Liberal"]) 
manglik_status = st.sidebar.selectbox("Horoscope Preference (Manglik/Dosha)", ["Any", "Non-Manglik Only", "Manglik Only"])

# Compatibility Calculator
st.sidebar.markdown("---")
st.sidebar.subheader("💞 Compatibility Check")
compatibility = "✅ Likely Compatible"

if user_gotra.strip().lower() == preferred_gotra.strip().lower():
    compatibility = "❌ Same Gotra – Not Traditionally Compatible"
if preferred_rashi != "Any" and user_rashi == preferred_rashi:
    compatibility += " | ✅ Same Rashi"
if preferred_nakshatra != "Any" and user_nakshatra == preferred_nakshatra:
    compatibility += " | ✅ Same Nakshatra"

st.sidebar.markdown(f"**Result:** {compatibility}")

# --- Population and Filtering Assumptions ---
total_city_population = {
    "Delhi": 20_000_000,
    "Mumbai": 18_000_000,
    "Chennai": 10_000_000,
    "Bangalore": 14_000_000,
    "Noida": 1_000_000,
    "Gurgaon": 1_000_000,
    "Kolkata": 14_000_000
}

# Mapping input to assumptions
region_filter_ratio = {
    "North India": 0.30,
    "South India": 0.30,
    "East India": 0.20,
    "West India": 0.20,
    "All India": 1.00
}
caste_ratio = 0.10 if caste != "Any" else 1.0
married_ratio = {"Single": 0.90, "Married": 0.10, "Any": 1.0}[marital_status]
income_ratio_map = {"50K": 0.30, "80K": 0.20, "1L": 0.10, "1.5L": 0.05, "2L": 0.02, "3L+": 0.01}
income_ratio = income_ratio_map[income_range]
region_selected_ratio = sum([region_filter_ratio.get(r, 0) for r in regions])
education_factor = 0.60 if education != "Any" else 1.0
profession_factor = 0.50 if profession != "Any" else 1.0
family_background_factor = 0.70 if family_background != "Any" else 1.0
manglik_filter_factor = 0.85 if manglik_status != "Any" else 1.0

# Estimate
pop = total_city_population.get(current_city, 10_000_000)
female_ratio = 0.50
gender_ratio = female_ratio if gender == "Female" else 1 - female_ratio
age_range_ratio = (age_max - age_min) / 27  # assume 18-45 range = 27 years

estimate = (
    pop * gender_ratio * age_range_ratio * region_selected_ratio * caste_ratio * married_ratio * income_ratio *
    education_factor * profession_factor * family_background_factor * manglik_filter_factor
)

estimate = round(estimate)

st.subheader("📊 Estimated Matches Based on Your Inputs")
st.success(f"✅ Estimated {gender}s in {current_city} matching your criteria: **{estimate:,}**")

# Optional summary
st.markdown("""
### 🔎 Summary of Criteria:
- Age Range: **{age_min}–{age_max}**
- Region: **{regions_str}**
- Caste: **{caste}**
- Status: **{marital_status}**
- Income: **₹{income_range}+**
- Gotra Filter: **{user_gotra} (You)** vs **{preferred_gotra} (Preferred)**
- Rashi: **{user_rashi} ↔ {preferred_rashi}**
- Nakshatra: **{user_nakshatra} ↔ {preferred_nakshatra}**
- Preferred Match Location: **{preferred_location}**
- Education: **{education}**, Profession: **{profession}**, Family: **{family_background}**, Manglik: **{manglik_status}**
""".format(
    age_min=age_min,
    age_max=age_max,
    regions_str=', '.join(regions),
    caste=caste,
    marital_status=marital_status,
    income_range=income_range,
    user_gotra=user_gotra,
    preferred_gotra=preferred_gotra,
    user_rashi=user_rashi,
    preferred_rashi=preferred_rashi,
    user_nakshatra=user_nakshatra,
    preferred_nakshatra=preferred_nakshatra,
    preferred_location=preferred_location,
    education=education,
    profession=profession,
    family_background=family_background,
    manglik_status=manglik_status
))
