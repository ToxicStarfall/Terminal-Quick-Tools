

def same(input):
	output = input
	return output


def units(unit_type, input_type, output_type, value):
	result = None
	# Temperature units have different conversion methods.
	if unit_type == "temperature":
		func_name = f"{input_type}_to_{output_type}"
		result = Temperature[func_name](value)

	# Normal unit converions with multipliers from a base unit.
	else:
		UnitMultipliers = ConversionMultipliers[unit_type]
		base = UnitMultipliers["base"]

		# If input is not the base type, convert to base type 
		if input_type != base:
			value = value / UnitMultipliers[input_type]
		# Continue with normal conversion from the base type.
		conversion = output_type
		multiplier = UnitMultipliers[conversion]
		result = value * multiplier
		return result
		# isinstance(x, dict)
		# result = "Error, No funcs"
	return result


# - - - - TEMPERATURE - - - - #
Temperature = {
	"celsius_to_fahrenheit": lambda x: x * 1.8 + 32,
	"celsius_to_kelvins": lambda x: x + 273.15,
	"fahrenheit_to_celsius": lambda x: (x - 32) / 1.8,
	"fahrenheit_to_kelvins": lambda x: (x + 459.67) * (5/9),
	"kelvins_to_celsius": lambda x: x - 273.15,
	"kelvins_to_fahrenheit": lambda x: (x * 1.8) - 459.67,
}

# - - OTHER CONVERSION UNITS - - #
ConversionMultipliers = {
	"length": {
		"base": "metres",
		"inches": 39.3701,
		"feet": 3.28084,
		"yards": 1.09361,
		"miles": 0.000621371,
		"millimetres": 1000,
		"centimetres": 100,
		"metres": 1,
		"kilometres": 0.001,
	},
	"mass": {
		"base": "grams",
		"ounces": 0.035274,
		"pounds": 0.00220462,
		"us_tons": 0.00000110231,
		"imperial_tons": 0.0000009842065,#2761106,
		"micrograms": 1e-6,
		"milligrams": 1000,
		"grams": 1,
		"kilograms": 0.001,
		"metric_tons": 1e+6,
	},
	"volume": {
		"base": "liters",
		"fluid_ounces": 33.814,
		"cups": 4.22675,
		"pints": 2.11338,
		"quarts": 1.05669,
		"gallons": 0.264172,
		"milliliters": 1000,
		"liters": 1,
	},
	"time": {
		"base": "seconds",
		"nanoseconds": 1000000000,
		"microseconds": 1000000,
		"milliseconds": 1000,
		"seconds": 1,
		"minutes": 1/60,
		"hours": 1/3600,
		"days": 1/86400,
		"weeks": 1/604800,
		"months": 1/2629746,
		"years": 1/31536000,
		# "decades": 0,
		# "centuries": 0,
		# "millennium": 0,
	},
}