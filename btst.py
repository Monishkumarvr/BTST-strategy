import pandas as pd
import datetime
import streamlit as st

st.title("BTST Swing trading strategy")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
else:
    st.write("Upload a File")
    
#df = pd.read_csv("Backtest Copy - BOSS SCANNER FOR BTST, Technical Analysis Scanner.csv")

grouped_df = df.groupby("symbol")

first_values = grouped_df.first()
first_values = first_values.reset_index()
first_values['date'] = pd.to_datetime(first_values['date'], dayfirst=True).dt.date
first_values = first_values.sort_values("date")

if st.button('Get Stocks'):
    st.write(first_values)
    #print(first_values)
