import xml.etree.ElementTree as ET
import os
import numpy as np
import matplotlib.pyplot as plt
def f(x,A):
    return -0.0001*(np.abs(np.sin(x)*np.sin(A)*np.exp(np.abs(100-np.sqrt(x**2+A**2)/np.pi)))+1)**0.1
p = ET.Element ('data')
#параметры
A=1.34941
x_values = np.linspace(-10, 10, 800)
#расчёт координат
y_values = f(x_values, A)
#cоздание директории
if not os.path.exists('results'):
    os.makedirs('results')
with open('results/function_values.xml', 'w') as file:
    for x, y in zip(x_values, y_values):
        row = ET.SubElement(p, 'row')
        arg_x = ET.SubElement(row, "x")
        arg_x.text = str(x)
        arg_y = ET.SubElement(row, "y")
        arg_y.text = str(y)
    tree = ET.ElementTree(p)
    tree.write("results/function_values.xml")
#построение графика функции
plt.figure(figsize=(16, 9))
plt.plot(x_values, y_values, label='f(x)', color='blue')
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
#plt.xscale('symlog')
plt.grid(True)
plt.legend()
#plt.savefig('results/function_plot.png')
plt.show()
