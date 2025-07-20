from textual import log
from textual.screen import Screen
from textual.containers import Horizontal, HorizontalGroup
from textual.containers import Vertical, VerticalGroup, VerticalScroll
from textual.widgets import Header, Footer, Static
from textual.widgets import Button, Input, Label, Select
# from textual.widgets import 
# from main import ToolMenu  # Causes cicular import error
import conversions as Convert


class Dropdown(Select):
	allow_blank = True
	# compact = True  # Use compact style

	def on_mount(self):
		# self.set_options(self.temperature_options)
		self.set_options([("asd","s")])
		# self.prompt = "None"
		# self.compact = True



class Converter(VerticalGroup):
	"""  """
	conversion_types = [
		("Temperature", "temperature"),
		("Length(WIP)", "length"),
		("Volumd(WIP)", "volume"),
	]
	conversion_options = {
		"temperature": [
			("Celsius", "celsius"),
			("Fahrenheit", "fahrenheit"),
			("Kelvins", "kelvins"),
		],
		"length": [],
		"weight": [],
		"volume": [],
	}
	conversion_functions = {
		"temperature": {
			"celsius_kelvin": Convert.celsius_to_kelvins
		}
	}
 
	selected_type = ""
	input_tpye = ""
	output_type = ""

	# def get_convert_function() -> None:
	# 	"""  """

	def convert_input(self) -> None:
		"""  """
		input_value = self.query_one("#value-input").value
		if input_value != "":  # Do not allow empty submission.
			input_value = float(input_value)
			# ouput_value = self.conversion_functions[self.selected_type]
			output_value = self.conversion_functions["temperature"]["celsius_kelvin"](input_value)
			# self.query_one("#value-output").update(input_value)
			self.query_one("#value-output").update(str(output_value))

	def on_input_submitted(self, event: Input.Submitted) -> None:
		self.convert_input()

	def on_button_pressed(self, event: Button.Pressed) -> None:
		if event.button.id == "convert-button":
			self.convert_input()

	def on_select_changed(self, event: Select.Changed) -> None:
		if event.select.id == "conversion-type-selector":
			self.selected_type = event.value
			select_input = self.query_one("#select-input")
			select_output = self.query_one("#select-output")
			select_input.set_options( self.conversion_options[self.selected_type] )
			select_output.set_options( self.conversion_options[self.selected_type] )
   
		if event.select.id == "select-input":
			self.input_type = event.value

		if event.select.id == "select-output":
			self.output_type = event.value

	def compose(self):
		with HorizontalGroup(id="conversion-tool-bar"):
			yield Label("Select conversion type:")
			yield Select(self.conversion_types, id="conversion-type-selector", compact=True)
			# yield Input(id="conversion-type-search")
			# yield Button("Save Conversion")
			# yield Button("Clear")
		with HorizontalGroup():
			# yield Select(self.temperature_options, id="select_input")
			yield Dropdown([], prompt="Input", id="select-input", compact=True)
			yield Button("swap", id="swap-button")
			yield Select([], prompt="Output", id="select-output", compact=True)
		with HorizontalGroup():
			yield Input(type="number", id="value-input")
			yield Button("-> Convert ->", id="convert-button")
			yield Label("asd", id="value-output")
			
		# yield 

	def on_mount(self):
		"""  """
		# self.border_title = "Temperature"
		# for i in self.query("Input"): i.border_title = "Temperature"
		# self.query_one("#value_input").border_subtitle = "Option"
		# self.query_one("#select_input").allow_blank = True



class UnitConverterScreen(Screen):

	# CSS_PATH = ""
	BINDINGS = [
		("a", "add_converter", "Add"),
	]

	def action_add_converter(self) -> None:
		new_converter = Converter()
		self.query_one("#converter-list").mount(new_converter)
		# new_converter.scroll_visible()


	def compose(self):
		yield Header()
		yield Footer()
		with Vertical():
			yield Converter()
		# with VerticalScroll(id="converter-list"):
