import csv

import cv2, PIL
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate

def removeNonBlackPixels():
    pass

def getCoordinates(img):
    image = cv2.imread(img)
    lower_boundary = np.array([0,0,0])
    higher_boundary = np.array([20,20,20])
    mask = cv2.inRange(image, lower_boundary, higher_boundary)
    coordinates = cv2.findNonZero(mask)
    coordinates = [tuple(c[0]) for c in coordinates]
    coordinates2 = averageCoordinateValues(coordinates, 1)
    coordinates3 = averageCoordinateValues(coordinates, 2)
   # x,y = adjustScale(coordinates) #original
    x2,y2 = adjustScale(coordinates2) #mean
    x3,y3 = adjustScale(coordinates3) #median
    plotTwoLines(x2= x2,y2=y2,x3=x3,y3=y3)
    # coordinates.sort(key=lambda x:(x[0]))
    # x = [c[0] * (.04/30) for c in coordinates] #.04/30 is the second per mm, there are 30 px per mm
    # y = [6-(c[1] * (.1/30) + 2) for c in coordinates] #.1/30 is .1mv per mm, there are 30 px per mm. Scaling for y is between 2 to 4 mv, +2 to fix offset. 6 - val to fix reverse y coord
    return x3,y3

def averageCoordinateValues(coordinates,  type=1):
    from collections import defaultdict
    d = defaultdict(list)
    coordList = []
    for x,y in coordinates:
        d[x].append(y)
    for k, v in d.items():
        if type ==1:
            coordList.append((k, sum(v) / len(v)))
        elif type==2:
            v.sort()
            coordList.append((k, v[len(v)//2]))
    return coordList


def adjustScale(coordinates):
    coordinates.sort(key=lambda x:(x[0]))
    x = [c[0] * (.04/30) for c in coordinates] #.04/30 is the second per mm, there are 30 px per mm
    y = [6-(c[1] * (.1/30) + 2) for c in coordinates] #.1/30 is .1mv per mm, there are 30 px per mm. Scaling for y is between 2 to 4 mv, +2 to fix offset. 6 - val to fix reverse y coord
    return x,y

    # x = [c[0] for c in coordinates]
    # x_set = set(x)
    # y = [c[1]for c in coordinates]
    #
    # updatedCoordlist = []
    # for xindex in x_set:
    #     ysum = 0
    #     count = 0
    #     for coord in coordinates:
    #         if xindex == coord[0]:
    #             ysum += coord[1]
    #             count += 1
    #     yAverage = ysum/count
    #     updatedCoordlist.append((xindex, yAverage))
    # return updatedCoordlist







def driver(continuousECG):
    pass

def plotTwoLines(x1=None,y1=None,x2=None,y2=None,x3=None,y3=None):
    if x1 != None and x2 != None:
        plt.plot(x1,y1, "b")
    if x2 != None and y2 != None:
        plt.plot(x2,y2, "r")
    if x3 != None and y3 != None:
        plt.plot(x3,y3, "g")
    plt.show()

def plot(x,y):
    print(x)
    print(y[-1])
    #plt.plot(x,y)
    plt.plot(x,y, 'or', linewidth=10.0)
    #plt.gca().invert_yaxis()
    plt.show()

def saveData(x,y):
    mergedCoordinates = tuple(zip(x,y))
    with open('data.csv', 'wb') as test_file:
        file_writer = csv.writer(test_file)
        for i in range(2):
            for x in mergedCoordinates:
                file_writer.writerow(x[i])
                break
            break
    test_file.close()


if __name__ == '__main__':
    x,y = getCoordinates(r'./continuousECG.png')
    #plot(x,y)
    #print(coord)