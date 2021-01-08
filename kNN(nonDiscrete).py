# Классификатор в непрерывном пространстве. В качестве пространства рассматривается плоскость, объекты - точки на плоскости.
# Объект принадлежит к классу == лежит внутри соответствующей окружности, количество классов == количество окружностей
import random
import math
import pylab as pl
import numpy as np
from matplotlib.colors import ListedColormap

def generateData (numberOfClassEl, numberOfClasses):
    data = []
    for classNum in range(numberOfClasses):
        x = random.uniform(0,15)
        y = random.uniform(0,15)
        r = random.uniform(1,4)
        for rowNum in range(numberOfClassEl):
            data.append([ [random.uniform(x - r, x + r), random.uniform(y - r, y + r)], classNum])
    return data

def showData (nClasses, nItemsInClass, data):
    trainData      = data
    classColormap  = ListedColormap(['#FF0000', '#00FF00', '#FFFF00', '#FF00FF'])
    pl.scatter([trainData[i][0][0] for i in range(len(trainData))],
               [trainData[i][0][1] for i in range(len(trainData))],
               c=[trainData[i][1] for i in range(len(trainData))],
               cmap=classColormap)
    pl.show()

# разделение всех объектов пространства на две выборки - тестовой и тренировчной, для реализации kNN
def splitTrainTest(data, testPercent):
    trainData = []
    testData = []
    for row in data:
        if random.random() < testPercent:
            testData.append(row)
        else:
              trainData.append(row)
    return trainData, testData
def classifyKNN (trainData, testData, k, numberOfClasses):
    def dist (a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    testLabels = []
    for testPoint in testData:
        testDist = [ [dist(testPoint, trainData[i][0]), trainData[i][1]] for i in range(len(trainData))]
        stat = [0 for i in range(numberOfClasses)]
        for d in sorted(testDist)[0:k]:
            stat[d[1]] += 1
        testLabels.append( sorted(zip(stat, range(numberOfClasses)), reverse=True)[0][1] )
    return testLabels
def calculateAccuracy (nClasses, nItemsInClass, k, testPercent):
    data = generateData (nItemsInClass, nClasses)
    trainData, testDataWithLabels = splitTrainTest (data, testPercent)
    testData = [testDataWithLabels[i][0] for i in range(len(testDataWithLabels))]
    testDataLabels = classifyKNN (trainData, testData, k, nClasses)
    showData(nClasses, nItemsInClass)
    print(testDataLabels)
nClass = int(input())
IteminClass = int(input())
k = int(input())
testPercent = float(input())
data = generateData (IteminClass, nClass)
trainData, testDataWithLabels = splitTrainTest (data, testPercent)
testData = [testDataWithLabels[i][0] for i in range(len(testDataWithLabels))]
kNN = classifyKNN(trainData,testData, k, nClass)
print(kNN)
s = 0
s1 = 0
average = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
for i in range(len(testDataWithLabels)):
    if testDataWithLabels[i][1] == 0:
        average[0][0] += testDataWithLabels[i][0][0]
        average[0][1] += testDataWithLabels[i][0][1]
        average[0][2] += 1
    if testDataWithLabels[i][1] == 1:
        average[1][0] += testDataWithLabels[i][0][0]
        average[1][1] += testDataWithLabels[i][0][1]
        average[1][2] += 1
    if testDataWithLabels[i][1] == 2:
        average[2][0] += testDataWithLabels[i][0][0]
        average[2][1] += testDataWithLabels[i][0][1]
        average[2][2] += 1
    if testDataWithLabels[i][1] == 3:
        average[3][0] += testDataWithLabels[i][0][0]
        average[3][1] += testDataWithLabels[i][0][1]
        average[3][2] += 1

for i in range(len(average)):
    average[i][0] = average[i][0] / average[i][2]
    average[i][1] = average[i][1] / average[i][2]
print("Average x: " + str(average[0][0]) + " Average y: " + str(average[0][1]) + " for class " + str(0) + " (RED color)")
print("Average x: " + str(average[1][0]) + " Average y: " + str(average[1][1]) + " for class " + str(1) + " (GREEN color)")
print("Average x: " + str(average[2][0]) + " Average y: " + str(average[2][1]) + " for class " + str(2) + " (YELLOW color)")
print("Average x: " + str(average[3][0]) + " Average y: " + str(average[3][1]) + " for class " + str(3) + " (PINK color)")
for i in range(len(testDataWithLabels)):
    if (testDataWithLabels[i][1] == kNN[i]):
        s += 1
print("Accuracy: " + str(float(s) / len(testDataWithLabels)))
showData(nClass, IteminClass, data)
