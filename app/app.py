import streamlit as st
from recommender import get_recommendations


hale_songs = ['Choose Hale Song...', 'The Day You Said Goodnight', 'Take No', 'Broken Sonnet', 'Blue Sky',
         'Wishing', 'Here Tonight',
       'Kahit Pa', 'Life Support', 'Underneath the Waves', 'Runaway',
       'Bent Down', 'Kung Wala Ka', 'Last Song', 'Fire in the Sky',
       'Empty Tears Empty Heart', 'The Ballad Of', 'Waltz',
       'Hide and Seek', 'Eyes Wide Shut', 'Liham', 'Shooting Star', '7,8',
       'Elegy', "Dahil Sa'yo Himig Ng Aking Gitara", 'Starting Over',
       'Brother', 'Over and Over', 'This Is a Happy Song', 'Sundown',
       'Pitong Araw', 'Sandali Na Lang', 'The End', 'Requim',
       'Back from Beginning', 'Tama Na Ba?', 'Skip the Drama',
       'Hagatna Bay', 'Treehouse', 'Leap of Faith', 'Bahay Kubo',
       'Kalesa', "Aso't Pusa", 'Ulap', 'Magkaibang Mundo', 'Bulalakaw',
       'Yakap', 'Harinawa', 'Toll Gate', 'Daylight', 'We Are', 'Fire',
       'Desire', 'Dreamcatcher', 'Simula Hanggang Huli', 'Hello Sunrise',
       'My Beating Heart', 'Alon', 'Sa Sunod Na Buhay', 'Saint Or Sinner',
       'You Or Nothing', 'See You', 'One Of These Days', 'Plasticine',
       'Home', 'The Day You Said Goodnight - Acoustic Version',
       'The Day You Said Goodnight (Leon Chaplain Massive Room Mix)']

def generate_iframe(track_id, rank):
    iframe_code = f"""
        <div style="display: flex; align-items: center; margin-bottom: 15px;">
            <span style="color: #33FF33; font-size: 20px; margin-right: 10px;">#{rank}</span>
            <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/{track_id}?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>
    """
    return iframe_code

# Setting the page layout to wide mode
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        .main .block-container {
            padding-top: 30px !important;
            margin-top: 0 !important;
        }
        .css-17eq0hr {
            background-color: #222222;
            color: white;
            padding: 10px 0px;
        }
        .stButton>button {
            background-color: #00FF00;
            color: black;
            width: 100%;
            height: 50px;
            font-size: 18px;
        }
        .spotwofy-title {
            background-color: black;
            color: #33FF33;  /* Neon green font color */
            padding: 10px 20px;
            font-size: 48px;
            display: inline-block;
            font-weight: normal;
            text-align: center;  /* Centering the text */
            width: 100%;  /* Making the container full width */
        }
        .spotwofy-title .bold {
            font-weight: bold;
        }
        .spotwofy-subtitle {
            text-align: center;  /* Centering the subtitle */
            font-size: 24px;
            color: #FFFFFF;
        }
        .spotwofy-subtitle2 {
            text-align: center;  /* Centering the subtitle */
            font-size: 20px;
            color: #FFFFFF;
        }
        /* For text inside the input box */
        .stTextInput input {
            color: white !important;
        }

        /* For selectbox text */
        .stSelectbox select {
            color: white !important;
        }
        
        .white-label {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.imgur.com/weXSou0.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

# Creating columns for layout
left_column, right_column = st.columns((7, 4))

# App title and tagline in the left column
with left_column:
    st.markdown('<div class="spotwofy-title">S  P  O <b class="bold"> T  W  O</b>  F  Y</div>', unsafe_allow_html=True)
    st.markdown('<div class="spotwofy-subtitle">F i n d&nbsp;&nbsp;y o u r&nbsp;&nbsp;s p o t&nbsp;&nbsp;i n&nbsp;&nbsp;t h e&nbsp;&nbsp;m u s i c&nbsp;&nbsp;s c e n e</div>', unsafe_allow_html=True)

    st.markdown('<hr style="color: white; background-color: white">', unsafe_allow_html=True)
    st.markdown("<div class='spotwofy-subtitle2' style='color: white;'>Today is a good day to expand your musical horizons!</div>",

                unsafe_allow_html=True)

    st.markdown('<div class="white-label">Select Hale song:</div>', unsafe_allow_html=True)
    song = st.selectbox("", hale_songs)  # empty label

    st.markdown('<div class="white-label">What I want recommended to me are</div>', unsafe_allow_html=True)
    recommender_style = st.selectbox("", ["Choose intention...",
                                          "Tracks that have similar audio features with selected song",
                                          "Tracks that have similar audio features and genre with selected song",
                                          "Tracks that have similar audio features and sentiment with selected song"])
    recommender_lookup = {"Tracks that have similar audio features with selected song" : 1,
                          "Tracks that have similar audio features and genre with selected song" : 2,
                          "Tracks that have similar audio features and sentiment with selected song" : 3}

    # If both select boxes have values, display tracks
    if song != "Choose a song..." and recommender_style != "Choose intention...":
        with st.spinner("Generating recommendations..."):
            recommended_track_ids = get_recommendations(song, recommender_lookup[recommender_style])
            st.markdown('<div class="white-label">Recommended tracks</div>', unsafe_allow_html=True)
            for index, track_id in enumerate(recommended_track_ids, start=1):
                st.markdown(generate_iframe(track_id, index), unsafe_allow_html=True)
