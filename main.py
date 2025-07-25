# import math
# import 

from textual.app import App, ComposeResult
from textual.screen import Screen
# from textual.containers import Container
from textual.containers import Horizontal, HorizontalGroup, HorizontalScroll
from textual.containers import Vertical, VerticalGroup, VerticalScroll
# from textual.widget import Widget  # Used for custom container with tcss 
from textual.widgets import Header, Footer, Static
from textual.widgets import Label, Button, Input, OptionList, ListView, ListItem
from textual.widgets.option_list import Option
from textual.widgets import Collapsible, ContentSwitcher

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
		"""  """
		# if event.button.id == "temp-button":
		# 	self.app.push_screen("unit_converter")
		button = event.button
		if "conversion-option" in button.classes:
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
					with VerticalGroup(id="unit-column"):
						# yield Label("Temperature", id="temperature", classes="group-title")
						# yield Button("Temperature", id="temp-button", classes="group-button", disabled=True)
						yield Static("Temperature", classes="group-title")
						with VerticalGroup(classes="item-container"):
							yield Button("Conversions", classes="conversion-option")
							# yield Button("Option 2")
						# yield OptionList(
						# 	Option("Conversions", id="a"),
						# 	Option("B", id="b"),
						# 	id="unit-items", classes="item-container", compact=True
						# 	# ,highlighted=None
    					# )
						# with ListView():
						# 	with ListItem(): yield Label("ASD", id="ASD")
						# 	yield ListItem(Label("Aad"))
						# )
				
				with Vertical():
					with VerticalGroup(id="length-column"):
						yield Button("Length(WIP)")
					with VerticalGroup(id="weight-column"):
						yield Button("Weight(WIP)")
					with VerticalGroup(id="volume-column"):
						yield Button("Volume(WIP)")

				with Vertical():
					with VerticalGroup(id="text-column"):
						yield Button("Text stuff(WIP)")
					with VerticalGroup(id="color-column"):
						yield Button("Colors(WIP)")

				with Vertical():
					with VerticalGroup(id="timezone-column"):
						yield Button("Timezones(WIP)")
					with VerticalGroup(id="currency-column"):
						yield Button("Currencies(WIP)")



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