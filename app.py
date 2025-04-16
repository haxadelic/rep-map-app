import streamlit as st
import plotly.express as px
import pandas as pd

# ----------------------------------------
# Data Setup
# ----------------------------------------
rep_data = {
    'VA': {
        'name': 'Kevin Flood',
        'title': 'Regional Sales Manager',
        'email': 'kevin@firstlinetech.com',
        'phone': '(555) 123-4567',
        'photo': 'https://via.placeholder.com/100?text=Kevin'
    },
    'CA': {
        'name': 'Amit Kapoor',
        'title': 'West Coast Rep',
        'email': 'amit@firstlinetech.com',
        'phone': '(555) 234-5678',
        'photo': 'https://via.placeholder.com/100?text=Amit'
    },
    'TX': {
        'name': 'Jeff Galbraith',
        'title': 'Southwest Rep',
        'email': 'jeff@firstlinetech.com',
        'phone': '(555) 345-6789',
        'photo': 'https://via.placeholder.com/100?text=Jeff'
    },
    'NY': {
        'name': 'Jane Doe',
        'title': 'Northeast Rep',
        'email': 'jane@firstlinetech.com',
        'phone': '(555) 456-7890',
        'photo': 'https://via.placeholder.com/100?text=Jane'
    },
    'FL': {
        'name': 'John Smith',
        'title': 'Southeast Rep',
        'email': 'john@firstlinetech.com',
        'phone': '(555) 567-8901',
        'photo': 'https://via.placeholder.com/100?text=John'
    }
}

# ----------------------------------------
# DataFrame for Map
# ----------------------------------------
df = pd.DataFrame({
    'state': list(rep_data.keys()),
    'rep': [rep_data[state]['name'] for state in rep_data]
})

# ----------------------------------------
# Streamlit Layout
# ----------------------------------------
st.set_page_config(page_title="Find Your Rep", layout="wide")
st.title("📍 Find Your Regional Representative")

# Map
fig = px.choropleth(df,
                    locations='state',
                    locationmode='USA-states',
                    scope='usa',
                    color_discrete_sequence=['#4db8ff'] * len(df),
                    hover_name='rep')

st.plotly_chart(fig, use_container_width=True)

# Dropdown
clicked_state = st.selectbox("Or select your state:", df['state'])
selected = rep_data[clicked_state]

# Rep Display
selected = rep_data[clicked_state]

st.markdown("### Your Representative:")

col1, col2 = st.columns([1, 3])

with col1:
    st.image(selected['photo'], width=100)

with col2:
    st.markdown(f"""
    **{selected['name']}**  
    *{selected['title']}*  
    📞 {selected['phone']}  
    📧 [{selected['email']}](mailto:{selected['email']})
    """)


col1, col2 = st.columns([1, 3])

with col1:
    st.image(selected['photo'], width=100)

with col2:
    st.markdown(f"""
    **{selected['name']}**  
    *{selected['title']}*  
    📞 {selected['phone']}  
    📧 [{selected['email']}](mailto:{selected['email']})
    """)

# Optional: Footer
st.markdown("---")
st.markdown("If you don't see your state, contact us at [info@firstlinetech.com](mailto:info@firstlinetech.com).")
