import streamlit as st
import joblib

# importing the models
# connecticut_lr = joblib.load('')
# connecticut_dt = joblib.load('')
# delaware_lr = joblib.load('')
# delaware_dt = joblib.load('')
# maine_lr = joblib.load('')
# maine_dt = joblib.load('')
# massachusetts_lr = joblib.load('')
# massachusetts_dt = joblib.load('')
# newhampshire_lr = joblib.load('')
# newhampshire_dt = joblib.load('')
# newjersey_lr = joblib.load('')
# newjersey_dt = joblib.load('')
# newyork_lr = joblib.load('')
# newyork_dt = joblib.load('')
# pennsylvania_lr = joblib.load('')
# pennsylvania_dt = joblib.load('')
# puertorico_lr = joblib.load('')
# puertorico_dt = joblib.load('')
# rhodeisland_lr = joblib.load('')
# rhodeisland_dt = joblib.load('')
# vermont_lr = joblib.load('')
# vermont_dt = joblib.load('')
# virginislands_lr = joblib.load('')
# virginislands_dt = joblib.load('')


# importing tranformations
# del_acre_lot_scalar = joblib.load('../models/trans/delaware_acre_lot_scaler.pkl')
# del_bed_scalar = joblib.load('../models/trans/delaware_bed_scaler.pkl')
# del_house_scalar = joblib.load('../models/trans/delaware_house_scaler.pkl')
# del_price_scalar = joblib.load('../models/trans/delaware_price_scaler.pkl.pkl')
# del_bath_scalar = joblib.load('../models/trans/delaware_bath_scaler.pkl.pkl')


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

        # status = st.radio(
        #     "Status : ",
        #     ['For sale', 'Ready to build']
        # )

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
        # bed , bath, acrelot , zipcode , housingsize, city , state
        input_bed = bed
        input_bath = bath
        input_acre = acre_lot
        input_zip = zip_code
        input_housing_size = housing_size
        input_city = city
        input_state = state


if __name__ == '__main__':
    main()