import streamlit as st

page = {
    "Your account": [
        st.Page{"create_account.py", title="Create your account"}
        st.Page{"manage_account.py", title="Manage your account"}
    ],
    "Resourse": [
        st.Page("learn.py", title="Learn about us"),
        st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()
