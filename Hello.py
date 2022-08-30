import streamlit as st 
from streamlit_option_menu import option_menu



st.set_page_config(page_title='Check Your Health', page_icon="♋", layout="wide")

st.sidebar.title('Title')

hide_menu_style = """
                <style>
                #MainMenu {visibility: hidden; }
                footer {visibility: hidden;}
                </style>
                """

st.markdown(hide_menu_style, unsafe_allow_html=True)


