import streamlit as st
import plotly.express as px
import pandas as pd

rep_data = {
    'VA': 'Kevin Flood',
    'CA': 'Amit Kapoor',
    'TX': 'Jeff Galbraith',
    'NY': 'Jane Doe',
    'FL': 'John Smith',
}

df = pd.DataFrame({'state': list(rep_data.keys()), 'rep': list(rep_data.values())})

fig = px.choropleth(df,
                    locations='state',
                    locationmode='USA-states',
                    scope='usa',
                    color_discrete_sequence=['#4db8ff']*len(df),
                    hover_name='rep')

st.title("Find Your Rep")
st.plotly_chart(fig, use_container_width=True)

clicked_state = st.selectbox("Or select your state:", df['state'])
st.markdown(f"### Your Representative:\n**{rep_data[clicked_state]}**")
