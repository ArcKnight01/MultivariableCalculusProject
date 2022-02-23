
import math
import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib import cm
from matplotlib.ticker import LinearLocator

def add_terms(terms_list:list):
    sum = 0
    terms = terms_list
    for term in terms:
        sum = sum + term
    return sum

def multiply_terms(terms_list:list):
    product = 1
    terms = terms_list
    for term in terms:
        product = product * term
    return product
lst = list([1,-2,3,5,7,1])

# print(lst)

# print(add_terms(lst))
# print(multiply_terms(lst))


# print(add_terms([multiply_terms([1,2,4]), multiply_terms([4,5,6]), multiply_terms([5,7,0.9])]))

def get_average(terms_list):
    terms = terms_list
    number_of_terms = len(terms)
    return(add_terms(terms)/number_of_terms)

# print(get_average(lst))

def construct_function(inputX, inputY, equation:str):
    term_data = []
    # dictionary = {"x" : inputX, "y": inputY}
    equation = str(equation)
    # print(equation)
    assert type(equation) == str, "equation is not a string!"
    alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
    dependent_variable = ""
    equation = equation.lower().replace(" ", "")
    assert equation.count('=') == 1, "not a valid equation!"
    if(equation.find("=") == 1):
        assert(equation[0] in alphabet), "the dependent variable in the form z = ... is not valid!"
        dependent_variable = equation[0]
    elif(equation.find("=") == 6):
        assert(equation[0] in alphabet), "dependent variable in the form f(x,y) = .... is not valid!"
        assert((equation[1] == "(") & (equation[5] == ")") & (equation[3] == ",")), "dependent variable in the form f(x,y) = .... is not valid!"
        dependent_variable = equation[0]
    # print(dependent_variable)
    num_independent = 0
    independent_variables = []
    for i,v in enumerate(equation):
        if (v in alphabet) & (v != dependent_variable):
            if v not in independent_variables:
                independent_variables.append(v)
                num_independent += 1
                assert num_independent <= 2, "too many independent variables!"
    # print(independent_variables)
    # print(equation.find("="))
    # print("eq. " + equation)
    if(equation.find("=")==6):
        equation = equation.replace(f"{dependent_variable}({independent_variables[0]},{independent_variables[1]})", f"{dependent_variable}")
        # print(equation)

    # print(equation.count(independent_variables[0]))
    # print(equation.count(independent_variables[1]))
    expression = equation.split("=")[1]
    # print(expression)
    num_terms = expression.count("+") + 1
    # print("number of terms is " + str(num_terms))
    if(num_terms > 1):
        expression = expression.split("+")
    else:
        expression = [expression,]
    
    for term in expression:
        assert type(term) == str, "terms must be string values!"
        constant = 1
        is_negative = False
        term_length = len(term)
        # print(f"length of term, {term} is {term_length}")
        assert term_length >= 1, "term length error"
        assert term.count(independent_variables[0]) <= 1, "only one independent allowed!"
        assert term.count(independent_variables[1]) <= 1, "only one independent allowed!"
        num_var_index0 = term.count(independent_variables[0])
        num_var_index1 = term.count(independent_variables[1])
        exponent_var_index0 = 0
        exponent_var_index1 = 0
        data = (constant, independent_variables[0], independent_variables[1], num_var_index0, num_var_index1, exponent_var_index0, exponent_var_index1)
        # print("data is " + str(data))
        
        if(term[0] == "-"):
            is_negative = True
            # print(term)
            # print(term_length)
            assert term_length >= 2, "term length error"
        
        if(is_negative == False):
            # print("term is not negative!")
            if(term[0] not in alphabet):
                str_constant = term[0]
                # print("constant: " + str_constant)
                constant = float(str_constant)
                # print(constant)
                if(term_length > 1):
                    assert term[1] in independent_variables, "invalid format, variable after constant must be one of the independent variables!"
                    if(term[1] == independent_variables[0]):
                        # print(f"{independent_variables[0]} is the first variable")
                        if(exponent_var_index0 == 0): 
                            exponent_var_index0 = 1
                        if (term_length > 2) & (num_var_index1 != 0):
                            if(term[2] in independent_variables):
                                if(term[2] == independent_variables[1]):
                                    # print(f"{independent_variables[1]} is the second variable")
                                    if(exponent_var_index1 == 0): 
                                        exponent_var_index1 = 1
                            if(term[2] == '*'):
                                assert(term_length > 4), "invalid exponent"
                                assert(term[3] == '*'), "invalid exponent"
                                if(term[4] not in alphabet):
                                    if(term[4] != "-"):
                                        str_exponent_var_index0 = term[4]
                                        # print(f"exponent is {str_exponent_var_index0}")
                                        exponent_var_index0 = float(str_exponent_var_index0)
                                        if(term_length > 5):
                                            if(term[5] in independent_variables):
                                                if(term[5] == independent_variables[1]):
                                                    # print(f"{independent_variables[1]} is the second variable")
                                                    if(exponent_var_index1 == 0): 
                                                        exponent_var_index1 = 1
                                                    if(term_length > 6):
                                                        if(term[6] == '*'):
                                                            assert(term_length > 8), "invalid exponent"
                                                            assert(term[7] == '*'), "invalid exponent"
                                                            if(term[8] not in alphabet):
                                                                if(term[8] != "-"):
                                                                    str_exponent_var_index1 = term[8]
                                                                    # print(f"exponent is {str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1)
                                                                elif(term[8] == "-"):
                                                                    str_exponent_var_index1 = term[9]
                                                                    # print(f"exponent is -{str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1) * -1
                                    elif(term[4] == "-"):
                                        str_exponent_var_index0 = term[5]
                                        # print(f"exponent is -{str_exponent_var_index0}")
                                        exponent_var_index0 = float(str_exponent_var_index0) * -1
                                        if(term_length > 6):
                                            if(term[6] in independent_variables):
                                                if(term[6] == independent_variables[1]):
                                                    # print(f"{independent_variables[1]} is the second variable")
                                                    if(exponent_var_index1 == 0): 
                                                        exponent_var_index1 = 1
                                                    if(term_length > 7):
                                                        if(term[7] == '*'):
                                                            assert(term_length > 9), "invalid exponent"
                                                            assert(term[8] == '*'), "invalid exponent"
                                                            if(term[9] not in alphabet):
                                                                if(term[9] != "-"):
                                                                    str_exponent_var_index1 = term[9]
                                                                    # print(f"exponent is {str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1)
                                                                elif(term[9] == "-"):
                                                                    str_exponent_var_index1 = term[10]
                                                                    # print(f"exponent is -{str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1) * -1





                    elif(term[1] == independent_variables[1]):
                        # print(f"{independent_variables[1]} is the first variable")
                        if (term_length > 2):
                            if(term[2] in independent_variables)& (num_var_index0 != 0):
                                if(term[2] == independent_variables[0]):
                                    # print(f"{independent_variables[0]} is the second variable")
                                    if(exponent_var_index0 == 0): 
                                        exponent_var_index0 = 1
                            if(term[2] == '*'):
                                assert(term_length > 4), "invalid exponent"
                                assert(term[3] == '*'), "invalid exponent"
                                if(term[4] not in alphabet):
                                    if(term[4] != "-"):
                                        str_exponent_var_index1 = term[4]
                                        # print(f"exponent is {str_exponent_var_index1}")
                                        exponent_var_index1 = float(str_exponent_var_index1)
                                        if(term_length > 5):
                                            if(term[5] in independent_variables):
                                                if(term[5] == independent_variables[0]):
                                                    # print(f"{independent_variables[0]} is the second variable")
                                                    if(exponent_var_index0 == 0): 
                                                        exponent_var_index0 = 1
                                                    if(term_length > 6):
                                                        if(term[6] == '*'):
                                                            assert(term_length > 8), "invalid exponent"
                                                            assert(term[7] == '*'), "invalid exponent"
                                                            if(term[8] not in alphabet):
                                                                if(term[8] != "-"):
                                                                    str_exponent_var_index0 = term[8]
                                                                    # print(f"exponent is {str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0)
                                                                elif(term[8] == "-"):
                                                                    str_exponent_var_index0 = term[9]
                                                                    # print(f"exponent is -{str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0) * -1
                                    elif(term[4] == "-"):
                                        str_exponent_var_index1 = term[5]
                                        # print(f"exponent is -{str_exponent_var_index1}")
                                        exponent_var_index1 = float(str_exponent_var_index1) * -1
                                        if(term_length > 6):
                                            if(term[6] in independent_variables):
                                                if(term[6] == independent_variables[0]):
                                                    # print(f"{independent_variables[0]} is the second variable")
                                                    if(exponent_var_index0 == 0): 
                                                        exponent_var_index0 = 1
                                                    if(term_length > 7):
                                                        if(term[7] == '*'):
                                                            assert(term_length > 9), "invalid exponent"
                                                            assert(term[8] == '*'), "invalid exponent"
                                                            if(term[9] not in alphabet):
                                                                if(term[9] != "-"):
                                                                    str_exponent_var_index0 = term[9]
                                                                    # print(f"exponent is {str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0)
                                                                elif(term[9] == "-"):
                                                                    str_exponent_var_index0 = term[10]
                                                                    # print(f"exponent is -{str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0) * -1


            if(term[0] in alphabet):
                constant = 1
                str_constant = "1"
                # print("constant: "+ str_constant)
                # print(constant)
                assert term[0] in independent_variables, "variable must be one of the independent variables!"
                if(term[0] == independent_variables[0]):
                    # print(f"{independent_variables[0]} is the first variable")
                    if(exponent_var_index0 == 0): 
                        exponent_var_index0 = 1
                    if (term_length > 1):
                            if(term[1] in independent_variables)& (num_var_index1 != 0):
                                if(term[1] == independent_variables[1]):
                                    # print(f"{independent_variables[1]} is the second variable")
                                    if(exponent_var_index1 == 0): 
                                        exponent_var_index1 = 1
                            if(term[1] == '*'):
                                assert(term_length > 3), "invalid exponent"
                                assert(term[2] == '*'), "invalid exponent"
                                if(term[3] not in alphabet):
                                    if(term[3] != "-"):
                                        str_exponent_var_index0 = term[3]
                                        # print(f"exponent is {str_exponent_var_index0}")
                                        exponent_var_index0 = float(str_exponent_var_index0)
                                        if(term_length > 4):
                                            if(term[4] in independent_variables):
                                                if(term[4] == independent_variables[1]):
                                                    # print(f"{independent_variables[1]} is the second variable")
                                                    if(term_length > 5):
                                                        if(term[5] == '*'):
                                                            assert(term_length > 7), "invalid exponent"
                                                            assert(term[6] == '*'), "invalid exponent"
                                                            if(term[7] not in alphabet):
                                                                if(term[7] != "-"):
                                                                    str_exponent_var_index1 = term[7]
                                                                    # print(f"exponent is {str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1)
                                                                elif(term[7] == "-"):
                                                                    str_exponent_var_index1 = term[8]
                                                                    # print(f"exponent is -{str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1) * -1
                                    elif(term[3] == "-"):
                                        str_exponent_var_index0 = term[4]
                                        # print(f"exponent is -{str_exponent_var_index0}")
                                        exponent_var_index0 = float(str_exponent_var_index0) * -1
                                        if(term_length > 5):
                                            if(term[5] in independent_variables):
                                                if(term[5] == independent_variables[1]):
                                                    # print(f"{independent_variables[1]} is the second variable")
                                                    if(exponent_var_index1 == 0): 
                                                        exponent_var_index1 = 1
                                                    if(term_length > 6):
                                                        if(term[6] == '*'):
                                                            assert(term_length > 8), "invalid exponent"
                                                            assert(term[7] == '*'), "invalid exponent"
                                                            if(term[8] not in alphabet):
                                                                if(term[8] != "-"):
                                                                    str_exponent_var_index1 = term[8]
                                                                    # print(f"exponent is {str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1)
                                                                elif(term[8] == "-"):
                                                                    str_exponent_var_index1 = term[9]
                                                                    # print(f"exponent is -{str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1) * -1



                elif(term[0] == independent_variables[1]):
                    # print(f"{independent_variables[1]} is the first variable")
                    if(exponent_var_index1 == 0): 
                        exponent_var_index1 = 1
                    if (term_length > 1):
                            if(term[1] in independent_variables) & (num_var_index0 != 0):
                                if(term[1] == independent_variables[0]):
                                    # print(f"{independent_variables[0]} is the second variable")
                                    if(exponent_var_index0 == 0): 
                                        exponent_var_index0 = 1
                            if(term[1] == '*'):
                                assert(term_length > 3), "invalid exponent"
                                assert(term[2] == '*'), "invalid exponent"
                                if(term[3] not in alphabet):
                                    if(term[3] != "-"):
                                        str_exponent_var_index1 = term[3]
                                        # print(f"exponent is {str_exponent_var_index1}")
                                        exponent_var_index1 = float(str_exponent_var_index1)
                                        if(term_length > 4):
                                            if(term[4] in independent_variables):
                                                if(term[4] == independent_variables[0]):
                                                    # print(f"{independent_variables[0]} is the second variable")
                                                    if(exponent_var_index0 == 0): 
                                                        exponent_var_index0 = 1
                                                    if(term_length > 5):
                                                        if(term[7] == '*'):
                                                            assert(term_length > 7), "invalid exponent"
                                                            assert(term[6] == '*'), "invalid exponent"
                                                            if(term[7] not in alphabet):
                                                                if(term[7] != "-"):
                                                                    str_exponent_var_index0 = term[7]
                                                                    # print(f"exponent is {str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0)
                                                                elif(term[7] == "-"):
                                                                    str_exponent_var_index0 = term[8]
                                                                    # print(f"exponent is -{str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0) * -1
                                    elif(term[3] == "-"):
                                        str_exponent_var_index1 = term[4]
                                        # print(f"exponent is -{str_exponent_var_index1}")
                                        exponent_var_index1 = float(str_exponent_var_index1) * -1
                                        if(term_length > 5):
                                            if(term[5] in independent_variables):
                                                if(term[5] == independent_variables[0]):
                                                    # print(f"{independent_variables[0]} is the second variable")
                                                    if(exponent_var_index0 == 0): 
                                                        exponent_var_index0 = 1
                                                    if(term_length > 6):
                                                        if(term[6] == '*'):
                                                            assert(term_length > 7), "invalid exponent"
                                                            assert(term[7] == '*'), "invalid exponent"
                                                            if(term[8] not in alphabet):
                                                                if(term[8] != "-"):
                                                                    str_exponent_var_index0 = term[8]
                                                                    # print(f"exponent is {str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0)
                                                                elif(term[8] == "-"):
                                                                    str_exponent_var_index0 = term[9]
                                                                    # print(f"exponent is -{str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0) * -1


        elif(is_negative == True):
            assert term[0] == '-', "claims to be negative but doesnt start with a '-' sign."
            assert term_length >= 2, "term length error, should be 2 or more characters if has the negative sign."
            # print("term is negative!")
            if(term[1] not in alphabet):
                str_constant = term[1]
                # print("constant: " + "-" + str_constant)
                constant = float(str_constant)*(-1)
                # print("constant value is " + str(constant) + ".")
                if(term_length > 2):
                    assert term[2] in independent_variables, "invalid format, variable after constant must be one of the independent variables!"
                    if(term[2] == independent_variables[0]):
                        # print(f"{independent_variables[0]} is the first variable")
                        if(exponent_var_index0 == 0): 
                            exponent_var_index0 = 1
                        if (term_length > 3):
                            if(term[3] in independent_variables) & (num_var_index1 != 0):
                                if(term[3] == independent_variables[1]):
                                    # print(f"{independent_variables[1]} is the second variable")
                                    if(exponent_var_index1 == 0): 
                                        exponent_var_index1 = 1
                            if(term[3] == '*'):
                                assert(term_length > 5), "invalid exponent"
                                assert(term[4] == '*'), "invalid exponent"
                                if(term[5] not in alphabet):
                                    if(term[5] != "-"):
                                        str_exponent_var_index0 = term[5]
                                        # print(f"exponent is {str_exponent_var_index0}")
                                        exponent_var_index0 = float(str_exponent_var_index0)
                                        if(term_length > 6):
                                            if(term[6] in independent_variables):
                                                if(term[6] == independent_variables[1]):
                                                    # print(f"{independent_variables[1]} is the second variable")
                                                    if(exponent_var_index1 == 0): 
                                                        exponent_var_index1 = 1
                                                    if(term_length > 7):
                                                        if(term[7] == '*'):
                                                            assert(term_length > 9), "invalid exponent"
                                                            assert(term[8] == '*'), "invalid exponent"
                                                            if(term[9] not in alphabet):
                                                                if(term[9] != "-"):
                                                                    str_exponent_var_index1 = term[9]
                                                                    # print(f"exponent is {str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1)
                                                                elif(term[9] == "-"):
                                                                    str_exponent_var_index1 = term[10]
                                                                    # print(f"exponent is -{str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1) * -1
                                    elif(term[5] == "-"):
                                        str_exponent_var_index0 = term[6]
                                        # print(f"exponent is -{str_exponent_var_index0}")
                                        exponent_var_index0 = float(str_exponent_var_index0) * -1
                                        if(term_length > 7):
                                            if(term[7] in independent_variables):
                                                if(term[7] == independent_variables[1]):
                                                    # print(f"{independent_variables[1]} is the second variable")
                                                    if(exponent_var_index1 == 0): 
                                                        exponent_var_index1 = 1
                                                    if(term_length > 8):
                                                        if(term[8] == '*'):
                                                            assert(term_length > 10), "invalid exponent"
                                                            assert(term[9] == '*'), "invalid exponent"
                                                            if(term[10] not in alphabet):
                                                                if(term[10] != "-"):
                                                                    str_exponent_var_index1 = term[10]
                                                                    # print(f"exponent is {str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1)
                                                                elif(term[10] == "-"):
                                                                    str_exponent_var_index1 = term[11]
                                                                    # print(f"exponent is -{str_exponent_var_index1}")
                                                                    exponent_var_index1 = float(str_exponent_var_index1) * -1





                    elif(term[2] == independent_variables[1]):
                        # print(f"{independent_variables[1]} is the first variable")
                        if(exponent_var_index1 == 0): 
                            exponent_var_index1 = 1
                        
                        
                        if (term_length > 3):
                            if(term[3] in independent_variables) & (num_var_index0 != 0):
                                if(term[3] == independent_variables[0]):
                                    # print(f"{independent_variables[0]} is the second variable")
                                    if(exponent_var_index0 == 0): 
                                        exponent_var_index0 = 1
                            if(term[3] == '*'):
                                assert(term_length > 5), "invalid exponent"
                                assert(term[4] == '*'), "invalid exponent"
                                if(term[5] not in alphabet):
                                    if(term[5] != "-"):
                                        str_exponent_var_index1 = term[5]
                                        # print(f"exponent is {str_exponent_var_index1}")
                                        exponent_var_index1 = float(str_exponent_var_index1)
                                        if(term_length > 6):
                                            if(term[6] in independent_variables):
                                                if(term[6] == independent_variables[0]):
                                                    # print(f"{independent_variables[0]} is the second variable")
                                                    if(exponent_var_index0 == 0): 
                                                        exponent_var_index0 = 1
                                                    if(term_length > 7):
                                                        if(term[7] == '*'):
                                                            assert(term_length > 9), "invalid exponent"
                                                            assert(term[8] == '*'), "invalid exponent"
                                                            if(term[9] not in alphabet):
                                                                if(term[9] != "-"):
                                                                    str_exponent_var_index0 = term[9]
                                                                    # print(f"exponent is {str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0)
                                                                elif(term[9] == "-"):
                                                                    str_exponent_var_index0 = term[10]
                                                                    # print(f"exponent is -{str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0) * -1
                                    elif(term[5] == "-"):
                                        str_exponent_var_index1 = term[6]
                                        # print(f"exponent is -{str_exponent_var_index1}")
                                        exponent_var_index1 = float(str_exponent_var_index1) * -1
                                        if(term_length > 7):
                                            if(term[7] in independent_variables):
                                                if(term[7] == independent_variables[0]):
                                                    # print(f"{independent_variables[0]} is the second variable")
                                                    if(exponent_var_index0 == 0): 
                                                        exponent_var_index0 = 1
                                                    if(term_length > 8):
                                                        if(term[8] == '*'):
                                                            assert(term_length > 10), "invalid exponent"
                                                            assert(term[9] == '*'), "invalid exponent"
                                                            if(term[10] not in alphabet):
                                                                if(term[10] != "-"):
                                                                    str_exponent_var_index0 = term[10]
                                                                    # print(f"exponent is {str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0)
                                                                elif(term[10] == "-"):
                                                                    str_exponent_var_index0 = term[11]
                                                                    # print(f"exponent is -{str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0) * -1



            if(term[1] in alphabet):
                constant = -1
                str_constant = "1"
                # print("constant: " + "-"+ str_constant)
                # print(constant)
                assert term[1] in independent_variables, "variable must be one of the independent variables!"
                if(term[1] == independent_variables[0]):
                    # print(f"{independent_variables[0]} is the first variable")
                    if(exponent_var_index0 == 0): 
                        exponent_var_index0 = 1
                    if (term_length > 2) & (num_var_index1 != 0):
                        if(term[2] in independent_variables):
                            if(term[2] == independent_variables[1]):
                                # print(f"{independent_variables[1]} is the second variable")
                                if(exponent_var_index1 == 0): 
                                        exponent_var_index1 = 1
                        if(term[2] == '*'):
                            assert(term_length > 4), "invalid exponent"
                            assert(term[3] == '*'), "invalid exponent"
                            if(term[4] not in alphabet):
                                if(term[4] != "-"):
                                    str_exponent_var_index0 = term[4]
                                    # print(f"exponent is {str_exponent_var_index0}")
                                    exponent_var_index0 = float(str_exponent_var_index0)
                                    if(term_length > 5):
                                        if(term[5] in independent_variables):
                                            if(term[5] == independent_variables[1]):
                                                # print(f"{independent_variables[1]} is the second variable")
                                                if(exponent_var_index1 == 0): 
                                                    exponent_var_index1 = 1
                                                if(term_length > 6):
                                                    if(term[6] == '*'):
                                                        assert(term_length > 8), "invalid exponent"
                                                        assert(term[7] == '*'), "invalid exponent"
                                                        if(term[8] not in alphabet):
                                                            if(term[8] != "-"):
                                                                str_exponent_var_index1 = term[8]
                                                                # print(f"exponent is {str_exponent_var_index1}")
                                                                exponent_var_index1 = float(str_exponent_var_index1)
                                                            elif(term[8] == "-"):
                                                                str_exponent_var_index1 = term[9]
                                                                # print(f"exponent is -{str_exponent_var_index1}")
                                                                exponent_var_index1 = float(str_exponent_var_index1) * -1
                                elif(term[4] == "-"):
                                    str_exponent_var_index0 = term[5]
                                    # print(f"exponent is -{str_exponent_var_index0}")
                                    exponent_var_index0 = float(str_exponent_var_index0) * -1
                                    if(term_length > 6):
                                        if(term[6] in independent_variables):
                                            if(term[6] == independent_variables[1]):
                                                # print(f"{independent_variables[1]} is the second variable")
                                                if(exponent_var_index1 == 0): 
                                                    exponent_var_index1 = 1
                                                if(term_length > 7):
                                                    if(term[7] == '*'):
                                                        assert(term_length > 9), "invalid exponent"
                                                        assert(term[8] == '*'), "invalid exponent"
                                                        if(term[9] not in alphabet):
                                                            if(term[9] != "-"):
                                                                str_exponent_var_index1 = term[9]
                                                                # print(f"exponent is {str_exponent_var_index1}")
                                                                exponent_var_index1 = float(str_exponent_var_index1)
                                                            elif(term[9] == "-"):
                                                                str_exponent_var_index1 = term[10]
                                                                # print(f"exponent is -{str_exponent_var_index1}")
                                                                exponent_var_index1 = float(str_exponent_var_index1) * -1





                elif(term[1] == independent_variables[1]):
                    # print(f"{independent_variables[1]} is the first variable")
                    if(exponent_var_index1 == 0): 
                        exponent_var_index1 = 1
                    if (term_length > 2) & (num_var_index0 != 0):
                            if(term[2] in independent_variables):
                                if(term[2] == independent_variables[0]):
                                    # print(f"{independent_variables[0]} is the second variable")
                                    if(exponent_var_index0 == 0): 
                                        exponent_var_index0 = 1
                            if(term[2] == '*'):
                                assert(term_length > 4), "invalid exponent"
                                assert(term[3] == '*'), "invalid exponent"
                                if(term[4] not in alphabet):
                                    if(term[4] != "-"):
                                        str_exponent_var_index1 = term[4]
                                        # print(f"exponent is {str_exponent_var_index1}")
                                        exponent_var_index1 = float(str_exponent_var_index1)
                                        if(term_length > 5):
                                            if(term[5] in independent_variables):
                                                if(term[5] == independent_variables[0]):
                                                    # print(f"{independent_variables[0]} is the second variable")
                                                    if(term_length > 6):
                                                        if(term[6] == '*'):
                                                            assert(term_length > 8), "invalid exponent"
                                                            assert(term[7] == '*'), "invalid exponent"
                                                            if(term[8] not in alphabet):
                                                                if(term[8] != "-"):
                                                                    str_exponent_var_index0 = term[8]
                                                                    # print(f"exponent is {str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0)
                                                                elif(term[8] == "-"):
                                                                    str_exponent_var_index0 = term[9]
                                                                    # print(f"exponent is -{str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0) * -1
                                    elif(term[4] == "-"):
                                        str_exponent_var_index1 = term[5]
                                        # print(f"exponent is -{str_exponent_var_index1}")
                                        exponent_var_index1 = float(str_exponent_var_index1) * -1
                                        if(term_length > 6):
                                            if(term[6] in independent_variables):
                                                if(term[6] == independent_variables[0]):
                                                    # print(f"{independent_variables[0]} is the second variable")
                                                    if(term_length > 7):
                                                        if(term[7] == '*'):
                                                            assert(term_length > 9), "invalid exponent"
                                                            assert(term[8] == '*'), "invalid exponent"
                                                            if(term[9] not in alphabet):
                                                                if(term[9] != "-"):
                                                                    str_exponent_var_index0 = term[9]
                                                                    # print(f"exponent is {str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0)
                                                                elif(term[9] == "-"):
                                                                    str_exponent_var_index0 = term[10]
                                                                    # print(f"exponent is -{str_exponent_var_index0}")
                                                                    exponent_var_index0 = float(str_exponent_var_index0) * -1

        # print("TERM: " + term)
        data = (constant, independent_variables[0], independent_variables[1], num_var_index0, num_var_index1, exponent_var_index0, exponent_var_index1)
        # print("data is " + str(data))
        # print("constructing function...")
        # if(num_var_index0 != 0) & (num_var_index1 != 0):
        #     # print(str(constant) + independent_variables[0] + "**" + str(exponent_var_index0) + independent_variables[1] + "**" + str(exponent_var_index1))
        #     # print(str(constant) + independent_variables[0] + "**" + str(exponent_var_index0) + independent_variables[1] + "**" + str(exponent_var_index1))
        # elif(num_var_index0 == 0) & (num_var_index1 != 0):
        #     # print(str(constant) + independent_variables[0] + "**" + str(exponent_var_index0) + independent_variables[1] + "**" + str(exponent_var_index1))
        #     # print(str(constant) + independent_variables[1] + "**" + str(exponent_var_index1))
        # elif(num_var_index0 != 0) & (num_var_index1 == 0):
        #     # print(str(constant) + independent_variables[0] + "**" + str(exponent_var_index0) + independent_variables[1] + "**" + str(exponent_var_index1))
        #     # print(str(constant) + independent_variables[0] + "**" + str(exponent_var_index0))
        # elif(num_var_index0 == 0) & (num_var_index1 == 0):
        #     # print(str(constant) + independent_variables[0] + "**" + str(exponent_var_index0) + independent_variables[1] + "**" + str(exponent_var_index1))
        #     # print(str(constant))
        # else:
        #     # print(str(constant) + independent_variables[0] + "**" + str(exponent_var_index0) + independent_variables[1] + "**" + str(exponent_var_index1))
            
        #     # print("error")
        term_data.append(data)
            



    return(term_data)


def function(x,y, user_input):
    term_data = construct_function(0,0, user_input)
    # print(term_data)
    term_outputs = []
    for data in term_data:
        term_output = data[0]*(x**data[5])*(y**data[6])
        term_outputs.append(term_output)
    output = add_terms(term_outputs)
    return(output)

def get_input():
    print("enter a function in the form 'z=k1x**q1y**q2+k2x**q1y**q2+...' or 'f(x,y)=k1x**q1y**q2+k2x**q1y**q2+...'; \nFor the purposes of this application, sin(x), cos(x), tan(x), e, and ln(x) do not work.")
    string_input = str(input())
    string_input = string_input.lower().replace(" ", "")
    print("entered equation: ", string_input) 
    return(string_input)


def plotFunction(domainX:tuple, domainY:tuple, tickLength):
    
    assert len(domainX) == 2, "domain should be a tuple containing 2 values"
    assert len(domainY) == 2, "range should be a tuple containing 2 values"
    x_coords = np.arange(domainX[0], domainX[1], tickLength)
    y_coords = np.arange(domainY[0], domainY[1], tickLength)
    x_coords, y_coords = np.meshgrid(x_coords, y_coords)
    # R = np.sqrt(X**2 + Y**2)
    # Z = np.sin(R)
    user_equation = get_input()

    vfunc = np.vectorize(function)
    Z = vfunc(x_coords, y_coords, user_equation)
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    # ax.scatter(x_coords, y_coords, function(x_coords, y_coords), marker = '.', c = 'k')
    surf = ax.plot_surface(x_coords, y_coords, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    # Customize the z axis.
    # ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')
    plt.show()
    pass

plotFunction((-10,10), (-10,10), .25)
