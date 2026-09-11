import os
import streamlit as st
import streamlit.components.v1 as components

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Happy Birthday Devhuti! 💜 | BTS Special Celebration",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Streamlit CSS to remove default padding for an immersive full-screen experience
st.markdown("""
<style>
    /* Hide Streamlit Header, Footer and Sidebar paddings */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    iframe {
        border: none !important;
        width: 100% !important;
        min-height: 100vh !important;
    }
</style>
""", unsafe_allow_html=True)

# Load HTML, CSS, JS from the local project files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(BASE_DIR, "index.html")
css_path = os.path.join(BASE_DIR, "styles.css")
js_path = os.path.join(BASE_DIR, "script.js")

html_content = ""
css_content = ""
js_content = ""

if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()

if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()

if os.path.exists(js_path):
    with open(js_path, "r", encoding="utf-8") as f:
        js_content = f.read()

# Inline CSS and JS into HTML for a completely self-contained Streamlit component
if "<link rel=\"stylesheet\" href=\"styles.css\">" in html_content:
    html_content = html_content.replace(
        '<link rel="stylesheet" href="styles.css">',
        f"<style>{css_content}</style>"
    )

if "<script src=\"script.js\"></script>" in html_content:
    html_content = html_content.replace(
        '<script src="script.js"></script>',
        f"<script>{js_content}</script>"
    )

# Render the interactive BTS Birthday app inside Streamlit
components.html(html_content, height=4500, scrolling=True)
