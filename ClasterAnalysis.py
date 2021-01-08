# testData - случайные центроиды из выборки
# теперь нужно реализовать k-MEANS и кластеризовать данные, но заранее зная классы
# нужно помимо центров кластеров, разделить все элементы по кластерам и затем сравнить с generateData
# arr.points == arr.testData; kpoints == arr.trainData(массив точек),

import random
import math
import pylab as pl
import numpy as np
from matplotlib.colors import ListedColormap

def generateData (numberOfClassEl, numberOfClasses):
    data = []
    radius = [0] * numberOfClasses
    for classNum in range(numberOfClasses):
        x = 0
        y = 0
        r = radius[classNum - 1] + 27
        radius[classNum] = r
        for rowNum in range(numberOfClassEl):
            if classNum == 0:
                data.append([ [random.uniform(x - radius[0], x + radius[0]), random.uniform(y - radius[0], y + radius[0])], classNum])
            else:
                x1 = random.uniform(x - radius[classNum], x + radius[classNum])
                y1 = random.uniform(y - radius[classNum], y + radius[classNum])
                while(x1**2 + y1**2 < (radius[classNum])**2):
                    x1 = random.uniform(x - radius[classNum], x + radius[classNum])
                    y1 = random.uniform(y - radius[classNum], y + radius[classNum])
                data.append([[x1, y1],classNum])
    return data

def showData (data):
    trainData      = data
    classColormap  = ListedColormap(['#FF0000', '#00FF00', '#FFFF00', '#FF00FF'])
    pl.scatter([trainData[i][0][0] for i in range(len(trainData))],
               [trainData[i][0][1] for i in range(len(trainData))],
               c=[trainData[i][1] for i in range(len(trainData))],
               cmap=classColormap)
    pl.show()

def splitTrainTest(data, k):
    trainData = []
    testData = []
    a = []
    for i in range(k):
        x = random.randint(0, len(data) - 1)
        testData.append(data[x])
        a.append(x)
    for i in range(len(data)):
        s = 0
        for j in range(len(a)):
            if i == a[j]:
                s += 1
        if (s == 0):
            trainData.append(data[i])
    return trainData, testData
print("Введите коэффициент похожести:")
coeff = int(input())
data = generateData(300,4)
kpoints, points = splitTrainTest(data, 4)


c = [[0 for j in range(5)] for i in range(len(points))]

s = 0
while (s != 0):
   k = 0
   t = -1
   s = 0

   for j in range(len(points)):
      c[j][3] = c[j][0]  # записываю старые координаты центров
      c[j][4] = c[j][1]
      c[j][0] = 0
      c[j][1] = 0  # зануляю новые координаты для пересчета
      c[j][2] = 0

   for i in range(len(kpoints)):
      min = 99999
      t = -1
      for j in range(len(points)):                   # нахожу ближайший центр для всех точек
         if math.sqrt((kpoints[i][0][0] - points[j][0][0])**2 + (kpoints[i][0][1] - points[j][0][1])**2) < min and math.sqrt((kpoints[i][0][0] - points[j][0][0])**2 + (kpoints[i][0][1] - points[j][0][1])**2) < coeff:
            min = math.sqrt((kpoints[i][0][0] - points[j][0][0])**2 + (kpoints[i][0][1] - points[j][0][1])**2)
            t = j

      if (t != -1):
         c[t][0] += kpoints[i][0][0]
         c[t][1] += kpoints[i][0][1]
         c[t][2] += 1

   for j in range(len(points)):
      if (c[j][2] != 0):
         c[j][0] = c[j][0] / c[j][2]
         c[j][1] = c[j][1] / c[j][2]
         points[j][0] = c[j][0]
         points[j][1] = c[j][1]

   for j in range(len(points)):
      s += c[j][0] + c[j][1] - c[j][3] - c[j][4]
print(points)

ppoints = [kpoints[i][1] for i in range(len(kpoints))]

for i in range(len(kpoints)):
    min = 99999
    t = -1
    for j in range(len(points)):
        if math.sqrt((kpoints[i][0][0] - points[j][0][0]) ** 2 + (
                kpoints[i][0][1] - points[j][0][1]) ** 2) < min and math.sqrt(
                (kpoints[i][0][0] - points[j][0][0]) ** 2 + (kpoints[i][0][1] - points[j][0][1]) ** 2) < coeff:
            min = math.sqrt((kpoints[i][0][0] - points[j][0][0]) ** 2 + (kpoints[i][0][1] - points[j][0][1]) ** 2)
            t = j # индекс ближайшего центра
    ppoints[i] = t # изменения ppoints по результатам кластеризации
s = 0

# осталось сравнить полученные результаты

for i in range(len(ppoints)):
    if ppoints[i] == kpoints[i][1]:
        s += 1
print("Accuracy is : " + str(float(s) / len(ppoints)))

showData(data)
