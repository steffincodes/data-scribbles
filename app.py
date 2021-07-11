import streamlit as st
from multiapp import MultiApp
# import your app modules here
from apps import home, about, search, random, request
from apps import template  # DO NOT PUBLISH
# StreamlitAPIException: set_page_config() can only be called once per app, and must be called as the first Streamlit command in your script.
st.set_page_config(
    page_title=" Steffin Blogs ",
    page_icon="🖖",  # halo...
    layout="wide",
    # StreamlitAPIException: initial_sidebar_state must be "auto" or "expanded" or "collapsed" (got "closed")
    initial_sidebar_state="auto",
)
app = MultiApp()

st.sidebar.markdown("""
# Hey there 👋

Welcome to my Data Blog! I hope you find what youare looking for!

## Contact me on:

[🐦 twitter@steffincodes](http://www.twitter.com/steffincodes)

[📷 instagram@steffincodes](http://www.instagram.com/steffincodes)
""")
# SIDE_MENU_OPTIONS : Final = [
#     # NTS: Think twice before changing
#     "⛺ Home",
#     "🥺 About",
#     "🔭 Search",
#     "🔀 Random",
#     "🙏 Requests"
# ]
# https://docs.streamlit.io/en/stable/api.html
# Add all your application here
app.add_app("⛺ Home", home.app)
app.add_app("🥺 About", about.app)
app.add_app("🔭 Search", search.app)
app.add_app("🔀 Random", random.app)
app.add_app("🙏 Requests", request.app)
# app.add_app(" Template", template.app)  # DO NOT PUBLISH
# The main app
app.run()
