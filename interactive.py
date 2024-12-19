import streamlit as st

import pandas as pd

source = pd.read_csv(
    "https://raw.githubusercontent.com/vega/vega-datasets/main/data/stocks.csv", 
    parse_dates=['date'], date_format="%b %d %Y"
    ).query(f"date < 2010 and date >= 2005")

stocks = ['AAPL', 'AMZN', 'GOOG', 'IBM', 'MSFT']

st.dataframe(source)

selected_stocks = st.multiselect("Select stocks for comparison", 
               stocks, default=["AAPL", 'AMZN'])

year = st.slider("Select a year", min_value=2005, max_value=2009)

# the querying step won't be tested in the final
subset = source.query(f"date < {year + 1} and date >= {year} and symbol in {selected_stocks}")

st.line_chart(subset, x="date", y="price", color="symbol",
              width=720, height=500)