import streamlit as st
import random

# Game Settings
if 'game_state' not in st.session_state:
    st.session_state.game_state = {
        'stage': 'map', # map, play, game_over
        'district': None,
        'fund': 10000,
        'votes': 0,
        'land': 0,
        'turn': 1,
        'logs': ["Game Shuru! MP ka Neta banne ka safar."]
    }

def play_action(cost, vote_gain, land_gain, msg):
    state = st.session_state.game_state
    if state['fund'] >= cost:
        state['fund'] -= cost
        state['votes'] += vote_gain
        state['land'] += land_gain
        state['turn'] += 1
        state['logs'].insert(0, f"Turn {state['turn']}: {msg} (-₹{cost}, +{vote_gain} Votes)")
    else:
        state['logs'].insert(0, "Fund kam hai! Jugaad karo.")

def reset_game():
    st.session_state.game_state = {
        'stage': 'map',
        'district': None, 'fund': 10000, 'votes': 0, 'land': 0, 'turn': 1, 'logs': ["Naya game shuru!"]
    }

# UI Logic
st.title("🗳️ MP Neta: Strategy Campaign")

if st.session_state.game_state['stage'] == 'map':
    st.subheader("Map Chunein:")
    districts = ["Indore", "Ujjain", "Bhopal", "Gwalior", "Jabalpur"]
    selected = st.selectbox("Apna Jila Chunein", districts)
    if st.button("Mission Shuru Karein"):
        st.session_state.game_state['stage'] = 'play'
        st.session_state.game_state['district'] = selected
        st.rerun()

elif st.session_state.game_state['stage'] == 'play':
    state = st.session_state.game_state
    st.sidebar.header(f"Jila: {state['district']}")
    st.sidebar.metric("Fund", f"₹{state['fund']}")
    st.sidebar.metric("Votes", state['votes'])
    st.sidebar.metric("Zameen", state['land'])
    
    st.write(f"Turn: {state['turn']} | Target: 2000 Votes")

    # Actions
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏢 Zameen Kharido (₹3000)"):
            play_action(3000, 100, 1, "Zameen ka kabza le liya!")
        if st.button("📢 Badi Rally (₹1500)"):
            play_action(1500, 500, 0, "Public me bhaukaal ban gaya.")
    with col2:
        if st.button("🤝 Builder se Donation (Jugaad)"):
            st.session_state.game_state['fund'] += 2000
            st.session_state.game_state['logs'].insert(0, "Builder se paisa liya, par Reputation down.")
            st.rerun()

    # Win Condition
    if state['votes'] >= 2000:
        st.success("Badhai ho! Aap jeet gaye!")
        if st.button("Wapas Map"):
            reset_game()
            st.rerun()

    st.subheader("Log Feed:")
    for log in state['logs'][:5]:
        st.text(log)

elif st.session_state.game_state['stage'] == 'game_over':
    st.write("Game Over!")
    if st.button("Restart"):
        reset_game()
        st.rerun()
