import streamlit as st
from datetime import date
from PIL import Image

# Setting the page title and icon
st.set_page_config(page_title="Prafull Sutar's Portfolio", page_icon="💻")

background_image_url = "bi.png"  # Ensure the path is correct based on where your file is

# Add custom CSS for styling
st.markdown(
    f"""
    <style>
        body {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .streamlit-expanderHeader {{
        background-color: rgba(255, 255, 255, 0.7) !important; /* Optional: make header background semi-transparent */
    }}
        body {{
            background-color: #f0f8ff; /* Light blue background */
            color: #333;
        }}
        .title {{
            font-family: 'Arial', sans-serif;
            color: #2b7bba;
        }}
        .subheader {{
            color: #2b7bba;
        }}
        .contact-icons {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .hobbies-icons {{
            display: flex;
            justify-content: space-around;
            margin-top: 10px;
        }}
        .hobby-icon {{
            text-align: center;
        }}
        .hobby-icon img {{
            width: 50px;
            height: 50px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Create two columns for side-by-side layout
col1, col2 = st.columns([3, 1])  # Adjust the width of the columns as needed

# Display name in the first column
with col1:
    st.markdown(
        """
        <h1 style="font-family: Arial, sans-serif; color: #2b7bba;">Prafull Sutar's Portfolio</h1>
        """,
        unsafe_allow_html=True
    )

# Display image in the second column
with col2:
    image = Image.open("my.png")  # Load the image (ensure it's in the same directory)
    st.image(image, width=120, caption="Prafull Sutar", use_container_width=True)

st.markdown(
    """
    **Hello!** I'm **Prafull Sutar**, a Python Developer with expertise in Data Science, Machine Learning, Django REST, and Full-Stack Development. My passion lies in creating impactful software solutions that drive growth and innovation.
    """
)

# Contact Information
st.subheader("Contact Information")
st.markdown(
    """
    <div class="contact-icons">
        <p>📞 **Phone**: +91-1234567890</p>
        <p>📧 **Email**: Sutarprafull18@gmail.com</p>
        <p>📍 **Location**: Pune, India</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Personal Information
st.subheader("Personal Information")
st.markdown(
    """
    - **Father's Name**: Maruti Sutar  
    - **Mother's Name**: Sharada Sutar  
    - **Gender**: Male  
    - **Permanent Address**: Koregaon, Sangli, Dist: Sangli  
    - **Date of Birth**: 18 June 1996  
    - **Marital Status**: Unmarried  
    - **Languages**: English, Hindi, Marathi  
    - **Passport Available**: YES  
    """
)

# Career Objective
st.subheader("Career Objective")
st.markdown(
    """
    To employ myself in a progressive organization that provides scope to update my practical knowledge and skills in accordance with the latest trends and be part of a team that dynamically works towards the growth of the organization. I aim to achieve a challenging position as a Python Developer where my skills in developing Data Science, Machine Learning, and Web Applications can contribute to continuous growth and advancement.
    """
)

# Education
st.subheader("Education")
st.markdown(
    """
    - **B.E. in Mechanical Engineering**  
      Kolhapur University  
    """
)

# Certifications
st.subheader("Certifications")
st.markdown(
    """
    - **Data Analytics and Visualization Job Simulation** from Accenture (November 8th, 2024)  
    """
)

# IT Skills
st.subheader("IT Skills")
st.markdown(
    """
    - **Technology Specialization**: Python Data Science, Machine Learning, Django REST, MongoDB, ETL, Data Warehousing, Unix, SQL  
    - **Core Libraries/Packages**: Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn, PySpark, Scipy, Plotly  
    - **Django REST Libraries**: Django-rest-framework, Django-Session, Django-Middleware, Django-ORM, Django-allauth, Django-filter  
    - **Tools and Technologies**: MongoDB, HTML, CSS, Bootstrap, Beautiful Soup, Tableau, XML Parsing, ETL  
    - **Machine Learning Algorithms**: Linear Regression, Logistic Regression, KNN, K-Means, Naive Bayes, Decision Trees, Random Forest, SVM, PCA  
    - **DevOps and Models**: DevOps, Agile, V-Model  
    - **Programming Knowledge**: Python, C, HTML, CSS, Bootstrap  
    """
)

# Projects
st.subheader("Key Projects")
st.markdown(
    """
    1. **Optical Omni Switch Series Synchronization**  
       - Responsibilities: Telecom OSS Provisioning, Inventory Management, Python Scripting
    2. **B2B Integration Platform**  
       - Responsibilities: E-commerce Data Analysis, ETL Development, Machine Learning Models
    """
)

# Technical Skills
st.subheader("Technical Skills")
st.markdown(
    """
    - **Frameworks**: Django, Flask, CSS, Bootstrap  
    - **Web Technologies**: HTML, CSS, JSON, XML  
    - **Programming Languages**: Python, HTML, CSS, SQL  
    - **Version Control**: Git, GitHub  
    - **Analytic Tools**: Pandas, NumPy  
    - **Databases**: MySQL, MSSQL, MongoDB, PostgreSQL  
    - **IDE/Development Tools**: PyCharm, Anaconda-Jupyter Notebook, Microsoft Visual Studio  
    - **Deployment Tools**: ETL  
    - **Web Service**: REST-JSON, ORM (Django Rest Framework)  
    """
)

# Achievements
st.subheader("Achievements")
st.markdown(
    """
    - Successfully implemented an ETL pipeline that reduced data processing time by 30%.
    - Designed and deployed a REST API with Django REST for seamless data integration.
    """
)

# Hobbies Section
st.subheader("Hobbies")
st.markdown(
    """
    <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
        <div>
            <p style="font-size: 24px;">📷 Photography</p>
        </div>
        <div>
            <p style="font-size: 24px;">🎵 Music</p>
        </div>
        <div>
            <p style="font-size: 24px;">✍ Writing</p>
        </div>
        <div>
            <p style="font-size: 24px;">📚 Reading</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer
st.markdown("---")
st.markdown(
    f"""  
    **Date**: {date.today()}  
    """
)
