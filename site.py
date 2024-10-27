#streamlit run .\site.py
import streamlit as st

# Set page title and layout
st.set_page_config(page_title="My Portfolio", layout="wide")

# --- SIDEBAR ---
st.sidebar.title("Navigation")  # This adds a clear label for navigation in the sidebar
navigation = st.sidebar.radio("Go to:", ["Home", "Skills", "Projects", "Contact"])

# --- HOME PAGE ---
if navigation == "Home":
    st.title("Welcome to My Portfolio")
    # Add an image with corrected path format and resized
    col1, col2 = st.columns([3, 1])  # Adjusted column ratios to prioritize text
    with col2:
        st.image(r"E:\folder\ML-DA-DS\live\gitfolder\site\image.jpg", caption="Ritik Barnwal", use_column_width=True, width=100)  # Further reduced width
    with col1:
        st.write("""
        Hello! I'm **Ritik Barnwal**, a passionate Data Scientist and Web Developer. I have a strong background in **_data analytics_**, **_machine learning_**, and **_web development_**.
        """)
        st.write("""
        #### About Me
        I am currently pursuing BCA in Data Science, and I have experience working on various projects involving data cleaning, automation, and machine learning. In addition, I enjoy working with **Python**, **SQL**, **Power BI**, and more.
        """)

# --- SKILLS PAGE ---
elif navigation == "Skills":
    st.title("Skills")
    st.write("""
    - **Programming Languages**: Python, SQL
    - **Data Analysis**: Pandas, NumPy, Power BI
    - **Machine Learning**: Scikit-Learn, TensorFlow
    - **Web Development**: Streamlit
    """)

# --- PROJECTS PAGE ---
elif navigation == "Projects":
    st.title("My Projects")

    # Project 1
    st.subheader("1. Customer Churn Prediction")
    st.write("""
    Built a machine learning model to predict customer churn with an accuracy of 93.33%.
    """)
    st.write("[View Project](https://github.com/username/churn-prediction)")

    # Project 2
    st.subheader("2. Iris Flow Prediction")
    st.write("""
    Developed a time series analysis project using ARIMA and Exponential Smoothing to predict stock prices.
    """)
    st.write("[View Project](https://github.com/username/stock-price-predictor)")

    # Project 3
    st.subheader("3. Web Development with Python")
    st.write("""
    Created a responsive and dynamic website using Streamlit, which showcases my projects and skills.
    """)
    st.write("[View Project](https://github.com/username/streamlit-portfolio)")

    # Project 4
    st.subheader("4. Power BI Dashboard for YHILLS Company")
    st.write("""
    Created a responsive and dynamic website using Streamlit, which showcases my projects and skills.
    """)
    st.write("[View Project](https://github.com/username/streamlit-portfolio)")

# --- CONTACT PAGE ---
elif navigation == "Contact":
    st.title("Contact Me")
    st.write("""
    Feel free to reach out to me via:
    - **Email**: theritikbarnwal@gmail.com
    - **LinkedIn**: [Ritik Barnwal](https://www.linkedin.com/in/theritikbarnwal/)
    - **GitHub**: [Ritik Barnwal](https://github.com/theritikbarnwal)
        """)

st.divider()
# Footer
st.write("© 2024-26 My Portfolio")
