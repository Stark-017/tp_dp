import streamlit as st
import base64
import os

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
# IMAGE
# Put img2.png in the SAME folder as app.py
# ---------------------------------------------------------

img_path = os.path.join(os.path.dirname(__file__), "img2.png")

if os.path.exists(img_path):
    with open(img_path, "rb") as img_file:
        b64_image = base64.b64encode(img_file.read()).decode()
else:
    b64_image = ""


# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------

st.markdown(
    f"""
    <style>

    /* =========================
       GLOBAL
       ========================= */

    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700;800&display=swap');

    * {{
        box-sizing: border-box;
    }}

    html, body {{
        margin: 0;
        padding: 0;
        background: #08050d;
    }}

    .stApp {{
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(126, 34, 206, 0.28),
                transparent 40%
            ),
            radial-gradient(
                circle at 10% 90%,
                rgba(168, 85, 247, 0.12),
                transparent 35%
            ),
            #08050d;

        color: white;
    }}

    /* Hide Streamlit UI */

    #MainMenu {{
        visibility: hidden;
    }}

    header {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    [data-testid="stToolbar"] {{
        visibility: hidden;
    }}

    .block-container {{
        max-width: 1200px !important;
        padding: 0 30px 80px 30px !important;
    }}


    /* =========================
       HERO SECTION
       ========================= */

    .hero {{
        min-height: 100vh;

        display: flex;
        flex-direction: column;

        justify-content: center;
        align-items: center;

        text-align: center;

        padding: 55px 20px 80px;

        position: relative;
    }}


    /* Small ARMY label */

    .eyebrow {{
        font-family: 'DM Sans', sans-serif;

        font-size: 0.78rem;
        font-weight: 700;

        letter-spacing: 4px;
        text-transform: uppercase;

        color: #d8b4fe;

        margin-bottom: 18px;

        animation: fadeDown 1s ease;
    }}


    /* Main heading */

    .hero-title {{
        font-family: 'DM Sans', sans-serif;

        font-size: clamp(3.2rem, 8vw, 7rem);

        font-weight: 700;

        line-height: 0.95;

        letter-spacing: -4px;

        margin: 0;

        color: white;

        text-shadow:
            0 0 25px rgba(168, 85, 247, 0.25);

        animation: fadeUp 1s ease;
    }}


    /* Devhuti */

    .hero-name {{
        display: block;

        font-family: 'Playfair Display', serif;

        font-size: clamp(3.7rem, 9vw, 8rem);

        font-weight: 800;

        font-style: italic;

        letter-spacing: -3px;

        margin-top: 8px;

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
    }}


    .heart {{
        display: inline-block;

        -webkit-text-fill-color: #c084fc;

        animation: heartbeat 1.6s infinite;
    }}


    /* Subtitle */

    .hero-subtitle {{
        max-width: 650px;

        margin: 28px auto 35px;

        font-family: 'DM Sans', sans-serif;

        font-size: 1rem;

        line-height: 1.7;

        color: rgba(255,255,255,0.68);

        animation: fadeUp 1.5s ease;
    }}


    /* =========================
       IMAGE CARD
       ========================= */

    .image-wrapper {{
        width: min(100%, 1050px);

        margin: 15px auto 0;

        padding: 10px;

        border-radius: 28px;

        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,0.15),
                rgba(168,85,247,0.15)
            );

        box-shadow:
            0 30px 100px rgba(0,0,0,0.7),
            0 0 80px rgba(168,85,247,0.18);

        position: relative;

        animation: imageAppear 1.5s ease;
    }}


    .image-wrapper::before {{
        content: "";

        position: absolute;

        inset: -2px;

        border-radius: 30px;

        background:
            linear-gradient(
                120deg,
                transparent,
                rgba(192,132,252,0.6),
                transparent
            );

        z-index: 0;

        filter: blur(5px);

        opacity: 0.5;
    }}


    .birthday-image {{
        position: relative;

        z-index: 1;

        display: block;

        width: 100%;

        height: auto;

        border-radius: 21px;

        box-shadow:
            inset 0 0 40px rgba(0,0,0,0.4);

        transition:
            transform 0.5s ease,
            filter 0.5s ease;
    }}


    .image-wrapper:hover .birthday-image {{
        transform: scale(1.012);

        filter:
            brightness(1.05)
            saturate(1.08);
    }}


    /* =========================
       BIRTHDAY MESSAGE
       ========================= */

    .message-section {{
        max-width: 760px;

        margin: 100px auto 0;

        text-align: center;

        padding: 50px 35px;

        border-radius: 28px;

        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.065),
                rgba(168,85,247,0.06)
            );

        border: 1px solid rgba(255,255,255,0.09);

        box-shadow:
            0 25px 80px rgba(0,0,0,0.35);
    }}


    .message-small {{
        font-family: 'DM Sans', sans-serif;

        text-transform: uppercase;

        letter-spacing: 3px;

        font-size: 0.7rem;

        color: #c084fc;

        font-weight: 700;
    }}


    .message-title {{
        font-family: 'Playfair Display', serif;

        font-size: clamp(2rem, 4vw, 3.2rem);

        margin: 12px 0 20px;

        color: white;
    }}


    .message-text {{
        font-family: 'DM Sans', sans-serif;

        color: rgba(255,255,255,0.68);

        font-size: 1rem;

        line-height: 1.8;

        margin: 0 auto;

        max-width: 600px;
    }}


    /* =========================
       BTS / ARMY FOOTER
       ========================= */

    .footer {{
        text-align: center;

        margin-top: 90px;

        padding-bottom: 20px;

        font-family: 'DM Sans', sans-serif;

        color: rgba(255,255,255,0.4);

        font-size: 0.78rem;

        letter-spacing: 2px;
    }}

    .footer-heart {{
        color: #c084fc;
        font-size: 1.1rem;
    }}


    /* =========================
       FLOATING HEARTS
       ========================= */

    .floating {{
        position: fixed;

        pointer-events: none;

        font-size: 20px;

        opacity: 0.12;

        color: #c084fc;

        z-index: 0;
    }}

    .heart-one {{
        left: 7%;
        top: 20%;

        animation: floatOne 8s ease-in-out infinite;
    }}

    .heart-two {{
        right: 8%;
        top: 35%;

        animation: floatTwo 10s ease-in-out infinite;
    }}

    .heart-three {{
        left: 15%;
        bottom: 15%;

        animation: floatTwo 7s ease-in-out infinite;
    }}


    /* =========================
       ANIMATIONS
       ========================= */

    @keyframes fadeUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}

        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes fadeDown {{
        from {{
            opacity: 0;
            transform: translateY(-20px);
        }}

        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes imageAppear {{
        from {{
            opacity: 0;
            transform: translateY(40px) scale(0.97);
        }}

        to {{
            opacity: 1;
            transform: translateY(0) scale(1);
        }}
    }}

    @keyframes gradientMove {{
        0% {{
            background-position: 0% 50%;
        }}

        50% {{
            background-position: 100% 50%;
        }}

        100% {{
            background-position: 0% 50%;
        }}
    }}

    @keyframes heartbeat {{
        0%, 100% {{
            transform: scale(1);
        }}

        50% {{
            transform: scale(1.18);
        }}
    }}

    @keyframes floatOne {{
        0%, 100% {{
            transform: translateY(0) rotate(-10deg);
        }}

        50% {{
            transform: translateY(-35px) rotate(10deg);
        }}
    }}

    @keyframes floatTwo {{
        0%, 100% {{
            transform: translateY(0) rotate(10deg);
        }}

        50% {{
            transform: translateY(30px) rotate(-10deg);
        }}
    }}


    /* =========================
       MOBILE
       ========================= */

    @media (max-width: 700px) {{

        .block-container {{
            padding: 0 15px 50px 15px !important;
        }}

        .hero {{
            min-height: auto;

            padding-top: 70px;
            padding-bottom: 40px;
        }}

        .hero-title {{
            letter-spacing: -2px;
        }}

        .hero-name {{
            letter-spacing: -1.5px;
        }}

        .hero-subtitle {{
            font-size: 0.9rem;

            margin-top: 22px;
        }}

        .image-wrapper {{
            margin-top: 20px;

            padding: 6px;

            border-radius: 18px;
        }}

        .birthday-image {{
            border-radius: 14px;
        }}

        .message-section {{
            margin-top: 60px;

            padding: 35px 22px;

            border-radius: 22px;
        }}

        .floating {{
            display: none;
        }}
    }}

    </style>


    <!-- Floating decorations -->

    <div class="floating heart-one">♡</div>
    <div class="floating heart-two">♥</div>
    <div class="floating heart-three">✦</div>


    <!-- HERO -->

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


        <!-- IMAGE -->

        <div class="image-wrapper">

            {
                f'<img class="birthday-image" src="data:image/png;base64,{b64_image}">'
                if b64_image
                else '<div style="padding:80px;color:#c084fc;">img2.png not found</div>'
            }

        </div>

    </section>


    <!-- MESSAGE -->

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
            Keep shining, keep laughing, keep being you.
            💜
        </p>

    </section>


    <div class="footer">
        MADE WITH <span class="footer-heart">♥</span>
        FOR DEVHUTI &nbsp; • &nbsp; BORAHAE 💜
    </div>

    """,
    unsafe_allow_html=True
)
