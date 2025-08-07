from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, HorizontalGroup, HorizontalScroll
from textual.containers import Vertical, VerticalGroup, VerticalScroll
# from textual.widget import Widget  # Used for custom container with tcss 
from textual.widgets import Header, Footer, Static
from textual.widgets import Label, Button, Input, TextArea, Select

import conversions as Convert



class BinAsciiTools(Vertical):
	# conversion_options = [
	# 	("Binary to Decimal", "bin_to_dec"),
	# 	("Binary to Ascii", "bin_to_asc"),
	# 	("Binary to Hexidecimal","bin_to_hex"),
	# 	("Decimal to Binary", ""),
	# 	# ("Decimal to ", ""),
	# 	# ("Decimal to ", ""),
	# 	("Ascii to Binary", ""),
	# 	("Ascii to Decimal", ""),
	# 	("Ascii to Hexidecimal", ""),
	# 	("Hexidecimal to ","b"),
	# 	# ("Hexidecimal to ","b"),
	# 	# ("Hexidecimal to ","b"),
	# ]
	conversion_options = [
		("Binary", "bin"),
		("Decimal", "dec"),
		("Hex (hexidecimal)","hex"),
		("Ascii", "ascii"),
	]
	InputTextArea = None
	OutputTextArea = None
	input_text = ""

	def convert_text(self):
		pass

	def on_select_changed(self, event: Select.Changed):
		pass

	def on_button_pressed(self, event: Button.Pressed):
		if event.button.id == "bin-ascii-swap-button":
			a = self.InputTextArea.text
			b = self.OutputTextArea.text
			self.InputTextArea.text = b
			self.OutputTextArea.text = a
		elif event.button.id == "bin-ascii-convert-button":
			self.OutputTextArea.text = Convert.ascii_to_decimal(self.input_text)

	def on_text_area_changed(self, event: TextArea.Changed):
		if event.text_area.id == "input-text-area":
			self.input_text = self.InputTextArea.text
	

	def compose(self):
		with HorizontalGroup(classes="h-group"):
			yield Label("INPUT")
			# yield Select(self.conversion_options, prompt="Select conversion", id="bin-ascii-conversion-selector", compact=True)
			yield Select(self.conversion_options, prompt="Select conversion", id="bin-ascii-input-selector", compact=True)
			yield Label("to")
			yield Select(self.conversion_options, prompt="Select conversion", id="bin-ascii-output-selector", compact=True)
		
		yield TextArea(name="asdpo", id="input-text-area",
				show_line_numbers=True)
		with HorizontalGroup(classes="h-group"):
			yield Label("OUTPUT")
			yield Button("Convert", id="bin-ascii-convert-button")
			yield Button("Swap", id="bin-ascii-swap-button")
		yield TextArea(id="output-text-area", 
				show_line_numbers=True, read_only=True)

	def on_mount(self):
		# Initialize widget variables
		self.InputTextArea = self.query_one("#input-text-area")
		self.OutputTextArea = self.query_one("#output-text-area")


class FindReplaceTools(Vertical):
	def on_select_changed(self, event: Select.Changed):
		pass
	def compose(self):
		with VerticalScroll():
			yield TextArea()
		with HorizontalGroup():
			yield Input()
			yield Button("Find")
			yield Button("Replace")
			yield Input()
		yield Label()
	def on_mount(self):
		pass


class TextToolsScreen(Screen):
	CSS_PATH = "text_tools.tcss"
	BINDINGS = []

	tool_options = [
		("Binary <--> Ascii Converter", "bin-ascii-tool"),
		("Find Text", "find-replace-tool"),
		("Replace Text", "find-replace-tool"),
	]
	tool_mode = ""

	def on_button_pressed(self, event: Button.Pressed):
		pass

	def compose(self):
		yield Header()
		yield Footer()
		with VerticalScroll(id="text-tool-content-container"):
			with HorizontalGroup(id="tool-select-bar"):
				yield Select(self.tool_options, prompt="Select a tool", id="text-tool-selector", compact=True)

			yield BinAsciiTools(id="bin-ascii-tools")
		# 	with Vertical(id="bin-ascii-tools"):
		# 		with HorizontalGroup(classes="h-group"):
		# 			yield Label("INPUT")
		# 			yield Select([], prompt="Select conversion", id="bin-ascii-conversion-selector", compact=True)
		# 		yield TextArea(name="asdpo", id="input-text-area",
		# 				show_line_numbers=True)
		# 		with HorizontalGroup(classes="h-group"):
		# 			yield Label("OUTPUT")
		# 			yield Button("Convert")
		# 			yield Button("Swap")
		# 		yield TextArea(id="output-text-area", 
		# 				show_line_numbers=True, read_only=True)

			# yield FindReplaceTools(id="find-replace-tools")

