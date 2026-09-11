import streamlit as st
import base64
import os
import textwrap

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Happy Birthday Devhuti 💜",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# LOAD IMAGE
# img2.png must be in the same folder as app.py
# ---------------------------------------------------------

img_path = os.path.join(os.path.dirname(__file__), "img2.png")

if os.path.exists(img_path):
    with open(img_path, "rb") as img_file:
        b64_image = base64.b64encode(img_file.read()).decode()
else:
    b64_image = None


# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------

css = """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600;1,700&display=swap');


/* ================================
   PAGE
================================ */

html, body {
    margin: 0;
    padding: 0;
    background: #08050d;
}

.stApp {
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(126, 34, 206, 0.30),
            transparent 42%
        ),
        radial-gradient(
            circle at 10% 90%,
            rgba(168, 85, 247, 0.12),
            transparent 35%
        ),
        #08050d;

    color: white;
}

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    visibility: hidden;
}

.block-container {
    max-width: 1200px !important;
    padding: 0 30px 70px 30px !important;
}


/* ================================
   HERO
================================ */

.hero {
    min-height: 100vh;

    display: flex;
    flex-direction: column;

    justify-content: center;
    align-items: center;

    text-align: center;

    padding: 60px 20px 80px;

    position: relative;
}


/* Tiny intro */

.eyebrow {
    font-family: 'DM Sans', sans-serif;

    font-size: 0.75rem;
    font-weight: 700;

    letter-spacing: 4px;
    text-transform: uppercase;

    color: #d8b4fe;

    margin-bottom: 20px;

    animation: fadeDown 1s ease;
}


/* HAPPY BIRTHDAY */

.hero-title {
    font-family: 'DM Sans', sans-serif;

    font-size: clamp(3rem, 7vw, 6.5rem);

    font-weight: 700;

    line-height: 0.95;

    letter-spacing: -4px;

    margin: 0;

    color: white;

    text-shadow:
        0 0 30px rgba(168, 85, 247, 0.25);

    animation: fadeUp 1s ease;
}


/* DEVHUTI */

.hero-name {
    font-family: 'Playfair Display', serif;

    font-size: clamp(3.5rem, 8vw, 7rem);

    font-weight: 700;

    font-style: italic;

    letter-spacing: -2px;

    margin-top: 12px;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #e9d5ff,
            #c084fc,
            #f5d0fe,
            #ffffff
        );

    background-size: 300% auto;

    -webkit-background-clip: text;
    background-clip: text;

    -webkit-text-fill-color: transparent;

    animation:
        gradientMove 5s linear infinite,
        fadeUp 1.2s ease;
}

.heart {
    -webkit-text-fill-color: #c084fc;

    display: inline-block;

    animation: heartbeat 1.5s infinite;
}


/* Subtitle */

.hero-subtitle {
    font-family: 'DM Sans', sans-serif;

    max-width: 620px;

    margin: 28px auto 38px;

    font-size: 1rem;

    line-height: 1.7;

    color: rgba(255,255,255,0.65);

    animation: fadeUp 1.5s ease;
}


/* ================================
   BTS IMAGE
================================ */

.image-wrapper {
    width: min(100%, 1050px);

    padding: 8px;

    border-radius: 28px;

    position: relative;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.16),
            rgba(168,85,247,0.15)
        );

    box-shadow:
        0 30px 100px rgba(0,0,0,0.75),
        0 0 80px rgba(168,85,247,0.20);

    animation: imageAppear 1.4s ease;
}

.birthday-image {
    display: block;

    position: relative;

    width: 100%;

    height: auto;

    border-radius: 21px;

    transition:
        transform 0.5s ease,
        filter 0.5s ease;
}

.image-wrapper:hover .birthday-image {
    transform: scale(1.012);

    filter:
        brightness(1.05)
        saturate(1.08);
}


/* ================================
   MESSAGE
================================ */

.message-section {
    max-width: 760px;

    margin: 90px auto 0;

    padding: 50px 35px;

    text-align: center;

    border-radius: 28px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.055),
            rgba(168,85,247,0.07)
        );

    border: 1px solid rgba(255,255,255,0.09);

    box-shadow:
        0 25px 80px rgba(0,0,0,0.35);
}

.message-small {
    font-family: 'DM Sans', sans-serif;

    font-size: 0.7rem;

    font-weight: 700;

    letter-spacing: 3px;

    text-transform: uppercase;

    color: #c084fc;
}

.message-title {
    font-family: 'Playfair Display', serif;

    font-size: clamp(2rem, 4vw, 3.2rem);

    margin: 12px 0 20px;
}

.message-text {
    font-family: 'DM Sans', sans-serif;

    max-width: 600px;

    margin: auto;

    color: rgba(255,255,255,0.65);

    font-size: 1rem;

    line-height: 1.8;
}


/* ================================
   FOOTER
================================ */

.footer {
    text-align: center;

    margin-top: 80px;

    font-family: 'DM Sans', sans-serif;

    font-size: 0.75rem;

    letter-spacing: 2px;

    color: rgba(255,255,255,0.35);
}

.footer-heart {
    color: #c084fc;

    font-size: 1rem;
}


/* ================================
   FLOATING DECORATIONS
================================ */

.floating {
    position: fixed;

    pointer-events: none;

    color: #c084fc;

    opacity: 0.12;

    z-index: 0;

    font-size: 25px;
}

.heart-one {
    left: 7%;
    top: 20%;

    animation: floatOne 8s ease-in-out infinite;
}

.heart-two {
    right: 8%;
    top: 35%;

    animation: floatTwo 10s ease-in-out infinite;
}

.heart-three {
    left: 15%;
    bottom: 15%;

    animation: floatTwo 7s ease-in-out infinite;
}


/* ================================
   ANIMATIONS
================================ */

@keyframes fadeUp {

    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }

}

@keyframes fadeDown {

    from {
        opacity: 0;
        transform: translateY(-20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }

}

@keyframes imageAppear {

    from {
        opacity: 0;
        transform: translateY(40px) scale(0.97);
    }

    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }

}

@keyframes gradientMove {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }

}

@keyframes heartbeat {

    0%, 100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.18);
    }

}

@keyframes floatOne {

    0%, 100% {
        transform: translateY(0) rotate(-10deg);
    }

    50% {
        transform: translateY(-35px) rotate(10deg);
    }

}

@keyframes floatTwo {

    0%, 100% {
        transform: translateY(0) rotate(10deg);
    }

    50% {
        transform: translateY(30px) rotate(-10deg);
    }

}


/* ================================
   MOBILE
================================ */

@media (max-width: 700px) {

    .block-container {
        padding: 0 15px 50px 15px !important;
    }

    .hero {
        min-height: auto;

        padding-top: 70px;
    }

    .hero-title {
        letter-spacing: -2px;
    }

    .hero-name {
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 0.9rem;

        margin-top: 22px;
    }

    .image-wrapper {
        padding: 5px;

        border-radius: 18px;
    }

    .birthday-image {
        border-radius: 14px;
    }

    .message-section {
        margin-top: 60px;

        padding: 35px 22px;

        border-radius: 22px;
    }

    .floating {
        display: none;
    }

}

</style>
"""

# Remove accidental indentation from the HTML/CSS
css = textwrap.dedent(css)

st.markdown(css, unsafe_allow_html=True)


# ---------------------------------------------------------
# FLOATING DECORATIONS
# ---------------------------------------------------------

st.markdown(
    """
    <div class="floating heart-one">♡</div>
    <div class="floating heart-two">♥</div>
    <div class="floating heart-three">✦</div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------

st.markdown(
    """
    <section class="hero">

        <div class="eyebrow">
            A little birthday surprise for an ARMY 💜
        </div>

        <h1 class="hero-title">
            HAPPY BIRTHDAY
        </h1>

        <div class="hero-name">
            Devhuti <span class="heart">♥</span>
        </div>

        <p class="hero-subtitle">
            Seven people. One chaotic birthday message.
            <br>
            And a whole lot of purple energy just for you.
        </p>

    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# IMAGE
# ---------------------------------------------------------

if b64_image:

    st.markdown(
        f"""
        <div class="image-wrapper">

            <img
                class="birthday-image"
                src="data:image/png;base64,{b64_image}"
                alt="Happy Birthday Devhuti from BTS"
            >

        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.error(
        "img2.png was not found. Make sure it is in the same folder as app.py."
    )


# ---------------------------------------------------------
# CLOSE HERO
# ---------------------------------------------------------

st.markdown(
    """
    </section>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# MESSAGE
# ---------------------------------------------------------

st.markdown(
    """
    <section class="message-section">

        <div class="message-small">
            To our favourite ARMY
        </div>

        <h2 class="message-title">
            This day is yours.
        </h2>

        <p class="message-text">
            May your year be ridiculously happy, slightly chaotic,
            full of unforgettable memories and surrounded by people
            who make you feel as loved as you deserve to be.
            <br><br>

            Keep shining. Keep laughing. Keep being you.
            <br>
            💜
        </p>

    </section>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">

        MADE WITH
        <span class="footer-heart">♥</span>
        FOR DEVHUTI
        &nbsp; • &nbsp;
        BORahae 💜

    </div>
    """,
    unsafe_allow_html=True
)
