import streamlit as st
from dataextract import fetch_crypto_price, fetch_coin_id
import plotly.express as px

def getdata():
    st.title('Crypto Details App')

    symbol = st.text_input('Enter the Crypto Coin Name')
    
    if st.button('Get Data'):
        id = fetch_coin_id(symbol)

        if id is not None:
            df = fetch_crypto_price(id,365)

            fig = px.line(df, x='Date', y='Price', markers=True, title=f"Price of {symbol} for Last 1 Year")

            st.plotly_chart(fig)

            max_price_row = df.loc[df['Price'].idxmax()]
            max_price_date = max_price_row['Date']
            max_price = max_price_row['Price']
            
            min_price_row = df.loc[df['Price'].idxmin()]
            min_price_date = min_price_row['Date']
            min_price = min_price_row['Price']

            st.info(f"Maximum Price: {max_price} CAD | Date: {str(max_price_date).split(" ")[0]}")
            st.info(f"Minimum Price: {min_price} CAD | Date: {str(min_price_date).split(" ")[0]}")
        else:
            st.info("Enter Valid Crypto Name")