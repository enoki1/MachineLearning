import numpy as np
import random
import matplotlib.pyplot as plt
import sklearn
import pandas as pd
import math


kills = pd.read_csv('./day_wise.csv.xls')
#kills["kill_distance"] = ((kills["killer_position_x"] - kills["victim_position_x"]) ** 2 + (kills["killer_position_y"] - kills["victim_position_y"]) ** 2) ** (1/2)


def Lin_coef(x, y):

    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # вычисление коэффициентов регрессии
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression(x, y, b, b1, b2, b3):
    plt.scatter(x, y, color="g",

                marker="o", s=20)

    y_pred = b[0] + b[1] * x
    y_pred2 = b1[0] + b1[1] * x + b1[2] * x**2
    y_pred3 = b2[0] + b2[1] * x + b2[2] * x**2 + b2[3] * x**3
    y_pred4 = (b3[1])**(x) * b3[0]
    plt.plot(x, y_pred, color="black")
    plt.plot(x, y_pred2, color="yellow")
    plt.plot(x, y_pred3, color="brown")
    plt.plot(x, y_pred4, color="blue")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def plot_regression_exp(x, y, b):
    plt.scatter(x, y, color="g",

                marker="o", s=20)

    y_pred = b[0] * (math.e)**(x*b[1])
    plt.plot(x, y_pred, color="black")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

'''
def plot_regression_quadratic(x, y, b):
    plt.scatter(x, y, color="g",

                marker="o", s=10)

    y_pred = b[0] + b[1] * x + b[2] * x**2
    plt.plot(x, y_pred, color="black")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
'''

arrx = []
arry = []

for ind in kills.index:
    if (ind < 3000 and ind > 0):
        arrx = np.append(arrx, ind)
        arry = np.append(arry, kills['Confirmed'][ind])
s1 = 0
y1 = 0
s2 = 0
x1y1 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
lny1 = 0
lnx1y1 = 0
x2y1 = 0
x3y1 = 0
s = len(arrx)

for i in range(len(arrx)):
    s1 += arrx[i]
    y1 += arry[i]
    s2 += arrx[i]**2
    s3 += arrx[i]**3
    s4 += arrx[i]**4
    s5 += arrx[i]**5
    s6 += arrx[i]**6
    lny1 += math.log(arry[i])
    lnx1y1 += math.log((arry[i])) * arrx[i]
    x3y1 += arrx[i]**3 * arry[i]
    x2y1 += arrx[i]**2 * arry[i]
    x1y1 += arrx[i] * arry[i]

    # линейная

b1 = [0,0]
M1 = np.array(([s, s1],[s1, s2]))
v1 = np.array([y1, x1y1])
solve1 = np.linalg.solve(M1, v1)
b1[0] = solve1[0]
b1[1] = solve1[1]

    # полиномиальная(парабола)

b2 = [0,0,0]
M2 = np.array(([s,s1,s2],[s1,s2,s3],[s2,s3,s4]))
v2 = np.array(([y1,x1y1,x2y1]))
solve2 = np.linalg.solve(M2, v2)
b2[0] = solve2[0]
b2[1] = solve2[1]
b2[2] = solve2[2]

    # полиномиальная(кубическая кривая)

b3 = [0,0,0,0]
M3 = np.array((([s,s1,s2,s3], [s1,s2,s3,s4],[s2,s3,s4,s5],[s3,s4,s5,s6])))
v3 = np.array(([y1,x1y1,x2y1,x3y1]))
solve3 = np.linalg.solve(M3,v3)
b3[0] = solve3[0]
b3[1] = solve3[1]
b3[2] = solve3[2]
b3[3] = solve3[3]

    # показательная

b4 = [0,0]
M4 = np.array((([s,s1],[s1,s2])))
v4 = np.array((([lny1,lnx1y1])))
solve4 = np.linalg.solve(M4,v4)
b4[0] = (math.e)**solve4[0]
b4[1] = (math.e)**solve4[1]
print("black : линейная")
print("yellow : парабола")
print("brown : кубическая")
print("blue : показательная")

    # экспонента

b5 = [0,0]
M5 = np.array(([s,s1], [s1,s2]))
v5 = np.array(([lny1, lnx1y1]))
solve5 = np.linalg.solve(M5,v5)
b5[0] = (math.e)**(solve5)[0]
b5[1] = solve5[1]

print("коэффициенты регрессий : ")
print(b1,b2,b3,b4)
z1 = 0
z2 = 0
z3 = 0
z4 = 0
z5 = 0

z1 = 0
z2 = 0
z3 = 0
z4 = 0
z5 = 0

for i in range(len(arrx)):

    z1 += -arry[i] + (b1[0] + b1[1] * arrx[i])
    z2 += -arry[i] + (b2[0] + b2[1] * arrx[i] + b2[2] * arrx[i]**2)
    z3 += -arry[i] + (b3[0] + b3[1] * arrx[i] + b3[2] * arrx[i]**2 + b3[3]*arrx[i]**3)
    z4 += -arry[i] + (b4[0] * (b4[1])**(arrx[i]))
    z5 += -arry[i] + (b5[0] * (math.e)**(arrx[i] * b5[1]))

#print(z1,z2,z3,z4,z5)

print("Accuracy for line: " + str(z1))
print("Accuracy for line: " + str(z2))
print("Accuracy for line: " + str(z3))
print("Accuracy for line: " + str(z4))
print("Accuracy for line: " + str(z5))


plot_regression(arrx,arry,b1,b2,b3,b4)
plot_regression_exp(arrx, arry, b5)