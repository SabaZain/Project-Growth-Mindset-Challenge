import streamlit as st
import pandas as pd

st.set_page_config(page_title= "Growth Mindset Project⭐")
st.title("🌷🧠 Growth Mindset Challenge!")

image_path = "Image/growth-mindset.jpg"
st.image(image_path, caption="Growth Mindset")

st.header("🙌🏻 Welcome to Your Growth Journey!")
st.write("Aims to help individuals develop a positive attitude toward challenges and learning through interactive exercises and reflections.It encorages continuous improvement by fostering resilience, persistence and self-belief💪🏻.")

# Quote
st.header("👨🏼‍🌾 Growth Mindset Quote")
st.write("Success is born from failure, and growth thrives in the face of both. 🏋🏿‍♂️ Every setback teaches us a lesson, and every victory fuels our journey forward.")

# User Input
st.header("⚡️ What challenge do you have today?")
user_input = st.text_input("Tell me about the challenge you are dealing with:")

# Condition
if user_input:
    st.success(f"You are dealing with: {user_input}. Stay focused and move forward!🚣")
else:
    st.warning("Share the challenge you faced when getting started!⚖️")

# Reflection
st.header("💡 Reflect on What You Have Learned!")
reflection = st.text_area("Tell your reflections here:")

if reflection:
    st.success(f"✨Great Insight! Your Reflection: {reflection}")
else:
    st.info("Reflecting on your journey helps with growth! Share the difficulties you faced.")

# Achievements
st.header("🏆 Acknowledge Your Achievements!")
achievement = st.text_input("Share something you have achieved recently:")

if achievement:
    st.success(f"🧑🏾‍🚀 Well Done, You Succeeded: {achievement}")
else:
    st.info("No matter the size, every achievement matters. Share one with us 🤩")

# File Upload
st.title("Upload Your File 📘")
uploaded_file = st.file_uploader("Please upload CSV file", type=["csv"])

if uploaded_file is not None:
    file_type = uploaded_file.type

    # If the file is CSV
    if file_type == "text/csv":
        st.write("CSV file uploaded successfully!")
        # Read and display CSV file
        df = pd.read_csv(uploaded_file)
        st.write(df)
   
# Footer
st.write("- - -")
st.write("Keep faith in your abilities, growth is a journey, not something you just reach 👋🏿")
# Motivation Provided
if st.button("Looking For More Inspiration🌞"):
    st.write("The journey of a thousand miles begins with one 🦶🏼 step. _ Lao Tzu")

st.write("*****📍 Created by Saba Ali Zain*****")

