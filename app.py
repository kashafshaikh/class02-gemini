import streamlit as st
from gemini_helper import get_gemini_response

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict[from_unit]:
        factor = conversion_dict[from_unit][to_unit]
        return factor(value) if callable(factor) else value * factor
    return None

# Conversion factors
conversion_factors = {
    "Length": {
        "Meters": {"Kilometers": 0.001, "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701},
        "Kilometers": {"Meters": 1000},
        "Miles": {"Meters": 1609.34},
        "Yards": {"Meters": 0.9144},
        "Feet": {"Meters": 0.3048},
        "Inches": {"Meters": 0.0254},
    },
    "Weight": {
        "Kilograms": {"Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274},
        "Grams": {"Kilograms": 0.001},
        "Pounds": {"Kilograms": 0.453592},
        "Ounces": {"Kilograms": 0.0283495},
    },
    "Temperature": {
        "Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
        "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9},
        "Kelvin": {"Celsius": lambda k: k - 273.15},
    },
    "Speed": {
        "Meters per second": {"Kilometers per hour": 3.6, "Miles per hour": 2.23694},
        "Kilometers per hour": {"Meters per second": 0.277778},
        "Miles per hour": {"Meters per second": 0.44704},
    },
    "Time": {
        "Seconds": {"Minutes": 1/60, "Hours": 1/3600},
        "Minutes": {"Seconds": 60},
        "Hours": {"Seconds": 3600},
    },
    "Volume": {
        "Liters": {"Milliliters": 1000, "Cups": 4.22675, "Gallons": 0.264172},
        "Milliliters": {"Liters": 0.001},
        "Cups": {"Liters": 0.236588},
        "Gallons": {"Liters": 3.78541},
    },
    "Area": {
        "Square meters": {"Square kilometers": 0.000001, "Square feet": 10.7639},
        "Square kilometers": {"Square meters": 1000000},
        "Square feet": {"Square meters": 0.092903},
    },
    "Digital Storage": {
        "Bytes": {"Kilobytes": 0.001, "Megabytes": 0.000001},
        "Kilobytes": {"Bytes": 1000},
        "Megabytes": {"Bytes": 1000000},
    },
    "Energy": {
        "Joules": {"Calories": 0.239006},
        "Calories": {"Joules": 4.184},
    },
    "Pressure": {
        "Pascals": {"Bar": 0.00001, "PSI": 0.000145038},
        "Bar": {"Pascals": 100000},
        "PSI": {"Pascals": 6894.76},
    },
}

# Page config
st.set_page_config(page_title="Gemini AI & Unit Converter", page_icon="💬", layout="centered")

# Custom Styling
st.markdown("""
    <style>
         body {
            background: linear-gradient(to right, #93ADDA , #C2E9FB);
            color: white;E3
        }
        .stApp {
            background: linear-gradient(to right, #93ADDA , #C2E9FB);
        }
        .response-box {
            background-color: #4CA5E4;
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
            font-weight: bold;
        }
        .error-box {
            background-color: #ffcccb;
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
            font-weight: bold;
            color: red;
        }
    </style>
""", unsafe_allow_html=True)

# Tabs for Chatbot & Converter
tab1, tab2 = st.tabs(["💬 Chatbot", "🔄 Unit Converter"])

with tab1:
    st.markdown('<h1 style="text-align:center;">💬 Gemini AI Chatbot</h1>', unsafe_allow_html=True)
    st.markdown('<h4 style="text-align:center; color:gray;">Ask me Anything!</h4>', unsafe_allow_html=True)
    
    user_input = st.text_area("👤 You:", "", height=100)
    submit = st.button("Send")
    
    if submit and user_input.strip():
        try:
            response = get_gemini_response(user_input)
            st.markdown(f'<div class="response-box">🤖 <b>Gemini:</b> {response}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="error-box">❌ Error: {e}</div>', unsafe_allow_html=True)

with tab2:
    st.title("Unit Converter 🔄")
    category = st.selectbox("Select Category", list(conversion_factors.keys()))
    from_unit = st.selectbox("From", list(conversion_factors[category].keys()))
    to_unit = st.selectbox("To", list(conversion_factors[category][from_unit].keys()))
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    
    if st.button("Convert"):
        conversion_result = convert_units(value, from_unit, to_unit, conversion_factors[category])
        if conversion_result is not None:
            st.success(f"{value} {from_unit} = {conversion_result:.2f} {to_unit}")
        else:
            st.error("Conversion not available")
