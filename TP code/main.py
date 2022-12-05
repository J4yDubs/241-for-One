from matrix_utils import *
from matrix_GE import *
from matrix_SOLE import *
from cmu_112_graphics import *
from animation_classes import *
from animation_helpers import *

def appStarted(app):
    fitToScreen(app)
    screensInit(app)

    # app.buttons indices:
    # 0: home, 1: calc, 2: add, 3: mult, 4: tpose
    app.buttons = [[],[],[],[],[],[],[]]
    backHomeButtonInit(app)
    backButtonInit(app)
    solveButtonInit(app)
    clearButtonInit(app)
    stepsButtonInit(app)

    # *** VALID KEYS ***
    app.numKeys = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-'}
    app.entryNavKeys = {'Up': -1, 'Down': +1, 'Left': -1, 'Right': +1}
    app.scrollKeys = {'Up': +10, 'Down': -10}

    # scrolling
    app.scrollY = 0

    # app.textBoxes indices:
    # 0: add, 1: mult, 2: tpose, 3: GE, 4: SOLE, 5: det, 6: dirGraph
    # innermost list stores dimension Text Boxes
    app.textBoxes = [[[]], [[],[]], [[]], [[]], [[]], [[]], [[]]]

    # Screen initializations
    homeScreenInit(app)
    calScreenInit(app)
    addScreenInit(app)
    mulScreenInit(app)
    tposeScreenInit(app)
    GEScreenInit(app)
    SOLEScreenInit(app)
    detScreenInit(app)

def keyPressed(app, event):
    if app.screen == 'matAdd':
        matAddKeyPressed(app, event)
    elif app.screen == 'matMul':
        matMulKeyPressed(app, event)
    elif app.screen == 'matTpose':
        matTposeKeyPressed(app, event)
    elif app.screen == 'GE':
        GEKeyPressed(app, event)
    elif app.screen == 'SOLE':
        SOLEKeyPressed(app, event)
        
    # scrolling for screens
    if app.screen == 'matMulSteps' or 'GESteps' or 'SOLESteps' or 'detSteps':   # extend to other steps screens
        scrollKeyPressed(app, event)

def mouseMoved(app, event):
    # For home screen
    if app.screen == 'home':
        for i in range(len(app.buttons[0])):
            app.buttons[0][i].mouseMoved(app, event.x, event.y)

    else:
        # back home and back buttons on all other screens
        app.backHomeButton.mouseMoved(app, event.x, event.y)
        app.backButton.mouseMoved(app, event.x, event.y)
        
        if app.screen == 'matCal':
            for i in range(len(app.buttons[1])):
                app.buttons[1][i].mouseMoved(app, event.x, event.y)
        
        elif app.screen == 'matAdd':
            app.solveButton.mouseMoved(app, event.x, event.y)
            app.clearButton.mouseMoved(app, event.x, event.y)
            for i in range(len(app.textBoxes[0][0])):
                app.textBoxes[0][0][i].mouseMoved(app, event.x, event.y)
            app.textBoxes[0][1].mouseMoved(app, event.x, event.y)
            app.textBoxes[0][2].mouseMoved(app, event.x, event.y)
        
        elif app.screen == 'matMul':
            app.solveButton.mouseMoved(app, event.x, event.y)
            app.clearButton.mouseMoved(app, event.x, event.y)
            for i in range(len(app.textBoxes[1][0])):
                app.textBoxes[1][0][i].mouseMoved(app, event.x, event.y)
            for i in range(len(app.textBoxes[1][1])):
                app.textBoxes[1][1][i].mouseMoved(app, event.x, event.y)
            app.textBoxes[1][2].mouseMoved(app, event.x, event.y)
            app.textBoxes[1][3].mouseMoved(app, event.x, event.y)
        
        elif app.screen == 'matMulResult':
            app.stepsButton.mouseMoved(app, event.x, event.y)
        
        elif app.screen == 'matTpose':
            app.solveButton.mouseMoved(app, event.x, event.y)
            app.clearButton.mouseMoved(app, event.x, event.y)
            for i in range(len(app.textBoxes[2][0])):
                app.textBoxes[2][0][i].mouseMoved(app, event.x, event.y)
            app.textBoxes[2][1].mouseMoved(app, event.x, event.y)

        elif app.screen == 'GE':
            app.solveButton.mouseMoved(app, event.x, event.y)
            app.clearButton.mouseMoved(app, event.x, event.y)
            for i in range(len(app.textBoxes[3][0])):
                app.textBoxes[3][0][i].mouseMoved(app, event.x, event.y)
            app.textBoxes[3][1].mouseMoved(app, event.x, event.y)

        elif app.screen == 'GEResult':
            app.stepsButton.mouseMoved(app, event.x, event.y)
        
        elif app.screen == 'SOLE':
            app.solveButton.mouseMoved(app, event.x, event.y)
            app.clearButton.mouseMoved(app, event.x, event.y)
            for i in range(len(app.textBoxes[4][0])):
                app.textBoxes[4][0][i].mouseMoved(app, event.x, event.y)
            app.textBoxes[4][1].mouseMoved(app, event.x, event.y)

        elif app.screen == 'SOLEResult':
            app.stepsButton.mouseMoved(app, event.x, event.y)
        
    
def mousePressed(app, event):
    # For home screen
    if app.screen == 'home':
        for i in range(len(app.buttons[0])):
            if app.buttons[0][i].mousePressed(app, event.x, event.y):
                app.screen = app.screens[i][0]
    else:
        if app.backHomeButton.mousePressed(app, event.x, event.y):
                app.screen = 'home'
                
        if app.screen == 'matCal':
            for i in range(len(app.buttons[1])):
                if app.buttons[1][i].mousePressed(app, event.x, event.y):
                    app.screen = app.screens[0][i+1][0]
        
        # For Matrix Addition and its sub-screens
        elif app.screen == 'matAdd':
            matAddMousePressed(app, event)
        elif app.screen == 'matAddResult':
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'matAdd'
        
        # For Matrix Multiplication and its sub-screens
        elif app.screen == 'matMul':
            matMulMousePressed(app, event)
        elif app.screen == 'matMulResult':
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'matMul'
            if app.stepsButton.mousePressed(app, event.x, event.y):
                app.scrollY = 0 # resets scroll value
                app.screen = 'matMulSteps'
        elif app.screen == 'matMulSteps':
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'matMulResult'
        
        # For Tranpose and its sub-screens
        elif app.screen == 'matTpose':
            tposeMousePressed(app, event)
        elif app.screen == 'matTposeResult':
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'matTpose'

        # For GE and its sub-screens
        elif app.screen == 'GE':
            GEMousePressed(app, event)
        elif app.screen == 'GEResult':
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'GE'
            if app.stepsButton.mousePressed(app, event.x, event.y):
                app.scrollY = 0 # resets scroll value
                app.screen = 'GESteps'
        elif app.screen == 'GESteps':
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'GEResult'

        # For SOLE and its sub-screens
        elif app.screen == 'SOLE':
            SOLEMousePressed(app, event)
        elif app.screen == 'SOLEResult':
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'SOLE'
            if app.stepsButton.mousePressed(app, event.x, event.y):
                app.scrollY = 0 # resets scroll value
                app.screen = 'SOLESteps'
        elif app.screen == 'SOLESteps':
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'SOLEResult'
        

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, width=0, fill='linen')
    if app.screen == 'home': redrawHomeScreen(app, canvas)

    elif app.screen == 'matCal': 
        redrawMatCalScreen(app,canvas)

    elif app.screen == 'matAdd': 
        redrawMatAddScreen(app, canvas)
    elif app.screen == 'matAddResult': 
        redrawMatAddResultScreen(app, canvas)

    elif app.screen == 'matMul': 
        redrawMatMulScreen(app, canvas)
    elif app.screen == 'matMulResult': 
        redrawMatMulResultScreen(app, canvas)
    elif app.screen == 'matMulSteps': 
        redrawMatMulStepsScreen(app, canvas)

    elif app.screen == 'matTpose': 
        redrawMatTposeScreen(app, canvas)
    elif app.screen == 'matTposeResult': 
        redrawMatTposeResultScreen(app, canvas)
    
    elif app.screen == 'GE': 
        redrawGEScreen(app, canvas)
    elif app.screen == 'GEResult': 
        redrawGEResultScreen(app, canvas)
    elif app.screen == 'GESteps': 
        redrawGEStepsScreen(app, canvas)

    elif app.screen == 'SOLE': 
        redrawSOLEScreen(app, canvas)
    elif app.screen == 'SOLEResult': 
        redrawSOLEResultScreen(app, canvas)
    elif app.screen == 'SOLESteps': 
        redrawSOLEStepsScreen(app, canvas)

    elif app.screen == 'det': 
        redrawDetScreen(app, canvas)

    elif app.screen == 'LU': 
        redrawLUScreen(app, canvas)
    elif app.screen == 'inverse': 
        redrawInverseScreen(app, canvas)
    elif app.screen == '4FS': 
        redraw4FSScreen(app, canvas)
    elif app.screen == 'GS': 
        redrawGSScreen(app, canvas)

def run241ForOne():
    runApp(title="241-for-One")

run241ForOne()