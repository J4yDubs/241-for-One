from matrix_utils import *
from matrix_GE import *
from matrix_SOLE import *

from cmu_112_graphics import *

# Classes below
class Button:
    def __init__(self, x0, y0, width, height, color, text, fontSize, fontStyle, bracketColor):
        self.x0 = x0
        self.y0 = y0
        self.x1 = self.x0 + width
        self.y1 = self.y0 + height
        self.baseColor = color
        self.color = self.baseColor
        self.text = text
        self.fontSize = fontSize
        self.fontStyle = fontStyle
        self.bracketColor = bracketColor

    def mouseMoved(self, app, eventX, eventY):
        if self.x0 <= eventX <= self.x1 and self.y0 <= eventY <= self.y1:
            self.color = 'tan2'
            self.fontStyle = 'bold'
            self.bracketColor = self.color
        else:
            self.color = self.baseColor
            self.fontStyle = ''
            self.bracketColor = ''
    
    def redraw(self, app, canvas):
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.color, width=0)
        canvas.create_text(mean(self.x0, self.x1), mean(self.y0, self.y1), text=self.text, fill='linen', 
        font=f'Century {self.fontSize} {self.fontStyle}', justify=CENTER)

class TextBox:
    def __init__(self, x0, y0, width, height, color, fontSize, fontStyle):
        self.x0 = x0
        self.y0 = y0
        self.x1 = self.x0 + width
        self.y1 = self.y0 + height
        self.baseColor = color
        self.color = self.baseColor
        self.fontSize = fontSize
        self.fontStyle = fontStyle
        self.text = ''

    def mouseMoved(self, app, eventX, eventY):
        pass

    def mousePressed(self, app, eventX, eventY):
        pass

    def keyPressed(self, app, eventKey):
        # checks if length if eventKey is 1
        if eventKey in app.numKeys:
            self.text += eventKey
        pass

    def redraw(self, app, canvas):
        pass

# Helper functions below

def mean(x,y):
    return (x+y)/2

# Taken from Piazza by instructor Joe Ritze (to get screen dimensions to get fullscreen)
def fitToScreen(app):
	app.width = app._theRoot.winfo_screenwidth()
	app.height = app._theRoot.winfo_screenheight()
	app.setSize(app.width, app.height)
	app.updateTitle()

def appStarted(app):
    fitToScreen(app)
    app.screens = [ ['matCal', ['matAdd', 'matAddResult'],
     ['matMul', 'matMulResult', 'matMulShowSteps'], 
     ['matTpose', 'matTposeResult']], 
    ['GE'], ['SOLE'], ['LU'], ['inverse'], ['4FS'], ['det'], ['GS'],
    ['home'] ]
    app.screen = app.screens[-1][0]

    app.buttons = [[],[],[],[],[]]
    # app.buttons.append(Button(300, 100)) # do in for loop
    # then iterate through app.buttons in redrawall, mousepressed
    # any button pressed = True if inside; else false; skip through body of code 
    # can use default values
    # if take in app as parameter, can directly modify app obj in button/textbox class

    # *** HOME SCREEN ***
    # button locations
    app.homeMargin = app.width/8
    app.homeScrButtonWidth = (0.75*app.width-0.75*app.homeMargin)/4
    app.homeScrButtonHeight = 0.4*app.homeScrButtonWidth
    # font sizes
    app.homeScrTitleSize = int(app.height/15)
    # app.homeButtonsText format: [(text, font size)]
    app.homeButtonsText = [
        ('General Matrix\nCalculator', int(app.homeScrTitleSize/3)), 
        ('Gaussian\nElimination', int(app.homeScrTitleSize/3)),
        ('Solving Systems of\nLinear Equations', int(app.homeScrTitleSize/3.3)), 
        ('LU-Factorization', int(app.homeScrTitleSize/3)), 
        ('Inverse', int(app.homeScrTitleSize/3)),
        ('4 Fundamental\nSubspaces', int(app.homeScrTitleSize/3)), 
        ('Determinant', int(app.homeScrTitleSize/3)),
        ('Orthonormal\nBases', int(app.homeScrTitleSize/3)),
        ]
    # creating home buttons with button object
    for i in range(8):
        app.buttons[0].append(Button(int( app.homeMargin + (i%4)*(app.homeScrButtonWidth + app.homeMargin/4) ),
                                0.5*app.height + (i//4)*(app.homeMargin/4 + app.homeScrButtonHeight),
                                app.homeScrButtonWidth, app.homeScrButtonHeight,
                                'tan4', app.homeButtonsText[i][0], app.homeButtonsText[i][1], '', ''))
    
    # *** KEYS AND KEYBINDINGS ***
    app.numKeys = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    
    # *** BACK HOME BUTTON ***
    app.backHomeButtonMargin = 10
    app.backHomeButtonWidth = 0.1*app.width
    app.backHomeButtonHeight = 0.05*app.height
    app.backHomeButtonsTextSize = int(app.height/70)
    app.backHomeButton = Button(app.backHomeButtonMargin, app.backHomeButtonMargin, 
                    app.backHomeButtonWidth, app.backHomeButtonHeight, 'tan4', 
                    '241-for-Me', app.backHomeButtonsTextSize, '', '')

    # *** GO BACK BUTTON ***
    app.backButtonMargin = 10
    app.backButtonWidth = 0.1*app.width
    app.backButtonHeight = 0.05*app.height
    app.backButtonsTextSize = int(app.height/70)
    app.backButton = Button(2*app.backButtonMargin + app.backHomeButtonWidth, app.backButtonMargin, 
                    app.backButtonWidth, app.backButtonHeight, 'tan4', 
                    'Back', app.backButtonsTextSize, '', '')

    # *** MATRIX CALCULATOR SCREEN ***
    # button locations
    app.calMargin = app.width/7
    app.calScrButtonWidth = (0.75*app.width-0.2*app.calMargin)/4
    app.calScrButtonHeight = 0.4*app.calScrButtonWidth
    app.calScrButtonSep = (app.width-2*app.calMargin-3*app.calScrButtonWidth)//2
    # font sizes
    app.calScrTitleSize = int(app.height/17)
    # button text
    app.calButtonsText = [
        ('Matrix\nAddition', int(app.calScrTitleSize/2.5)), 
        ('Matrix\nMultiplication', int(app.calScrTitleSize/2.5)),
        ('Obtain\nTranspose', int(app.calScrTitleSize/2.5)), 
        ]
    # creating buttons with button object
    for i in range(3):
        app.buttons[1].append(Button(int( app.calMargin + i*(app.calScrButtonWidth + app.calScrButtonSep) ),
                                0.5*app.height,
                                app.calScrButtonWidth, app.calScrButtonHeight,
                                'tan4', app.calButtonsText[i][0], app.calButtonsText[i][1], '', ''))

    # *** MATRIX ADDITION SCREEN *** (no showing steps)
    app.matAddMargin = app.width/3
    app.addScrButtonWidth = (0.75*app.width-0.2*app.matAddMargin)/6
    app.addScrButtonHeight = 0.4*app.addScrButtonWidth
    app.addScrButtonSep = (app.width-2*app.matAddMargin-2*app.addScrButtonWidth)
    # font sizes
    app.addScrTitleSize = int(app.height/20)
    # button text
    app.addButtonsText = [
        ('Solve', int(app.addScrTitleSize/2.5)), 
        ('Clear entries', int(app.addScrTitleSize/2.5)),
        ]
    # creating buttons with button object
    for i in range(2):
        app.buttons[2].append(Button(int( app.matAddMargin + i*(app.addScrButtonWidth + app.addScrButtonSep) ),
                                0.8*app.height,
                                app.addScrButtonWidth, app.addScrButtonHeight,
                                'tan4', app.addButtonsText[i][0], app.addButtonsText[i][1], '', ''))
    
    # dimension text boxes

    # matrix entry text boxes

    # *** MATRIX MULTIPLICATION SCREEN ***

    # *** MATRIX TRANSPOSE SCREEN *** (no showing steps)


def getCellBounds(app, row, col):
    colWidth = (app.width-2*app.margin) / app.cols
    rowHeight = (app.height-2*app.margin) / app.rows
    x0 = app.margin + col * colWidth
    x1 = app.margin + (col+1)* colWidth
    y0 = app.margin + row * rowHeight
    y1 = app.margin + (row+1) * rowHeight
    return (x0, y0, x1, y1)

def keyPressed(app, event):
    # create dictionary of keybindings

    # For home screen
    pass

def mouseMoved(app, event):
    # For home screen
    if app.screen == 'home':
        for i in range(len(app.buttons[0])):
            app.buttons[0][i].mouseMoved(app, event.x, event.y)

    # for back home button
    else:
        app.backHomeButton.mouseMoved(app, event.x, event.y)
        app.backButton.mouseMoved(app, event.x, event.y)
        
        if app.screen == 'matCal':
            for i in range(len(app.buttons[1])):
                app.buttons[1][i].mouseMoved(app, event.x, event.y)
    


def mousePressed(app, event):
    # For home screen
    if app.screen == 'home':
        for i in range(len(app.buttons[0])):
            if app.buttons[0][i].x0 <= event.x <= app.buttons[0][i].x1 and\
                app.buttons[0][i].y0 <= event.y <= app.buttons[0][i].y1:
                app.screen = app.screens[i][0]
    
    else:
        if app.backHomeButton.x0 <= event.x <= app.backHomeButton.x1 and\
                app.backHomeButton.y0 <= event.y <= app.backHomeButton.y1:
                app.screen = 'home'
                
        if app.screen == 'matCal':
            for i in range(len(app.buttons[1])):
                if app.buttons[1][i].x0 <= event.x <= app.buttons[1][i].x1 and\
                    app.buttons[1][i].y0 <= event.y <= app.buttons[1][i].y1:
                    app.screen = app.screens[0][i+1][0]
        
        elif app.screen == 'matAdd':
            if app.backButton.x0 <= event.x <= app.backButton.x1 and\
                app.backButton.y0 <= event.y <= app.backButton.y1:
                app.screen = 'matCal'
        
        elif app.screen == 'matMul':
            if app.backButton.x0 <= event.x <= app.backButton.x1 and\
                app.backButton.y0 <= event.y <= app.backButton.y1:
                app.screen = 'matCal'
        
        elif app.screen == 'matTpose':
            if app.backButton.x0 <= event.x <= app.backButton.x1 and\
                app.backButton.y0 <= event.y <= app.backButton.y1:
                app.screen = 'matCal'


    # elif app.screen == 'matCal':


def redrawHomeScreen(app, canvas):
    canvas.create_text(app.width/2, 0.13*app.height, text="241-for-One",
    fill='tan4', font=f'Century {app.homeScrTitleSize} bold', justify=CENTER)
    # canvas.create_text(app.width/2, 0.13*app.height, text="(           )",
    # fill='tan4', font=f'Century {app.homeScrTitleSize*2} bold')
    canvas.create_text(app.width/2, mean(0.15*app.height, app.buttons[0][0].y0), 
    text='''
    <Insert app description here> 
    
    Now start by choosing one of the functions below!
    ''',
    fill='tan4', font=f'Century {int(app.homeScrTitleSize/3)}', justify=CENTER)
    canvas.create_text(app.width/2, mean(app.buttons[0][0].y0, app.buttons[0][4].y1), 
    text="["+ " "*(int(app.homeScrTitleSize/5)) +"]", # makes this dynamically resize
    fill='tan4', font=f'Century {app.homeScrTitleSize*5}')

    for i in range(len(app.buttons[0])):
        app.buttons[0][i].redraw(app, canvas)
        canvas.create_text(mean(app.buttons[0][i].x0, app.buttons[0][i].x1),
        mean(app.buttons[0][i].y0, app.buttons[0][i].y1), 
        text="["+ " "*(int(app.homeScrButtonWidth/42)) +"]", # makes this dynamically resize
        fill=app.buttons[0][i].bracketColor, font=f'Century {app.homeScrTitleSize*2}', 
        justify=CENTER)

def drawBackHomeButton(app, canvas):
    app.backHomeButton.redraw(app, canvas)
    canvas.create_text(mean(app.backHomeButton.x0, app.backHomeButton.x1), 
    mean(app.backHomeButton.y0, app.backHomeButton.y1),
    text="["+ " "*(int(app.backHomeButtonWidth/17)) +"]", fill=app.backHomeButton.bracketColor, 
    font=f'Century {app.backHomeButton.fontSize*4}', justify=CENTER)

def drawBackButton(app, canvas):
    app.backButton.redraw(app, canvas)
    canvas.create_text(mean(app.backButton.x0, app.backButton.x1), 
    mean(app.backButton.y0, app.backButton.y1),
    text="["+ " "*(int(app.backButtonWidth/17)) +"]", fill=app.backButton.bracketColor, 
    font=f'Century {app.backButton.fontSize*4}', justify=CENTER)

def redrawMatCalScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    canvas.create_text(app.width/2, 0.25*app.height, text="General Matrix\nCalculator",
    fill='tan4', font=f'Century {app.calScrTitleSize} bold', justify=CENTER)

    for i in range(len(app.buttons[1])):
        app.buttons[1][i].redraw(app, canvas)

def redrawMatAddScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    canvas.create_text(app.width/2, 0.05*app.height, text="Matrix Addition",
    fill='tan4', font=f'Century {app.addScrTitleSize} bold', justify=CENTER)

    for i in range(len(app.buttons[2])):
        app.buttons[2][i].redraw(app, canvas)

def redrawMatMulScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)

def redrawMatTposeScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)

def redrawGEScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    
def redrawSOLEScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    
def redrawLUScreen(app, canvas):
    drawBackHomeButton(app, canvas)

def redrawInverseScreen(app, canvas):
    drawBackHomeButton(app, canvas)

def redraw4FSScreen(app, canvas):
    drawBackHomeButton(app, canvas)

def redrawDetScreen(app, canvas):
    drawBackHomeButton(app, canvas)

def redrawGSScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, width=0, fill='linen')
    if app.screen == 'home':
        redrawHomeScreen(app, canvas)
    elif app.screen == 'matCal':
        redrawMatCalScreen(app,canvas)
    elif app.screen == 'matAdd':
        redrawMatAddScreen(app, canvas)
    elif app.screen =='matMul':
        redrawMatMulScreen(app, canvas)
    elif app.screen == 'matTpose':
        redrawMatTposeScreen(app, canvas)
    elif app.screen == 'GE':
        redrawGEScreen(app, canvas)
    elif app.screen == 'SOLE':
        redrawSOLEScreen(app, canvas)
    elif app.screen == 'LU':
        redrawLUScreen(app, canvas)
    elif app.screen == 'inverse':
        redrawInverseScreen(app, canvas)
    elif app.screen == '4FS':
        redraw4FSScreen(app, canvas)
    elif app.screen == 'det':
        redrawDetScreen(app, canvas)
    elif app.screen == 'GS':
        redrawGSScreen(app, canvas)

def run241ForOne():
    runApp(title="241-for-One")

run241ForOne()