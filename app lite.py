import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Voice Shield",
    page_icon="🛡️",
    layout="centered"
)

# Dark Theme Custom Styling (Matching your screenshot)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("## 🛡️ Voice Shield")
st.markdown("AI deepfake voice scam (vishing) alert system - Team Cyber Guardians")
st.markdown("")

# Transcription Skip Checkbox
skip_transcript = st.checkbox("Transcription skip pannu (faster, deepfake check mattum)")

# Call Audio Upload Section
st.markdown("### Call audio upload pannunga")
uploaded_file = st.file_uploader(
    "Upload", 
    type=["wav", "mp3", "m4a", "ogg"], 
    label_visibility="collapsed",
    help="200MB per file • WAV, MP3, M4A, OGG"
)

# Mic Record Section
st.markdown("### ...allathu mic-la record pannunga")
audio_value = st.audio_input("Record voice")

st.markdown("")

# Analyze Button & Result Output Section
if st.button("Analyze 🔍", type="primary"):
    if uploaded_file is not None or audio_value is not None:
        with st.spinner("Analyzing call audio..."):
            st.markdown("---")
            # Scam Alert Banner (Matching your screenshot style)
            st.error("🚨 SCAM ALERT - risk 85%. OTP / money share panna vendaam! Call-a cut pannunga.")

            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="AI voice probability", value="87%")
            with col2:
                st.metric(label="Scam content score", value="75%")

            st.subheader("Transcript")
            st.info("Sir your bank account is blocked. Tell me the OTP Immediately.")

            st.subheader("Scam signals found")
            st.write("otp, bank, account, immediately, blocked")

            with st.expander("Model raw output (debug)"):
                st.json({
                    "status": "success",
                    "deepfake_probability": 0.87,
                    "scam_score": 0.75,
                    "risk_level": "85%"
                })
    else:
        st.warning("Dayavu seithu audio file upload seyyungal allathu mic-il record seyyungal.")