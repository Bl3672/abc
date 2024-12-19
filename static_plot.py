import pandas as pd
import streamlit as st


source = pd.read_csv("https://raw.githubusercontent.com/vega/vega-datasets/main/data/stocks.csv", 
                     parse_dates=['date'], date_format="%b %d %Y")
st.dataframe(source)


st.markdown("### Stock price")

st.line_chart(source, x="date", y="price", color="symbol",
              width=720, height=500)

year = 2005
selected_stocks=["AAPL", 'AMZN', 'IBM', 'MSFT']

