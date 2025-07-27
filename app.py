import streamlit as st
import datetime
import os
import json
from pathlib import Path
import sys

# Add src/stockpicker to sys.path for imports
sys.path.append(str(Path(__file__).parent / 'src' / 'stockpicker'))

from src.stockpicker.main import run as stockpicker_run

st.set_page_config(page_title="AI Stock Picker", layout="wide")
st.title("🤖 AI Stock Picker Dashboard")

# Sidebar for user input
st.sidebar.header("Input Parameters")

# Sector selection (customize as needed)
sectors = [
    "Technology", "Healthcare", "Finance", "Consumer Goods", "Energy", "Utilities", "Industrials", "Materials", "Real Estate", "Telecommunications"
]
sector = st.sidebar.selectbox("Select Sector", sectors)

date = st.sidebar.date_input("Date", datetime.date.today())

# Run button
if st.sidebar.button("Run Stock Picker"):
    st.markdown("It will take 3-4 minutes approximately.")
    with st.spinner("Running stock picker..."):

        # Patch the run() function to accept parameters
        # For now, we monkeypatch the inputs in main.py
        # You may want to refactor main.py to accept parameters
        # For now, we run as is and display output files
        stockpicker_run(sector)

    st.success("Stock picking complete!")

    # Display final decision
    decision_path = Path("output/decision.md")
    if decision_path.exists():
        st.subheader("Final Decision")
        with open(decision_path) as f:
            st.markdown(f.read())
        st.download_button("Download Decision", decision_path.read_bytes(), file_name="decision.md")
    else:
        st.warning("No decision file found.")

    # Display research report
    report_path = Path("output/research_report.json")
    if report_path.exists():
        st.subheader("Research Report")
        with open(report_path) as f:
            report = json.load(f)
        st.json(report)
        st.download_button("Download Research Report", report_path.read_bytes(), file_name="research_report.json")
    else:
        st.warning("No research report found.")

    # Display trending companies
    trending_path = Path("output/trending_companies.json")
    if trending_path.exists():
        st.subheader("Trending Companies")
        with open(trending_path) as f:
            trending = json.load(f)
        st.json(trending)
        st.download_button("Download Trending Companies", trending_path.read_bytes(), file_name="trending_companies.json")
    else:
        st.info("No trending companies file found.")
else:
    st.info("Select parameters and click 'Run Stock Picker' to begin.") 