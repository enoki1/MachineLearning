#1) Есть сетка(город(квадратный)) внутри сетки выбираются точки(люди) в узлах школы, человек может ходить лишь только по улицам, найти школу к которой человек относится
# заданы прямые k1 и k2 штук(заданы коодринаты школ) далее набор координат жителей. найти ближайшую школу для человека(ходим только по сетке, когда мы в одной клетке то можем шагнуть перпендикулярно)
import math
def m_distance1(x,y):
    min = 1000000
    x1 = 123123
    x2 = 123123123
    for i in range(school_n):
        if abs(x - sx[i]) + abs(y - sy[i]) < min:
            min = abs(x - sx[i]) + abs(y - sy[i])
    return min
def m_distance2(x,y):
    min = 1000000
    x1 = 123123
    x2 = 123123123
    for i in range(school_n):
        if abs(x - sx[i]) + abs(y - sy[i]) < min:
            x1 = sx[i]
            x2 = sy[i]
            min = abs(x - sx[i]) + abs(y - sy[i])
    print(x1,x2)
kx = int(input())
ky = int(input())
min1 = 1000000
min2 = 1000000
min3 = 1123123123
min4 = 123123123
min5 = 0
minx = 100000
miny = 100000
school_n = int(input())
sweller_n = int(input())
sx = [0] * school_n
sy = [0] * school_n
swx = [0] * sweller_n
swy = [0] * sweller_n
for i in range(school_n):
    sx[i] = int(input())
    sy[i] = int(input())
for i in range(sweller_n):
    swx[i] = float(input())
    swy[i] = float(input())
# считаю что масштаб равен 1 и сетка квадратная(все расстояния равны)
# координаты по x и по y у каждого объекта в своем массиве(по x и по y соответственно)
for i in range(sweller_n):
    if swx[i] == math.floor(swx[i]) and swy[i] == math.floor(swy[i]):
        print("minimal distance for sweller number" + " " + str(i + 1) + ":" + str(m_distance1(swx[i], swy[i])))
        print("the school is:")
        m_distance2(swx[i],swy[i])
    if swx[i] == math.floor(swx[i]) and swy[i] != math.floor(swy[i]):
        min1 = m_distance1(swx[i], math.floor(swy[i]))
        min2 = m_distance1(swx[i], math.floor(swy[i] + 1))
        if min1 + abs(swy[i] - math.floor(swy[i])) < min2 + abs(math.floor(swy[i] + 1) - swy[i]):
            print("minimal distance for sweller number" + " " + str(i + 1) +  ": " + str(min1 + swy[i] - math.floor(swy[i])))
            print("the school is:")
            m_distance2(swx[i], math.floor(swy[i]))
        else:
            print("minimal distance for sweller number" + " " + str(i + 1) + ": " + str(min2 - swy[i] + math.floor(swy[i] + 1)))
            print("the school is:")
            m_distance2(swx[i], math.floor(swy[i] + 1))
    if swx[i] != math.floor(swx[i]) and swy[i] == math.floor(swy[i]):
        min1 = m_distance1(math.floor(swx[i]),swy[i])
        min2 = m_distance1(math.floor(swx[i] + 1),swy[i])
        if min1 + abs(swx[i] - math.floor(swx[i])) < min2 + abs(math.floor(swx[i] + 1) - swx[i]):
            print("minimal distance for sweller number" + " " + str(i + 1) + ": " + str(min1 + abs(swx[i] - math.floor(swx[i]))))
            print("the school is:")
            m_distance2(math.floor(swx[i]),swy[i])
        else:
            print("minimal distance for sweller number" + " " + str(i + 1) +  ": " + str(min2 - swx[i] + math.floor(swx[i] + 1)))
            m_distance2(math.floor(swx[i] + 1),swy[i])
    if swx[i] != math.floor(swx[i]) and swy[i] != math.floor(swy[i]):
        min1 = m_distance1(math.floor(swx[i]),math.floor(swy[i])) + swx[i] - math.floor(swx[i]) + swy[i] - math.floor(swy[i])
        min2 = m_distance1(math.floor(swx[i] + 1),math.floor(swy[i])) - swx[i] + math.floor(swx[i] + 1) + swy[i] - math.floor(swy[i])
        min3 = m_distance1(math.floor(swx[i] + 1), math.floor(swy[i] + 1)) - swx[i] + math.floor(swx[i] + 1) - swy[i] + math.floor(swy[i] + 1)
        min4 = m_distance1(math.floor(swx[i]), math.floor(swy[i] + 1)) + swx[i] - math.floor(swx[i]) - swy[i] + math.floor(swy[i] + 1)
        min5 = min(min1,min2,min3,min4)
        if min5 == min1:
            print("minimal distance for sweller number" + " " + str(i + 1) + ": " + str(min1))
            print("the school is:")
            m_distance2(math.floor(swx[i]), math.floor(swy[i]))
        if min5 == min2 and min5 != min1:
            print("minimal distance for sweller number" + " " + str(i + 1) + ": " + str(min2))
            print("the school is:")
            m_distance2(math.floor(swx[i] + 1),math.floor(swy[i]))
        if min5 == min3 and min5 != min1 and min5 != min2:
            print("minimal distance for sweller number" + " " + str(i + 1) + ": " + str(min3))
            print("the school is:")
            m_distance2(math.floor(swx[i] + 1), math.floor(swy[i] + 1))
        if min5 == min4 and min5 != min1 and min5 != min2 and min5 != min3:
            print("minimal distance for sweller number" + " " + str(i + 1) + ": " + str(min4))
            print("the school is:")
            m_distance2(math.floor(swx[i]), math.floor(swy[i] + 1))
        min1 = 123123
        min2 = 12312313
        min3 = 123123123
        min4 = 123123123
        min5 = 123123123

