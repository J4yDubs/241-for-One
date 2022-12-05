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

# ********** BUTTON INITIALIZATIONS **********

# Back home button
def backHomeButtonInit(app):
    app.backHomeButtonMargin = 10
    app.backHomeButtonWidth = 0.1*app.width
    app.backHomeButtonHeight = 0.05*app.height
    app.backHomeButtonsTextSize = int(app.height/70)
    app.backHomeButton = button(app.backHomeButtonMargin, app.backHomeButtonMargin, 
                    app.backHomeButtonWidth, app.backHomeButtonHeight, 'tan4', 
                    '241-for-One', app.backHomeButtonsTextSize, '', '')

# Go back button
def backButtonInit(app):
    app.backButtonMargin = 10
    app.backButtonWidth = 0.1*app.width
    app.backButtonHeight = 0.05*app.height
    app.backButtonsTextSize = int(app.height/70)
    app.backButton = button(2*app.backButtonMargin + app.backHomeButtonWidth, app.backButtonMargin, 
                    app.backButtonWidth, app.backButtonHeight, 'tan4', 
                    'Back', app.backButtonsTextSize, '', '')

# Solve button
def solveButtonInit(app):
    app.solveButtonMargin = app.width/3
    app.solveButtonWidth = (0.75*app.width-0.2*app.solveButtonMargin)/6
    app.solveButtonHeight = 0.4*app.solveButtonWidth
    app.solveButtonTextSize = int(app.height/50)
    app.solveButton = button(app.solveButtonMargin, 0.8*app.height,
                                app.solveButtonWidth, app.solveButtonHeight,
                                'tan4', 'Solve', app.solveButtonTextSize, '', '')

# Clear button
def clearButtonInit(app):
    app.clearButtonMargin = app.width/3
    app.clearButtonWidth = (0.75*app.width-0.2*app.clearButtonMargin)/6
    app.clearButtonHeight = 0.4*app.clearButtonWidth
    app.clearButtonTextSize = int(app.height/50)
    app.clearButtonSep = (app.width-2*app.clearButtonMargin-2*app.clearButtonWidth)
    app.clearButton = button(app.solveButtonMargin + app.solveButtonWidth + app.clearButtonSep,
                                 0.8*app.height,
                                app.clearButtonWidth, app.clearButtonHeight,
                                'tan4', 'Clear', app.clearButtonTextSize, '', '')

# Show steps button
def stepsButtonInit(app):
    app.stepsButtonWidth = app.width/10
    app.stepsButtonHeight = 0.4*app.stepsButtonWidth
    app.stepsButtonTextSize = int(app.height/50)
    app.stepsButton = button(app.width/2 - app.stepsButtonWidth/2, 0.8*app.height,
                                app.stepsButtonWidth, app.stepsButtonHeight,
                                'tan4', 'Show steps', app.stepsButtonTextSize, '', '')

# ********** SCREEN INITIALIZATIONS **********

# Main Screens
def screensInit(app):
    app.screens = [ ['matCal',
     ['matAdd', 'matAddResult'],
     ['matMul', 'matMulResult', 'matMulSteps'], 
     ['matTpose', 'matTposeResult']], 
    ['GE', 'GEResult', 'GESteps'], 
    ['SOLE', 'SOLEResult', 'SOLESteps'],
    ['det', 'detResult', 'detSteps'], ['inverse'], ['4FS'], ['LU'], ['GS'],
    ['home'] ]
    app.screen = app.screens[-1][0]

# Home Screen Initialization
def homeScreenInit(app):
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
        ('Determinant', int(app.homeScrTitleSize/3)),   
        ('Inverse', int(app.homeScrTitleSize/3)),
        ('4 Fundamental\nSubspaces', int(app.homeScrTitleSize/3)), 
        ('LU-Factorization', int(app.homeScrTitleSize/3)),
        ('Orthonormal\nBases', int(app.homeScrTitleSize/3)),
        ]
    # creating home buttons with button object
    for i in range(8):
        app.buttons[0].append(button(int( app.homeMargin + (i%4)*(app.homeScrButtonWidth + app.homeMargin/4) ),
                                0.5*app.height + (i//4)*(app.homeMargin/4 + app.homeScrButtonHeight),
                                app.homeScrButtonWidth, app.homeScrButtonHeight,
                                'tan4', app.homeButtonsText[i][0], app.homeButtonsText[i][1], '', ''))

# General matrix calculator screen initialization
def calScreenInit(app):
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
    for i in range(len(app.calButtonsText)):
        app.buttons[1].append(button(int( app.calMargin + i*(app.calScrButtonWidth + app.calScrButtonSep) ),
                                0.5*app.height,
                                app.calScrButtonWidth, app.calScrButtonHeight,
                                'tan4', app.calButtonsText[i][0], app.calButtonsText[i][1], '', ''))

# Addition screen and its sub-screens initializations
def addScreenInit(app):
    # *** MATRIX ADDITION SCREEN *** (no showing steps)
    # text box margins
    app.matAddMargin = app.width/3
    # font sizes
    app.addScrTitleSize = int(app.height/20)
    # Text Box Dims
    # i) dimension text boxes 
    # app.addScrDimTB prefix - addition Screen Dimension Text Box
    app.addScrDimTBWidth = 0.05*app.width
    app.addScrDimTBHeight = app.addScrDimTBWidth
    app.addScrDimTBSep = (app.width-2*app.matAddMargin-2*app.addScrDimTBWidth)
    for i in range(2):
        app.textBoxes[0][0].append(DimTextBox(int( app.matAddMargin + i*(app.addScrDimTBWidth + app.addScrDimTBSep) ),
         0.11*app.height, 
         app.addScrDimTBWidth, app.addScrDimTBHeight, 
         'peach puff', 'tan4', app.addScrDimTBHeight/2, app))
    # ii) entry text boxes
    app.addScrEntryTBX0 = app.width/9
    app.addScrEntryTBY0 = 0.27*app.height
    app.addScrEntryTBX1 = app.width/2-app.addScrEntryTBX0
    app.addScrEntryTBY1 = app.addScrEntryTBY0 + (app.addScrEntryTBX1 - app.addScrEntryTBX0) # square
    app.addScrEntryTBRows = int(app.textBoxes[0][0][0].text)
    app.addScrEntryTBCols = int(app.textBoxes[0][0][1].text)
    app.addScrEntryFontSize = min((app.addScrEntryTBY1-app.addScrEntryTBY0)/(2*app.addScrEntryTBRows),
    (app.addScrEntryTBX1-app.addScrEntryTBX0)/(2*app.addScrEntryTBCols))
    for i in range(2):
        app.textBoxes[0].append(MatrixEntry( app.addScrEntryTBRows, app.addScrEntryTBCols, 
        app.addScrEntryTBX0 + i*app.width/2, app.addScrEntryTBY0, 
        app.addScrEntryTBX1 + i*app.width/2, app.addScrEntryTBY1, 
        'peach puff', 'tan4', app.addScrEntryFontSize, app))
    
    # *** ADDITION RESULT SCREEN ***
    app.addResultX0 = app.width/3
    app.addResultY0 = app.height/5
    app.addResultX1 = app.width - app.addResultX0
    app.addResultY1 = app.addResultY0 + (app.addResultX1 - app.addResultX0)
    app.addResultMatrix = create2DList(app.addScrEntryTBRows, app.addScrEntryTBCols)
    app.addResult = OutputMatrix(app.addResultMatrix, app.addResultX0, app.addResultY0, 
    app.addResultX1, app.addResultY1, 'peach puff', 'tan4', app.addScrEntryFontSize, app)

# Multiplication screen and its sub-screens initializations
def mulScreenInit(app):
    # *** MATRIX MULTIPLICATION SCREEN ***
    # text box margin
    app.matMulMargin = app.width/3
    # font sizes
    app.mulScrTitleSize = int(app.height/20)
    # Text Box Dims
    # i) dimension text boxes
    app.mulScrDimTBWidth = 0.05*app.width
    app.mulScrDimTBHeight = app.mulScrDimTBWidth
    app.mulScrDimTBSep = (app.width/2-1*app.matMulMargin-2*app.mulScrDimTBWidth)
    for i in range(2):
        app.textBoxes[1][0].append(DimTextBox(int( app.matMulMargin/2 + i*(app.mulScrDimTBWidth + app.mulScrDimTBSep) ),
         0.11*app.height, 
         app.mulScrDimTBWidth, app.mulScrDimTBHeight, 
         'peach puff', 'tan4', app.mulScrDimTBHeight/2, app))
        app.textBoxes[1][1].append(DimTextBox(int( app.matMulMargin/2 + app.width/2 + i*(app.mulScrDimTBWidth + app.mulScrDimTBSep) ),
         0.11*app.height, 
         app.mulScrDimTBWidth, app.mulScrDimTBHeight, 
         'peach puff', 'tan4', app.mulScrDimTBHeight/2, app))
    # ii) entry text boxes
    app.mulScrEntryTBX0 = app.width/9
    app.mulScrEntryTBY0 = 0.27*app.height
    app.mulScrEntryTBX1 = app.width/2-app.mulScrEntryTBX0
    app.mulScrEntryTBY1 = app.mulScrEntryTBY0 + (app.mulScrEntryTBX1 - app.mulScrEntryTBX0) # square
    app.mulScrEntryTBWidth = app.mulScrEntryTBX1 - app.mulScrEntryTBX0
    app.mulScrEntryTBHeight = app.mulScrEntryTBY1 - app.mulScrEntryTBY0
    app.mulScrEntryTB1Rows = int(app.textBoxes[1][0][0].text)
    app.mulScrEntryTB1Cols = int(app.textBoxes[1][0][1].text)
    app.mulScrEntryTB2Rows = int(app.textBoxes[1][1][0].text)
    app.mulScrEntryTB2Cols = int(app.textBoxes[1][1][1].text)
    app.mulScrEntry1FontSize = min((app.mulScrEntryTBHeight)/(2*app.mulScrEntryTB1Rows),
    (app.mulScrEntryTBWidth)/(2*app.mulScrEntryTB1Cols))
    app.mulScrEntry2FontSize = min((app.mulScrEntryTBHeight)/(2*app.mulScrEntryTB2Rows),
    (app.mulScrEntryTBWidth)/(2*app.mulScrEntryTB2Cols))
    # Entry Text Box 1 (app.textBoxes[1][2])
    app.textBoxes[1].append(MatrixEntry( app.mulScrEntryTB1Rows, app.mulScrEntryTB1Cols, 
    app.mulScrEntryTBX0, app.mulScrEntryTBY0, app.mulScrEntryTBX1, app.mulScrEntryTBY1, 
    'peach puff', 'tan4', app.mulScrEntry1FontSize, app))
    # Entry Text Box 2 (app.textBoxes[1][3])
    for i in range(2):
        app.textBoxes[1].append(MatrixEntry( app.mulScrEntryTB2Rows, app.mulScrEntryTB2Cols, 
        app.mulScrEntryTBX0 + app.width/2, app.mulScrEntryTBY0, 
        app.mulScrEntryTBX1 + app.width/2, app.mulScrEntryTBY1, 
        'peach puff', 'tan4', app.mulScrEntry2FontSize, app))

    # *** MULTIPLICATION RESULT SCREEN ***
    app.mulResultX0 = app.width/3
    app.mulResultY0 = app.height/5
    app.mulResultX1 = app.width - app.mulResultX0
    app.mulResultY1 = app.mulResultY0 + (app.mulResultX1 - app.mulResultX0)
    app.mulResultMatrix = create2DList(app.mulScrEntryTB1Rows, app.mulScrEntryTB2Cols)
    app.mulResult = OutputMatrix(app.mulResultMatrix, app.mulResultX0, app.mulResultY0, 
    app.mulResultX1, app.mulResultY1, 'peach puff', 'tan4', 
    min(app.mulScrEntry1FontSize,app.mulScrEntry2FontSize), app)

    # *** MULTIPLICATION STEPS SCREEN ***
    app.mulSteps = []


# Transpose screen and its sub-screens initializations
def tposeScreenInit(app):
    # *** MATRIX TRANSPOSE SCREEN *** (no showing steps)
    # text box margins
    app.tposeMargin = app.width/2.5
    # font sizes
    app.tposeScrTitleSize = int(app.height/20)
    # Text Box Dims
    # i) dimension text boxes
    app.tposeScrDimTBWidth = 0.05*app.width
    app.tposeScrDimTBHeight = app.tposeScrDimTBWidth
    app.tposeScrDimTBSep = (app.width-2*app.tposeMargin-2*app.tposeScrDimTBWidth)
    for i in range(2):
        app.textBoxes[2][0].append(DimTextBox(int( app.tposeMargin + i*(app.tposeScrDimTBWidth + app.tposeScrDimTBSep) ),
         0.11*app.height, 
         app.tposeScrDimTBWidth, app.tposeScrDimTBHeight, 
         'peach puff', 'tan4', app.tposeScrDimTBHeight/2, app))
    # ii) entry text boxes
    app.tposeScrEntryTBX0 = app.width/10
    app.tposeScrEntryTBY0 = 0.27*app.height
    app.tposeScrEntryTBX1 = app.width/2-app.tposeScrEntryTBX0
    app.tposeScrEntryTBY1 = app.tposeScrEntryTBY0 + (app.tposeScrEntryTBX1 - app.tposeScrEntryTBX0) # square
    app.tposeScrEntryTBWidth = app.tposeScrEntryTBX1 - app.tposeScrEntryTBX0
    app.tposeScrEntryTBHeight = app.tposeScrEntryTBY1 - app.tposeScrEntryTBY0
    app.tposeScrEntryTBRows = int(app.textBoxes[2][0][0].text)
    app.tposeScrEntryTBCols = int(app.textBoxes[2][0][1].text)
    app.tposeScrEntryFontSize = min((app.tposeScrEntryTBHeight)/(2*app.tposeScrEntryTBRows),
    (app.tposeScrEntryTBWidth)/(2*app.tposeScrEntryTBCols))
    app.textBoxes[2].append(MatrixEntry( app.tposeScrEntryTBRows, app.tposeScrEntryTBCols, 
    app.width/2 - app.tposeScrEntryTBWidth/2, app.tposeScrEntryTBY0, 
    app.width/2 + app.tposeScrEntryTBWidth/2, app.tposeScrEntryTBY1, 
    'peach puff', 'tan4', app.tposeScrEntryFontSize, app))

    # *** TRANSPOSE RESULT SCREEN ***
    app.tposeResultX0 = app.width/3
    app.tposeResultY0 = app.height/5
    app.tposeResultX1 = app.width - app.tposeResultX0
    app.tposeResultY1 = app.tposeResultY0 + (app.tposeResultX1 - app.tposeResultX0)
    app.tposeResultMatrix = create2DList(app.tposeScrEntryTBRows, app.tposeScrEntryTBCols)
    app.tposeResult = OutputMatrix(app.tposeResultMatrix, app.tposeResultX0, app.tposeResultY0, 
    app.tposeResultX1, app.tposeResultY1, 'peach puff', 'tan4', app.tposeScrEntryFontSize, app)

# Gaussian Elimination screen and its sub-screens initializations
def GEScreenInit(app):
    # *** GE SCREEN ***
    # text box margins
    app.GEMargin = app.width/2.5
    # font sizes
    app.GEScrTitleSize = int(app.height/20)
    # Text Box Dims
    # i) dimension text boxes
    app.GEScrDimTBWidth = 0.05*app.width
    app.GEScrDimTBHeight = app.GEScrDimTBWidth
    app.GEScrDimTBSep = (app.width-2*app.GEMargin-2*app.GEScrDimTBWidth)
    for i in range(2):
        app.textBoxes[3][0].append(DimTextBox(int( app.GEMargin + i*(app.GEScrDimTBWidth + app.GEScrDimTBSep) ),
         0.11*app.height, 
         app.GEScrDimTBWidth, app.GEScrDimTBHeight, 
         'peach puff', 'tan4', app.GEScrDimTBHeight/2, app))
    # ii) entry text boxes
    app.GEScrEntryTBX0 = app.width/10
    app.GEScrEntryTBY0 = 0.27*app.height
    app.GEScrEntryTBX1 = app.width/2-app.GEScrEntryTBX0
    app.GEScrEntryTBY1 = app.GEScrEntryTBY0 + (app.GEScrEntryTBX1 - app.GEScrEntryTBX0) # square
    app.GEScrEntryTBWidth = app.GEScrEntryTBX1 - app.GEScrEntryTBX0
    app.GEScrEntryTBHeight = app.GEScrEntryTBY1 - app.GEScrEntryTBY0
    app.GEScrEntryTBRows = int(app.textBoxes[3][0][0].text)
    app.GEScrEntryTBCols = int(app.textBoxes[3][0][1].text)
    app.GEScrEntryFontSize = min((app.GEScrEntryTBHeight)/(2*app.GEScrEntryTBRows),
    (app.GEScrEntryTBWidth)/(2*app.GEScrEntryTBCols))
    app.textBoxes[3].append(MatrixEntry( app.GEScrEntryTBRows, app.GEScrEntryTBCols, 
    app.width/2 - app.GEScrEntryTBWidth/2, app.GEScrEntryTBY0, 
    app.width/2 + app.GEScrEntryTBWidth/2, app.GEScrEntryTBY1, 
    'peach puff', 'tan4', app.GEScrEntryFontSize, app))

    # *** GE RESULT SCREEN ***
    app.GEResultX0 = app.width/3
    app.GEResultY0 = app.height/5
    app.GEResultX1 = app.width - app.GEResultX0
    app.GEResultY1 = app.GEResultY0 + (app.GEResultX1 - app.GEResultX0)
    app.GEResultMatrix = create2DList(app.GEScrEntryTBRows, app.GEScrEntryTBCols)
    app.GEResult = OutputMatrix(app.GEResultMatrix, app.GEResultX0, app.GEResultY0, 
    app.GEResultX1, app.GEResultY1, 'peach puff', 'tan4', app.GEScrEntryFontSize, app)

    # *** GE STEPS SCREEN ***
    app.GESteps = []

# Sys of Linear Eqns (SOLE) screen and its sub-screens initializations
def SOLEScreenInit(app):
    # *** SOLE SCREEN ***
    # text box margins
    app.SOLEMargin = app.width/2.5
    # font sizes
    app.SOLEScrTitleSize = int(app.height/20)
    # Text Box Dims
    # i) dimension text boxes
    app.SOLEScrDimTBWidth = 0.05*app.width
    app.SOLEScrDimTBHeight = app.SOLEScrDimTBWidth
    app.SOLEScrDimTBSep = (app.width-2*app.SOLEMargin-2*app.SOLEScrDimTBWidth)
    for i in range(2):
        app.textBoxes[4][0].append(DimTextBox(int( app.SOLEMargin + i*(app.SOLEScrDimTBWidth + app.SOLEScrDimTBSep) ),
         0.11*app.height, 
         app.SOLEScrDimTBWidth, app.SOLEScrDimTBHeight, 
         'peach puff', 'tan4', app.SOLEScrDimTBHeight/2, app))
    # ii) entry text boxes
    app.SOLEScrEntryTBX0 = app.width/10
    app.SOLEScrEntryTBY0 = 0.27*app.height
    app.SOLEScrEntryTBX1 = app.width/2-app.SOLEScrEntryTBX0
    app.SOLEScrEntryTBY1 = app.SOLEScrEntryTBY0 + (app.SOLEScrEntryTBX1 - app.SOLEScrEntryTBX0) # square
    app.SOLEScrEntryTBWidth = app.SOLEScrEntryTBX1 - app.SOLEScrEntryTBX0
    app.SOLEScrEntryTBHeight = app.SOLEScrEntryTBY1 - app.SOLEScrEntryTBY0
    app.SOLEScrEntryTBRows = int(app.textBoxes[4][0][0].text)
    app.SOLEScrEntryTBCols = int(app.textBoxes[4][0][1].text)+1
    app.SOLEScrEntryFontSize = min((app.SOLEScrEntryTBHeight)/(2*app.SOLEScrEntryTBRows),
    (app.SOLEScrEntryTBWidth)/(2*app.SOLEScrEntryTBCols))
    app.textBoxes[4].append(AMEntryTextBox( app.SOLEScrEntryTBRows, app.SOLEScrEntryTBCols, 
    app.width/2 - app.SOLEScrEntryTBWidth/2, app.SOLEScrEntryTBY0, 
    app.width/2 + app.SOLEScrEntryTBWidth/2, app.SOLEScrEntryTBY1, 
    'peach puff', 'tan4', app.SOLEScrEntryFontSize, app))

    # *** SOLE RESULT SCREEN ***
    # SOLE Result State (0 - No soln; 1 - Unique soln; 2 - infinite solns)
    app.SOLEResultState = None

    app.SOLEResultX0 = app.width/5
    app.SOLEResultY0 = app.height/4
    app.SOLEResultX1 = app.width - app.SOLEResultX0
    app.SOLEResultY1 = app.SOLEResultY0 + (1/3)*app.width
    app.SOLEResultMatrix = create2DList(app.SOLEScrEntryTBRows, app.SOLEScrEntryTBCols)
    app.SOLEResult = OutputMatrix(app.SOLEResultMatrix, app.SOLEResultX0, app.SOLEResultY0, 
    app.SOLEResultX1, app.SOLEResultY1, 'peach puff', 'tan4', app.SOLEScrEntryFontSize, app)

    # *** SOLE STEPS SCREEN ***
    app.SOLESteps = []

# Determinant screen and its sub-screens initializations
def detScreenInit(app):
    # *** DET SCREEN ***
    # text box margins
    app.detMargin = app.width/2.5
    # font sizes
    app.detScrTitleSize = int(app.height/20)
    # Text Box Dims
    # i) dimension text box (only 1 as square matrix required)
    app.detScrDimTBWidth = 0.05*app.width
    app.detScrDimTBHeight = app.detScrDimTBWidth
    # app.detScrDimTBSep = (app.width-2*app.detMargin-2*app.detScrDimTBWidth)
    app.textBoxes[5][0].append(DimTextBox(int( app.width/2 - app.detScrDimTBWidth/2 ),
        0.11*app.height, 
        app.detScrDimTBWidth, app.detScrDimTBHeight, 
        'peach puff', 'tan4', app.detScrDimTBHeight/2, app))
    # ii) entry text boxes
    app.detScrEntryTBX0 = app.width/10
    app.detScrEntryTBY0 = 0.27*app.height
    app.detScrEntryTBX1 = app.width/2-app.detScrEntryTBX0
    app.detScrEntryTBY1 = app.detScrEntryTBY0 + (app.detScrEntryTBX1 - app.detScrEntryTBX0) # square
    app.detScrEntryTBWidth = app.detScrEntryTBX1 - app.detScrEntryTBX0
    app.detScrEntryTBHeight = app.detScrEntryTBY1 - app.detScrEntryTBY0
    app.detScrEntryTBRows, app.detScrEntryTBCols = int(app.textBoxes[5][0][0].text), int(app.textBoxes[5][0][0].text)
    app.detScrEntryFontSize = min((app.detScrEntryTBHeight)/(2*app.detScrEntryTBRows),
    (app.detScrEntryTBWidth)/(2*app.detScrEntryTBCols))
    app.textBoxes[5].append(MatrixEntry( app.detScrEntryTBRows, app.detScrEntryTBCols, 
    app.width/2 - app.detScrEntryTBWidth/2, app.detScrEntryTBY0, 
    app.width/2 + app.detScrEntryTBWidth/2, app.detScrEntryTBY1, 
    'peach puff', 'tan4', app.detScrEntryFontSize, app))

    # *** GE RESULT SCREEN ***
    app.detResultX0 = app.width/3
    app.detResultY0 = app.height/5
    app.detResultX1 = app.width - app.detResultX0
    app.detResultY1 = app.detResultY0 + (app.detResultX1 - app.detResultX0)
    app.detResultMatrix = create2DList(app.detScrEntryTBRows, app.detScrEntryTBCols)
    app.detResult = OutputMatrix(app.detResultMatrix, app.detResultX0, app.detResultY0, 
    app.detResultX1, app.detResultY1, 'peach puff', 'tan4', app.detScrEntryFontSize, app)

    # *** GE STEPS SCREEN ***
    app.detSteps = [] 

# *****************************************************************
# ********************* KEYPRESSED FUNCTIONS **********************
# *****************************************************************

# Addition screen keyPressed function
def matAddKeyPressed(app, event):
    for i in range(len(app.textBoxes[0][0])):
        if app.textBoxes[0][0][i].keyPressed(app, event.key):
            if app.textBoxes[0][0][0].text != '':
                app.addScrEntryTBRows = int(app.textBoxes[0][0][0].text)
                app.addScrEntryFontSize = min((app.addScrEntryTBY1-app.addScrEntryTBY0)/(2*app.addScrEntryTBRows),
                (app.addScrEntryTBX1-app.addScrEntryTBX0)/(2*app.addScrEntryTBCols))
            if app.textBoxes[0][0][1].text != '':
                app.addScrEntryTBCols = int(app.textBoxes[0][0][1].text)
                app.addScrEntryFontSize = min((app.addScrEntryTBY1-app.addScrEntryTBY0)/(2*app.addScrEntryTBRows),
                (app.addScrEntryTBX1-app.addScrEntryTBX0)/(2*app.addScrEntryTBCols))
            app.textBoxes[0][1] = MatrixEntry( app.addScrEntryTBRows, app.addScrEntryTBCols, 
                app.addScrEntryTBX0, app.addScrEntryTBY0, 
                app.addScrEntryTBX1, app.addScrEntryTBY1, 
                'peach puff', 'tan4', app.addScrEntryFontSize, app)
            app.textBoxes[0][2] = MatrixEntry( app.addScrEntryTBRows, app.addScrEntryTBCols, 
                app.addScrEntryTBX0 + app.width/2, app.addScrEntryTBY0, 
                app.addScrEntryTBX1 + app.width/2, app.addScrEntryTBY1, 
                'peach puff', 'tan4', app.addScrEntryFontSize, app)
            app.addResultMatrix = create2DList(app.addScrEntryTBRows, app.addScrEntryTBCols)
    for i in range(1, len(app.textBoxes[0])):
        app.textBoxes[0][i].keyPressed(app, event.key)

# Multiplication screen keyPressed function
def matMulKeyPressed(app, event):
    for i in range(len(app.textBoxes[1][0])):
        if app.textBoxes[1][0][i].keyPressed(app, event.key):
            if app.textBoxes[1][0][0].text != '':
                app.mulScrEntryTB1Rows = int(app.textBoxes[1][0][0].text)
                app.mulScrEntry1FontSize = min((app.mulScrEntryTBHeight)/(2*app.mulScrEntryTB1Rows),
                (app.mulScrEntryTBWidth)/(2*app.mulScrEntryTB1Cols))
            if app.textBoxes[1][0][1].text != '':
                app.mulScrEntryTB1Cols = int(app.textBoxes[1][0][1].text)
                app.mulScrEntry1FontSize = min((app.mulScrEntryTBHeight)/(2*app.mulScrEntryTB1Rows),
                (app.mulScrEntryTBWidth)/(2*app.mulScrEntryTB1Cols))
            app.textBoxes[1][2] = MatrixEntry( app.mulScrEntryTB1Rows, app.mulScrEntryTB1Cols, 
                app.mulScrEntryTBX0, app.mulScrEntryTBY0, 
                app.mulScrEntryTBX1, app.mulScrEntryTBY1, 
                'peach puff', 'tan4', app.mulScrEntry1FontSize, app)
    for i in range(len(app.textBoxes[1][1])):
        if app.textBoxes[1][1][i].keyPressed(app, event.key):
            if app.textBoxes[1][1][0].text != '':
                app.mulScrEntryTB2Rows = int(app.textBoxes[1][1][0].text)
                app.mulScrEntry2FontSize = min((app.mulScrEntryTBHeight)/(2*app.mulScrEntryTB2Rows),
                (app.mulScrEntryTBWidth)/(2*app.mulScrEntryTB2Cols))
            if app.textBoxes[1][1][1].text != '':
                app.mulScrEntryTB2Cols = int(app.textBoxes[1][1][1].text)
                app.mulScrEntry2FontSize = min((app.mulScrEntryTBHeight)/(2*app.mulScrEntryTB2Rows),
                (app.mulScrEntryTBWidth)/(2*app.mulScrEntryTB2Cols))
            app.textBoxes[1][3] = MatrixEntry( app.mulScrEntryTB2Rows, app.mulScrEntryTB2Cols, 
                app.mulScrEntryTBX0 + app.width/2, app.mulScrEntryTBY0, 
                app.mulScrEntryTBX1 + app.width/2, app.mulScrEntryTBY1, 
                'peach puff', 'tan4', app.mulScrEntry2FontSize, app)
            # app.mulResultMatrix = create2DList(app.addScrEntryTBRows, app.addScrEntryTBCols)
    for i in range(2, len(app.textBoxes[1])):
        app.textBoxes[1][i].keyPressed(app, event.key)

# Transpose screen keyPressed function
def matTposeKeyPressed(app, event):
    for i in range(len(app.textBoxes[2][0])):
        if app.textBoxes[2][0][i].keyPressed(app, event.key):
            if app.textBoxes[2][0][0].text != '':
                app.tposeScrEntryTBRows = int(app.textBoxes[2][0][0].text)
                app.tposeScrEntryFontSize = min((app.tposeScrEntryTBHeight)/(2*app.tposeScrEntryTBRows),
                (app.tposeScrEntryTBWidth)/(2*app.tposeScrEntryTBCols))
            if app.textBoxes[2][0][1].text != '':
                app.tposeScrEntryTBCols = int(app.textBoxes[2][0][1].text)
                app.tposeScrEntryFontSize = min((app.tposeScrEntryTBHeight)/(2*app.tposeScrEntryTBRows),
                (app.tposeScrEntryTBWidth)/(2*app.tposeScrEntryTBCols))
            app.textBoxes[2][1] = MatrixEntry( app.tposeScrEntryTBRows, app.tposeScrEntryTBCols, 
                    app.width/2 - app.tposeScrEntryTBWidth/2, app.tposeScrEntryTBY0, 
                    app.width/2 + app.tposeScrEntryTBWidth/2, app.tposeScrEntryTBY1, 
                    'peach puff', 'tan4', app.tposeScrEntryFontSize, app)
            app.tposeResultMatrix = create2DList(app.tposeScrEntryTBRows, app.tposeScrEntryTBCols)
    app.textBoxes[2][1].keyPressed(app, event.key)

# Gaussian Elimination screen keyPressed function
def GEKeyPressed(app, event):
    for i in range(len(app.textBoxes[3][0])):
        if app.textBoxes[3][0][i].keyPressed(app, event.key):
            if app.textBoxes[3][0][0].text != '':
                app.GEScrEntryTBRows = int(app.textBoxes[3][0][0].text)
                app.GEScrEntryFontSize = min((app.GEScrEntryTBHeight)/(2*app.GEScrEntryTBRows),
                (app.GEScrEntryTBWidth)/(2*app.GEScrEntryTBCols))
            if app.textBoxes[3][0][1].text != '':
                app.GEScrEntryTBCols = int(app.textBoxes[3][0][1].text)
                app.GEScrEntryFontSize = min((app.GEScrEntryTBHeight)/(2*app.GEScrEntryTBRows),
                (app.GEScrEntryTBWidth)/(2*app.GEScrEntryTBCols))
            app.textBoxes[3][1] = MatrixEntry( app.GEScrEntryTBRows, app.GEScrEntryTBCols, 
                    app.width/2 - app.GEScrEntryTBWidth/2, app.GEScrEntryTBY0, 
                    app.width/2 + app.GEScrEntryTBWidth/2, app.GEScrEntryTBY1, 
                    'peach puff', 'tan4', app.GEScrEntryFontSize, app)
            app.GEResultMatrix = create2DList(app.GEScrEntryTBRows, app.GEScrEntryTBCols)
    app.textBoxes[3][1].keyPressed(app, event.key)

# SOLE screen keyPressed function
def SOLEKeyPressed(app, event):
    for i in range(len(app.textBoxes[4][0])):
        if app.textBoxes[4][0][i].keyPressed(app, event.key):
            if app.textBoxes[4][0][0].text != '':
                app.SOLEScrEntryTBRows = int(app.textBoxes[4][0][0].text)
                app.SOLEScrEntryFontSize = min((app.SOLEScrEntryTBHeight)/(2*app.SOLEScrEntryTBRows),
                (app.SOLEScrEntryTBWidth)/(2*app.SOLEScrEntryTBCols))
            if app.textBoxes[4][0][1].text != '':
                app.SOLEScrEntryTBCols = int(app.textBoxes[4][0][1].text)+1
                app.SOLEScrEntryFontSize = min((app.SOLEScrEntryTBHeight)/(2*app.SOLEScrEntryTBRows),
                (app.SOLEScrEntryTBWidth)/(2*app.SOLEScrEntryTBCols))
            app.textBoxes[4][1] = AMEntryTextBox( app.SOLEScrEntryTBRows, app.SOLEScrEntryTBCols, 
                    app.width/2 - app.SOLEScrEntryTBWidth/2, app.SOLEScrEntryTBY0, 
                    app.width/2 + app.SOLEScrEntryTBWidth/2, app.SOLEScrEntryTBY1, 
                    'peach puff', 'tan4', app.SOLEScrEntryFontSize, app)
            app.SOLEResultMatrix = create2DList(app.SOLEScrEntryTBRows, app.SOLEScrEntryTBCols)
    app.textBoxes[4][1].keyPressed(app, event.key)

# Scrolling keyPressed
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

# Matrix addition mousePressed
def matAddMousePressed(app, event):
    if app.backButton.mousePressed(app, event.x, event.y):
        app.screen = 'matCal'
    for i in range(len(app.textBoxes[0][0])):
        app.textBoxes[0][0][i].mousePressed(app, event.x, event.y)
    app.textBoxes[0][1].mousePressed(app, event.x, event.y)
    app.textBoxes[0][2].mousePressed(app, event.x, event.y)

    # Solving here
    if app.solveButton.mousePressed(app, event.x, event.y) and \
        app.textBoxes[0][1].isFilled() and app.textBoxes[0][2].isFilled():
        app.addResultMatrix = create2DList(app.addScrEntryTBRows, app.addScrEntryTBCols)  # clears result list
        for i in range(app.addScrEntryTBRows):
            for j in range(app.addScrEntryTBCols):
                app.addResultMatrix[i][j] += float(app.textBoxes[0][1].text[i][j]) + float(app.textBoxes[0][2].text[i][j])
        app.addResult = OutputMatrix(app.addResultMatrix, app.addResultX0, app.addResultY0, 
                app.addResultX1, app.addResultY1, 'peach puff', 'tan4', app.addScrEntryFontSize/2, app)
        app.screen = 'matAddResult'
    
    # Clearing here
    if app.clearButton.mousePressed(app, event.x, event.y):
        app.textBoxes[0][1].clear()
        app.textBoxes[0][2].clear()

# Matrix multiplication mousePressed
def matMulMousePressed(app, event):
    if app.backButton.mousePressed(app, event.x, event.y):
        app.screen = 'matCal'
    for i in range(len(app.textBoxes[1][0])):
        app.textBoxes[1][0][i].mousePressed(app, event.x, event.y)
        app.textBoxes[1][1][i].mousePressed(app, event.x, event.y)
    app.textBoxes[1][2].mousePressed(app, event.x, event.y)
    app.textBoxes[1][3].mousePressed(app, event.x, event.y)

    # Solving here
    if app.solveButton.mousePressed(app, event.x, event.y)\
        and app.textBoxes[1][2].isFilled() and app.textBoxes[1][3].isFilled() \
        and app.textBoxes[1][0][1].text == app.textBoxes[1][1][0].text: # dim check
        M1, M2 = app.textBoxes[1][2].matrix(), app.textBoxes[1][3].matrix()
        # M1, M2 = [[1, 7, 4, 2], [2, 3, 3, 3], [2, 8, 5, 3]], [[1, 3, 0], [4, 2, 1], [3, 7, 5], [2, 4, 4]]
        app.mulResultMatrix, app.mulSteps = matMulWithSteps(M1, M2)
        app.mulResult = OutputMatrix(app.mulResultMatrix, app.mulResultX0, app.mulResultY0, 
        app.mulResultX1, app.mulResultY1, 'peach puff', 'tan4', 
        min(app.mulScrEntry1FontSize,app.mulScrEntry2FontSize)/2, app)
        app.screen = 'matMulResult'

    # Clearing here
    if app.clearButton.mousePressed(app, event.x, event.y):
        app.textBoxes[1][2].clear()
        app.textBoxes[1][3].clear()

# Transpose mousePressed
def tposeMousePressed(app, event):
    if app.backButton.mousePressed(app, event.x, event.y):
        app.screen = 'matCal'
    for i in range(len(app.textBoxes[2][0])):
        app.textBoxes[2][0][i].mousePressed(app, event.x, event.y)
    app.textBoxes[2][1].mousePressed(app, event.x, event.y)

    # Solving here
    if app.solveButton.mousePressed(app, event.x, event.y)\
    and app.textBoxes[2][1].isFilled():
        M = app.textBoxes[2][1].matrix()
        # M = [[1, 3, 0], [4, 2, 1], [3, 7, 5], [2, 4, 4]]
        app.tposeResultMatrix = matTpose(M)
        app.tposeResult = OutputMatrix(app.tposeResultMatrix, app.tposeResultX0, app.tposeResultY0, 
                app.tposeResultX1, app.tposeResultY1, 'peach puff', 'tan4', app.tposeScrEntryFontSize/2, app)
        app.screen = 'matTposeResult'
    
    # Clearing here
    if app.clearButton.mousePressed(app, event.x, event.y):
        app.textBoxes[2][1].clear()

# Gaussian Elimination mousePressed
def GEMousePressed(app, event):
    for i in range(len(app.textBoxes[3][0])):
        app.textBoxes[3][0][i].mousePressed(app, event.x, event.y)
    app.textBoxes[3][1].mousePressed(app, event.x, event.y)

    # Solving here
    if app.solveButton.mousePressed(app, event.x, event.y)\
    and app.textBoxes[3][1].isFilled():
        M = app.textBoxes[3][1].matrix()
        # M = [[1, -5, 3], [7, 0, -9], [-1, 0, 3]]
        app.GEResultMatrix, app.GESteps = GEWithSteps(M)
        app.GEResult = OutputMatrix(app.GEResultMatrix, app.GEResultX0, app.GEResultY0, 
                app.GEResultX1, app.GEResultY1, 'peach puff', 'tan4', app.GEScrEntryFontSize/2, app)
        app.screen = 'GEResult'

    # Clearing here
    if app.clearButton.mousePressed(app, event.x, event.y):
        app.textBoxes[3][1].clear()

# SOLE mousePressed
def SOLEMousePressed(app, event):
    for i in range(len(app.textBoxes[4][0])):
        app.textBoxes[4][0][i].mousePressed(app, event.x, event.y)
    app.textBoxes[4][1].mousePressed(app, event.x, event.y)

    # Solving here
    if app.solveButton.mousePressed(app, event.x, event.y) \
    and app.textBoxes[4][1].isFilled():
        M = app.textBoxes[4][1].matrix()

        # M = [[1, -5, 3], [7, 0, -9], [-1, 0, 3]]  # no solutions
        # M = [[1, -5, 3, -4], [7, 0, -9, 3], [-1, 0, 3, -2]] # unique solution
        # infinite solutions M below
        # M = \
        # [[3, 2, 3, 4, 2, 2, 7, 2],
        # [1, 2, 7, 6, 4, 5, 2, 3],
        # [4, 2, 2, 3, 2, 4, 6, 1],
        # [4, 5, 6, 2, 3, 1, 4, 0]]

        # check if matrix has solutions based on result state
        app.SOLEResultState, app.SOLEResultMatrix, app.SOLESteps = SOLEWithSteps(M)
        header = []  # contains headers labelling each col of output with respective value
        if app.SOLEResultState == 0:    # No solutions
            for i in range(len(app.SOLEResultMatrix[0])-1):
                header.append(f'a{i+1}')
            header.append('c')
            app.SOLEResultMatrix.insert(0, header)
        elif app.SOLEResultState == 1:  # Unique solution
            for i in range(len(app.SOLEResultMatrix)):
                header.append(f'x{i+1}')
            app.SOLEResultMatrix=[header, app.SOLEResultMatrix]
        else:   # Infinite solutions
            for i in range(len(app.SOLEResultMatrix[0])):
                header.append(f'x{i+1}')
            app.SOLEResultMatrix.insert(0, header)
            for i in range(0, len(app.SOLEResultMatrix)):
                if i == 0:
                    app.SOLEResultMatrix[i].insert(0, '')
                else:
                    app.SOLEResultMatrix[i].insert(0, f't{i}')
        app.SOLEResult = OutputMatrix(app.SOLEResultMatrix, app.SOLEResultX0, app.SOLEResultY0, 
                    app.SOLEResultX1, app.SOLEResultY1, 'peach puff', 'tan4', app.SOLEScrEntryFontSize/2, app)
        app.screen = 'SOLEResult'

    # Clearing here
    if app.clearButton.mousePressed(app, event.x, event.y):
        app.textBoxes[4][1].clear()

# *****************************************************************
# ******************** REDRAW BUTTON FUNCTIONS ********************
# *****************************************************************

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

def drawSolveButton(app, canvas):
    app.solveButton.redraw(app, canvas)

def drawClearButton(app, canvas):
    app.clearButton.redraw(app, canvas)

def drawStepsButton(app, canvas):
    app.stepsButton.redraw(app, canvas)

# *****************************************************************
# ******************** REDRAW SCREEN FUNCTIONS ********************
# *****************************************************************

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

def redrawMatCalScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    canvas.create_text(app.width/2, 0.25*app.height, text="General Matrix\nCalculator",
    fill='tan4', font=f'Century {app.calScrTitleSize} bold', justify=CENTER)

    for i in range(len(app.buttons[1])):
        app.buttons[1][i].redraw(app, canvas)

def redrawMatAddScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    drawSolveButton(app, canvas)
    drawClearButton(app, canvas)
    canvas.create_text(app.width/2, 0.05*app.height, text="Matrix Addition",
    fill='tan4', font=f'Century {app.addScrTitleSize} bold', justify=CENTER)
    
    for i in range(len(app.textBoxes[0][0])):
        app.textBoxes[0][0][i].redraw(app, canvas)
    
    canvas.create_text(app.matAddMargin + 0.5*app.addScrDimTBWidth,
         0.22*app.height, text='rows', fill='tan4', font=f'Century {int(app.addScrTitleSize/2)}', justify=CENTER)
    canvas.create_text(int( app.matAddMargin + 1.5*app.addScrDimTBWidth + app.addScrDimTBSep) ,
         0.22*app.height, text='columns', fill='tan4', font=f'Century {int(app.addScrTitleSize/2)}', justify=CENTER)
    
    app.textBoxes[0][1].redraw(app, canvas)
    app.textBoxes[0][2].redraw(app, canvas)

    canvas.create_text(app.width/2, app.height/2, text="+",
    fill='tan4', font=f'Century {app.addScrTitleSize*3} bold', justify=CENTER)

def redrawMatAddResultScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    canvas.create_text(app.width/2, 0.1*app.height, text="Matrix Addition\nResult:",
    fill='tan4', font=f'Century {app.addScrTitleSize} bold', justify=CENTER)
    app.addResult.redraw(app, canvas)

def redrawMatMulScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    drawSolveButton(app, canvas)
    drawClearButton(app, canvas)
    canvas.create_text(app.width/2, 0.05*app.height, text="Matrix Multiplication",
    fill='tan4', font=f'Century {app.mulScrTitleSize} bold', justify=CENTER)

    for i in range(len(app.textBoxes[0][0])):
        app.textBoxes[1][0][i].redraw(app, canvas)
        app.textBoxes[1][1][i].redraw(app, canvas)
        canvas.create_text(int(app.matMulMargin/2 + app.mulScrDimTBWidth/2 + i*app.width/2),
         0.22*app.height, text='rows', fill='tan4', font=f'Century {int(app.addScrTitleSize/2)}', justify=CENTER)
        canvas.create_text(int(app.matMulMargin/2 + app.mulScrDimTBWidth + app.mulScrDimTBSep + app.mulScrDimTBWidth/2 + i*app.width/2),
         0.22*app.height, text='columns', fill='tan4', font=f'Century {int(app.addScrTitleSize/2)}', justify=CENTER)
    
    app.textBoxes[1][2].redraw(app, canvas)
    app.textBoxes[1][3].redraw(app, canvas)

    canvas.create_text(app.width/2, app.height/2, text="×",
    fill='tan4', font=f'Century {app.addScrTitleSize*3} bold', justify=CENTER)

def redrawMatMulResultScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    canvas.create_text(app.width/2, 0.1*app.height, text="Matrix Multiplication\nResult:",
    fill='tan4', font=f'Century {app.mulScrTitleSize} bold', justify=CENTER)
    app.mulResult.redraw(app, canvas)
    drawStepsButton(app, canvas)

def redrawMatMulStepsScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    canvas.create_text(app.width/2, 0.1*app.height + app.scrollY, text="Matrix Multiplication\nResult:",
    fill='tan4', font=f'Century {app.mulScrTitleSize} bold', justify=CENTER)

    for i in range(len(app.mulSteps)-1):
        canvas.create_text(app.width/2, 0.3*app.height + i*0.15*app.height + app.scrollY, text=f'{app.mulSteps[i]}',
    fill='tan4', font=f'Century {int(app.mulScrTitleSize/2)}', justify=CENTER)
    canvas.create_text(app.width/2, 0.3*app.height + (i+1)*0.15*app.height + app.scrollY, text=f'{app.mulSteps[-1]}',
    fill='tan4', font=f'Century {int(app.mulScrTitleSize/2)} bold', justify=CENTER)

def redrawMatTposeScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    drawSolveButton(app, canvas)
    drawClearButton(app, canvas)
    canvas.create_text(app.width/2, 0.05*app.height, text="Obtain Transpose",
    fill='tan4', font=f'Century {app.tposeScrTitleSize} bold', justify=CENTER)

    for i in range(len(app.textBoxes[2][0])):
        app.textBoxes[2][0][i].redraw(app, canvas)
    
    canvas.create_text(app.tposeMargin + 0.5*app.tposeScrDimTBWidth,
         0.22*app.height, text='rows', fill='tan4', font=f'Century {int(app.tposeScrTitleSize/2)}', justify=CENTER)
    canvas.create_text(int( app.tposeMargin + 1.5*app.tposeScrDimTBWidth + app.tposeScrDimTBSep) ,
         0.22*app.height, text='columns', fill='tan4', font=f'Century {int(app.tposeScrTitleSize/2)}', justify=CENTER)
    
    app.textBoxes[2][1].redraw(app, canvas)

def redrawMatTposeResultScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    canvas.create_text(app.width/2, 0.1*app.height, text="Obtain Transpose\nResult:",
    fill='tan4', font=f'Century {app.tposeScrTitleSize} bold', justify=CENTER)
    app.tposeResult.redraw(app, canvas)


def redrawGEScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawSolveButton(app, canvas)
    drawClearButton(app, canvas)
    canvas.create_text(app.width/2, 0.05*app.height, text="Gaussian Elimination",
    fill='tan4', font=f'Century {app.GEScrTitleSize} bold', justify=CENTER)

    for i in range(len(app.textBoxes[3][0])):
        app.textBoxes[3][0][i].redraw(app, canvas)

    canvas.create_text(app.GEMargin + 0.5*app.GEScrDimTBWidth,
         0.22*app.height, text='rows', fill='tan4', font=f'Century {int(app.GEScrTitleSize/2)}', justify=CENTER)
    canvas.create_text(int( app.GEMargin + 1.5*app.GEScrDimTBWidth + app.GEScrDimTBSep) ,
         0.22*app.height, text='columns', fill='tan4', font=f'Century {int(app.GEScrTitleSize/2)}', justify=CENTER)

    app.textBoxes[3][1].redraw(app, canvas)

def redrawGEResultScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    canvas.create_text(app.width/2, 0.1*app.height, text="Gaussian Elimination\nResult:",
    fill='tan4', font=f'Century {app.GEScrTitleSize} bold', justify=CENTER)
    app.GEResult.redraw(app, canvas)
    drawStepsButton(app, canvas)

def redrawGEStepsScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    canvas.create_text(app.width/2, 0.1*app.height + app.scrollY, text="Gaussian Elimination\nResult:",
    fill='tan4', font=f'Century {app.GEScrTitleSize} bold', justify=CENTER)

    canvas.create_text(app.width/2, 0.3*app.height + app.scrollY, text=f'{app.GESteps[0]}',
    fill='tan4', font=f'Century {int(app.GEScrTitleSize/2)} bold', justify=CENTER)
    for i in range(1, len(app.GESteps)-1):
        canvas.create_text(app.width/2, 0.3*app.height + i*app.GEScrEntryTBRows/13*app.height + app.scrollY, text=f'{app.GESteps[i]}',
    fill='tan4', font=f'Century {int(app.GEScrTitleSize/2)}', justify=CENTER)
    if len(app.GESteps) > 2:
        canvas.create_text(app.width/2, 0.3*app.height + (i+1)*app.GEScrEntryTBRows/13*app.height + app.scrollY, text=f'{app.GESteps[-1]}',
        fill='tan4', font=f'Century {int(app.GEScrTitleSize/2)} bold', justify=CENTER)
    
def redrawSOLEScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawSolveButton(app, canvas)
    drawClearButton(app, canvas)
    canvas.create_text(app.width/2, 0.05*app.height, text="Systems of Linear Equations",
    fill='tan4', font=f'Century {app.SOLEScrTitleSize} bold', justify=CENTER)

    for i in range(len(app.textBoxes[4][0])):
        app.textBoxes[4][0][i].redraw(app, canvas)

    canvas.create_text(app.SOLEMargin + 0.5*app.SOLEScrDimTBWidth,
         0.22*app.height, text='rows', fill='tan4', font=f'Century {int(app.SOLEScrTitleSize/2)}', justify=CENTER)
    canvas.create_text(int( app.SOLEMargin + 1.5*app.SOLEScrDimTBWidth + app.SOLEScrDimTBSep) ,
         0.22*app.height, text='columns', fill='tan4', font=f'Century {int(app.SOLEScrTitleSize/2)}', justify=CENTER)

    app.textBoxes[4][1].redraw(app, canvas)

def redrawSOLEResultScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    canvas.create_text(app.width/2, 0.1*app.height, text="System of Linear Equations\nResult:",
    fill='tan4', font=f'Century {app.SOLEScrTitleSize} bold', justify=CENTER)
    app.SOLEResult.redraw(app, canvas)
    drawStepsButton(app, canvas)
    drawBackButton(app, canvas)

    if app.SOLEResultState == 0:
        canvas.create_text(app.width/2, 0.22*app.height, text="No solution. See REF matrix below:",
    fill='tan4', font=f'Century {int(app.SOLEScrTitleSize/1.5)} bold', justify=CENTER)
    elif app.SOLEResultState == 1:
        canvas.create_text(app.width/2, 0.22*app.height, text="Unique solution",
    fill='tan4', font=f'Century {int(app.SOLEScrTitleSize/1.5)} bold', justify=CENTER)
    else:
        canvas.create_text(app.width/2, 0.22*app.height, text="Special solutions",
    fill='tan4', font=f'Century {int(app.SOLEScrTitleSize/1.5)} bold', justify=CENTER)


def redrawSOLEStepsScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    canvas.create_text(app.width/2, 0.1*app.height, text="System of Linear Equations\nResult:",
    fill='tan4', font=f'Century {app.SOLEScrTitleSize} bold', justify=CENTER)

    if app.SOLEResultState == 0:
        for i in range(0, len(app.SOLESteps)-1):
            canvas.create_text(app.width/2, 0.3*app.height + i*app.SOLEScrEntryTBRows/15*app.height + app.scrollY, text=f'{app.SOLESteps[i]}',
            fill='tan4', font=f'Century {int(app.SOLEScrTitleSize/2)}', justify=CENTER)
        # if len(app.SOLESteps) > 2:
        canvas.create_text(app.width/2, 0.3*app.height + (i+1)*app.SOLEScrEntryTBRows/15*app.height + app.scrollY, text=f'{app.SOLESteps[-1]}',
            fill='tan4', font=f'Century {int(app.SOLEScrTitleSize/2)} bold', justify=CENTER)
    
    else:
        for i in range(0, len(app.SOLESteps)-(len(app.SOLEResultMatrix)-1)):
            canvas.create_text(app.width/2, 0.3*app.height + i*(app.SOLEScrEntryTBRows/15*app.height + 60) + app.scrollY, text=f'{app.SOLESteps[i]}',
            fill='tan4', font=f'Century {int(app.SOLEScrTitleSize/2)}', justify=CENTER)
        for j in range(len(app.SOLESteps)-(len(app.SOLEResultMatrix)-1), len(app.SOLESteps)):
            canvas.create_text(app.width/2, 
            0.3*app.height + (i+1)*(app.SOLEScrEntryTBRows/15*app.height + 60) + (j-(len(app.SOLESteps)-(len(app.SOLEResultMatrix)-1)))*(app.SOLEScrEntryTBRows/15*app.height + 10) + app.scrollY, 
            text=f'{app.SOLESteps[j]}',
            fill='tan4', font=f'Century {int(app.SOLEScrTitleSize/2)} bold', justify=CENTER)
    
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