import streamlit as st
from dataextract import fetch_crypto_price, fetch_coin_id
import plotly.express as px
import pandas as pd

def compare():
    st.title('Compare Cryptos')

    symbol1 = st.text_input('Enter Crypto Coin 1:', key='symbol1')
    symbol2 = st.text_input('Enter Crypto Coin 2:', key='symbol2')

    timeframe = st.selectbox('Select Time Frame', ['1 Week', '1 Month', '1 Year', '5 Years'])

    if st.button('Compare'):
        id1 = fetch_coin_id(symbol1)
        id2 = fetch_coin_id(symbol2)

        if id1 is not None and id2 is not None:
            if timeframe is not '5 Years':
                timeframe_to_days = {
                    '1 Week': 7,
                    '1 Month': 30,
                    '1 Year': 365,
                    '5 Years': 365 * 5
                }

                days = timeframe_to_days[timeframe]
                df1 = fetch_crypto_price(id1, days)
                df2 = fetch_crypto_price(id2, days)

                df1['label'] = f'{symbol1}'
                df2['label'] = f'{symbol2}'

                df_combined = pd.concat([df1, df2])

                fig = px.line(df_combined, x='Date', y='Price', color='label', markers=True, 
                            title=f"Crypto Price Comparison: {symbol1} vs. {symbol2} for {timeframe}",
                            color_discrete_map={f'{symbol1}': 'red', f'{symbol2}': 'blue'})

                st.plotly_chart(fig)

                max_price_row1 = df1.loc[df1['Price'].idxmax()]
                max_price_date1 = max_price_row1['Date']
                max_price1 = max_price_row1['Price']
                
                min_price_row1 = df1.loc[df1['Price'].idxmin()]
                min_price_date1 = min_price_row1['Date']
                min_price1 = min_price_row1['Price']

                max_price_row2 = df2.loc[df1['Price'].idxmax()]
                max_price_date2 = max_price_row2['Date']
                max_price2 = max_price_row2['Price']
                
                min_price_row2 = df1.loc[df2['Price'].idxmin()]
                min_price_date2 = min_price_row2['Date']
                min_price2 = min_price_row2['Price']

                st.info(f"Maximum Price for {symbol1}: {max_price1} CAD | Date: {str(max_price_date1).split(" ")[0]}")
                st.info(f"Minimum Price for {symbol1}: {min_price1} CAD | Date: {str(min_price_date1).split(" ")[0]}")

                st.info(f"Maximum Price for {symbol2}: {max_price2} CAD | Date: {str(max_price_date2).split(" ")[0]}")
                st.info(f"Minimum Price for {symbol2}: {min_price2} CAD | Date: {str(min_price_date2).split(" ")[0]}")
            else:
                st.info("Unfortunately, the API used in this App can only fetch the data for last one year. Hence the app can't fetch the data for last 5 years")
        else:
            if id1 is None:
                st.info("Please enter a Valid Crypto Name 1")
                if id2 is None:
                    st.info("Please enter a Valid Crypto Name 2")
            else:
                st.info("Please enter a Valid Crypto Name 2")
