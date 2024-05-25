import streamlit as st
from datetime import datetime
import requests
# import pandas as pd
print('before make_sidebar on page2')
from navigation import menu
print('after make_sidebar on page2')

def backtest_main():


    date_format = "%Y-%m-%d"
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        ib_ticker = st.selectbox("Select Ticker", ['a','b','c'])
    with col2:
        ib_start_dt = st.date_input("Start Date",
                                    datetime.strptime("2020-01-01", date_format),
                                    min_value=datetime.strptime("1998-01-02", date_format),
                                    max_value=datetime.strptime("2023-12-31", date_format))
    with col3:
        ib_end_dt = st.date_input("End Date",
                                  datetime.strptime("2023-12-31", date_format),
                                  min_value=datetime.strptime("1998-01-02", date_format),
                                  max_value=datetime.strptime("2023-12-31", date_format))
    with col4:
        ib_backtest = st.selectbox("Select Backtest", ['t1', 't2'])

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        btn_ts = st.button('Get Time Series Data')
    with col4:
        btn_bt = st.button('Perform BackTest')


menu()
st.title('Backtesting Page (pages/page2.py)')
backtest_main()

