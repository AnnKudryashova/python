#Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

Z = int(input('введите номер плоскости Z: '))
if (Z==1):
    print('x>0, y>0')
elif (Z==2):
    print('x<0, y>0')
elif (Z==3):
    print('x<0, y<0')
elif (Z==4):
    print('x>0, y<0')
else:
    print('введено неверное значение плоскости')   