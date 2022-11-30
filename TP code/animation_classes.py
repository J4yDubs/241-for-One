from matrix_utils import *
from matrix_GE import *
from matrix_SOLE import *
from cmu_112_graphics import *

class button:
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
                if not isinstance(matrix[i][j], str):
                    self.text[i][j] = str("%.2f" % matrix[i][j])
                else: self.text[i][j] = matrix[i][j]
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


class MatrixTextBox(TextBox):
    def __init__(self, rows, cols, x0, y0, x1, y1, color, outline, fontSize, fontStyle, app):
        super().__init__(x0, y0, color, outline, fontSize, fontStyle, app)
        self.rows = rows
        self.cols = cols
