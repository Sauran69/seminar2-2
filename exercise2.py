AB = input('длина первого катета:')
AC = input('длина второго катета:')


AB = float(AB)
AC = float(AC)


BC = (AB**2 + AC**2)

S = (AB*AC)/2
P = AB + AC + BC

print('площадь треугольника' , S)
print('периметр треугольника', P)
print('гипотенуза треугольника', BC)

