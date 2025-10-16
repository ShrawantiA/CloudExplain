import streamlit as st
import pandas as pd

st.title("CloudExplain")
st.write("Prototype dashboard for visualising AI-driven operational decisions.")

data = pd.DataFrame({
    "Metric": ["CPU", "Memory", "Latency"],
    "Value": [75, 43, 120],
    "Status": ["Normal", "Normal", "Alert"]
})
st.dataframe(data)

st.write("Placeholder for explanation graphs and reliability scores.")
