# import math
# import 

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Container, Center
from textual.containers import Horizontal, HorizontalGroup, HorizontalScroll
from textual.containers import Vertical, VerticalGroup, VerticalScroll
# from textual.widget import Widget  # Used for custom container with tcss 
from textual.widgets import Header, Footer, Static
from textual.widgets import Label
from textual.widgets import Button, Input
from textual.widgets import Collapsible, ContentSwitcher

from unit_converter import UnitConverterScreen


class ToolMenu(VerticalScroll):
	""" A sidebar popup with a list of tools """
	
	def compose(self) -> ComposeResult:
		# with Collapsible():
			yield Button("Binary/Text", id="a")
			yield Button("B", id="b")
			yield Button("Graph", id="c")


class ToolPage(ContentSwitcher):
	"""  """
	def compose(self) -> ComposeResult:
		yield Button("BASDOP", id="b")


class HomeScreen(Screen):
	"""  """
	def compose(self) -> ComposeResult:
		with VerticalScroll(id="HomePage"):
			with Center():
				yield Label("I AM A LABLE", id="title")
			with HorizontalGroup(id="tool-display"):
				with VerticalGroup(id="unit-column"):
					yield Button("Temperature")
					yield Button("Weight")
				with VerticalGroup(id="text-column"):
					yield Button("Text stuff(WIP)")
				with VerticalGroup(id="color-column"):
					yield Button("Color Tools(WIP)")
				with VerticalGroup(id="timezone-column"):
					yield Button("Timezones(WIP)")



class QuickTools(App):
	""" a """
	
	CSS_PATH = "main.tcss"
	BINDINGS = [
		("esc", "action_open_menu", "Home"),
	]
	# ENABLE_COMMAND_PALETTE = False
	SCREENS = {
		"unit_converter": UnitConverterScreen,
		"home_screen": HomeScreen
	}
	
	def compose(self) -> ComposeResult:
		yield Header()
		with Horizontal():
			yield ToolMenu()
			yield ToolPage()


	def action_open_menu(self) -> None:
		self.push_screen("home_screen")
				
	def on_button_pressed(self, event: Button.Pressed) -> None:
		"""  """
		# toolpage = self.query_one("ToolPage")
		# if event.button.id == "a":
		# 	toolpage.current = "BinaryTool"
		# else:
		# 	toolpage.current = event.button.id

	def on_mount(self):
		self.query_one("ToolPage").current = "b"
		# self.install_screen(UnitConverterScreen(), name="unit_converter")
		self.push_screen("unit_converter")
		# self.push_screen("home_screen")



if __name__ == "__main__":
	app = QuickTools()
	app.run()