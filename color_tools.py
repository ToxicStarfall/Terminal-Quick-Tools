import re

from textual.color import Color
from textual.screen import Screen
# from textual.containers import *
from textual.containers import Horizontal, HorizontalGroup, HorizontalScroll, Grid
from textual.containers import Vertical, VerticalGroup, VerticalScroll
from textual.widgets import Header, Footer, Static
from textual.widgets import Label, Button, Input, TextArea, Select

import conversions as Convert



# Static container which displays selected color (small)
class ColorPatch(Static):
	pass

# Static container which displays selected color (large)
class ColorDisplay(Static):
	color = "ffffff"

	def set_color(self, hex: str):
		self.styles.background = hex

	def update_color():
		pass

#
class HexGroup(Horizontal):
	def set_color(self, hex):
		self.query_one(".hex-input").value = hex
	
	def compose(self):
		yield Label("Hex:")
		yield Input(classes="hex-input", compact=True, restrict=r"^#?([0-9a-fA-F]{0,6})$")

#
class RGBGroup(Horizontal):
	color = None
	r = g = b = None

	def validate(self):
		valid = True
		for Input in self.query("Input"):
			if Input.value == "":
				Input.add_class("error")
				valid = False
		return valid

	def set_color(self, hex):
		self.color = Color.parse(hex)
		self.update_color()
	
	def update_color(self):
		self.r.value = str(self.color.r)
		self.g.value = str(self.color.g)
		self.b.value = str(self.color.b)
	
	def get_color(self):
		return Color.parse(f"rgb({self.r.value},{self.g.value},{self.b.value})")

	def compose(self):
		yield Label("R:")
		yield Input(type="number", classes="red-input", compact=True, restrict=r".{0,4}")
		yield Label("G:")
		yield Input(type="number", classes="green-input", compact=True, restrict=r".{0,4}")
		yield Label("B:")
		yield Input(type="number", classes="blue-input", compact=True, restrict=r".{0,4}")

	# Initialize rgb Inputs
	def on_mount(self):
		self.r = self.query_one(".red-input")
		self.g = self.query_one(".green-input")
		self.b = self.query_one(".blue-input")


#
class HSVGroup(Horizontal):
	color = None
	h = s = v = None

	def validate(self):
		valid = True
		for Input in self.query("Input"):
			if Input.value == "":
				Input.add_class("error")
				valid = False
			else: Input.remove_class("error")
		return valid
	
	def set_color(self, hex):
		self.color = Color.parse(hex)
		self.update_color()
	
	def update_color(self):
		self.h.value = str(self.color.hsv.h)
		self.s.value = str(self.color.hsv.s)
		self.v.value = str(self.color.hsv.v)
	
	def get_color(self):
		return Color.from_hsv(float(self.h.value), float(self.s.value), float(self.v.value))

	def compose(self):
		yield Label("H:")
		yield Input(type="number", classes="hue-input", compact=True, restrict=r".{0,4}")
		yield Label("S:")
		yield Input(type="number", classes="saturation-input", compact=True, restrict=r".{0,4}")
		yield Label("V:")
		yield Input(type="number", classes="value-input", compact=True, restrict=r".{0,4}")

	# Initialize hsv Inputs
	def on_mount(self):
		self.h = self.query_one(".hue-input")#.value = str(newcolor.h)
		self.s = self.query_one(".saturation-input")#.value = str(newcolor.s)
		self.v = self.query_one(".value-input")#.value = str(newcolor.v)


#
class ColorCodeGroup(VerticalGroup):
	def set_color(self, hex):
		self.query_one("HexGroup").set_color(hex)
		self.query_one("RGBGroup").set_color(hex)
		self.query_one("HSVGroup").set_color(hex)
	
	# def validate(self):
	# 	pass

	def compose(self):
		yield HexGroup()
		yield RGBGroup()
		yield HSVGroup()


#
class ColorDisplayTools(HorizontalGroup):
	def compose(self):
		# with Horizontal():
			# yield Button("Clear")
			# yield Button("Lock")
			# yield Button("Edit")
		with HorizontalGroup():
			# yield Button("<--")
			# yield Button("A")
			# yield Label("Index")
			# yield Button("-->")


#
class ColorDisplayGroup(Vertical):
	ColorDisplay = None
	ColorCodeGroup = None

	def apply_color(self, hex):
		self.ColorDisplay.set_color(hex)
		self.ColorCodeGroup.set_color(hex)

	def on_input_submitted(self, event: Input.Submitted):
		Input = event.input
		if isinstance(Input.parent, HexGroup):
			# Add "#" if missing
			if not re.match(r"#", Input.value): Input.value = "#" + Input.value
			# Stop a invalid hex (incorrect length)
			if not re.fullmatch(r"^.{4,5}|.{7}$", Input.value): # +1 for "#"
				# Input.error()
				self.app.bell() # Error sound
			else:
				self.apply_color(Input.value)
		else:
			# Valid if rgb/hsv inputs are filled
			if Input.parent.validate():
				if isinstance(Input.parent, RGBGroup):
					self.apply_color( Input.parent.get_color().hex6 )
				if isinstance(Input.parent, HSVGroup):
					self.apply_color( Input.parent.get_color().hex6 )
			
			else: # Play error sound
				self.app.bell()

	def compose(self):
		yield ColorDisplay()
		yield ColorCodeGroup()
		yield ColorDisplayTools()

	def on_mount(self):
		self.ColorDisplay = self.query_one("ColorDisplay")
		self.ColorCodeGroup = self.query_one("ColorCodeGroup")


#
class ColorTools(HorizontalScroll):
	BINDINGS = [
		("a", "add_color_display", "Add Color Tool"),
		("alt+left", "focus_left", "Focus Left"),
		("alt+right", "focus_right", "Focus Right"),
	]

	focused_tool_idx = 0

	def action_focus_left(self):
		siblings = self.query("ColorDisplayGroup")
		self.focused_tool_idx -= 1
		if self.focused_tool_idx == -1:
			self.focused_tool_idx = len(siblings) - 1
		self.screen.set_focus( siblings[self.focused_tool_idx].query_one("Input") )

	def action_focus_right(self):
		siblings = self.query("ColorDisplayGroup")
		self.focused_tool_idx += 1
		if self.focused_tool_idx == len(siblings):
			self.focused_tool_idx = 0
		self.screen.set_focus( siblings[self.focused_tool_idx].query_one("Input") )
		
	def action_add_color_display(self):
		a = ColorDisplayGroup()
		self.query_one("ColorTools").mount(a)
		a.scroll_visible()


	def compose(self):
			yield ColorDisplayGroup()
			yield ColorDisplayGroup()
			yield ColorDisplayGroup()

			# with Vertical():
			# 	yield Button("Convert")
			# 	yield Button("Swap")
				



class ColorToolsScreen(Screen):
	CSS_PATH = "color_tools.tcss"
	BINDINGS = [
		# ("a", "add_color_display", "Add Color Tool")
	]

	def compose(self):
		yield Header()
		yield Footer()
		with VerticalScroll():

			with HorizontalGroup(id="tool-select-bar"):
				yield Select([], prompt="Select a tool", id="color-tool-selector")
			
			yield ColorTools(id="color-tools-content-container")
			# with Vertical(id=""):
				# with HorizontalGroup():
					# yield Select([], prompt="", id="", compact=True)

	def on_mount(self):
		self.screen.set_focus( self.query_one("#color-tools-content-container") )

