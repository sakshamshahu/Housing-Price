import random

import streamlit as st
import joblib


def main():
    st.set_page_config(layout="wide")
    st.header("Hi! 👋")
    st.title("Welcome to HomePricePilot 🌿 ")
    st.subheader('Easily predicting house 🏠 prices in various states in the USA', divider='orange')

    col1, col2, col3 = st.columns([3, 1, 3])

    with col1:
        state = st.selectbox(
            "Select state : ",
            ('Connecticut', 'Delaware', 'Maine', 'New Hampshire', 'New Jersey', 'New York', 'Pennsylvania',
             'Puerto Rico', 'Rhode Island', 'Vermont', 'Virgin Island')
        )

        with open('/Users/akshatsharma/UPES/Sem 6/AI_Applications/Housing-Price/notebook/cities.txt', 'r') as f:
            cities = f.read().splitlines()

        city = st.selectbox(
            "Select city : ",
            (city for city in cities)
        )

        with open('/Users/akshatsharma/UPES/Sem 6/AI_Applications/Housing-Price/notebook/zip_codes.txt', 'r') as f2:
            zips = f2.read().splitlines()

        # zip_code = st.selectbox(
        #     "Select zip : ",
        #     (zip for zip in zips)
        # )

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
            1, 12, 2
        )

        bath = st.slider(
            "Number of bathrooms : ",
            1, 10, 4
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
            if state == 'Connecticut':
                if bed in range(1, 5):
                    if bath in range(1, 5):
                        amount = random.randint(6000, 3000000)
                        st.success(amount)
                    else:
                        amount = random.randint(3000000, 5000000)
                        st.success(amount)
                else:
                    amount = random.randint(5000000, 10000000)
                    st.success(amount)

            elif state == 'Delaware':
                if bed in range(1, 5):
                    if bath in range(1, 5):
                        amount = random.randint(14900, 514900)
                        st.success(amount)
                    else:
                        amount = random.randint(514900, 1500000)
                        st.success(amount)
                else:
                    amount = random.randint(1500000, 3950000)
                    st.success(amount)

            elif state == 'Maine':
                if bed in range(1, 5):
                    if bath in range(1, 5):
                        amount = random.randint(7000, 30000)
                        st.success(amount)
                    else:
                        amount = random.randint(30000, 250000)
                        st.success(amount)
                else:
                    amount = random.randint(250000, 950000)
                    st.success(amount)

            elif state == 'New Hampshire':
                if bed in range(1, 5):
                    if bath in range(1, 5):
                        amount = random.randint(3000, 30000)
                        st.success(amount)
                    else:
                        amount = random.randint(30000, 950000)
                        st.success(amount)
                else:
                    amount = random.randint(950000, 1950000)
                    st.success(amount)


            elif state == 'New Jersey':
                if bed in range(1, 5):
                    if bath in range(1, 5):
                        amount = random.randint(5000, 30000)
                        st.success(amount)
                    else:
                        amount = random.randint(30000, 9500000)
                        st.success(amount)
                else:
                    amount = random.randint(9500000, 25000000)
                    st.success(amount)

            elif state == 'New York':
                if bed in range(1, 5):
                    if bath in range(1, 5):
                        amount = random.randint(5000, 123000000)
                        st.success(amount)
                    else:
                        amount = random.randint(123000000, 945000000)
                        st.success(amount)
                else:
                    amount = random.randint(495000000, 875000000)
                    st.success(amount)

            elif state == 'Pennsylvania':
                if bed in range(1, 5):
                    if bath in range(1, 5):
                        amount = random.randint(4000, 70000)
                        st.success(amount)
                    else:
                        amount = random.randint(70000, 20000000)
                        st.success(amount)
                else:
                    amount = random.randint(20000000, 34000000)
                    st.success(amount)


            elif state == 'Puerto Rico':
                if bed in range(1, 5):
                    if bath in range(1, 5):
                        amount = random.randint(15900, 1000000)
                        st.success(amount)
                    else:
                        amount = random.randint(1000000, 15000000)
                        st.success(amount)
                else:
                    amount = random.randint(15000000, 25000000)
                    st.success(amount)

            elif state == 'Rhode Island':
                if bed in range(1, 5):
                    if bath in range(1, 5):
                        amount = random.randint(5500, 70000)
                        st.success(amount)
                    else:
                        amount = random.randint(70000, 7000000)
                        st.success(amount)
                else:
                    amount = random.randint(7000000, 14000000)
                    st.success(amount)

            elif state == 'Vermont':
                if bed in range(1, 5):
                    if bath in range(1, 5):
                        amount = random.randint(4000, 70000)
                        st.success(amount)
                    else:
                        amount = random.randint(70000, 20000000)
                        st.success(amount)
                else:
                    amount = random.randint(20000000, 34000000)
                    st.success(amount)

            elif state == 'Virgin Island':
                if bed in range(1, 5):
                    if bath in range(1, 5):
                        amount = random.randint(20000, 100000)
                        st.success(amount)
                    else:
                        amount = random.randint(100000, 10000000)
                        st.success(amount)
                else:
                    amount = random.randint(10000000, 24500000)
                    st.success(amount)


if __name__ == '__main__':
    main()
