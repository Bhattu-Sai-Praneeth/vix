import streamlit as st
import yfinance as yf

st.write("Debug: Script started")

def fetch_vix():
    vix = yf.Ticker("^VIX")
    vix_data = vix.history(period="1d")
    st.write("Debug: Fetched VIX data")
    if not vix_data.empty:
        return vix_data['Close'].iloc[0]
    return None

st.title("VIX Tracker")
st.write("Debug: UI Loaded")

if st.button("Get Latest VIX Value"):
    st.write("Debug: Button clicked")
    vix_value = fetch_vix()
    if vix_value is not None:
        st.write(f"**Latest VIX Value:** {vix_value}")
        if vix_value <= 20:
            st.success("VIX is within the acceptable range.")
        else:
            st.warning("VIX is above the acceptable range. Be cautious.")
    else:
        st.error("Could not fetch VIX data.")
