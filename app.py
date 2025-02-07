# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
from io import BytesIO

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Andiswa Majikijela"
field = "Bioinformatics"
institution = "University of Cape Town"


#st.title("Qualifications:")        
#qualifications = ["Machine Learning", "Molecular Biology", "Human Biology", "Statistics"]
#selection = st.segmented_control(
 #   "Options", qualifications, selection_mode="multi"
#)
#st.markdown(f"Your selected options: {selection}.")


# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")




# Streamlit App Title
st.title("📄 Qualification Uploader")

# File Upload
uploaded_files = st.file_uploader(
    "Upload your qualifications (PDF, Image, or Text)", 
    type=["pdf", "png", "jpg", "jpeg", "txt"], 
    accept_multiple_files=True
)

# Display uploaded files
if uploaded_files:
    st.subheader("Uploaded Files:")
    for file in uploaded_files:
        file_name = file.name
        st.write(f"📌 **{file_name}** uploaded successfully!")

        # If it's a text file, display the content
        if file.type == "text/plain":
            content = file.getvalue().decode("utf-8")
            st.text_area(f"📜 {file_name}", content, height=200)

        # If it's an image, display it
        elif file.type in ["image/png", "image/jpeg"]:
            st.image(file, caption=f"🖼 {file_name}", use_column_width=True)

        # If it's a PDF, provide a download option
        elif file.type == "application/pdf":
            st.download_button(
                label=f"📥 Download {file_name}",
                data=file,
                file_name=file_name,
                mime="application/pdf"
            )

st.success("✅ Upload your qualifications securely!") 

# Streamlit App Title
st.title("🎓 Academic Background")

# Your academic information
data = {
    "Degree": ["BSc in Physiology and Genetics", "Hons in Bioinformatics"],
    "Institution": ["University of Cape Town", "University of Cape Town"],
    "Year": ["2020-2023", "1 year"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display Table
st.table(df)
        
# CSV file to store personal statements
csv_file = "personal_statements.csv"

# Example Personal Statement (Replace with your own if you want)
example_statement = """I am passionate about Bioinformatics and its intersection with genetics and physiology. 
My research interests lie in analyzing biological data to uncover meaningful insights and drive scientific progress.
With a background in Physiology, Genetics, and Bioinformatics, I aim to contribute to cutting-edge research that advances healthcare and genomics.
"""

# Try loading existing personal statement or create an empty DataFrame
try:
    user_data = pd.read_csv(csv_file)
except FileNotFoundError:
    user_data = pd.DataFrame(columns=["Name", "Personal Statement"])


# Streamlit UI
st.title("🔬 My Research Interests & Expertise")

# Research Interests and Expertise (static)
research_info = """
I am passionate about **Bioinformatics** and its application in understanding human biology, genetics, and disease mechanisms. 
My research focuses on the following areas:

- **Data Science**: Applying statistical analysis and machine learning techniques to biological data.
- **Genomics**: Investigating the relationship between genes and disease, with a focus on **Genetic Variability**.
- **Physiology**: Studying human physiology with a view to improving healthcare outcomes.
- **Computational Biology**: Developing models and algorithms to better understand complex biological systems.

**Expertise**:
- Bioinformatics tools and technologies
- Genomic data analysis
- Molecular biology and genetics
- Data visualization and statistical modeling
"""

# Display the information in a readable format
st.markdown(research_info)
# Streamlit UI
st.title("📝 Personal Statement Creator")

# Display Example Statement
st.subheader("📌 Example Personal Statement")
st.write(example_statement)

# User Input Fields
st.subheader("✍️ Write Your Own Personal Statement")
name = st.text_input("👤 Name")
personal_statement = st.text_area("📝 Your Personal Statement", height=200)

# Save Personal Statement
if st.button("💾 Save Personal Statement"):
    if name and personal_statement:
        new_entry = pd.DataFrame([[name, personal_statement]], columns=user_data.columns)
        user_data = pd.concat([user_data, new_entry], ignore_index=True)
        user_data.to_csv(csv_file, index=False)  # Save to CSV
        st.success("✅ Your personal statement has been saved!")
        st.experimental_rerun()
    else:
        st.warning("⚠️ Please enter your name and personal statement before saving.")

# Display Saved Statements
st.subheader("📄 Saved Personal Statements")
st.dataframe(user_data)

# Option to Edit/Delete Statements (if any exist)
if not user_data.empty:
    delete_index = st.number_input("Enter row number to delete (0-based index)", min_value=0, max_value=len(user_data)-1, step=1)
    if st.button("❌ Delete Statement"):
        user_data = user_data.drop(delete_index).reset_index(drop=True)
        user_data.to_csv(csv_file, index=False)
        st.success("✅ Personal statement deleted!")
        st.experimental_rerun()





# Streamlit UI
st.title("📞 My Contact Information")

# Display your contact information (static)
contact_info = {
    
    "Email": "andiswamajikijela201@gmail.com",
    "Phone": "0217891234"
}

# Display the information in a table-like format
for key, value in contact_info.items():
    st.write(f"**{key}:** {value}")










