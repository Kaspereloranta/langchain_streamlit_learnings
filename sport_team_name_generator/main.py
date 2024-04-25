import streamlit as st
import langchain_helper

st.title("Sport team name and branding strategy generator.")

sport = st.sidebar.selectbox("Pick a Sport", ("Hockey", "Soccer", "Basketball", "Baseball", "Football"))

if sport:
    
    response = langchain_helper.generate_sport_team_name_and_branding_strategy(sport)

    st.header(response['Name'].strip())
    
    branding_info = response['branding_info'].strip().split("\n")
    
    st.write("**Sport team**")
    
    for info in branding_info:
        st.write("-", info)