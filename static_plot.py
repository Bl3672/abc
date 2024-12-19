import pandas as pd
import streamlit as st
source = pd.read_csv("https://raw.githubusercontent.com/vega/vega-datasets/main/
data/stocks.csv",
parse_dates=['date'], date_format="%b %d %Y")
st.dataframe(source)
st.markdown("### Stock price")
st.line_chart(source, x="date", y="price", color="symbol",
width=720, height=500)
year = 2005
selected_stocks=["AAPL", 'AMZN', 'IBM', 'MSFT']
# the querying step won't be tested in the final
stocks_2005 = source.query(f"date < {year + 1} and date >= {year} and symbol in
{selected_stocks}")
st.markdown(f"### Stock prices in {year}<br>", unsafe_allow_html=True)
st.line_chart(stocks_2005, x="date", y="price", color="symbol",
width=720, height=500)
