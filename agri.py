
import streamlit as st
import os
import subprocess

st.set_page_config(page_title="Agricultural Dashboard Launcher",page_icon="🌾", layout="wide")
#-------------------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Remove sidebar padding (optional, adjust if needed) */
    .css-18e3th9, .css-1d391kg {
        padding-left: 0rem !important;
    }

    .fixed-title {
        position: fixed;
        top: 3.5rem;
        left: 0;
        right: 0;
        width: 100%;
        height: 60px;
        background: linear-gradient(to right, #a8e063, #f2e863, #f8b500); /* green to yellow to brown */
        color: #2e2e2e;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
        border-bottom: 2px solid #a1882d;
        z-index: 9999;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .spacer {
        height: 70px;
    }
    </style>

    <div class="fixed-title">
        🌾 AGRICULTURAL DASHBOARD LAUNCHER
    </div>
    <div class="spacer"></div>
""", unsafe_allow_html=True)
#------------------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .centered-text {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    <div class="centered-text">Welcome to the interactive agricultural data platform.</div>
    """,
    unsafe_allow_html=True
)
#-------------------------------------------------------------------------------------

    # Provide the full path to your .pbix file
pbix_path = r"C:\\DS_Programs\\Project2_AgriData\\agri_sql.pbix"
st.markdown("""
    <style>
    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 30px;
        margin-bottom: 30px;
    }
    div.stButton > button:first-child {
        background: linear-gradient(to right, #a5d6a7, #388e3c);
        color: white;
        padding: 12px 30px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        transition: background 0.3s ease;
    }
    div.stButton > button:hover {
        background: linear-gradient(to right, #81c784, #2e7d32);
    }
    </style>
""", unsafe_allow_html=True)
if st.button("Open Power BI Dashboard"):
    try:
         # Launch the PBIX file
         os.startfile(pbix_path)  # This works on Windows
    except Exception as e:
        st.error(f"Failed to open file: {e}")


#-------------------------------------------------------------------------------------


st.image("C://DS_Programs//Project2_AgriData//image//9.jpg", use_container_width=True)

