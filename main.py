# import math
# import 

from textual.app import App, ComposeResult
from textual.screen import Screen
# from textual.containers import Container
from textual.containers import Horizontal, HorizontalGroup, HorizontalScroll
from textual.containers import Vertical, VerticalGroup, VerticalScroll
# from textual.widget import Widget  # Used for custom container with tcss 
from textual.widgets import Header, Footer, Static
from textual.widgets import Label, Button, Input, ListView, ListItem
from textual.widgets import ContentSwitcher

import unit_converter
from unit_converter import UnitConverterScreen

from art import text2art



class ToolMenu(VerticalScroll):
	""" A sidebar popup with a list of tools """
	def compose(self) -> ComposeResult:
		# with Collapsible():
			yield Button("Binary/Text", id="a")
			yield Button("B", id="b")
			yield Button("Graph", id="c")

class ToolPage(ContentSwitcher):
	def compose(self) -> ComposeResult:
		yield Button("BASDOP", id="b")



class HomeScreen(Screen): #Horizontal):
	"""  """

	def on_button_pressed(self, event: Button.Pressed) -> None:
		button = event.button
		if "conversion-option" in button.classes:
			unit_converter.conversion_type = button.id
			self.app.push_screen("unit_converter")
   
	# def on_enter(self, event: Events.Enter) -> None:
	# 	"""  """
	# 	if evnet.node is Button:
	# 		"""  """

	def compose(self) -> ComposeResult:
		# yield Header()
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
							yield Button("Weight(WIP)", classes="conversion-option")
							yield Button("Volume(WIP)", classes="conversion-option")
						# with ListView():
						# 	with ListItem(): yield Label("ASD", id="ASD")
						# 	yield ListItem(Label("Aad"))
						# )
				
				with Vertical():
					with VerticalGroup(id="color-column", classes="group-container"):
						yield Static("Colors(WIP)", classes="group-title")
						with VerticalGroup(classes="group-tool-list"):
							yield Button("Color Tool 1")
							yield Button("Color Tool 2")

				with Vertical():
				# yield Vertical()
					with VerticalGroup(id="text-column", classes="group-container"):
						yield Static("Text Tools(WIP)", classes="group-title")
						with VerticalGroup(classes="group-tool-list"):
							yield Button("Text stuff")
							yield Button("Find Text")
							yield Button("Replace Text")
							# yield Button("Regex")
				with Vertical():
				# yield Vertical()
					with VerticalGroup(id="timezone-columnm", classes="group-container"):
						yield Static("Timezones(WIP)", classes="group-title")
						with VerticalGroup(classes="group-tool-list"):
							yield Button("Timezones")

					with VerticalGroup(id="currency-column", classes="group-container"):
						yield Static("Currencies(WIP)", classes="group-title")
						with VerticalGroup(classes="group-tool-list"):
							yield Button("Currencies tool")



class QuickTools(App):
	""" a """
	
	CSS_PATH = "main.tcss"
	BINDINGS = [
		("a", "open_menu", "Home"),
	]
	# ENABLE_COMMAND_PALETTE = False
	SCREENS = {
		"unit_converter": UnitConverterScreen,
		"home_screen": HomeScreen,
	}
	
	# def compose(self) -> ComposeResult:
		# yield Header()
		# yield HomeScreen()
		# with Horizontal():
		# 	yield ToolMenu()
			# yield ToolPage()


	def action_open_menu(self) -> None:
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
		"""  """
		# self.query_one("ToolPage").current = "b"
		# self.install_screen(UnitConverterScreen(), name="unit_converter")
		self.push_screen("home_screen")
		# self.push_screen("unit_converter")



if __name__ == "__main__":
	app = QuickTools()
	app.run()
#pyinstaller --add-data conversions.py:. --add-data unit_converter.py:. --add-data main.tcss:. --add-data unit_converter.tcss:. main.py