from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, HorizontalGroup, HorizontalScroll
from textual.containers import Vertical, VerticalGroup, VerticalScroll
# from textual.widget import Widget  # Used for custom container with tcss 
from textual.widgets import Header, Footer, Static
from textual.widgets import Label, Button, Input, TextArea, Select

import conversions as Convert


class ColorDisplay(Static):
	color = ""

	def update():
		pass


class ColorToolsScreen(Screen):
	# CSS_PATH = "unit_converter.tcss"
	BINDINGS = []


	def on_button_pressed(self, event: Button.Pressed):
		pass

	def compose(self):
		yield Header()
		yield Footer()
		with VerticalScroll():

			with HorizontalGroup(id="tool-select-bar"):
				yield Select([], prompt="Select a tool", id="color-tool-selector")

			with HorizontalGroup():
				with Vertical():
					yield Static(id="color-display-1")
					yield Input()
					yield Input()
					yield Input()
				with Vertical():
					yield Button("Convert")
					yield Button("Swap")
					
				with Vertical():
					yield Static(id="color-display-2")
					yield Input()
					yield Input()
					yield Input()
			# with Vertical(id=""):
				# with HorizontalGroup():
					# yield Select([], prompt="", id="", compact=True)


