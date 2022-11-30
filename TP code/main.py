from matrix_utils import *
from matrix_GE import *
from matrix_SOLE import *

from cmu_112_graphics import *
from animation_classes import *
from animation_helpers import *

def appStarted(app):
    fitToScreen(app)
    app.screens = [ ['matCal',
     ['matAdd', 'matAddResult'],
     ['matMul', 'matMulResult', 'matMulSteps'], 
     ['matTpose', 'matTposeResult']], 
    ['GE', 'GEResult', 'GESteps'], 
    ['SOLE', 'SOLEResult', 'SOLESteps'], 
    ['LU'], ['inverse'], ['4FS'], ['det'], ['GS'],
    ['home'] ]
    app.screen = app.screens[-1][0]

    # scrolling
    app.scrollY = 0
    app.scrollKeys = {'Up': 5, 'Down': -5}

    # app.buttons indices:
    # 0: home, 1: calc, 2: add, 3: mult, 4: tpose
    app.buttons = [[],[],[],[],[],[],[]]

    # app.textBoxes indices:
    # 0: add, 1: mult, 2: tpose, 3: GE
    # innermost list stores dimension Text Boxes
    app.textBoxes = [[[]], [[],[]], [[]], [[]]]

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
        app.buttons[0].append(button(int( app.homeMargin + (i%4)*(app.homeScrButtonWidth + app.homeMargin/4) ),
                                0.5*app.height + (i//4)*(app.homeMargin/4 + app.homeScrButtonHeight),
                                app.homeScrButtonWidth, app.homeScrButtonHeight,
                                'tan4', app.homeButtonsText[i][0], app.homeButtonsText[i][1], '', ''))
    
    # *** KEYS AND KEYBINDINGS ***
    app.numKeys = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
    
    # *** BACK HOME BUTTON ***
    app.backHomeButtonMargin = 10
    app.backHomeButtonWidth = 0.1*app.width
    app.backHomeButtonHeight = 0.05*app.height
    app.backHomeButtonsTextSize = int(app.height/70)
    app.backHomeButton = button(app.backHomeButtonMargin, app.backHomeButtonMargin, 
                    app.backHomeButtonWidth, app.backHomeButtonHeight, 'tan4', 
                    '241-for-One', app.backHomeButtonsTextSize, '', '')

    # *** GO BACK BUTTON ***
    app.backButtonMargin = 10
    app.backButtonWidth = 0.1*app.width
    app.backButtonHeight = 0.05*app.height
    app.backButtonsTextSize = int(app.height/70)
    app.backButton = button(2*app.backButtonMargin + app.backHomeButtonWidth, app.backButtonMargin, 
                    app.backButtonWidth, app.backButtonHeight, 'tan4', 
                    'Back', app.backButtonsTextSize, '', '')

    # *** SOLVE BUTTON ***
    app.solveButtonMargin = app.width/3
    app.solveButtonWidth = (0.75*app.width-0.2*app.solveButtonMargin)/6
    app.solveButtonHeight = 0.4*app.solveButtonWidth
    app.solveButtonTextSize = int(app.height/50)
    app.solveButton = button(app.solveButtonMargin, 0.8*app.height,
                                app.solveButtonWidth, app.solveButtonHeight,
                                'tan4', 'Solve', app.solveButtonTextSize, '', '')

    # *** CLEAR ENTRIES BUTTON ***
    app.clearButtonMargin = app.width/3
    app.clearButtonWidth = (0.75*app.width-0.2*app.clearButtonMargin)/6
    app.clearButtonHeight = 0.4*app.clearButtonWidth
    app.clearButtonTextSize = int(app.height/50)
    app.clearButtonSep = (app.width-2*app.clearButtonMargin-2*app.clearButtonWidth)
    app.clearButton = button(app.solveButtonMargin + app.solveButtonWidth + app.clearButtonSep,
                                 0.8*app.height,
                                app.clearButtonWidth, app.clearButtonHeight,
                                'tan4', 'Clear', app.clearButtonTextSize, '', '')

    # *** SHOW STEPS BUTTON ***
    app.stepsButtonWidth = app.width/10
    app.stepsButtonHeight = 0.4*app.stepsButtonWidth
    app.stepsButtonTextSize = int(app.height/50)
    app.stepsButton = button(app.width/2 - app.stepsButtonWidth/2, 0.8*app.height,
                                app.stepsButtonWidth, app.stepsButtonHeight,
                                'tan4', 'Show steps', app.stepsButtonTextSize, '', '')

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
    for i in range(len(app.calButtonsText)):
        app.buttons[1].append(button(int( app.calMargin + i*(app.calScrButtonWidth + app.calScrButtonSep) ),
                                0.5*app.height,
                                app.calScrButtonWidth, app.calScrButtonHeight,
                                'tan4', app.calButtonsText[i][0], app.calButtonsText[i][1], '', ''))

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
    app.textBoxes[2].append(MatrixEntry( app.GEScrEntryTBRows, app.GEScrEntryTBCols, 
    app.width/2 - app.GEScrEntryTBWidth/2, app.GEScrEntryTBY0, 
    app.width/2 + app.GEScrEntryTBWidth/2, app.GEScrEntryTBY1, 
    'peach puff', 'tan4', app.GEScrEntryFontSize, app))

def keyPressed(app, event):
    # *** MATRIX ADDITION SCREEN ***
    if app.screen == 'matAdd':
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
    
    elif app.screen == 'matMul':
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
    
    elif app.screen == 'matTpose':
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
                app.tposeResultMatrix = create2DList(app.addScrEntryTBRows, app.addScrEntryTBCols)
        app.textBoxes[2][1].keyPressed(app, event.key)
        
    if app.screen == 'matMulSteps' or '':   # extend to other steps screens
        if event.key in app.scrollKeys:
            if app.scrollY > 0:
                if app.scrollKeys[event.key] < 0:
                    app.scrollY += app.scrollKeys[event.key]
            else: app.scrollY += app.scrollKeys[event.key]
    # create dictionary of keybindings

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
                        app.addResultX1, app.addResultY1, 'peach puff', 'tan4', app.addScrEntryFontSize, app)
                app.screen = 'matAddResult'
            
            # Clearing here
            if app.clearButton.mousePressed(app, event.x, event.y):
                app.textBoxes[0][1].clear()
                app.textBoxes[0][2].clear()

        elif app.screen == 'matAddResult':
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'matAdd'
        
        # For Matrix Multiplication and its sub-screens
        elif app.screen == 'matMul':
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'matCal'
            for i in range(len(app.textBoxes[1][0])):
                app.textBoxes[1][0][i].mousePressed(app, event.x, event.y)
                app.textBoxes[1][1][i].mousePressed(app, event.x, event.y)
            app.textBoxes[1][2].mousePressed(app, event.x, event.y)
            app.textBoxes[1][3].mousePressed(app, event.x, event.y)

            # Solving here (MULT)
            if app.solveButton.mousePressed(app, event.x, event.y) \
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
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'matCal'
            for i in range(len(app.textBoxes[2][0])):
                app.textBoxes[2][0][i].mousePressed(app, event.x, event.y)
            app.textBoxes[2][1].mousePressed(app, event.x, event.y)

            # Solving here (EDIT)
            if app.solveButton.mousePressed(app, event.x, event.y):
            # and app.textBoxes[2][1].isFilled():
                # M = app.textBoxes[2][1].matrix()
                M = [[1, 3, 0], [4, 2, 1], [3, 7, 5], [2, 4, 4]]
                app.tposeResultMatrix = matTpose(M)
                app.tposeResult = OutputMatrix(app.tposeResultMatrix, app.tposeResultX0, app.tposeResultY0, 
                        app.tposeResultX1, app.tposeResultY1, 'peach puff', 'tan4', app.tposeScrEntryFontSize/2, app)
                app.screen = 'matTposeResult'
            
            # Clearing here
            if app.clearButton.mousePressed(app, event.x, event.y):
                app.textBoxes[2][1].clear()
            
        elif app.screen == 'matTposeResult':
            if app.backButton.mousePressed(app, event.x, event.y):
                app.screen = 'matTpose'


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

# ***** BUTTON REDRAW FUNCTIONS *****
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

# ***** SCREEN REDRAW FUNCTIONS *****
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
    drawSolveButton(app, canvas)
    drawClearButton(app, canvas)
    canvas.create_text(app.width/2, 0.1*app.height + app.scrollY, text="Matrix Multiplication\nResult:",
    fill='tan4', font=f'Century {app.mulScrTitleSize} bold', justify=CENTER)

    for i in range(len(app.mulSteps)):
        canvas.create_text(app.width/2, 0.3*app.height + i*0.15*app.height + app.scrollY, text=f'{app.mulSteps[i]}',
    fill='tan4', font=f'Century {int(app.mulScrTitleSize/2)}', justify=CENTER)

def redrawMatTposeScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    drawSolveButton(app, canvas)
    drawClearButton(app, canvas)
    canvas.create_text(app.width/2, 0.05*app.height, text="Obtain Transpose",
    fill='tan4', font=f'Century {app.addScrTitleSize} bold', justify=CENTER)

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
    fill='tan4', font=f'Century {app.mulScrTitleSize} bold', justify=CENTER)
    app.tposeResult.redraw(app, canvas)


def redrawGEScreen(app, canvas):
    drawBackHomeButton(app, canvas)

def redrawGEResultScreen(app, canvas):
    drawBackHomeButton(app, canvas)

def redrawGEStepsScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    
def redrawSOLEScreen(app, canvas):
    drawBackHomeButton(app, canvas)

def redrawSOLEResultsScreen(app, canvas):
    drawBackHomeButton(app, canvas)

def redrawSOLEStepsScreen(app, canvas):
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
    if app.screen == 'home': redrawHomeScreen(app, canvas)
    elif app.screen == 'matCal': redrawMatCalScreen(app,canvas)
    elif app.screen == 'matAdd': redrawMatAddScreen(app, canvas)
    elif app.screen == 'matAddResult': redrawMatAddResultScreen(app, canvas)
    elif app.screen == 'matMul': redrawMatMulScreen(app, canvas)
    elif app.screen == 'matMulResult': redrawMatMulResultScreen(app, canvas)
    elif app.screen == 'matMulSteps': redrawMatMulStepsScreen(app, canvas)
    elif app.screen == 'matTpose': redrawMatTposeScreen(app, canvas)
    elif app.screen == 'matTposeResult': redrawMatTposeResultScreen(app, canvas)
    elif app.screen == 'GE': redrawGEScreen(app, canvas)
    elif app.screen == 'SOLE': redrawSOLEScreen(app, canvas)
    elif app.screen == 'LU': redrawLUScreen(app, canvas)
    elif app.screen == 'inverse': redrawInverseScreen(app, canvas)
    elif app.screen == '4FS': redraw4FSScreen(app, canvas)
    elif app.screen == 'det': redrawDetScreen(app, canvas)
    elif app.screen == 'GS': redrawGSScreen(app, canvas)

def run241ForOne():
    runApp(title="241-for-One")

run241ForOne()