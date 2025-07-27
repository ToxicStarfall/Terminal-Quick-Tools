

def same(input):
    output = input
    return output

def units(group, input_type, output_type, value):
    result = None
    if group == "temperature":
        func_name = f"{input_type}_to_{output_type}"
        result = Temperature[func_name](value)
    elif group == "length":
        result = length(input_type, output_type, value)
    else:
        result = "Error, No funcs"
    return result


# - - - - TEMPERATURE - - - - #
# def celsius_to_fahrenheit(input: float):
#     return input * 1.8 + 32
# def celsius_to_kelvins(input: float):
#     return input + 273.15
# def fahrenheit_to_celsius(input: float):
#     return (input - 32) / 1.8
# def fahrenheit_to_kelvins(input: float):
#     return (input + 459.67) * (5 / 9)
# def kelvins_to_celsius(input: float):
#     return input - 273.15
# def kelvins_to_fahrenheit(input: float):
    # return (input * 1.8) - 459.67

Temperature = {
    "celsius_to_fahrenheit": lambda x: x * 1.8 + 32,
    "celsius_to_kelvins": lambda x: x + 273.15,
    "fahrenheit_to_celsius": lambda x: (x - 32) / 1.8,
    "fahrenheit_to_kelvins": lambda x: (x + 459.67) * (5/9),
    "kelvins_to_celsius": lambda x: x - 273.15,
    "kelvins_to_fahrenheit": lambda x: (x * 1.8) - 459.67,
}

# - - - - LENGTH - - - - #
LengthMulitpliers = {
    "metres_to_inches": 39.3701,
    "metres_to_feet": 3.28084,
    "metres_to_yards": 1.09361,
    "metres_to_miles": 0.000621371,
    "metres_to_millimetres": 1000,
    "metres_to_centimetres": 100,
    "metres_to_metres": 1,
    "metres_to_kilometres": 0.001,
}

def length(input_type, output_type, value):
    # If input is not in Metres, convert to Metres
    if input_type != "metres":
        value = value / LengthMulitpliers[f"metres_to_{input_type}"]
    # Continue with normal conversion from Metres.
    conversion = f"metres_to_{output_type}"
    multiplier = LengthMulitpliers[conversion]
    result = value * multiplier
    return result
    

# - - - - WEIGHT - - - - #
# - - - - VOLUME - - - - #