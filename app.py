import streamlit as st
import random

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Political Empire",
    page_icon="🗳️",
    layout="wide"
)

# -------------------------------------------------
# GAME TITLE
# -------------------------------------------------

st.title("🗳️ Political Empire")
st.caption("Ujjain Campaign • Student Union Election • 2002")

# -------------------------------------------------
# PLAYER
# -------------------------------------------------

DEFAULT_PLAYER = {

    "name": "Shashank",

    "money": 5000,

    "land": 0.50,

    "popularity": 5,

    "trust": 10,

    "supporters": 20,

    "turn": 1,

    "stage": "Student Union",

    "bio": 25,

    "commerce": 50,

    "arts": 15,

    "girls": 35,

    "completed": False

}

if "player" not in st.session_state:

    st.session_state.player = DEFAULT_PLAYER.copy()

player = st.session_state.player

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("Player")

st.sidebar.metric("Money", f"₹{player['money']}")

st.sidebar.metric("Land", f"{player['land']:.2f} Acre")

st.sidebar.metric("Popularity", f"{player['popularity']} %")

st.sidebar.metric("Trust", f"{player['trust']} %")

st.sidebar.metric("Supporters", player["supporters"])

st.sidebar.divider()

st.sidebar.write("### Hidden Survey")

def stars(value):

    if value >= 80:
        return "★★★★★"

    elif value >= 60:
        return "★★★★☆"

    elif value >= 40:
        return "★★★☆☆"

    elif value >= 20:
        return "★★☆☆☆"

    else:
        return "★☆☆☆☆"


st.sidebar.write("Bio :", stars(player["bio"]))

st.sidebar.write("Commerce :", stars(player["commerce"]))

st.sidebar.write("Arts :", stars(player["arts"]))

st.sidebar.write("Girls :", stars(player["girls"]))

st.sidebar.divider()

if st.sidebar.button("Restart Game"):

    st.session_state.player = DEFAULT_PLAYER.copy()

    st.rerun()

# -------------------------------------------------
# HEADER
# -------------------------------------------------

left, right = st.columns(2)

with left:

    st.info(f"""
### Election

Year : **2002**

Stage : **{player['stage']}**

Turn : **{player['turn']} / 10**
""")

with right:

    st.success("""
### Objective

✅ Win Election

✅ Save Money

✅ Increase Popularity

✅ Buy More Land
""")
