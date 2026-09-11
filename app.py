import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Happy Birthday Devhuti 💜",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Path to the BTS image
img_path = os.path.join(os.path.dirname(__file__), "bts_bg.png")

# Base64 encode for reliable display on any screen
b64_image = ""
if os.path.exists(img_path):
    with open(img_path, "rb") as img_file:
        b64_image = base64.b64encode(img_file.read()).decode()

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@800;900&display=swap');

    /* Remove Streamlit chrome */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)), url("data:image/png;base64,{b64_image}") no-repeat center center fixed;
        background-size: cover;
        background-position: center top;
        height: 100vh;
        width: 100vw;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }}

    .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    .content-wrapper {{
        width: 100%;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 20px;
        box-sizing: border-box;
    }}

    .birthday-heading {{
        font-family: 'Poppins', sans-serif;
        font-size: clamp(2.8rem, 7vw, 6.5rem);
        font-weight: 900;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 3px;
        line-height: 1.15;
        text-shadow: 0 4px 25px rgba(0, 0, 0, 0.95), 0 0 35px rgba(168, 85, 247, 0.8);
        margin: 0;
    }}

    .name-highlight {{
        display: block;
        color: #f3e8ff;
        background: linear-gradient(135deg, #ffffff 0%, #e9d5ff 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 25px rgba(192, 132, 252, 0.9));
    }}
    </style>

    <div class="content-wrapper">
        <h1 class="birthday-heading">
            Happy Birthday <br>
            <span class="name-highlight">Devhuti 💜</span>
        </h1>
    </div>
""", unsafe_allow_html=True)
