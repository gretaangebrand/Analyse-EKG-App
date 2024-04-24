import streamlit as st
#importiert die Funktionen get_person_data und get_person_list aus read_data.py
from read_data import get_person_data, get_person_list

#eingefügt von read_data.py
person_data = get_person_data()
names = get_person_list(person_data)

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

#Überschrift 1 erstellen
st.write('# Analyse EKG App')

#Überschrift der zweiten Ebene
st.write('## Versuchsperson auswählen')

# Eine Auswahlbox erstellen
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = names, key ="sbVersuchsperson")

st.write("Currently selected user is: " + st.session_state.current_user)