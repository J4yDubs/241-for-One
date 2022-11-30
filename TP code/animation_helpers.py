from matrix_utils import *
from matrix_GE import *
from matrix_SOLE import *
from cmu_112_graphics import *
from animation_classes import *

# Taken from Piazza by instructor Joe Ritze (to get screen dimensions to get fullscreen)
def fitToScreen(app):
	app.width = app._theRoot.winfo_screenwidth()
	app.height = app._theRoot.winfo_screenheight()
	app.setSize(app.width, app.height)
	app.updateTitle()

# *****************************************************************
# ********************* APPSTARTED FUNCTIONS **********************
# *****************************************************************
# def screenIni(app):
#     app.screens = [ ['matCal',
#      ['matAdd', 'matAddResult'],
#      ['matMul', 'matMulResult', 'matMulSteps'], 
#      ['matTpose', 'matTposeResult']], 
#     ['GE', 'GEResult', 'GESteps'], 
#     ['SOLE', 'SOLEResult', 'SOLESteps'], 
#     ['LU'], ['inverse'], ['4FS'], ['det'], ['GS'],
#     ['home'] ]
#     app.screen = app.screens[-1][0]

# *****************************************************************
# ********************* KEYPRESSED FUNCTIONS **********************
# *****************************************************************

# scroll keypressed
def scrollKeyPressed(app, event):
    if event.key in app.scrollKeys:
            if app.scrollY > 0:
                if app.scrollKeys[event.key] < 0:
                    app.scrollY += app.scrollKeys[event.key]
            else: app.scrollY += app.scrollKeys[event.key]

# *****************************************************************
# ********************* MOUSEMOVED FUNCTIONS **********************
# *****************************************************************

# *****************************************************************
# ********************* MOUSEPRESSED FUNCTIONS ********************
# *****************************************************************

# *****************************************************************
# ******************** REDRAW BUTTON FUNCTIONS ********************
# *****************************************************************

# *****************************************************************
# ******************** REDRAW SCREEN FUNCTIONS ********************
# *****************************************************************
