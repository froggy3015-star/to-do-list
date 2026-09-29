import streamlit as st

if "to_do_list" not in st.session_state:
    st.session_state.to_do_list = []

st.title("To-Do List:")

item_input = st.text_input("Enter your task here", key="text_input")

if st.button("Enter", key="submit_btn"):
    if item_input.strip():
        st.session_state.to_do_list.append(item_input.strip())

nonitem_input = st.text_input("Remove your task here", key="delete_input")

if st.button("Delete", key="delete_btn"):
    if nonitem_input.strip():
        if int(nonitem_input) <= len(st.session_state.to_do_list):
            del st.session_state.to_do_list[int(nonitem_input) - 1]

for idx, item in enumerate(st.session_state.to_do_list, start=1):
    st.write(f"{idx}. {item}")