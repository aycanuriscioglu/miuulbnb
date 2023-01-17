import streamlit as st
from PIL import Image
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import joblib
from collections.abc import Iterable
from catboost import CatBoostRegressor
import numpy as np

st.title("Miuul BnB")
back_gr = Image.open("images/berlin.jpeg")
st.image(back_gr, width=600)

st.sidebar.title("Filters")
st.sidebar.title("Berlin")

neighbourhood = st.sidebar.selectbox("Neighbourhood", ("Neighbourhood", 'Neukölln', 'Reinickendorf', 'Charlottenburg-Wilm',
                                                'Friedrichshain-Kreuzberg', 'Tempelhof - Schöneberg', 'Mitte',
                                                'Spandau', 'Steglitz - Zehlendorf', 'Treptow - Köpenick',
                                                'Marzahn - Hellersdorf', 'Lichtenberg', 'Pankow'))
if neighbourhood == "Neighbourhood":
    st.sidebar.write("Neighbourhood")
elif neighbourhood == "Neukölln":
    st.sidebar.write("Neukölln")
elif neighbourhood == "Reinickendorf":
    st.sidebar.write("Reinickendorf")
elif neighbourhood == "Charlottenburg-Wilm":
    st.sidebar.write("Charlottenburg-Wilm")
elif neighbourhood == "Friedrichshain-Kreuzberg":
    st.sidebar.write("Friedrichshain-Kreuzberg")
elif neighbourhood == "Tempelhof - Schöneberg":
    st.sidebar.write("Tempelhof - Schöneberg")
elif neighbourhood == "Mitte":
    st.sidebar.write("Mitte")
elif neighbourhood == "Spandau":
    st.sidebar.write("Spandau")
elif neighbourhood == "Steglitz - Zehlendorf":
    st.sidebar.write("Steglitz - Zehlendorf")
elif neighbourhood == "Treptow - Köpenick":
    st.sidebar.write("Treptow - Köpenick")
elif neighbourhood == "Marzahn - Hellersdorf":
    st.sidebar.write("Marzahn - Hellersdorf")
elif neighbourhood == "Lichtenberg":
    st.sidebar.write("Lichtenberg")
elif neighbourhood == "Pankow":
    st.sidebar.write("Pankow")
guests_included= st.sidebar.selectbox("Add Guests", ("Add Guests", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"))
if guests_included == "Add Guests":
    st.sidebar.write("Add Guests")
elif guests_included == "1":
    st.sidebar.write("1")
elif guests_included == "2":
    st.sidebar.write("2")
elif guests_included == "3":
    st.sidebar.write("3")
elif guests_included == "4":
    st.sidebar.write("4")
elif guests_included == "5":
    st.sidebar.write("5")
elif guests_included == "6":
    st.sidebar.write("6")
elif guests_included == "7":
    st.sidebar.write("7")
elif guests_included == "8":
    st.sidebar.write("8")
elif guests_included == "9":
    st.sidebar.write("9")
elif guests_included == "10":
    st.sidebar.write("10")
elif guests_included == "11":
    st.sidebar.write("11")
elif guests_included == "12":
    st.sidebar.write("12")
elif guests_included == "13":
    st.sidebar.write("13")
elif guests_included == "14":
    st.sidebar.write("14")
elif guests_included == "15":
    st.sidebar.write("15")
room_type = st.sidebar.selectbox("Room Type", ("Room Type", "Home", "Private room", "Shared room"))
if room_type == "Room Type":
    st.sidebar.write("Room Type")
elif room_type == "Home":
    st.sidebar.write("Home")
elif room_type == "Private room":
    st.sidebar.write("Private room")
elif room_type == "Shared room":
    st.sidebar.write("Shared room")
bedrooms = st.sidebar.selectbox("Bedrooms", ("Bedrooms", "1", "2", "3", "4", "5", "6", "7", "8"))
if bedrooms == "Bedrooms":
    st.sidebar.write("Bedrooms")
elif bedrooms == "1":
    st.sidebar.write("1")
elif bedrooms == "2":
     st.sidebar.write("2")
elif bedrooms == "3":
    st.sidebar.write("3")
elif bedrooms == "4":
    st.sidebar.write("4")
elif bedrooms == "5":
    st.sidebar.write("5")
elif bedrooms == "6":
    st.sidebar.write("6")
elif bedrooms == "7":
    st.sidebar.write("7")
elif bedrooms == "8":
    st.sidebar.write("8")
beds = st.sidebar.selectbox("Beds", ("Beds", "1", "2", "3", "4", "5", "6", "7", "8"))
if beds == "Beds":
    st.sidebar.write("Beds")
elif beds == "1":
    st.sidebar.write("1")
elif beds == "2":
    st.sidebar.write("2")
elif beds == "3":
    st.sidebar.write("3")
elif beds == "4":
    st.sidebar.write("4")
elif beds == "5":
    st.sidebar.write("5")
elif beds == "6":
    st.sidebar.write("6")
elif beds == "7":
    st.sidebar.write("7")
elif beds == "8":
    st.sidebar.write("8")
bed_type = st.sidebar.selectbox("Bed Type", ("Bed Type", "Real Bed", "Pull-out Sofa", "Futon", "Couch", "Airbed "))
if bed_type == "Bed Type":
    st.sidebar.write("Bed Type")
elif bed_type == "Real Bed":
    st.sidebar.write("Real Bed")
elif bed_type == "Pull-out Sofa":
    st.sidebar.write("Pull-out Sofa")
elif bed_type == "Futon":
    st.sidebar.write("Futon")
elif bed_type == "Couch":
    st.sidebar.write("Couch")
elif bed_type == "Airbed":
    st.sidebar.write("Airbed")
bathrooms = st.sidebar.selectbox("Bathrooms", ("Bathrooms", "0", "1", "2", "3"))
if bathrooms == "Bathrooms":
    st.sidebar.write("Bathrooms")
elif bathrooms == "0":
    st.sidebar.write("0")
elif bathrooms == "1":
    st.sidebar.write("1")
elif bathrooms == "2":
    st.sidebar.write("2")
elif bathrooms == "3":
    st.sidebar.write("3")
cleaning_fee = st.sidebar.slider("Cleaning Fee", 0, 100)
st.sidebar.write(f"Value: {cleaning_fee}")
security_deposit = st.sidebar.slider("Security Deposit Fee", 0, 100)
st.sidebar.write(f"Value: {security_deposit}")
minimum_nights = st.sidebar.slider("Minimum Nights", 0, 30)
st.sidebar.write(f"Value: {minimum_nights}")


pred_df = pd.DataFrame({"neighbourhood": neighbourhood,
                        "room_type": room_type, "bathrooms": bathrooms,
                        "bedrooms": bedrooms, "beds": beds, "bed_type": bed_type,
                        "security_deposit": security_deposit, "cleaning_fee": cleaning_fee,
                        "guests_included": guests_included, "minimum_nights": minimum_nights}, index=[0])


approving = st.sidebar.button("Approving Filters")
model = joblib.load("final_son_model.pkl")

if approving:
    # TAHMİN
    st.success(f"Estimated price of your house per night: **{model.predict(pred_df)[0]}**")

#terminale girip sayfayı aktifleştirme
#streamlit run final_canlı.py
