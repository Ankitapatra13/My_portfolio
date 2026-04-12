import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")
st.session_state.setdefault('show_css_demo_video', False)
# Header
st.markdown("<h1 style='text-align: center; color: steelblue;'>👩‍💻 ANKITA PATRA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-size: 16;'>🎯 AI/ML Engineer | Data Scientist | Problem Solver</p>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("[ptra.ankita@gmail.com](mailto:ptra.ankita@gmail.com)") 
with col2:
    st.markdown("[(+91) 7439404917](tel:+917439404917)") 
with col3:
    st.markdown("[GitHub](https://github.com/Ankitapatra13)") 
with col4:
    st.markdown("[Kaggle](https://www.kaggle.com/ankitapatra13)")

st.markdown("<h2 style='font-size: 18';> 🤖 Aspiring AI/ML Engineer</h2>", unsafe_allow_html=True)
st.divider()

# About 
st.header("📋 PROFESSIONAL SUMMARY")
st.write("""Passionate and driven AI/ML Engineer with hands-on experience in developing machine learning models and deploying data-driven applications. 
Skilled in Python, data analysis, and machine learning algorithms, with expertise in clustering techniques (K-Means), classification models (XGBoost), and feature engineering. 
Proven track record in building end-to-end solutions for customer segmentation and predictive analytics, delivering actionable business insights. 
Committed to solving real-world problems through innovative data science approaches and continuous learning in the rapidly evolving field of AI.""")

# Projects
st.header("🚀 PROJECTS")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🛒 Customer Segmentation System",divider="blue",width="content")
    st.markdown("""
    **Key Technologies & Methods:**
    - **K-Means Clustering**: Identifies distinct customer groups for targeted marketing
    - **Model Validation**: Elbow Method and Silhouette Score ensure well-defined clusters
    - **Feature Engineering**: Total spendings, children count, age, and demographic data
    - **Data Visualization**: Interactive scatter plots show customer market positioning
    - **Business Impact**: Generates actionable insights and ROI optimization recommendations
    """)
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        st.link_button("🔗 View GitHub", "https://github.com/Ankitapatra13/Customer_Segmentation_System")
    with subcol2:
        st.link_button("🌐 Live App","https://customersegmentationsystem-2zsgwv5dsdgbyvg2l3rt2t.streamlit.app/")
    
with col2:
    img_col1, img_col2 = st.columns(2)
    with img_col1:
        st.image("images/UI.png", caption="Home Page")
        st.image("images/Prediction.png", caption="Prediction Screen")
    with img_col2:
        st.image("images/Visualization.png", caption=" Segment Visualization")
        st.image("images/Cluster_Summary.png", caption="Cluster Summary")
    col_left, col_video, col_right = st.columns([1, 2, 1])
    with col_video:
        if not st.session_state.show_css_demo_video:
            if st.button("▶ Play Demo Video", key="play_demo_btn", use_container_width=True):
                st.session_state.show_css_demo_video = True
                st.rerun()
            st.image("images/UI.png", caption="Click to watch demo")
        else:
            st.video("videos/customer_segmentation_demo_video.mp4", subtitles="videos/customer_segmentation_demo_video.vtt")
            if st.button("✕ Close Video", key="close_demo_btn", use_container_width=True):
                st.session_state.show_css_demo_video = False
                st.rerun()

col3, col4 = st.columns(2)
with col3:
    img_col3, img_col4 = st.columns(2)
    with img_col3:
        st.image("images/dropout/dropout_ui.png")
        st.image("images/dropout/dropout_ui2.png")
        st.image("images/dropout/dropout_ui3.png", caption="Home Page")

    with img_col4:
        st.image("images/dropout/dropout_result.png", caption="Prediction Screen")
        st.image("images/dropout/dropout_insights.png", caption="Insights Screen")
        st.image("images/dropout/dropout_recommendations.png", caption="Recommendations Screen")
with col4:
    st.subheader("🎓 Student Dropout Prediction System",divider="blue",width="content")
    st.markdown("""
    **Model Performance:**
    - **Accuracy**: ~63%
    - **F1-Score**: 0.63 for balanced evaluation
    
    **Key Features:**
    - **XGBoost Algorithm**: Multi-class classification for Low, Medium, High dropout risk
    - **Advanced Preprocessing**: Feature engineering and class imbalance handling
    - **Data Pipeline**: Robust preprocessing pipelines ensuring training/inference consistency
    - **Deployment**: Real-time predictions through user-friendly Streamlit interface
    """)
    subcol3, subcol4 = st.columns(2)
    with subcol3:
        st.link_button("🔗 View GitHub", "https://github.com/Ankitapatra13/Student_dropout_prediction_system")
    with subcol4:
        st.link_button("🌐 Live App", "https://studentdropoutpredictionsystem-b927fxzz9awqk4ajbtzcna.streamlit.app/")

st.divider()
# Skills
st.header("💡 SKILLS")
st.markdown("**🐍 Programming** : Python (Numpy, Pandas, Scikit-learn)")
st.markdown("**🛠️ Tools & Frameworks** : Git, GitHub, VS Code, Streamlit, Kaggle")
st.markdown("**📊 Specializations** : Machine Learning, Data Analysis, Clustering, Classification")
st.divider()
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>© 2026 Ankita Patra | Portfolio powered by Streamlit</p>", unsafe_allow_html=True)


