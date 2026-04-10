import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")
# Header
st.markdown("<h1 style='text-align: center;'>👩‍💻 ANKITA PATRA</h1>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.link_button("ptra.ankita@gmail.com","mailto:ptra.ankita@gmail.com") 
with col2:
    st.link_button("(+91) 7439404917","tel:+917439404917") 
with col3:
    st.link_button("GitHub","https://github.com/Ankitapatra13") 
with col4:
    st.link_button("Kaggle","https://www.kaggle.com/ankitapatra13")
st.subheader("Aspiring AI/ML Engineer",divider="grey",width="content",text_alignment="center")

# About 
st.header("PROFESSIONAL SUMMARY",divider="grey",width="content")
st.write("""I am an aspiring AI/ML Engineer with hands-on experience in building machine learning models 
         and deploying data-driven applications. 
         I enjoy solving real-world problems using data.""")

# Projects
st.header("PROJECTS",divider="grey",width="content")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🛒 Customer Segmentation System",divider="grey",width="content")
    st.write("""
    - **K-Means clustering** is used to identify distinct customer groups. 
    - Used **Elbow Method** and **Silhouette Score** to ensure well-defined clusters. 
    - **Engineered features** (Total spendings, Total children, Age and more) 
    - Used scatter plot in application to show customer's position in market. 
    - Generated Business insights and recommendations for better ROI. 
    """)
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        st.link_button("🔗 View GitHub", "https://github.com/Ankitapatra13/Customer_Segmentation_System")
    with subcol2:
        st.link_button("🌐 Live App","https://customersegmentationsystem-2zsgwv5dsdgbyvg2l3rt2t.streamlit.app/")

with col2:
    st.subheader("🎓 Student Dropout Prediction System",divider="grey",width="content",text_alignment="center")
    st.markdown("""
    - Used XGBoost model to predict student dropout risk using behavioral, academic, and lifestyle data.  
    - ~**63%** accuracy, F1-score: 0.63  
    - Feature engineering + class imbalance handling 
    - Applied preprocessing **pipelines** and trained an optimized XGBoost model for multi-class classification (Low, Medium, High).
    - **Aligned** training and inference **features**, **eliminating** prediction **mismatches**.
    - **Deployed** on **Streamlit** for **real-time predictions** with structured user inputs.
                            """)
    subcol3, subcol4 = st.columns(2)
    with subcol3:
        st.link_button("🔗 View GitHub", "https://github.com/Ankitapatra13/Student_dropout_prediction_system")
    with subcol4:
        st.link_button("🌐 Live App", "https://studentdropoutpredictionsystem-b927fxzz9awqk4ajbtzcna.streamlit.app/")
st.divider()

# Skills
st.header("SKILLS",divider="grey",width="content")
st.markdown(" **Programming** : Python(Numpy,Pandas,Scikit-learn)")
st.markdown(" **Tools & Frameworks** : Git, GitHub, VS Code, Streamlit, Kaggle")

