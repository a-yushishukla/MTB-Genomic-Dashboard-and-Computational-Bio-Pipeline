import streamlit as st
import pandas as pd

st.set_page_config(page_title="MTB Genomic Portal", layout="wide")
st.title("🧬 MTB Genomic Surveillance Dashboard")

st.sidebar.header("Pipeline Controls")
analysis_type = st.sidebar.selectbox("Select Task", ["Drug Resistance Screening", "Lineage Identification", "Variant Calling"])

st.info(f"Currently running: {analysis_type} on MTB Clinical Strains")

# Mock Data to show you can handle Databases/Portals
data = {
    'Strain_ID': ['MTB_001', 'MTB_002', 'MTB_003'],
    'Lineage': ['Lineage 2 (East-Asian)', 'Lineage 4 (Euro-American)', 'Lineage 1 (Indo-Oceanic)'],
    'Drug_Resistance': ['MDR', 'Sensitive', 'XDR']
}
df = pd.DataFrame(data)
st.table(df)
