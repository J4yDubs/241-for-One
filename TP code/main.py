from matrix_utils import *
from matrix_GE import *
from matrix_SOLE import *

from cmu_112_graphics import *

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
    # might need to make app.screens 2D list for sub modes
    # app.screens = ['matAdd', 'matMul', 'GE', 'SOLE', 'LU', 'inverse', '4FS', 'det', 'home']
    app.screens = [ ['matCal', 'matAdd', 'matMul', 'matTpose'], 
    ['GE'], ['SOLE'], ['LU'], ['inverse'], ['4FS'], ['det'], ['GS'],
    ['home'] ]
    app.screen = app.screens[-1][0]

    # ***Home Screen***
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
    app.homeScrButtonAttrib = []
    for i in range(8):  # number of buttons; separated by app.homeMargin/4
        x0 = int( app.homeMargin + (i%4)*(app.homeScrButtonWidth + app.homeMargin/4) )
        x1 = x0 + app.homeScrButtonWidth
        y0 = 0.5*app.height + (i//4)*(app.homeMargin/4 + app.homeScrButtonHeight)
        y1 = y0 + app.homeScrButtonHeight
        # attributes format: x0, y0, x1, y1, font color, font style, button text, bracket color
        app.homeScrButtonAttrib.append([x0, y0, x1, y1, 'tan4', '', app.homeButtonText[i], ''])

    # ***Back Home Button***
    app.backHomeButtonMargin = 10
    app.backHomeButtonWidth = 0.1*app.width
    app.backHomeButtonHeight = 0.05*app.height
    app.backHomeButtonTextSize = int(app.height/70)
    app.backHomeButtonAttrib = [app.backHomeButtonMargin, app.backHomeButtonMargin,
     app.backHomeButtonMargin+app.backHomeButtonWidth, app.backHomeButtonMargin+app.backHomeButtonHeight,
    'tan4', '', '241-for-Me', 'linen']

    # ***Addition Screen***


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

def mousePressed(app, event):
    # For home screen
    if app.screen == 'home':
        for i in range(len(app.homeScrButtonAttrib)):
            if app.homeScrButtonAttrib[i][0] <= event.x <= app.homeScrButtonAttrib[i][2] and\
                app.homeScrButtonAttrib[i][1] <= event.y <= app.homeScrButtonAttrib[i][3]:
                app.screen = app.screens[i][0]
    
    elif app.screen != 'home':
        if app.backHomeButtonAttrib[0] <= event.x <= app.backHomeButtonAttrib[2] and\
                app.backHomeButtonAttrib[1] <= event.y <= app.backHomeButtonAttrib[3]:
                app.screen = 'home'

def mouseMoved(app, event):
    # For home screen
    if app.screen == 'home':
        for i in range(len(app.homeScrButtonAttrib)):
            if app.homeScrButtonAttrib[i][0] <= event.x <= app.homeScrButtonAttrib[i][2] and\
                app.homeScrButtonAttrib[i][1] <= event.y <= app.homeScrButtonAttrib[i][3]:
                app.homeScrButtonAttrib[i][4] = 'tan2'
                app.homeScrButtonAttrib[i][5] = 'bold'
                app.homeScrButtonAttrib[i][7] = 'tan2'
            else: 
                app.homeScrButtonAttrib[i][4] = 'tan4'
                app.homeScrButtonAttrib[i][5] = ''
                app.homeScrButtonAttrib[i][7] = ''

    # for home button
    if app.screen != 'home':
        if app.backHomeButtonAttrib[0] <= event.x <= app.backHomeButtonAttrib[2] and\
                app.backHomeButtonAttrib[1] <= event.y <= app.backHomeButtonAttrib[3]:
            app.backHomeButtonAttrib[4] = 'tan2'
            app.backHomeButtonAttrib[7] = 'tan2'
        else:
            app.backHomeButtonAttrib[4] = 'tan4'
            app.backHomeButtonAttrib[7] = ''

def redrawHomeScreen(app, canvas):
    canvas.create_text(app.width/2, 0.13*app.height, text="241-for-One",
    fill='tan4', font=f'Century {app.homeScrTitleSize} bold', justify=CENTER)
    # canvas.create_text(app.width/2, 0.13*app.height, text="(           )",
    # fill='tan4', font=f'Century {app.homeScrTitleSize*2} bold')
    canvas.create_text(app.width/2, mean(0.15*app.height, app.homeScrButtonAttrib[0][1]), 
    text='''
    <Insert app description here> 
    
    Now start by choosing one of the functions below!
    ''',
    fill='tan4', font=f'Century {int(app.homeScrTitleSize/3)}', justify=CENTER)
    canvas.create_text(app.width/2, mean(app.homeScrButtonAttrib[0][1], app.homeScrButtonAttrib[4][3]), 
    text="["+ " "*(int(app.homeScrTitleSize/5)) +"]", # makes this dynamically resize
    fill='tan4', font=f'Century {app.homeScrTitleSize*5}')
    for i in range(len(app.homeScrButtonAttrib)):
        canvas.create_rectangle(app.homeScrButtonAttrib[i][0], app.homeScrButtonAttrib[i][1],
        app.homeScrButtonAttrib[i][2], app.homeScrButtonAttrib[i][3], width=0, fill=app.homeScrButtonAttrib[i][4])
        canvas.create_text(mean(app.homeScrButtonAttrib[i][0], app.homeScrButtonAttrib[i][2]),
        mean(app.homeScrButtonAttrib[i][1], app.homeScrButtonAttrib[i][3]), 
        text=app.homeScrButtonAttrib[i][6][0],
        fill='linen', font=f'Century {app.homeScrButtonAttrib[i][6][1]} {app.homeScrButtonAttrib[i][5]}', 
        justify=CENTER)
        canvas.create_text(mean(app.homeScrButtonAttrib[i][0], app.homeScrButtonAttrib[i][2]),
        mean(app.homeScrButtonAttrib[i][1], app.homeScrButtonAttrib[i][3]), 
        text="["+ " "*(int(app.homeScrButtonWidth/42)) +"]", # makes this dynamically resize
        fill=app.homeScrButtonAttrib[i][7], font=f'Century {app.homeScrTitleSize*2}', 
        justify=CENTER)

def drawBackHomeButton(app, canvas):
    canvas.create_rectangle(app.backHomeButtonAttrib[0], app.backHomeButtonAttrib[1],
    app.backHomeButtonAttrib[2], app.backHomeButtonAttrib[3], width=0, fill=app.backHomeButtonAttrib[4])
    canvas.create_text(mean(app.backHomeButtonAttrib[0], app.backHomeButtonAttrib[2]),
    mean(app.backHomeButtonAttrib[1], app.backHomeButtonAttrib[3]),
    text="241-for-One", fill='linen', font=f'Century {app.backHomeButtonTextSize} bold')
    canvas.create_text(mean(app.backHomeButtonAttrib[0], app.backHomeButtonAttrib[2]),
    mean(app.backHomeButtonAttrib[1], app.backHomeButtonAttrib[3]),
    text="["+ " "*(int(app.backHomeButtonWidth/17)) +"]",
    fill=app.backHomeButtonAttrib[7], 
    font=f'Century {app.backHomeButtonTextSize*4}', 
        justify=CENTER
    )

def redrawMatCalScreen(app, canvas):
    drawBackHomeButton(app, canvas)

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