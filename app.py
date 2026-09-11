import streamlit as st
import os

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Happy Birthday Devhuti 💜",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# IMAGE
# --------------------------------------------------

image_path = os.path.join(
    os.path.dirname(__file__),
    "img2.png"
)

# --------------------------------------------------
# SIMPLE, CLEAN CSS
# --------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap');

html, body {
    margin: 0;
    padding: 0;
}

.stApp {
    background:
        radial-gradient(
            circle at 50% 0%,
            #3b1764 0%,
            #16091f 35%,
            #07030b 80%
        );

    color: white;
}

/* Hide Streamlit UI */
#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Remove default page spacing */
.block-container {
    max-width: 1400px !important;
    padding: 0 !important;
}

/* Main title */
.main-title {
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(3rem, 7vw, 7rem);
    font-weight: 900;
    letter-spacing: -4px;
    text-align: center;
    line-height: 1;
    margin-top: 55px;
    margin-bottom: 10px;

    color: white;

    text-shadow:
        0 0 20px rgba(180, 100, 255, 0.35),
        0 0 60px rgba(150, 50, 255, 0.25);
}

/* Name */
.name {
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(2.5rem, 5vw, 5rem);
    font-weight: 700;
    text-align: center;

    color: #d8b4fe;

    margin-bottom: 15px;

    text-shadow:
        0 0 25px rgba(192, 132, 252, 0.6);
}

/* Small subtitle */
.subtitle {
    font-family: 'Montserrat', sans-serif;
    text-align: center;

    font-size: 1rem;
    letter-spacing: 2px;

    color: rgba(255,255,255,0.65);

    margin-bottom: 45px;
}

/* Image container */
.image-container {
    max-width: 1200px;
    margin: auto;

    padding: 10px;

    border-radius: 24px;

    background: linear-gradient(
        135deg,
        rgba(255,255,255,0.18),
        rgba(168,85,247,0.18)
    );

    box-shadow:
        0 30px 100px rgba(0,0,0,0.7),
        0 0 70px rgba(168,85,247,0.20);
}

/* Image itself */
[data-testid="stImage"] {
    display: flex;
    justify-content: center;
}

[data-testid="stImage"] img {
    border-radius: 18px;
}

/* Bottom text */
.bottom-text {
    font-family: 'Montserrat', sans-serif;

    text-align: center;

    font-size: 0.9rem;

    letter-spacing: 2px;

    color: rgba(255,255,255,0.5);

    margin-top: 35px;
    margin-bottom: 50px;
}

/* Mobile */
@media (max-width: 700px) {

    .main-title {
        margin-top: 35px;
        letter-spacing: -2px;
    }

    .subtitle {
        padding: 0 20px;
        margin-bottom: 30px;
    }

    .image-container {
        margin: 0 12px;
        padding: 5px;
        border-radius: 16px;
    }

    [data-testid="stImage"] img {
        border-radius: 12px;
    }

}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LANDING PAGE
# --------------------------------------------------

st.markdown(
    '<div class="main-title">HAPPY BIRTHDAY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="name">DEVHUTI 💜</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">A VERY SPECIAL MESSAGE FROM YOUR FAVOURITE BOYS ✨</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# BIG BTS IMAGE
# --------------------------------------------------

if os.path.exists(image_path):

    st.image(
        image_path,
        use_container_width=True
    )

else:

    st.error("img2.png could not be found.")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="bottom-text">BORahae 💜 &nbsp; • &nbsp; MADE ESPECIALLY FOR DEVHUTI</div>',
    unsafe_allow_html=True
)
