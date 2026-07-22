import random
import time
import streamlit as st


st.set_page_config(
    page_title="Web Page Input",
    layout="centered"
)


# Cache the result for exactly 60 seconds
@st.cache_data(ttl=60)
def generate_entropy():
    random_number = random.randint(0, 32767)
    current_time = int(time.time())

    return random_number ^ current_time


entropy_val = generate_entropy()


st.header("Web page Input")

with st.form("web_input_form"):
    name = st.text_input(
        "Name:",
        value="Carl"
    )

    favorite_color = st.text_input(
        "Favorite Color:",
        value="Blue"
    )

    st.text_input(
        "Result of command (( RANDOM ^ (date +%s) )):",
        value=str(entropy_val),
        disabled=True
    )

    submitted = st.form_submit_button("Submit")


st.divider()

st.header("Web page Output")

if submitted:
    st.write(f"Hi, my name is {name}.")
    st.write(f"My favorite color is {favorite_color}")
    st.write(f"This is my entropy {entropy_val}")
