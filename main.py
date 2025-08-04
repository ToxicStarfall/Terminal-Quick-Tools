# import math

from textual.app import App, ComposeResult
from textual.screen import Screen
# from textual.containers import Container
from textual.containers import Horizontal, HorizontalGroup, HorizontalScroll
from textual.containers import Vertical, VerticalGroup, VerticalScroll
# from textual.widget import Widget  # Used for custom container with tcss 
from textual.widgets import Header, Footer, Static
from textual.widgets import Label, Button, Input#, ListView, ListItem
#from textual.widgets import ContentSwitcher

import unit_converter
from unit_converter import UnitConverterScreen
from text_tools import TextToolsScreen
from color_tools import ColorToolsScreen

from art import text2art



# class ToolMenu(VerticalScroll):
# 	""" A sidebar popup with a list of tools """
# 	def compose(self) -> ComposeResult:
# 		# with Collapsible():
# 			yield Button("Binary/Text", id="a")
# 			yield Button("B", id="b")
# 			yield Button("Graph", id="c")



class HomeScreen(Screen):
	# BINDINGS = [
	# 	("q", "focus_left", "Focus Left"),
	# 	("e", "focus_right", "Focus Right"),
	# ]

	def on_button_pressed(self, event: Button.Pressed) -> None:
		button = event.button
		if "conversion-option" in button.classes:
			unit_converter.conversion_type = button.id
			self.app.push_screen("unit_converter")
		if "text-tool-option" in button.classes:
			self.app.push_screen("text_tools")
		if "color-tool-option" in button.classes:
			self.app.push_screen("color_tools")
   
	# def on_enter(self, event: Events.Enter) -> None:
	# 	if evnet.node is Button:
	# 		"""  """

	def compose(self) -> ComposeResult:
		yield Footer()

		with VerticalScroll(id="home-page"):
			yield Static(text2art("Quick Tools", space=1), id="title")

			with HorizontalGroup(id="tool-display"):
				with Vertical():
					with VerticalGroup(id="unit-conversion-column", classes="group-container"):
						yield Static("Unit Conversions", classes="group-title")
						with VerticalGroup(classes="group-tool-list"):
							yield Button("Temperature", id="temperature", classes="conversion-option")
							yield Button("Length", id="length", classes="conversion-option")
							yield Button("Weight & Mass", id="mass", classes="conversion-option")
							yield Button("Volume", id="volume", classes="conversion-option")
							yield Button("Time", id="time", classes="conversion-option")
						# with ListView():
						# 	with ListItem(): yield Label("ASD", id="ASD")
						# 	yield ListItem(Label("Aad"))
						# )
				
				with Vertical():
					with VerticalGroup(id="color-column", classes="group-container"):
						yield Static("Colors(WIP)", classes="group-title")
						with VerticalGroup(classes="group-tool-list"):
							yield Button("RGB, HSV, Hex", classes="color-tool-option")
							yield Button("Color Codes", classes="color-tool-option")
							yield Button("Color Tool 2", classes="color-tool-option")

				with Vertical():
					with VerticalGroup(id="text-column", classes="group-container"):
						yield Static("Text Tools(WIP)", classes="group-title")
						with VerticalGroup(classes="group-tool-list"):
							yield Button("Binary Converter", classes="text-tool-option")
							yield Button("Find Text", classes="text-tool-option")
							yield Button("Replace Text", classes="text-tool-option")
							# yield Button("Regex")
				
				with Vertical():
					with VerticalGroup(id="miscellaneous-columnm", classes="group-container"):
						yield Static("Miscellaneous(WIP)", classes="group-title")
						with VerticalGroup(classes="group-tool-list"):
							yield Button("Timezones")
							yield Button("Currencies tool")

					# with VerticalGroup(id="currency-column", classes="group-container"):
					# 	yield Static("Currencies(WIP)", classes="group-title")
					# 	with VerticalGroup(classes="group-tool-list"):



class QuickTools(App):
	""" a """
	
	CSS_PATH = "main.tcss"
	BINDINGS = [
		("a", "open_home_screen", "Home"),
	]
	# ENABLE_COMMAND_PALETTE = False
	SCREENS = {
		"unit_converter": UnitConverterScreen,
		"text_tools": TextToolsScreen,
		"color_tools": ColorToolsScreen,
		"home_screen": HomeScreen,
	}
	
	# def compose(self) -> ComposeResult:
		# yield Header()
		# yield HomeScreen()
		# with Horizontal():
		# 	yield ToolMenu()


	def action_open_home_screen(self) -> None:
		self.push_screen("home_screen")
		# self.pop_screen()
				
	def on_button_pressed(self, event: Button.Pressed) -> None:
		"""  """
		# toolpage = self.query_one("ToolPage")
		# if event.button.id == "a":
		# 	toolpage.current = "BinaryTool"
		# else:
		# 	toolpage.current = event.button.id

	def on_mount(self):
		# self.install_screen(UnitConverterScreen(), name="unit_converter")
		self.push_screen("home_screen")
		# self.push_screen("unit_converter")



if __name__ == "__main__":
	app = QuickTools()
	app.run()

""" 
cd Downloads/Terminal-graphing-app
pyinstaller --add-data conversions.py:. --add-data unit_converter.py:. --add-data main.tcss:. --add-data unit_converter.tcss:. main.py
"""