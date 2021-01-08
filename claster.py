import random
import math
import time


start_time = time.time()
start_time1 = time.time()
number_of_circles = int(input())
number_of_points = int(input())
points_in_circle = int(number_of_points / number_of_circles)
if (number_of_points >= 10000):
   hier_point = random.randint(int(number_of_points / 15), int(number_of_points / 10))
if (number_of_points >= 1000 and number_of_points < 10000):
   hier_point = random.randint(int(number_of_points / 20), 900)
else:
   hier_point = int(number_of_points / 2)
coeff = float(input()) # коэффициент похожести для прерывания иерархической кластеризации
circles = [[0 for j in range(3)] for i in range(number_of_circles)]
points = [[0 for j in range(2)] for i in range(hier_point)]
kpoints = [[0 for j in range(2)] for i in range(number_of_points)]
for i in range(number_of_circles):
   circles[i][0] = int(input())
   circles[i][1] = int(input())
   circles[i][2] = int(input())
# генерирую точки
s = 0
for i in range(number_of_circles):
   for j in range(points_in_circle):
      x = random.uniform(circles[i][0] - circles[i][2], circles[i][0] + circles[i][2])
      y = random.uniform(circles[i][1] - circles[i][2], circles[i][1] + circles[i][2])
      kpoints[s][0] = x
      kpoints[s][1] = y
      s = s + 1

for i in range(hier_point):
   t = random.randint(0, number_of_points - 1)
   points[i][0] = kpoints[t][0]
   points[i][1] = kpoints[t][1]

min = 99999999
q = 1

while (q != 0):
   q = 0
   for i in range(len(points) - 1):
      for j in range(i + 1,len(points)):
            c = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            if (c < min and c <= coeff):
               min = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
               k = j
               t = i
               q = 1
   min = 9999999
   if (k != t):
      points[t][0] = (points[t][0] + points[k][0]) / 2.0
      points[t][1] = (points[t][1] + points[k][1]) / 2.0
      points.pop(k)
   k = 0
   t = 0
print(points)
k = len(points) # приблизительное число кластеров
print(str(k) + "" + ": приблизительное число кластеров")
print("--- %s seconds ---" % (time.time() - start_time))

c = [[0 for j in range(5)] for i in range(len(points))] # массив обновляемых центров

# K-MEANS

while (s > 1/100):
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
         if math.sqrt((kpoints[i][0] - points[j][0])**2 + (kpoints[i][1] - points[j][1])**2) < min and math.sqrt((kpoints[i][0] - points[j][0])**2 + (kpoints[i][1] - points[j][1])**2) < coeff:
            min = math.sqrt((kpoints[i][0] - points[j][0])**2 + (kpoints[i][1] - points[j][1])**2)
            t = j

      if (t != -1):
         c[t][0] += kpoints[i][0]
         c[t][1] += kpoints[i][1]
         c[t][2] += 1

   for j in range(len(points)):
      if (c[j][2] != 0):
         c[j][0] = c[j][0] / c[j][2]
         c[j][1] = c[j][1] / c[j][2]
         points[j][0] = c[j][0]
         points[j][1] = c[j][1]

   for j in range(len(points)):
      s += c[j][0] + c[j][1] - c[j][3] - c[j][4]
            # K-means, пока координаты центров меняются, множество кластеризируется дальше
print(points)
print("--- %s seconds ---" % (time.time() - start_time1))