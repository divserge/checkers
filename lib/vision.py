import cv2
import numpy as np
from copy import copy, deepcopy

def is_rect(poly):
    vecs = []
    for ind, point in enumerate((list(poly) + [poly[0]])[1:]):
        vec = (point - poly[ind]).reshape(-1)
        vec = vec/np.linalg.norm(vec)
        vecs.append(vec)
    
    for ind, vec in enumerate(vecs[1:]):
        if vec.dot(vecs[ind]) > 0.5:
            return False       
    return True

# typical value for mindark is 120 and for superwhite is 190
# needs to be adjust for different boards, draught types and lightening
def get_rect(img, white_figures_thresh, dark_cells_thresh):
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(gray, 0, white_figures_thresh)
    gray = 255 - (gray & mask)
    thresh = cv2.threshold(gray, 255 - dark_cells_thresh, 255, cv2.THRESH_BINARY)[1]
    ker = np.ones((4, 4), dtype=np.int0)
    
    thresh = cv2.dilate(copy(thresh), ker) # dilation to close blinks on each cell
    
    for _ in range(5): # erosion to delete connections between cells
        thresh = cv2.erode(copy(thresh), ker)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    rects = []
    for c in cnts[1]:
        poly = cv2.approxPolyDP(c, 20, True)
        if len(poly) == 4:
            if is_rect(poly):
                rects.append(c)
                
    return rects, thresh, gray

# -1 stands for black checkers, 1 stands for white checkers, 0 stands for empty cells
def get_grid_from_rect_contours(rects, img  ):
    
    mat = np.zeros((8, 4), dtype=np.int0)
    rect_cents = []
    for c in rects:
        rect = cv2.boxPoints(cv2.minAreaRect(c))
        rect_cents.append(rect.mean(axis=0))

    rect_cents = np.array(rect_cents)
    rect_cents = rect_cents[np.lexsort((rect_cents[:, 0], rect_cents[:, 1]))]

    for i, _ in enumerate(mat):
        for j, _ in enumerate(mat[i]):
            center =rect_cents[4 * i + j]
            color = img[int(center[1]), int(center[0])]
            print('center: ', center, ' color ', color.mean())
            if color.mean() > 180:
                mat[i][j] = 1
            elif color.mean() > 80:
                mat[i][j] = 0
            else:
                mat[i][j] = -1
    
    return mat
