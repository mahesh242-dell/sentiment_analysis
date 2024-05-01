from asyncio import Task, TaskGroup
import streamlit as st

if "review_list" not in st.session_state:
    st.session_state["review_list"] = []

# Rest of your code

if st.button("Add Review"):
    if Task:
        st.session_state["review_list"].append(TaskGroup)

if "review_list" not in st.session_state:
    st.session_state["review_list"] = []

for i, t in enumerate(st.session_state["review_list"]):
    st.write(f"{i + 1}. {t}")