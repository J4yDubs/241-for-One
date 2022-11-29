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
    
    def mousePressed(self, app, eventX, eventY):
        if self.x0 <= eventX <= self.x1 and self.y0 <= eventY <= self.y1:
            return True
    
    def redraw(self, app, canvas):
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.color, width=0)
        canvas.create_text(mean(self.x0, self.x1), mean(self.y0, self.y1), text=self.text, fill='linen', 
        font=f'Century {self.fontSize} {self.fontStyle}', justify=CENTER)

class TextBox:
    def __init__(self, x0, y0, width, height, color, outline, fontSize, app):
        self.x0 = x0
        self.y0 = y0
        self.x1 = self.x0 + width
        self.y1 = self.y0 + height
        self.baseColor = color
        self.color = self.baseColor
        self.outline = outline
        self.fontSize = fontSize
        self.text = ''
        self.isSelected = None

    def mouseMoved(self, app, eventX, eventY):
        if self.x0 <= eventX <= self.x1 and self.y0 <= eventY <= self.y1 and not self.isSelected:
            self.color = 'navajo white'
        else:
            if self.isSelected:
                self.color = 'tan1'
            else:
                self.color = self.baseColor

    def mousePressed(self, app, eventX, eventY):
        if self.x0 <= eventX <= self.x1 and self.y0 <= eventY <= self.y1:
            self.color = 'tan1'
            self.isSelected = True
        else:
            self.color = self.baseColor
            self.isSelected = False

    def keyPressed(self, app, eventKey):
        # checks if length if eventKey is 1
        if self.isSelected:
            if eventKey in app.numKeys:
                self.text += eventKey
                return True
            elif eventKey == 'Backspace' or eventKey == 'Delete':
                self.text = self.text[:-1]
                return True

    def redraw(self, app, canvas):
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.color, outline=self.outline)
        if self.isSelected:
            canvas.create_text(mean(self.x0, self.x1), mean(self.y0, self.y1), text=self.text, fill='linen', 
            font=f'Century {int(self.fontSize)}', justify=CENTER)
        else: canvas.create_text(mean(self.x0, self.x1), mean(self.y0, self.y1), text=self.text, fill=f'{self.outline}', 
            font=f'Century {int(self.fontSize)}', justify=CENTER)

class DimTextBox(TextBox):
    def __init__(self, x0, y0, width, height, color, outline, fontSize, app):
        super().__init__(x0, y0, width, height, color, outline, fontSize, app)
        self.text = '3'     # pre-set dimension

class MatrixEntry():
    def __init__(self, rows, cols, x0, y0, x1, y1, color, outline, fontSize, app):
        self.rows, self.cols = rows, cols
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.width = (x1 - x0)/cols
        self.height = (y1 - y0)/rows
        self.baseColor = color
        self.color = [([self.baseColor]*self.cols) for row in range(self.rows)]
        self.outline = outline
        self.fontSize = fontSize
        self.text = [(['']*self.cols) for row in range(self.rows)]
        self.isSelected = [([None]*self.cols) for row in range(self.rows)]

    def mouseMoved(self, app, eventX, eventY):
        for i in range(self.rows):
            for j in range(self.cols):
                entryX0 = self.x0 + j*self.width
                entryX1 = entryX0 + self.width
                entryY0 = self.y0 + i*self.height
                entryY1 = entryY0 + self.height
                if entryX0 <= eventX <= entryX1 and entryY0 <= eventY <= entryY1 and not self.isSelected[i][j]:
                    self.color[i][j] = 'navajo white'
                else:
                    if self.isSelected[i][j]:
                        self.color[i][j] = 'tan1'
                    else:
                        self.color[i][j] = self.baseColor

    def mousePressed(self, app, eventX, eventY):
        for i in range(self.rows):
            for j in range(self.cols):
                entryX0 = self.x0 + j*self.width
                entryX1 = entryX0 + self.width
                entryY0 = self.y0 + i*self.height
                entryY1 = entryY0 + self.height
                if entryX0 <= eventX <= entryX1 and entryY0 <= eventY <= entryY1:
                    self.color[i][j] = 'tan1'
                    self.isSelected[i][j] = True
                else:
                    self.color[i][j] = self.baseColor
                    self.isSelected[i][j] = False

    def keyPressed(self, app, eventKey):
        # checks if length if eventKey is 1
        for i in range(self.rows):
            for j in range(self.cols):
                if self.isSelected[i][j]:
                    if eventKey in app.numKeys:
                        self.text[i][j] += eventKey
                    elif eventKey == 'Backspace' or eventKey == 'Delete':
                        self.text[i][j] = self.text[i][j][:-1]

    def redraw(self, app, canvas):
        if self.rows and self.cols > 0:
            for i in range(self.rows):
                for j in range(self.cols):
                    entryX0 = self.x0 + j*self.width
                    entryX1 = entryX0 + self.width
                    entryY0 = self.y0 + i*self.height
                    entryY1 = entryY0 + self.height
                    canvas.create_rectangle(entryX0, entryY0, entryX1, entryY1, fill=self.color[i][j], outline=self.outline)
                    if self.isSelected[i][j]:
                        canvas.create_text(mean(entryX0, entryX1), mean(entryY0, entryY1), text=self.text[i][j], fill='linen', 
                        font=f'Century {int(self.fontSize)}', justify=CENTER)
                    else: canvas.create_text(mean(entryX0, entryX1), mean(entryY0, entryY1), text=self.text[i][j], fill=f'{self.outline}', 
                        font=f'Century {int(self.fontSize)}', justify=CENTER)
    
    def isFilled(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.text[i][j] == '':
                    return False
        return True
    
    def matrix(self):
        M = create2DList(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.text[i][j] == '':
                    M[i][j] = 0
                else:
                    M[i][j] = float(self.text[i][j])
        return M

    def clear(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.text[i][j] = ''

class OutputMatrix:
    def __init__(self, matrix, x0, y0, x1, y1, color, outline, fontSize, app):
        self.matrix = matrix    # input list
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.width = (x1 - x0)/self.cols
        self.height = (y1 - y0)/self.rows
        self.baseColor = color
        self.color = [([self.baseColor]*self.cols) for row in range(self.rows)]
        self.outline = outline
        self.fontSize = fontSize
        self.text = [(['']*self.cols) for row in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.text[i][j] = str("%.2f" % matrix[i][j])
        self.isSelected = [([None]*self.cols) for row in range(self.rows)]
    
    def mouseMoved(self, app, eventX, eventY):
        for i in range(self.rows):
            for j in range(self.cols):
                entryX0 = self.x0 + j*self.width
                entryX1 = entryX0 + self.width
                entryY0 = self.y0 + i*self.height
                entryY1 = entryY0 + self.height
                if entryX0 <= eventX <= entryX1 and entryY0 <= eventY <= entryY1 and not self.isSelected[i][j]:
                    self.color[i][j] = 'navajo white'
                else:
                    if self.isSelected[i][j]:
                        self.color[i][j] = 'tan1'
                    else:
                        self.color[i][j] = self.baseColor
    
    def redraw(self, app, canvas):
        for i in range(self.rows):
            for j in range(self.cols):
                entryX0 = self.x0 + j*self.width
                entryX1 = entryX0 + self.width
                entryY0 = self.y0 + i*self.height
                entryY1 = entryY0 + self.height
                canvas.create_rectangle(entryX0, entryY0, entryX1, entryY1, fill=self.color[i][j], outline=self.outline)
                if self.isSelected[i][j]:
                    canvas.create_text(mean(entryX0, entryX1), mean(entryY0, entryY1), text=self.text[i][j], fill='linen', 
                    font=f'Century {int(self.fontSize)}', justify=CENTER)
                else: canvas.create_text(mean(entryX0, entryX1), mean(entryY0, entryY1), text=self.text[i][j], fill=f'{self.outline}', 
                    font=f'Century {int(self.fontSize)}', justify=CENTER)



# class MatrixTextBox(TextBox):
#     def __init__(self, rows, cols, x0, y0, x1, y1, color, outline, fontSize, fontStyle, app):
#         super().__init__(x0, y0, color, outline, fontSize, fontStyle, app)
#         self.rows = rows
#         self.cols = cols

# do a child class dim textbox that restricts entry size


# *****************************************************************
# ********************** ANIMATION FUNCTIONS **********************
# *****************************************************************

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

    # app.buttons indices:
    # 0: home, 1: calc, 2: add, 3: mult, 4: tpose
    app.buttons = [[],[],[],[],[],[],[]]

    # app.textBoxes indices:
    # 0: add, 1: mult, 2: tpose
    app.textBoxes = [[[]],[[],[]],[]]

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
    app.numKeys = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
    
    # *** BACK HOME BUTTON ***
    app.backHomeButtonMargin = 10
    app.backHomeButtonWidth = 0.1*app.width
    app.backHomeButtonHeight = 0.05*app.height
    app.backHomeButtonsTextSize = int(app.height/70)
    app.backHomeButton = Button(app.backHomeButtonMargin, app.backHomeButtonMargin, 
                    app.backHomeButtonWidth, app.backHomeButtonHeight, 'tan4', 
                    '241-for-One', app.backHomeButtonsTextSize, '', '')

    # *** GO BACK BUTTON ***
    app.backButtonMargin = 10
    app.backButtonWidth = 0.1*app.width
    app.backButtonHeight = 0.05*app.height
    app.backButtonsTextSize = int(app.height/70)
    app.backButton = Button(2*app.backButtonMargin + app.backHomeButtonWidth, app.backButtonMargin, 
                    app.backButtonWidth, app.backButtonHeight, 'tan4', 
                    'Back', app.backButtonsTextSize, '', '')

    # *** SOLVE BUTTON ***
    app.solveButtonMargin = app.width/3
    app.solveButtonWidth = (0.75*app.width-0.2*app.solveButtonMargin)/6
    app.solveButtonHeight = 0.4*app.solveButtonWidth
    app.solveButtonTextSize = int(app.height/50)
    app.solveButton = Button(app.solveButtonMargin, 0.8*app.height,
                                app.solveButtonWidth, app.solveButtonHeight,
                                'tan4', 'Solve', app.solveButtonTextSize, '', '')

    # *** CLEAR ENTRIES BUTTON ***
    app.clearButtonMargin = app.width/3
    app.clearButtonWidth = (0.75*app.width-0.2*app.clearButtonMargin)/6
    app.clearButtonHeight = 0.4*app.clearButtonWidth
    app.clearButtonTextSize = int(app.height/50)
    app.clearButtonSep = (app.width-2*app.clearButtonMargin-2*app.clearButtonWidth)
    app.clearButton = Button(app.solveButtonMargin + app.solveButtonWidth + app.clearButtonSep,
                                 0.8*app.height,
                                app.clearButtonWidth, app.clearButtonHeight,
                                'tan4', 'Clear', app.clearButtonTextSize, '', '')

    # *** SHOW STEPS BUTTON ***

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
        app.buttons[1].append(Button(int( app.calMargin + i*(app.calScrButtonWidth + app.calScrButtonSep) ),
                                0.5*app.height,
                                app.calScrButtonWidth, app.calScrButtonHeight,
                                'tan4', app.calButtonsText[i][0], app.calButtonsText[i][1], '', ''))

    # *** MATRIX ADDITION SCREEN *** (no showing steps)
    # text box margins
    app.matAddMargin = app.width/3
    # font sizes
    app.addScrTitleSize = int(app.height/20)
    # Dimension text boxes 
    # app.addScrDimTB prefix - addition Screen Dimension Text Box
    app.addScrDimTBWidth = 0.05*app.width
    app.addScrDimTBHeight = app.addScrDimTBWidth
    app.addScrDimTBSep = (app.width-2*app.matAddMargin-2*app.addScrDimTBWidth)
    for i in range(2):
        app.textBoxes[0][0].append(DimTextBox(int( app.matAddMargin + i*(app.addScrDimTBWidth + app.addScrDimTBSep) ),
         0.13*app.height, 
         app.addScrDimTBWidth, app.addScrDimTBHeight, 
         'peach puff', 'tan4', app.addScrDimTBHeight/2, app))
    # matrix entry text boxes
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
         0.13*app.height, 
         app.mulScrDimTBWidth, app.mulScrDimTBHeight, 
         'peach puff', 'tan4', app.mulScrDimTBHeight/2, app))
        
        app.textBoxes[1][1].append(DimTextBox(int( app.matMulMargin/2 + app.width/2 + i*(app.mulScrDimTBWidth + app.mulScrDimTBSep) ),
         0.13*app.height, 
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

    # *** MATRIX TRANSPOSE SCREEN *** (no showing steps)

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
                app.mulResultMatrix = matMul(M1,M2)
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
        
        # For Tranpose and its sub-screens
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
    canvas.create_text(app.width/2, 0.05*app.height, text="Matrix Addition",
    fill='tan4', font=f'Century {app.addScrTitleSize} bold', justify=CENTER)

    drawSolveButton(app, canvas)
    drawClearButton(app, canvas)
    
    for i in range(len(app.textBoxes[0][0])):
        app.textBoxes[0][0][i].redraw(app, canvas)
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

    # for i in range(len(app.addResult)):
    #     for j in range(len(app.addResult[0])):
    #         canvas.create_text

def redrawMatMulScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    canvas.create_text(app.width/2, 0.05*app.height, text="Matrix Multiplication",
    fill='tan4', font=f'Century {app.mulScrTitleSize} bold', justify=CENTER)

    drawSolveButton(app, canvas)
    drawClearButton(app, canvas)

    for i in range(len(app.textBoxes[0][0])):
        app.textBoxes[1][0][i].redraw(app, canvas)
        app.textBoxes[1][1][i].redraw(app, canvas)
    
    app.textBoxes[1][2].redraw(app, canvas)
    app.textBoxes[1][3].redraw(app, canvas)

def redrawMatMulResultScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    canvas.create_text(app.width/2, 0.1*app.height, text="Matrix Multiplication\nResult:",
    fill='tan4', font=f'Century {app.mulScrTitleSize} bold', justify=CENTER)
    app.mulResult.redraw(app, canvas)

def redrawMatTposeScreen(app, canvas):
    drawBackHomeButton(app, canvas)
    drawBackButton(app, canvas)
    canvas.create_text(app.width/2, 0.05*app.height, text="Obtain Transpose",
    fill='tan4', font=f'Century {app.addScrTitleSize} bold', justify=CENTER)

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
    elif app.screen == 'matAddResult':
        redrawMatAddResultScreen(app, canvas)
    elif app.screen == 'matMul':
        redrawMatMulScreen(app, canvas)
    elif app.screen == 'matMulResult':
        redrawMatMulResultScreen(app, canvas)
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