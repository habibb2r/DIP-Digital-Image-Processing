# -*- coding: utf-8 -*-
"""Digital-Image-lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OOQUoiyVJWVDqmsVP-t2coJ070-xHBNh
"""

#Digital Image Proccessing

x = [[1, 2, 3, 4, 5], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]]



print(x[1])
# print(x[0][2])
print(len(x))
print(x[2][1:3])
print(x[0][0::2])

x = [[1, 2, 3, 4, 5], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]]
y =[0, 0, 0]

for i in x:
  sum = 0
  for j in i:
    sum = sum + j
    avg = sum / len(i)
  y[x.index(i)] = avg

print(y)

x = [[1, 2, 3, 4, 5], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]]
y = [0, 0, 0]
z = [0, 0, 0, 0, 0]

for j in x:
    for i, value in enumerate(j):
        z[i] = z[i] + value / len(x)

print(z)

#HW
x = [1, 3, 5, 6, 7, 8, 6, 1, 2, 3]
y = [0, 0, 0, 0, 0, 0, 0, 0]

i = 0
while i < len(x) - 2:
    average = sum(x[i:i+3]) / 3.0
    y[i] = average
    i = i + 1

print(y)

x = [1, 3, 5, 6, 7, 8, 6, 1, 2, 3]
y = [0, 0, 0, 0, 0, 0, 0, 0]

def average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)

print("Average  x =", average(x))
print("Average  y =", average(y))