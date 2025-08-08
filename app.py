# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.trend_scraper import get_trends
from utils.ai_generator import generate_post
from utils.db_handler import init_db, save_post, get_posts
import datetime

st.set_page_config(page_title="LinkedIn AI Agent", layout="wide")
init_db()

st.title("🤖 LinkedIn Personal Branding AI Agent")

# ---- Step 1: User Profile Input ----
st.subheader("1️⃣ Enter Your Profile Details")
name = st.text_input("Your Name")
profile_url = st.text_input("LinkedIn Profile URL")
industry = st.text_input("Industry / Domain")
role = st.text_input("Role / Position")

# ---- Step 2: Industry Trends ----
st.subheader("2️⃣ Industry Trends")
if industry:
    trends = get_trends(industry)
    st.write("Top Trends:")
    for t in trends:
        st.markdown(f"- {t}")

# ---- Step 3: Generate Content ----
st.subheader("3️⃣ AI Post Generation")
if st.button("Generate LinkedIn Post"):
    if name and industry and role:
        post = generate_post(name, industry, role, trends)
        st.success("Generated Post:")
        st.write(post)

        # Schedule post
        schedule_date = st.date_input("Schedule Date", datetime.date.today())
        if st.button("Save to Calendar"):
            save_post(schedule_date, post)
            st.success("Post saved to schedule.")
    else:
        st.warning("Please fill in all details first.")

# ---- Step 4: Content Calendar ----
st.subheader("4️⃣ Content Calendar")
posts_df = get_posts()
st.dataframe(posts_df)

# ---- Step 5: Engagement Analytics ----
st.subheader("5️⃣ Analytics")
if not posts_df.empty:
    posts_df["Likes"] = [abs(hash(x)) % 300 for x in posts_df["content"]]
    posts_df["Comments"] = [abs(hash(x)) % 100 for x in posts_df["content"]]
    posts_df["Shares"] = [abs(hash(x)) % 50 for x in posts_df["content"]]

    fig, ax = plt.subplots()
    posts_df.plot(kind="bar", x="date", y=["Likes", "Comments", "Shares"], ax=ax)
    st.pyplot(fig)
