import streamlit as st
import pandas as pd
from scripts.data_prep import prepare_data  # your existing data prep function
from scripts.llm_interface import generate_summary
from scripts.data_prep import format_for_llm

st.set_page_config(
    page_title="AI-powered FP&A Copilot",
    layout="centered"
)

st.title("AI-powered FP&A Copilot")
st.write(
    "Upload structured FP&A data and generate executive-ready financial insights using AI."
)

# ---- Upload CSV ----
uploaded_file = st.file_uploader(
    "Upload FP&A CSV file",
    type=["csv"]
)

if uploaded_file:
    df_raw = pd.read_csv(uploaded_file)
    st.subheader("Raw Data Preview")
    st.dataframe(df_raw.head())

    # Optional: prepare data using your existing logic
    df_prepared = prepare_data(df_raw)
    st.subheader("Prepared FP&A Data")
    st.dataframe(df_prepared.head())


if st.button("Generate Executive Summary"):
    with st.spinner("Generating insights..."):
        data_text = format_for_llm(df_prepared)

        prompt = f"""
You are a senior FP&A analyst preparing executive commentary.

Below is monthly FP&A performance data:

{data_text}

Please provide:
1. Revenue vs Budget highlights
2. Expense vs Budget highlights
3. Key risks or trends
4. Clear management recommendations

Write concisely in an executive tone.
"""

        summary = generate_summary(prompt)

    st.subheader("Executive Summary")
    st.write(summary)
