# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
"""
st.title("Streamlit is amazing!")
st.title("Hello world")

st.write("This is my first web app")

number = st.slider("Pick an number", 1,100)
st.write(f"You picked {number}")
"""
# My Plot of data
"""
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)
"""



st.title("Qualifications:")        
qualifications = ["Machine Learning", "Molecular Biology", "Human Biology", "Statistics"]
selection = st.segmented_control(
    "Directions", qualifications, selection_mode="multi"
)
st.markdown(f"Your selected options: {selection}.")


# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Andiswa Majikijela"
field = "Bioinformatics"
institution = "University of Cape Town"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")
        


# Add a contact section
st.header("Contact Information")
email = "andiswamajikijela@example.com"
st.write(f"You can reach {name} at {email}.")










