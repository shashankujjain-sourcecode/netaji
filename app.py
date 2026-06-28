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
# -------------------------------------------------
# SCENARIOS
# -------------------------------------------------

SCENARIOS = [

{
"issue":"Bio students demand Sports Kits before election.",

"choices":[

{
"text":"Provide Sports Kits (₹1000)",

"money":-1000,

"bio":15,

"commerce":0,

"arts":0,

"girls":0,

"trust":2,

"popularity":5,

"supporters":8

},

{
"text":"Ignore",

"money":0,

"bio":-10,

"commerce":0,

"arts":0,

"girls":0,

"trust":-2,

"popularity":-3,

"supporters":-5

}

]

},

{

"issue":"Girls want Cultural Festival.",

"choices":[

{

"text":"Organize Festival (₹2000)",

"money":-2000,

"bio":0,

"commerce":0,

"arts":0,

"girls":20,

"trust":4,

"popularity":5,

"supporters":10

},

{

"text":"Reject",

"money":0,

"bio":0,

"commerce":0,

"arts":0,

"girls":-15,

"trust":-3,

"popularity":-2,

"supporters":-4

}

]

},

{

"issue":"Commerce students want Placement Fair.",

"choices":[

{

"text":"Conduct Placement Fair",

"money":-1500,

"bio":0,

"commerce":20,

"arts":0,

"girls":5,

"trust":3,

"popularity":5,

"supporters":7

},

{

"text":"Promise Later",

"money":0,

"bio":0,

"commerce":-10,

"arts":0,

"girls":0,

"trust":-2,

"popularity":0,

"supporters":0

}

]

}

]

# -------------------------------------------------
# GAMEPLAY
# -------------------------------------------------

st.divider()

if player["turn"] <= len(SCENARIOS):

    scene = SCENARIOS[player["turn"]-1]

    st.subheader(f"Turn {player['turn']}")

    st.warning(scene["issue"])

    options = [x["text"] for x in scene["choices"]]

    selected = st.radio(

        "Select your decision",

        options,

        key=f"turn_{player['turn']}"

    )

    if st.button("Confirm Decision"):

        decision = None

        for item in scene["choices"]:

            if item["text"] == selected:

                decision = item

                break

        player["money"] += decision["money"]

        player["bio"] += decision["bio"]

        player["commerce"] += decision["commerce"]

        player["arts"] += decision["arts"]

        player["girls"] += decision["girls"]

        player["trust"] += decision["trust"]

        player["popularity"] += decision["popularity"]

        player["supporters"] += decision["supporters"]

        # Clamp Values

        for grp in ["bio","commerce","arts","girls"]:

            player[grp]=max(0,min(100,player[grp]))

        player["turn"]+=1

        st.success("Decision Applied")

        st.rerun()
