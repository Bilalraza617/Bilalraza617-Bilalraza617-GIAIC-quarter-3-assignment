import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    # Convert all units to meters first
    to_meter = {
        "millimeter": value * 0.001,
        "centimeter": value * 0.01,
        "meter": value,
        "kilometer": value * 1000,
        "inch": value * 0.0254,
        "foot": value * 0.3048,
        "yard": value * 0.9144,
        "mile": value * 1609.34,
    }
    meters = to_meter.get(from_unit, value)  # Default to value if unit not found

    # Convert meters to the target unit
    from_meter = {
        "millimeter": meters / 0.001,
        "centimeter": meters / 0.01,
        "meter": meters,
        "kilometer": meters / 1000,
        "inch": meters / 0.0254,
        "foot": meters / 0.3048,
        "yard": meters / 0.9144,
        "mile": meters / 1609.34,
    }
    return from_meter.get(to_unit, meters)

def convert_weight(value, from_unit, to_unit):
    # Convert all units to kilograms first
    to_kilogram = {
        "milligram": value * 0.000001,
        "gram": value * 0.001,
        "kilogram": value,
        "tonne": value * 1000,
        "ounce": value * 0.0283495,
        "pound": value * 0.453592,
    }
    kilograms = to_kilogram.get(from_unit, value)

    # Convert kilograms to the target unit
    from_kilogram = {
        "milligram": kilograms / 0.000001,
        "gram": kilograms / 0.001,
        "kilogram": kilograms,
        "tonne": kilograms / 1000,
        "ounce": kilograms / 0.0283495,
        "pound": kilograms / 0.453592,
    }
    return from_kilogram.get(to_unit, kilograms)

def convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15

    # Convert Celsius to the target unit
    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return (celsius * 9 / 5) + 32
    elif to_unit == "kelvin":
        return celsius + 273.15

def convert_volume(value, from_unit, to_unit):
    # Convert all units to liters first
    to_liter = {
        "milliliter": value * 0.001,
        "liter": value,
        "cubic meter": value * 1000,
        "gallon": value * 3.78541,
        "quart": value * 0.946353,
        "pint": value * 0.473176,
        "cup": value * 0.24,
    }
    liters = to_liter.get(from_unit, value)

    # Convert liters to the target unit
    from_liter = {
        "milliliter": liters / 0.001,
        "liter": liters,
        "cubic meter": liters / 1000,
        "gallon": liters / 3.78541,
        "quart": liters / 0.946353,
        "pint": liters / 0.473176,
        "cup": liters / 0.24,
    }
    return from_liter.get(to_unit, liters)

# Streamlit App
st.title("Advanced Unit Converter 📏")

# Dropdown for selecting conversion type
conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Weight", "Temperature", "Volume"],
)

# Input fields
value = st.number_input("Enter value to convert:", min_value=0.0)

# Unit selection based on conversion type
if conversion_type == "Length":
    units = ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"]
elif conversion_type == "Weight":
    units = ["milligram", "gram", "kilogram", "tonne", "ounce", "pound"]
elif conversion_type == "Temperature":
    units = ["celsius", "fahrenheit", "kelvin"]
elif conversion_type == "Volume":
    units = ["milliliter", "liter", "cubic meter", "gallon", "quart", "pint", "cup"]

from_unit = st.selectbox("From unit:", units)
to_unit = st.selectbox("To unit:", units)

# Perform conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif conversion_type == "Volume":
        result = convert_volume(value, from_unit, to_unit)

    st.success(f"Converted value: **{result:.4f} {to_unit}**")