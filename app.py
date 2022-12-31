import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer

# 1. Getting started with streamlit
st.write("Hello World!")

# 2. Text Elements
# Markdown
st.markdown("# Hello, bold")

# Title
st.title("This is a title")

# Header
st.header("This is a header")

# Sub header
st.subheader("This is a sub header")

# Caption
st.caption("This is a caption")

# Code block
st.code("a = 123")

# Preformatted text
st.text("This is a preformatted text")

# LaTeX
st.latex("123\s")

# 3. Data Display Elements

data, target = load_breast_cancer(return_X_y=True)

# Dataframe
st.dataframe(data)

# Tables
st.table(data)

# Metrics
st.metric("This is a metrics:", 0)

# JSON
st.json({
    "mhs1": {
        'name': 'Wahyu Adi Nugroho',
        'nim': 'A11.2019.12310',
        'age': 22,
    },
    "mhs2": {
        'name': 'Slamet Wahyunigsih',
        'nim': 'A11.2020.12310',
        'age': 21,
    },
    "mhs3": {
        'name': 'Dharma Edi Sanjaya',
        'nim': 'A11.2019.12311',
        'age': 20,
    }
})
