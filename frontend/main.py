import requests
import streamlit as st

st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("This is an Streamlit Application")

BASEURL = "http://backend:8000/{}"

def get_endpoint(endpoint):
    return BASEURL.format(endpoint)

system_info = requests.get(get_endpoint("ping")).json()

st.write(system_info)