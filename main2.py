# from textual import log
from textual.app import App, ComposeResult
from textual.containers import Horizontal, HorizontalGroup, HorizontalScroll
from textual.containers import Vertical, VerticalGroup, VerticalScroll
from textual.widget import Widget  # Used for custom container with tcss 
from textual.widgets import Header, Footer, Static
from textual.widgets import Button, Input

from textual_plotext import PlotextPlot


# def get_function(ox=0, oy=0, scale=1) -> list:
# 	a = []
#     # for i in range(0 - scale*100, 0 + scale*100):
#     for i in range(0,):
#     	a.insert(-1, i / 100)
# 	return a


class GraphInputs(Input):
	""" Graph Input widget """
	
	def compose(self) -> ComposeResult:
		yield Input()


class GraphView(Static):
	"""  """
	def compose(self) -> ComposeResult:
		yield PlotextPlot()

	def on_mount(self) -> None:
		plt = self.query_one(PlotextPlot).plt
		# y = plt.sin() # sinusoidal test signal
		
		y = 100
		x = 200
		# xmin = 0
		# xmax = 20
  
		a = y/x
  
		yl = []
		# for i in range(0, x):
		for i in range(0-100, 0+100):
			# yl.insert(-1, a * i)
			yl.insert(-1, i/100)
		# yl = get_function()
   
		# plt.scatter(y)
		# plt.plot([1, 2, 4])
		plt.plot(yl)
		plt.title("Scatter Plot") # to apply a title


class GraphControls(Horizontal):
	"""  """
	def compose(self) -> ComposeResult:
		# yield Button("Zoom Focus", id="zoom_focus")
		# yield Button("Focus", id="pan_focus")
		# yield Input(id="input_focus_point")
		yield Button("Pan Left", id="pan_left")
		yield Button("Pan Up", id="pan_up")
		yield Button("Pan Down", id="pan_down")
		yield Button("Pan Right", id="pan_right")


class GraphingApp(App):
	""" a """
	
	CSS_PATH = "main2.tcss"
	BINDINGS = [
		# ("d", "toggle_dark", "Toggle dark mode"),
	]
	
	def compose(self) -> ComposeResult:
		yield Header()
		with Horizontal():
			# with VerticalGroup():
			# 	yield Input()
			# 	yield Input()
			with VerticalScroll():
				yield GraphView()
				yield GraphControls()


if __name__ == "__main__":
	app = GraphingApp()
	app.run()