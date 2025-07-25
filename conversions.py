

def same(input):
    output = input
    return output


# - - - - TEMPERATURE - - - - #
def celsius_to_fahrenheit(input: float):
    return input * 1.8 + 32

def celsius_to_kelvins(input: float):
    return input + 273.15

def fahrenheit_to_celsius(input: float):
    return (input - 32) / 1.8

def fahrenheit_to_kelvins(input: float):
    return (input + 459.67) * (5 / 9)

def kelvins_to_celsius(input: float):
    return input - 273.15

def kelvins_to_fahrenheit(input: float):
    return (input * (9 / 5)) - 459.67


# - - - - LENGTH - - - - #

imperial_multipliers = [
    
]
# Divide by X to go down, Multiply with X - 1 to go to up.
metric_multipliers = [
    0.1,   # Millimetre
    0.01,  # Centimetre
    0.001, # Metre
    0.01,  # Kilometre
]

def convert_length_metric():
    """  """
    # Convert by recursivly applying  *0.1 or /0.1 depending of levels of differnce



# - - - - WEIGHT - - - - #
# - - - - VOLUME - - - - #