import streamlit as st
import random

st.set_page_config(page_title="Notenrechner", page_icon="🧮")

st.title("🧮 Notenrechner für Schüler (10–12 Jahre)")
st.write("Gib deine Noten ein und berechne deinen (gewichteten) Durchschnitt 📊")

# Lobtexte
lobtexte = [
    "Super gemacht! 🌟",
    "Tolle Leistung! 👏",
    "Weiter so! 🚀",
    "Das hast du richtig gut gemacht! ⭐",
    "Klasse Arbeit! 🏆"
]

# Session State für dynamische Eingaben
if "noten" not in st.session_state:
    st.session_state.noten = [1]

if "gewichte" not in st.session_state:
    st.session_state.gewichte = [1.0]

def farbe_fuer_note(note):
    if note == 1:
        return "blue"
    elif note in [2, 3]:
        return "green"
    elif note == 4:
        return "orange"
    else:
        return "red"

st.subheader("✏️ Deine Noten")

for i in range(len(st.session_state.noten)):
    col1, col2 = st.columns(2)

    with col1:
        st.session_state.noten[i] = st.number_input(
            f"Note {i+1}",
            min_value=1,
            max_value=6,
            step=1,
            value=st.session_state.noten[i],
            key=f"note_{i}"
        )

    with col2:
        st.session_state.gewichte[i] = st.number_input(
            f"Gewicht {i+1}",
            min_value=0.1,
            step=0.1,
            value=st.session_state.gewichte[i],
            key=f"gewicht_{i}"
        )

    farbe = farbe_fuer_note(st.session_state.noten[i])
    st.markdown(
        f"<span style='color:{farbe}; font-weight:bold;'>Note: {st.session_state.noten[i]}</span>",
        unsafe_allow_html=True
    )

st.button(
    "➕ Note hinzufügen",
    on_click=lambda: (
        st.session_state.noten.append(1),
        st.session_state.gewichte.append(1.0)
    )
)

# Berechnung
if st.session_state.noten:
    gesamtgewicht = sum(st.session_state.gewichte)
    gewichtete_summe = sum(
        n * g for n, g in zip(st.session_state.noten, st.session_state.gewichte)
    )

    durchschnitt = round(gewichtete_summe / gesamtgewicht, 1)

    st.subheader("📊 Ergebnis")

    farbe = farbe_fuer_note(round(durchschnitt))
    st.markdown(
        f"<h2 style='color:{farbe};'>Durchschnitt: {durchschnitt}</h2>",
        unsafe_allow_html=True
    )

    if durchschnitt < 2.0:
        st.success(random.choice(lobtexte))
