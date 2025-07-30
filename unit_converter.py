# from textual import log
from textual.screen import Screen
from textual.containers import Horizontal, HorizontalGroup, Grid
from textual.containers import Vertical, VerticalGroup, VerticalScroll
from textual.widgets import Header, Footer, Static
from textual.widgets import Button, Input, Label, Select
# from textual.widgets import 
# from main import ToolMenu  # Causes cicular import error
import conversions as Convert


# class Dropdown(Select):
	# allow_blank = True
	# compact = True  # Use compact style

	# def on_mount(self):
		# self.set_options(self.temperature_options)
		# self.set_options([("asd","s")])
		# self.prompt = "None"
		# self.compact = True


conversion_type = ""
class Converter(VerticalGroup):
	# Options for the conversion type selector.
	conversion_types = [
		("Temperature", "temperature"),
		("Length", "length"),
		("Weight & Mass", "weight"),
		("Volume", "volume"),
		("Time", "time"),
	]
	# Unit options for the selected conversion type.
	conversion_options = {
		"temperature": [
			("Celsius", "celsius"),
			("Fahrenheit", "fahrenheit"),
			("Kelvins", "kelvins"),
		],
		"length": [
			("Millimetres", "millimetres"),
			("Centimetres", "centimetres"),
			("Metres", "metres"),
			("Kilometres", "kilometres"),
			("Inches", "inches"),
			("Feet", "feet"),
			("Yards", "yards"),
			("Miles", "miles"),
    	],
		"mass": [
			("Ounces", "ounces"),
			("Pounds", "pounds"),
			("US Tons", "us_tons"),
			("Imperial Tons", "imperial_tons"),
			("Micrograms", "micrograms"),
			("Milligrams", "milligrams"),
			("Grams", "grams"),
			("Kilograms", "kilograms"),
			("Metric Tons", "metric_tons"),
    	],
		"volume": [
			("Fluid Ounces", "fluid_ounces"),
			("Cups", "cups"),
			("Pints", "pints"),
			("Quarts", "quarts"),
			("Gallons", "gallons"),
			("Millileters", "millileters"),
			("Liters", "liters"),
		],
		"time": [
			("Nanoseconds", "nanoseconds"),
			("Microseconds", "microseconds"),
			("Milliseconds", "milliseconds"),
			("Seconds", "seconds"),
			("Minutes", "minutes"),
			("Hours", "hours"),
			("Days", "days"),
			("Weeks", "weeks"),
			("Months", "months"),
			("Years", "years"),
			# ("Decades", "secades"),
			# ("Centuries", "centuries"),
			# ("Millennium", "millennium"),
		],
	}
	conversion_descriptions = {}
 
	# conversion_type = ""

	SelectInput = None
	SelectOutput = None
	input_type = ""
	output_type = ""

	ValueInput = None
	ValueOutput = None


	# Updates the selected conversion type.
	def set_conversion_type(self):
		self.query_one("#conversion-type-selector").value = conversion_type
		self.SelectInput.set_options( self.conversion_options[conversion_type] )
		self.SelectOutput.set_options( self.conversion_options[conversion_type] )


	# Swaps selected input and output types.
	def swap_types(self) -> None:
		# Changing Select()'s value automatically updates selection.
		a = self.SelectInput.value
		b = self.SelectOutput.value
		self.SelectInput.value = b
		self.SelectOutput.value = a

	
	def convert_input(self) -> None:
		"""  """
		warning_label = self.query_one("#warning-label")
		# Do not allow empty input and output conversion types.
		if self.input_type != "":
			if self.output_type != "":
				input_value = self.ValueInput.value
				
				# Do not allow empty input submission.
				if input_value != "":  
					input_value = float(input_value)  # Convert to float for math ops
					# On conversion, if input & output are the same, return input as output.
					if self.input_type == self.output_type:
						output_value = Convert.same(input_value)
						self.ValueOutput.update(str(output_value))
    				# Otherwise, get matching convert function
					else:
						output_value = Convert.units(
							conversion_type,
							self.input_type,
							self.output_type,
							input_value
						)
						self.ValueOutput.update(str(output_value))
					warning_label.update("Operaton success.")

				else: warning_label.update("*Please insert a value.")
			else: warning_label.update("*Please select a output type.")
		else: warning_label.update("*Please select a input type.")


	def on_input_submitted(self, event: Input.Submitted) -> None:
		self.convert_input()

	def on_button_pressed(self, event: Button.Pressed) -> None:
		if event.button.id == "swap-button":
			self.swap_types()
		if event.button.id == "convert-button":
			self.convert_input()

	# Gets values of selectors and stores them.
	def on_select_changed(self, event: Select.Changed) -> None:
		if event.select.id == "conversion-type-selector":
			global conversion_type # Identifies it as global in order to assign value.
			conversion_type = event.value
			self.set_conversion_type()

		# Changes the unit type for input and output selectors.
		else:
			# If no option is selected, set the value to "" for type safety.
			if event.value == Select.BLANK:
				event.value = ""
			# Forward the value, empty or not.
			if event.select.id == "select-input":
				self.input_type = str(event.value)
			if event.select.id == "select-output":
				self.output_type = str(event.value)
			# Clears warning label when a different input or output type is selected
			if event.value != "":
				self.query_one("#warning-label").update("")


	def compose(self):
		with HorizontalGroup(id="conversion-tool-bar"):
			yield Label("Select conversion:")
			yield Select(self.conversion_types, id="conversion-type-selector", compact=True)
			yield HorizontalGroup(
				Label("", id="warning-label")
			)
			# yield Input(id="conversion-type-search")
			# yield Button("Save Conversion")
			# yield Button("Clear")
		with Grid():
			yield Static("text", id="explanation")

			yield Select([], prompt="Input type", id="select-input", compact=True)
			yield Button("swap", id="swap-button")
			yield Select([], prompt="Output type", id="select-output", compact=True)
	
			yield Input(type="number", id="value-input", placeholder="Insert value")
			yield Button("-> Convert ->", id="convert-button")
			yield Label("Output value", id="value-output")


	def on_mount(self):
		""" Initialize variables for DOM access """
		self.SelectInput = self.query_one("#select-input")
		self.SelectOutput = self.query_one("#select-output")
		self.ValueInput = self.query_one("#value-input")
		self.ValueOutput = self.query_one("#value-output")
		self.set_conversion_type()




class UnitConverterScreen(Screen):

	CSS_PATH = "unit_converter.tcss"
	BINDINGS = [
		# ("a", "add_converter", "Add"),
		# ("c", "clear", "Clear"),
	]

	def action_add_converter(self) -> None:
		new_converter = Converter()
		self.query_one("#converter-list").mount(new_converter)
		# new_converter.scroll_visible()


	def compose(self):
		yield Header()
		yield Footer()
		with Vertical():
			yield Converter(id="converter")
		# with VerticalScroll(id="converter-list"):
