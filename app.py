import streamlit as st
import random

# Initialize the list of names in memory
if 'names' not in st.session_state:
    st.session_state.names = []

st.title("Team Picker")

# Input to add a new name
new_name = st.text_input("Add a Name")

if st.button("Add Name"):
    if new_name:
        st.session_state.names.append(new_name)
        st.success(f"Added {new_name} to the list!")
    else:
        st.warning("Please enter a name.")

# Display the current list of names
st.subheader("Names List")
if st.session_state.names:
    for i, name in enumerate(st.session_state.names):
        st.write(f"{i + 1}. {name}")
else:
    st.write("No names added yet.")

# Input for number of teams
num_teams = st.number_input(
    "Number of Teams", min_value=2, max_value=len(st.session_state.names) if st.session_state.names else 2, value=2
)

if st.button("Split Teams"):
    if len(st.session_state.names) < num_teams:
        st.warning("Not enough names to split into this many teams.")
    else:
        shuffled_names = st.session_state.names.copy()
        random.shuffle(shuffled_names)
        teams = [shuffled_names[i::num_teams] for i in range(num_teams)]
        st.subheader("Teams")
        for i, team in enumerate(teams):
            st.write(f"**Team {i + 1}:**")
            for member in team:
                st.write(f"- {member}")

# Button to clear all names
if st.button("Clear All Names"):
    st.session_state.names = []
    st.success("Cleared all names.")

# Button to delete a specific name
st.subheader("Delete a Name")
name_to_delete = st.selectbox("Select a name to delete", st.session_state.names)

if st.button("Delete Name"):
    if name_to_delete:
        st.session_state.names.remove(name_to_delete)
        st.success(f"Deleted {name_to_delete}.")
    else:
        st.warning("No name selected for deletion.")