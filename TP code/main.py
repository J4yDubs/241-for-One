from matrix_utils import *
from matrix_GE import *
from matrix_SOLE import *

from cmu_112_graphics import *

# Taken from Piazza by instructor Joe Ritze (to get screen dimensions to get fullscreen)
def fitToScreen(app):
	app.width = app._theRoot.winfo_screenwidth()
	app.height = app._theRoot.winfo_screenheight()
	app.setSize(app.width, app.height)
	app.updateTitle()

def appStarted(app):
    fitToScreen(app)
    pass

def keyPressed(app, event):
    pass

def mousePressed(app, event):
    pass

def redrawAll(app, canvas):
    pass

def run241ForOne():
    runApp()

run241ForOne()