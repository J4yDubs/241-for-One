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
    def __init__(self, name, color1, color2):
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
    app.screens = [ ['matCal', 'matAdd', 'matMul', 'matTpose'], 
    ['GE'], ['SOLE'], ['LU'], ['inverse'], ['4FS'], ['det'], ['GS'],
    ['home'] ]
    app.screen = app.screens[-1][0]

    app.buttons = [[]]
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
    # app.homeButtonText format: [(text, font size)]
    app.homeButtonText = [
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
                                'tan4', app.homeButtonText[i][0], app.homeButtonText[i][1], '', ''))

    # *** BACK HOME BUTTON ***
    app.backHomeButtonMargin = 10
    app.backHomeButtonWidth = 0.1*app.width
    app.backHomeButtonHeight = 0.05*app.height
    app.backHomeButtonTextSize = int(app.height/70)
    app.backHomeButton = Button(app.backHomeButtonMargin, app.backHomeButtonMargin, 
                    app.backHomeButtonWidth, app.backHomeButtonHeight, 'tan4', 
                    '241-for-Me', app.backHomeButtonTextSize, '', '')

    # *** MATRIX CALCULATOR SCREEN ***
    app.matCalTitleSize = int(app.height/20)


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

    # for home button
    if app.screen != 'home':
        app.backHomeButton.mouseMoved(app, event.x, event.y)

def mousePressed(app, event):
    # For home screen
    if app.screen == 'home':
        for i in range(len(app.buttons[0])):
            if app.buttons[0][i].x0 <= event.x <= app.buttons[0][i].x1 and\
                app.buttons[0][i].y0 <= event.y <= app.buttons[0][i].y1:
                app.screen = app.screens[i][0]
    
    elif app.screen != 'home':
        if app.backHomeButton.x0 <= event.x <= app.backHomeButton.x1 and\
                app.backHomeButton.y0 <= event.y <= app.backHomeButton.y1:
                app.screen = 'home'

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

def redrawMatCalScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    canvas.create_text(app.width/2, 0.08*app.height, text="Matrix Calculator",
    fill='tan4', font=f'Century {app.matCalTitleSize} bold', justify=CENTER)

def redrawMatAddScreen(app, canvas):
    drawBackHomeButton(app, canvas)

def redrawMatMulScreen(app, canvas):
    drawBackHomeButton(app, canvas)

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