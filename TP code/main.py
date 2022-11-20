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
    app.screens = ['matAdd', 'matMul', 'GE', 'SOLE', 'LU', 'inverse', '4FS', 'det', 'home']
    app.screen = app.screens[-1]

    # ***Home Screen***
    # button locations
    app.homeMargin = app.width/8
    app.homeButtonWidth = (0.75*app.width-0.75*app.homeMargin)/4
    app.homeButtonHeight = 0.4*app.homeButtonWidth
    # font sizes
    app.homeTitleSize = int(app.height/15)
    # app.homeButtonText format: [(text, font size)]
    app.homeButtonText = [
        ('Matrix\nAddition', int(app.homeTitleSize/3)), 
        ('Matrix\nMultiplication', int(app.homeTitleSize/3)),
        ('Gaussian\nElimination', int(app.homeTitleSize/3)),
        ('Solving Systems of\nLinear Equations', int(app.homeTitleSize/3.3)), 
        ('LU-Factorization', int(app.homeTitleSize/3)), 
        ('Inverse', int(app.homeTitleSize/3)),
        ('4 Fundamental\nSubspaces', int(app.homeTitleSize/3)), 
        ('Determinant', int(app.homeTitleSize/3))
        ]
    app.homeButtonAttrib = []
    for i in range(8):  # number of buttons; separated by app.homeMargin/4
        x0 = int( app.homeMargin + (i%4)*(app.homeButtonWidth + app.homeMargin/4) )
        x1 = x0 + app.homeButtonWidth
        y0 = 0.5*app.height + (i//4)*(app.homeMargin/4 + app.homeButtonHeight)
        y1 = y0 + app.homeButtonHeight
        # attributes format: x0, y0, x1, y1, font color, font style, button text, bracket color
        app.homeButtonAttrib.append([x0, y0, x1, y1, 'tan4', '', app.homeButtonText[i], 'linen'])

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
        for i in range(len(app.homeButtonAttrib)):
            if app.homeButtonAttrib[i][0] <= event.x <= app.homeButtonAttrib[i][2] and\
                app.homeButtonAttrib[i][1] <= event.y <= app.homeButtonAttrib[i][3]:
                app.screen = app.screens[i]
                print(app.screen)


def mouseMoved(app, event):
    # For home screen
    if app.screen == 'home':
        for i in range(len(app.homeButtonAttrib)):
            if app.homeButtonAttrib[i][0] <= event.x <= app.homeButtonAttrib[i][2] and\
                app.homeButtonAttrib[i][1] <= event.y <= app.homeButtonAttrib[i][3]:
                app.homeButtonAttrib[i][4] = 'tan2'
                app.homeButtonAttrib[i][5] = 'bold'
                app.homeButtonAttrib[i][7] = 'tan2'
            else: 
                app.homeButtonAttrib[i][4] = 'tan4'
                app.homeButtonAttrib[i][5] = ''
                app.homeButtonAttrib[i][7] = 'linen'

def redrawHomeScreen(app, canvas):
    canvas.create_text(app.width/2, 0.13*app.height, text="241-for-One",
    fill='tan4', font=f'Century {app.homeTitleSize} bold')
    # canvas.create_text(app.width/2, 0.13*app.height, text="(           )",
    # fill='tan4', font=f'Century {app.homeTitleSize*2} bold')
    canvas.create_text(app.width/2, mean(0.15*app.height, app.homeButtonAttrib[0][1]), 
    text='''
    <Insert app description here>
    ''',
    fill='tan4', font=f'Century {int(app.homeTitleSize/3)}')
    canvas.create_text(app.width/2, mean(app.homeButtonAttrib[0][1], app.homeButtonAttrib[4][3]), 
    text="[          ]", # make this dynamically resize
    fill='tan4', font=f'Century {app.homeTitleSize*5}')
    for i in range(len(app.homeButtonAttrib)):
        canvas.create_rectangle(app.homeButtonAttrib[i][0], app.homeButtonAttrib[i][1],
        app.homeButtonAttrib[i][2], app.homeButtonAttrib[i][3], width=0, fill=app.homeButtonAttrib[i][4])
        canvas.create_text(mean(app.homeButtonAttrib[i][0], app.homeButtonAttrib[i][2]),
        mean(app.homeButtonAttrib[i][1], app.homeButtonAttrib[i][3]), 
        text=app.homeButtonAttrib[i][6][0],
        fill='linen', font=f'Century {app.homeButtonAttrib[i][6][1]} {app.homeButtonAttrib[i][5]}', 
        justify=CENTER)
        canvas.create_text(mean(app.homeButtonAttrib[i][0], app.homeButtonAttrib[i][2]),
        mean(app.homeButtonAttrib[i][1], app.homeButtonAttrib[i][3]), 
        text='[     ]', # make this dynamically resize
        fill=app.homeButtonAttrib[i][7], font=f'Century {app.homeTitleSize*2}', 
        justify=CENTER)

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, width=0, fill='linen')
    if app.screen == 'home':
        redrawHomeScreen(app, canvas)

def run241ForOne():
    runApp(title="241-for-One")

run241ForOne()