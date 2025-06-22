import streamlit as st
from conversions.temperature import convert_temperature
from conversions.distance import convert_distance
from conversions.currency import convert_currency

st.set_page_config(page_title="🌐 Unit Converter Assistant", layout="centered")

st.title("🌐 Unit Converter Assistant")
st.write("Choose a conversion type and enter your values below:")

conversion_type = st.selectbox("Conversion Type", ["Temperature", "Distance", "Currency"])

if conversion_type == "Temperature":
    st.subheader("🌡️ Temperature Conversion")

    temperature = st.number_input("Enter temperature value:", format="%.2f")
    from_unit = st.selectbox("From unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To unit", ["Celsius", "Fahrenheit", "Kelvin"])

    if st.button("Convert Temperature"):
        result = convert_temperature(temperature, from_unit, to_unit)
        st.success(f"{temperature} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Distance":
    st.subheader("📏 Distance Conversion")

    distance = st.number_input("Enter distance value:", min_value=0.0, format="%.4f")
    from_unit = st.text_input("From unit (e.g., km, feet, inches, metres)")
    to_unit = st.text_input("To unit (e.g., miles, mm, yard)")

    if st.button("Convert Distance"):
        result = convert_distance(distance, from_unit, to_unit)
        if isinstance(result, str):  # error message
            st.error(result)
        else:
            st.success(f"{distance} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Currency":
    st.subheader("💱 Currency Conversion")

    amount = st.number_input("Enter currency amount:", min_value=0.0, format="%.2f")
    from_currency = st.text_input("From currency code (e.g., INR, USD, EUR)")
    to_currency = st.text_input("To currency code (e.g., AED, CHF, GBP)")

    if st.button("Convert Currency"):
        result = convert_currency(amount, from_currency, to_currency)
        if isinstance(result, str):  # error message
            st.error(result)
        else:
            st.success(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
