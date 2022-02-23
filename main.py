
'''
Aidan Carrier Multivariable Coding Project ''main.py''
Author @Aidan Carrier
--
Description:
The purpose of this program is to take an input from the user -- which is a multivariable function in the form of z = f(x,y);
and then (a) plot the multivariable function using mathplot, (b) be given input from the user to take the partial derivative of z with respect to either 'x' or 'y'
then (c) be able to find the volume under the curve over region R = {a<=x<=b; c<=y<=d}; possibly find (d) the Surface Area of the sheet
Also, there should (e) be functionality for vector functions: r(t) = f(t)i_hat + g(t)j_hat + h(t)k_hat. '''

#imports needed in this project

import math
import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

string_input = ""
parsed_input = []
alphabet = []
alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
print("please enter an equation in the form of z = f(x,y):\n--use ^ for squares and sqrt functions")
string_input = input()
subequations = []
#simplify string into a space less equation with lowercase.
string_input = string_input.lower().replace(" ", "")
print("entered equation: ", string_input) 

if(string_input.count("=")==1):
    print("valid equation!")
else:
    print("invalid equation -- please use only one '=' sign.")

parsed_input = string_input.split('=')
if(len(parsed_input[0]) == 1): 
    print("not implicit, single variable, ", parsed_input[0])
    dependent_variable = parsed_input[0]
    if(dependent_variable in alphabet):
        print(f"valid single variable")

for term in parsed_input:
    for char in term:
        # print(term, " : ", char)
        pass
    
    
    string = term.lower().replace(" ", "")
    equation = string
    if term == dependent_variable:
        subequations.append([dependent_variable, string])
        continue
    print("original equation = ", string)
    
    #create an array fromt he string of letters
    array = []
    for char in equation:
        letter = char
        array.append(letter)
    arr = np.array(array)
    

    for i in range(equation.count("(")):
        a = equation.find('(')
        b = equation.find(')')
        #create an array fromt he string of letters
        array = []
        for char in equation:
            letter = char
            array.append(letter)
        arr = np.array(array)

        arrInPar = arr[a:b+1]

        string = "".join(arrInPar).lstrip("(").rstrip(")")
        print("parentheses = ", string)
        for character in alphabet:
            if character not in equation:
                subequations.append([character, string])
                equation = equation.replace("".join(arrInPar), character)
                print(equation)
                break
        print(subequations)
    
    for i in range(equation.count("^")):
        string = equation
        a = string.find("^")
        
        #create array of letters from equation
        array = []
        for char in equation:
            letter = char
            array.append(letter)
        arr = np.array(array)

        string = "".join(arr[a-1:a+2])

        print("exponent = ", string)

        for character in alphabet:
            if character not in equation:
                subequations.append([character, string])
                equation = equation.replace("".join(string), character)
                print(equation)
                break
        print(subequations)

        print("---\n\n")
        print(equation)
        
        string = equation.split("+")
        print(string)
        

def function(x, y):
    z = x**2 + y**2
    return z

def double_integral(x,y):
    
    function(x,y)*dx*dy

def deriv_partial_x(x, y):
    dz_dx = 2*x
    return dz_dx
    


def create_function(string, independent1, independent2):
    return (output)





        



    




tickLength = 1
valueDomainX = 5
valueDomainY = 5



        # plt.plot(x, y, function(x, y))


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for x in range(-valueDomainX, valueDomainX, tickLength):
    for y in range(-valueDomainY, valueDomainY, tickLength):
        # print(function(x, y))
        ax.scatter(x, y, function(x,y), marker = '.', c = 'k')
        ax.scatter(x, y, deriv_partial_x(x, y), marker = '.', c = 'r')
    
# ax.scatter(data[(label==0).squeeze(),0], data[(label==0).squeeze(),1], data[(label==0).squeeze(),2], marker='o', c='k')
# ax.scatter(data[(label==1).squeeze(),0], data[(label==1).squeeze(),1], data[(label==1).squeeze(),2], marker='o', c='r')
# ax.scatter(center[0,0], center[0,1], center[0,2], marker='x', c='k')
# ax.scatter(center[1,0], center[1,1], center[1,2], marker='x', c='r')
plt.show()

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()