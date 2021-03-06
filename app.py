from Helper import DO_DEBUG
import streamlit as st
from multiapp import MultiApp
# import your app modules here
from pages.home import Home
from pages.project import Project
from pages.page import Page
# StreamlitAPIException: set_page_config() can only be called once per app, and must be called as the first Streamlit command in your script.
st.set_page_config(
    page_title=" Steffin Blogs ",
    page_icon="🖖",  # halo...
    layout="wide",
    # StreamlitAPIException: initial_sidebar_state must be "auto" or "expanded" or "collapsed" (got "closed")
    initial_sidebar_state="auto",
)
# Streamlit encourages well-structured code, like starting execution in a main() function.
def main():
    app = MultiApp()
    # Add all your application here
    app.add_app("⛺ Home", Home.app)
    app.add_app("🏗️ Project", Project.app)
    app.add_app("🗃️ Pages", Page.app)
    # The main app
    app.run(group_name="Navbar") # is there some other name for this?
    st.sidebar.markdown("""
    ## Say Hi to me!

    🐦 twitter[@steffincodes](http://www.twitter.com/steffincodes)

    📷 instagram[@steffin.codes](http://www.instagram.com/steffin.codes)
    """)
if __name__ == "__main__":
    if DO_DEBUG:
        main()
    else:
        try:
            main()
        except:
            st.warning("Oops! Please rerun 😬")
