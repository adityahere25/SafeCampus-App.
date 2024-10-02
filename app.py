import streamlit as st
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium

# Initialize app
st.title("SafeCampus: University Women's Safety App")
st.sidebar.header("Navigation")
options = st.sidebar.radio("Go to", ['Emergency SOS', 'Real-Time Location', 'Admin Dashboard', 'Check-In/Out', 'Safety Tips', 'Incident Reporting'])

# Emergency SOS Button
if options == 'Emergency SOS':
    st.header("Emergency SOS")
    st.write("Press the button to send an emergency distress signal.")
    if st.button("Send SOS"):
        st.success("Distress signal sent with your location!")
        # Add live location sharing logic here

# Real-Time Location Sharing
elif options == 'Real-Time Location':
    st.header("Real-Time Location Sharing")
    st.write("Share your live GPS location.")
    
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("Your current location")
    
    # Create map with folium
    if location:
        m = folium.Map(location=[location.latitude, location.longitude], zoom_start=12)
        folium.Marker([location.latitude, location.longitude], tooltip="You are here").add_to(m)
        st_folium(m, width=700)

# Admin Dashboard
elif options == 'Admin Dashboard':
    st.header("Admin Dashboard")
    st.write("View and manage emergency reports.")

# Check-In/Out System
elif options == 'Check-In/Out':
    st.header("Check-In/Out System")
    st.write("Check in or out when entering or leaving a potentially risky area.")

# Safety Tips and Resources
elif options == 'Safety Tips':
    st.header("Safety Tips and Resources")
    st.write("Access safety guidelines and resources.")
    st.markdown("""
    * Always be aware of your surroundings.
    * Use well-lit, populated areas.
    * Avoid walking alone at night.
    """)

# Incident Reporting
elif options == 'Incident Reporting':
    st.header("Report an Incident")
    st.write("Report any suspicious activity or incident.")
    incident_type = st.selectbox("Type of Incident", ["Suspicious Activity", "Harassment", "Other"])
    description = st.text_area("Describe the incident")
    location = st.text_input("Location")
    if st.button("Submit Report"):
        st.success("Incident report submitted successfully!")
