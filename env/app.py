import streamlit as st


# Create the navigation and run it
pg = st.navigation([st.Page('main.py', icon="🔍",title="Enery prediction"), st.Page('eda.py',icon="📈",title="Insights for user")])
pg.run()
