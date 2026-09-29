import streamlit as st

st.title("Welcome to my web app")
st.write("This is a simple web app created using Streamlit.")

# Sidebar
st.sidebar.title("About")
st.sidebar.write("This app demonstrates basic Streamlit features.")

# Input widgets
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Display data
data = {
    "Column A": [1, 2, 3, 4],
    "Column B": [10, 20, 30, 40],
    "Column C": [100, 200, 300, 400]
}
st.write("## Sample Data:")
st.dataframe(data)

# Buttons
if st.button("Click Me"):
    st.write("Button clicked!")


st.header("This is header")
st.subheader("this is subheader")
 

agree = st.checkbox("I agree")
if agree:
    st.write("You agreed!")

level = st.slider("Select a Level:", 1, 10, 5)


st.file_uploader("Upload a File", type=["csv", "txt"])