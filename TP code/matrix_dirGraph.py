import math
from matrix_utils import *
from cmu_112_graphics import *
import tkinter as tk

# returns node with most edges for them to be placed in the center
# if there are multiple nodes, it returns the first max node
def mostEdges(M):
    rows, cols = len(M), len(M[0])
    edgeCountList = [0]*cols
    for row in range(rows):
        for col in range(cols):
            if M[row][col] != 0: edgeCountList[row] += 1    # row-wise sum
    for col in range(cols):
        for row in range(rows):
            if M[row][col] != 0: edgeCountList[col] += 1    # col-wise sum
    return(edgeCountList.index(max(edgeCountList)))

# returns list of each node's center x and centre y (each stored as a tuple)
# takes in screen center coordinates
# nodes are radially arranged
# remember to remove center node from numNodes
def getNodesCoords(cx, cy, r, M):
    numNodes = len(M)-1
    nodesCoords = []
    for i in range(numNodes):
        theta = (2*math.pi)/numNodes  # basic angle
        nodesCoords.append((cx+r*math.cos(i*theta), cy+r*math.sin(i*theta)))
    nodesCoords.insert(mostEdges(M), (cx, cy))
    return nodesCoords

# converts input adjacent matrix and node coordinates to arrow coordinates
# arrow coordinates in format x0, y0, x1, y1
def getArrowsCoords(M, nodesCoords):
    rows, cols = len(M), len(M[0])
    arrowCoords = []
    for row in range(rows):
        for col in range(cols):
            if M[row][col] != 0: arrowCoords.append((nodesCoords[row][0], nodesCoords[row][1], 
                                                    nodesCoords[col][0], nodesCoords[col][1]))
    return arrowCoords

# directed matrix below
# M =\
#     [
#     [0, 1, 1, 0, 0], 
#     [0, 0, 1, 0, 1],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0],
#     ]
# print(mostEdges(M))


# test animation below:

def appStarted(app):
    app.M = \
    [
    [0, 1, 1, 0, 0], 
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
    
        # [0, 1, 1, 1],
        # [1, 0, 1, 1], 
        # [1, 1, 0, 1],
        # [1, 1, 1, 0]

        # [0, 1, 0, 1],
        # [1, 0, 1, 0], 
        # [0, 1, 0, 1],
        # [1, 0, 1, 0]
    ]
    app.cx, app.cy = app.width/2, app.height/2
    app.r = 0.8*app.cy
    app.nodeR = 10
    app.nodesCoords = getNodesCoords(app.cx, app.cy, app.r, app.M)
    app.arrowsCoords = getArrowsCoords(app.M, app.nodesCoords)

def redrawAll(app, canvas):
    for i in range(len(app.nodesCoords)):
        x0, y0 = app.nodesCoords[i][0] - app.nodeR, app.nodesCoords[i][1] - app.nodeR 
        x1, y1 = app.nodesCoords[i][0] + app.nodeR, app.nodesCoords[i][1] + app.nodeR
        canvas.create_oval(x0, y0, x1, y1, fill='red')
        canvas.create_text(app.nodesCoords[i][0], app.nodesCoords[i][1], 
        text=f'{i+1}', fill='linen')
    for i in range(len(app.arrowsCoords)):
        x0, y0, x1, y1 = app.arrowsCoords[i]
        canvas.create_line(x0, y0, x1, y1, arrow=tk.LAST)

runApp(title="matrix_dirGraph test")