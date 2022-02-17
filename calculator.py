from sys import exit
from math import sin,cos,tan,log
from mpmath import cot
from numpy import power


def main():
    op1 = introduction()
    if (op1 == 1): ## Basic calculator
#         op2_2 = 1
        while (op1 == 1):  # To cover several repetitions
            op1 = basic_calc()
        
        if (op1 == 2): # Back to main menu
            op1 = 9 # makes sure every nested main exits
            main()
            
#     print('this is ',op1)
    if (op1 == 2): ## Scientific calculator
        op1 = scientific_calc()
        while (op1 == 1):  # To cover several repetitions
            op1 = scientific_calc()
            
        if (op1 == 2): # Back to main menu
            op1 = 9 # makes sure every nested main exits
            main()
        
    if (op1 == 3): ## Conversion calculator
        op1 = conversion_calc()
        while (op1 == 1):  # To cover several repetitions
            op1 = conversion_calc()
            
        if (op1 == 2): # Back to main menu
            op1 = 9 # makes sure every nested main exits
            main()
            
    if (op1==9):   ## Scape calculator
        scape

def scape():
    exit()
###########################################################################
    
def introduction():
    print('\nWELCOME TO CALCULATOR PLUS \n')
    try: 
        op1 = int(input('''Select one of the modes: 
                1-Basic Calculator 
                2-Scientific Calculator
                3-Conversion Calculator
                9-Exit the program\n '''))
        if (op1 not in [1,2,3,9]):
                print('Error, it must be a number from [1,2,3 or 9]')
    except:
        print('Error, it must be a number from [1,2,3 or 9]')  # shows message
    return op1


########################################################################### BASIC CALCULATOR FUNCS
def basic_calc():
    print('''\nBasic calculator is set to work as follows:
          - The user specifies the amount of values to operate
          - Then the user specifies sequentially the values and operations (+,-,*,/)''')
    try:
        op2_1 = int(input('Amount of values to operate with\n'))
        
        if (input_posints(op2_1)): # checker of only natural values
            op2_3 = options_afteroperations()
            return op2_3
        
        if op2_1 < 2: # Check more than two inputs to operate
            print('\n[error] One parameter at least is required')
            op2_3 = options_afteroperations()
            return op2_3
        
        ## Gets the formula and solves it.
        sum_of_str = operations_loop(op2_1)
        
        # Check specs conditions in formula
        for i,item in enumerate(sum_of_str):
            if((i+1) % 2 == 0): # operador is on list ['+','-','/','*']
                flag_operador = is_operator_basic(item)
                if flag_operador:
                    op2_3 = options_afteroperations()
                    return op2_3
        
        # solves formula
        print('\nInput formula is '+sum_of_str,'\n','Result> ', eval(sum_of_str))
        
        ## Asks the next step
        op2_2 = options_afteroperations()
        return op2_2
    
    ## Checkers
    except (SyntaxError,ValueError,TypeError):
        print('\n[error] Somethings was wrong in the input')
        op2_3 = options_afteroperations()
        return op2_3
    
    except Exception as excp:
        print('hello you got some error\n')
        raise excp
                    
def input_posints(a):
    if (a < 0):
        print('\n[error] Only positive numbers are accepted')
        return True
    
def operations_loop(n): # n is the amount of values to operate with
    l_val_op = []
    for i in range(n):
        l_val_op.append(str(input('value in position {}\n'.format(i+1))))
        if (i != n-1): # Last element is a number not an operation
            l_val_op.append(str(input('operator in position {}\n'.format(i+1))))
            
    ## Miss checkers here        
    
    ## sum of strings
    sum_of_str = ''
    for item in l_val_op:
        sum_of_str =  sum_of_str + item
    
    return sum_of_str
    
def is_operator_basic(a):
    if (a not in ['+','-','/','*']):
        print('\n[error] Only operators in [+,-,/,*] are accepted')
        return True

def options_afteroperations():
    temp = int(input('''\n\nWhat next?: 
                1-Calculate new formula 
                2-Back to main menu
                9-Exit the program\n '''))
    return temp
########################################################################### SCIENTIFIC CALC.
def scientific_calc():
    print('''\nScientific calculator is set to work as follows:
          - The user specifies the amount of values to operate
          - Then the user specifies sequentially the values and operations (+,-,*,/,root,^,log,sin,cos,tan,cot)
          - Trigonometric funcs are in radians.''')
    try:
        op2_1 = int(input('Amount of values to operate with\n'))
        
        if (input_posints(op2_1)): # checker of only natural values
            op2_3 = options_afteroperations()
            return op2_3
        
        if op2_1 < 2: # Check more than two inputs to operate
            print('\n[error] One parameter at least is required')
            op2_3 = options_afteroperations()
            return op2_3
        
        ## Gets the formula and solves it.
        sum_of_str = operations_loop_sci(op2_1)
        
        # Check specs conditions in formula
#         for i,item in enumerate(sum_of_str):
#             print(i+1,item)
#             if((i+1) % 2 == 0): # operador is on list ['+','-','/','*']
#                 flag_operador = is_operator_scientific(item)
#                 if flag_operador:
#                     op2_3 = options_afteroperations()
#                     return op2_3
        
        # solves formula
        print('\nInput formula is '+sum_of_str,'\n')
        print('Result> ', eval(sum_of_str))
        
        ## Asks the next step
        op2_2 = options_afteroperations()
        return op2_2
    
    ## Checkers
    except (SyntaxError,ValueError,TypeError):
        print('\n[error] Somethings was wrong in the input')
        op2_3 = options_afteroperations()
        return op2_3
    
    except Exception as excp:
        print('hello you got some error\n')
        raise excp
                    
def input_posints(a):
    if (a < 0):
        print('\n[error] Only positive numbers are accepted')
        return True
    
def operations_loop_sci(n): # n is the amount of values to operate with
    l_val_op = []
    for i in range(n):
        l_val_op.append(str(input('value in position {}\n'.format(i+1))))
        if (i != n-1): # Last element, a x values formala has x-1 operations
            temp_operator = str(input('operator in position {}\n'.format(i+1)))
            
            if temp_operator in ['+','-','/','*']:
                l_val_op.append(temp_operator)
            
            if (temp_operator in ['sin','cos','tan','cot','log','root','^']):
                input_1 = str(input('Input the first basic operator\n'))
                if is_operator_basic(input_1):
                    scape
                
                if (temp_operator in ['sin','cos','tan','cot']):
                    input_2 = str(input('Input the number to apply the operation to\n'))
                    
                    # Solve the [sin,cos...] and add its sol to the rest of formula with the input_1 and input_3
                    small_operation = str(eval(temp_operator+'('+input_2+')'))
                    
                if (temp_operator in ['root','log','^']):
                    input_2_1 = str(input('Input the base value\n'))
                    input_2_2 = str(input('Input the value to apply the operation to\n'))
                    
                    if (temp_operator == 'root'):
                        input_2 = 'nthroot({},{})'.format(input_2_2,input_2_1)
                        small_operation = str(eval(input_2))
                    
                    if (temp_operator == 'log'):
                        input_2 = 'log({},{})'.format(input_2_2,input_2_1)
                        small_operation = str(eval(input_2))
                        
                    if (temp_operator == '^'):
                        input_2 = '{}**{}'.format(input_2_1,input_2_2)
                        small_operation = str(eval(input_2))
                    
                input_3 = str(input('Input the last basic operator\n'))
                if is_operator_basic(input_3):
                    scape
                
                l_val_op.append(input_1)
                l_val_op.append(small_operation)
                l_val_op.append(input_3)
            

    ## sum of strings
    sum_of_str = ''
    for item in l_val_op:
        sum_of_str =  sum_of_str + item
    return sum_of_str
    
def is_operator_scientific(a):
    if (a not in ['+','-','/','*','sin','cos','tan','cot','log','root','^']):
        print('\n[error] Only operators in [+,-,/,*,sin,cos,tan,cot,log,root,^] are accepted')
        return True

def nthroot(a,n):
    return power(a,(1/n))
########################################################################### CONVERSION CALCULATOR

def conversion_calc():
    print('''\nConversion calculator is set to work as follows:
          - The user specifies the magnitude type
          - Then select the conversion mode
          - Input the value''')
    try:
        op2_1 = int(input('''Magnitude type:
                1-Distance 
                2-Time
                3-Weight
                4-Temperature\n'''))
        
        if (op2_1 == 1): # Distance
            distance_func()
            op2_2 = options_afteroperations()
            return op2_2
        
        if (op2_1 == 2): # time
            time_func()
            op2_2 = options_afteroperations()
            return op2_2
        
        if (op2_1 == 3): # weight
            weight_func()
            op2_2 = options_afteroperations()
            return op2_2
        
        if (op2_1 == 4): # temperature
            temperature_func()
            op2_2 = options_afteroperations()
            return op2_2
        
        else:
            op2_3 = options_afteroperations()
            return op2_3

#         if op2_1 < 2: # Check more than two inputs to operate
#             print('\n[error] One parameter at least is required')
#             op2_3 = options_afteroperations()
#             return op2_3
        
       
#         # solves formula
#         print('\nInput formula is '+sum_of_str,'\n')
#         print('Result> ', eval(sum_of_str))
        
#         ## Asks the next step
#         op2_2 = options_afteroperations()
#         return op2_2
    
#     ## Checkers
#     except (SyntaxError,ValueError,TypeError):
#         print('\n[error] Somethings was wrong in the input')
#         op2_3 = options_afteroperations()
#         return op2_3
    
    except Exception as excp:
        print('hello you got some error\n')
        raise excp
        
def distance_func():
        op2_2_1 = int(input('''Select option:
                1-Km to Mile 
                2-Mile to Km
                3-cm to inch
                4-inch to cm\n'''))
        
        if (op2_2_1 == 1): # Km to Miles
            input_1 = float(input('input value:\n'))
            resul = input_1 * 0.621371
            print('{} Km are {} Miles'.format(input_1,resul))
            
        if (op2_2_1 == 2): # Miles to Km
            input_1 = float(input('input value:\n'))
            resul = input_1 / 0.621371
            print('{} Miles are {} Km'.format(input_1,resul))
        
        if (op2_2_1 == 3): # Cm to Inch
            input_1 = float(input('input value:\n'))
            resul = input_1 * 0.393701
            print('{} Cm are {} inches'.format(input_1,resul))
            
        if (op2_2_1 == 4):  # Inch to cm
            input_1 = float(input('input value:\n'))
            resul = input_1 / 0.393701
            print('{} inches are {} Cm'.format(input_1,resul))
        return
        
def time_func():
        op2_2_1 = int(input('''Select option:
                1-Hours to minutes 
                2-Hours to seconds
                3-Minutes to hours
                4-Minutes to seconds
                5-Seconds to hours
                6-Seconds to minutes\n'''))
        
        if (op2_2_1 == 1): # H to min
            input_1 = float(input('input value:\n'))
            resul = input_1 * 60
            print('{} H are {} min'.format(input_1,resul))
            
        if (op2_2_1 == 2): # H to s
            input_1 = float(input('input value:\n'))
            resul = input_1 * 60 * 60
            print('{} H are {} s'.format(input_1,resul))
        
        if (op2_2_1 == 3): # Min to H
            input_1 = float(input('input value:\n'))
            resul = input_1 / 60
            print('{} min are {} h'.format(input_1,resul))
            
        if (op2_2_1 == 4):  # Min to s
            input_1 = float(input('input value:\n'))
            resul = input_1 * 60
            print('{} min are {} s'.format(input_1,resul))
            
        if (op2_2_1 == 5):  # s to h
            input_1 = float(input('input value:\n'))
            resul = input_1 / 60 / 60
            print('{} seconds are {} h'.format(input_1,resul))
            
        if (op2_2_1 == 6):  # s to min
            input_1 = float(input('input value:\n'))
            resul = input_1 / 60
            print('{} s are {} mins'.format(input_1,resul))
        return

def weight_func():
        op2_2_1 = int(input('''Select option:
                1-Kg to pound 
                2-Pound to Kg\n'''))
        
        if (op2_2_1 == 1): # Kg to pound
            input_1 = float(input('input value:\n'))
            resul = input_1 * 2.20462
            print('{} Kg are {} pound'.format(input_1,resul))
            
        if (op2_2_1 == 2): # H to s
            input_1 = float(input('input value:\n'))
            resul = input_1 / 2.20462
            print('{} pounds are {} kg'.format(input_1,resul))
            
        return
            
def temperature_func():
        op2_2_1 = int(input('''Select option:
                1-Celsius to Fahrenheit 
                2-Celsius to Kelvin
                3-Fahrenheit to Celsius
                4-Fahrenheit to Kelvin
                5-Kelvin to Celsius
                6-Kelvin to Fahrenheit\n'''))
        
        if (op2_2_1 == 1): # cel to F
            input_1 = float(input('input value:\n'))
            resul = (input_1 * 9 / 5) + 32
            print('{} º are {} F'.format(input_1,resul))
            
        if (op2_2_1 == 2): # cel to K
            input_1 = float(input('input value:\n'))
            resul = input_1 + 273.15
            print('{} º are {} K'.format(input_1,resul))
            
        if (op2_2_1 == 3): # F to C
            input_1 = float(input('input value:\n'))
            resul = (input_1 - 32) * 5/9
            print('{} F are {} º'.format(input_1,resul))
            
        if (op2_2_1 == 4):  # F to K
            input_1 = float(input('input value:\n'))
            resul = ((input_1 - 32) * 5/9) + 273.15
            print('{} F are {} K'.format(input_1,resul))
            
        if (op2_2_1 == 5):  # K to cel
            input_1 = float(input('input value:\n'))
            resul = input_1 - 273.15
            print('{} K are {} º'.format(input_1,resul))
            
        if (op2_2_1 == 6):  # K to F
            input_1 = float(input('input value:\n'))
            resul = ((input_1 - 273.15) * 9 / 5) + 32
            print('{} K are {} F'.format(input_1,resul))
            
        return
###########################################################################

if __name__ == "__main__":
    main()