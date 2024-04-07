'''Main'''
import streamlit as st
from getdata import getdata
from compare import compare
from imageclassifier import imageclassifier

def main():
    '''Main'''
    st.sidebar.title("Navigation")
    pages = ["Get Data", "Compare Cryptos", "Image Classifier"]
    choice = st.sidebar.radio("Go to", pages)

    if choice == "Get Data":
        getdata()
    elif choice == "Compare Cryptos":
        compare()
    elif choice == "Image Classifier":
        imageclassifier()

if __name__ == "__main__":
    main()
