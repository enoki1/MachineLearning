import numpy as np
import pandas as pd
import time
import math
import random
import pylab as pl
from matplotlib.colors import ListedColormap

start_time = time.time()
kills = pd.read_csv('./kill_match_stats_final_0.csv')
killsS = kills.loc[(kills['map'] == "ERANGEL")]
killsS = killsS.reset_index(drop=True)


kpoints = [[[0,0],0] for i in range(len(killsS))]

for ind in killsS.index:
    if (ind < len(killsS)):
        kpoints[ind][0][0] = killsS['victim_position_x'][ind]
        kpoints[ind][0][1] = killsS['victim_position_y'][ind]
    else:
        break


k = 10

points = [[[0,0],0] for i in range(k)] # центроиды

for i in range(k):
    x = random.randint(0, len(kpoints) - 1)
    points[i][0][0] = kpoints[x][0][0]
    points[i][0][1] = kpoints[x][0][1]
    points[i][1] = 0
c = [[0 for j in range(5)] for i in range(len(points))] # массив обновляемых центров

s = 0

while (s > 1/100):
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
         points[j][0][0] = c[j][0]
         points[j][0][1] = c[j][1]

   for j in range(len(points)):
      s += c[j][0] + c[j][1] - c[j][3] - c[j][4]
            # K-means, пока координаты центров меняются, множество кластеризируется дальше

def showData (data):
    trainData      = data
    classColormap  = ListedColormap(['#FF0000', '#00FF00', '#FFFF00', '#FF00FF', '#0000FF'])
    pl.scatter([trainData[i][0][0] for i in range(len(trainData))],
               [trainData[i][0][1] for i in range(len(trainData))],
               c=[trainData[i][1] for i in range(len(trainData))],
               cmap=classColormap)
    pl.show()
print(points)
for i in range(len(points)):
    points[i][0][0] = points[i][0][0]
    points[i][0][1] = points[i][0][1]
print("--- %s seconds ---" % (time.time() - start_time))
showData(points)


