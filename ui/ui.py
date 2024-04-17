import streamlit as st
import joblib


def make_prediction(model, data):
#      make prediction


def main():
    st.set_page_config(layout="wide")
    st.header("Hi! 👋")
    st.title("Welcome to HomePricePilot 🌿 ")
    st.subheader('Easily predicting house 🏠 prices in various states in the USA', divider='orange')

    col1, col2, col3 = st.columns([3,1,3])

    with col1:
        state = st.selectbox(
            "Select state : ",
            ('Connecticut', 'Delaware', 'Maine', 'New Hampshire', 'New Jersey', 'New York', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'Vermont', 'Virgin Island')
        )

        with open('/Users/akshatsharma/UPES/Sem 6/AI_Applications/Housing-Price/notebook/cities.txt' , 'r') as f:
            cities = f.read().splitlines()

        city = st.selectbox(
            "Select city : ",
            (city for city in cities)
        )

        with open('/Users/akshatsharma/UPES/Sem 6/AI_Applications/Housing-Price/notebook/zip_codes.txt', 'r') as f2:
            zips = f2.read().splitlines()

        zip_code = st.selectbox(
            "Select zip : ",
            (zip for zip in zips)
        )

        status = st.radio(
            "Status : ",
            ['For sale', 'Ready to build']
        )

        model_choice = st.radio(
            "Which model would you like to use?",
            ['Linear Regression', 'Decision Tree'],
            captions=["A simple linear approach to predicting house prices.",
                      "A tree-based machine learning model for predicting house prices. "]
        )


    with col3:
       bed = st.slider(
           "Number of bedrooms : ",
           1, 123, 50
       )

       bath = st.slider(
           "Number of bathrooms : ",
           1, 198, 50
       )

       acre_lot = st.slider(
           "Acre lot : ",
           0, 100000, 50000
       )

       housing_size = st.slider(
           "Housing size : ",
           4, 1450112, 50000
       )

       if st.button("Predict", type="primary"):
            # process the inputs


            if model_choice == 'Linear Regression':



if __name__ == '__main__':
    main()