import streamlit as st
import json
import random

st.set_page_config(page_title="Team Pick", page_icon=":game_die:", layout="wide")

if "names" not in st.session_state:
    st.session_state.names = [name for name in json.load(open("./data/names.json"))]


st.title("Team Pick! :game_die:")

col1, col2 = st.columns(2)

with col1:
    new_name = st.text_input("Add a name", "")
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        if st.button("Add"):
            if new_name and new_name not in st.session_state.names:
                st.session_state.names.append(new_name)
            elif new_name in st.session_state.names:
                st.write(f"{new_name} already in list")
    with col1_2:
        if st.button("Remove"):
            if new_name and new_name in st.session_state.names:
                st.session_state.names.remove(new_name)
            elif new_name and new_name not in st.session_state.names:
                st.write(f"{new_name} not in list")

    st.header("Players:")
    for name in st.session_state.names:
        st.write(f"{name}")

    n_teams = st.number_input(
        "Number of teams", min_value=2, max_value=len(st.session_state.names), value=2
    )

    shuffle = st.button("Shuffle")


if shuffle:
    # Shuffle the names
    random.shuffle(st.session_state.names)

    # Calculate the size of each team
    team_size = len(st.session_state.names) // n_teams
    remainder = len(st.session_state.names) % n_teams

    # Split names into teams
    teams = []
    start = 0
    for i in range(n_teams):
        end = start + team_size + (1 if i < remainder else 0)
        teams.append(st.session_state.names[start:end])
        start = end

    # Display teams
    with col2:
        n_cols = st.columns(n_teams)
        for i, team in enumerate(teams, 1):
            with n_cols[i - 1]:
                with st.container(border=True):
                    st.subheader(f"Team {i}")
                    for name in team:
                        st.write(name)
