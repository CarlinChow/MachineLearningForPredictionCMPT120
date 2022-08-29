#   function file for functions used in main.py

import turtle
#   import turtle used for graphing function

def generate_input(filename, ColumnStartPos, ColumnEndPos):
    #   input ~ name of the file, the position of the start column used for input set, and the end position of column + 1 
    #   output ~ a list of sublist with float values from the columns selected
    file = open(filename, 'r', encoding='utf8', errors='ignore')
    unecessary_header = file.readline()
    input_list = []
    for line in file:
        datalist = line.strip().split(',')
        input_data = datalist[ColumnStartPos:ColumnEndPos]
        input_sublist = []
        for i in input_data:
            input_sublist.append(float(i))
        input_list.append(input_sublist)
    return(input_list)
        
def generate_output(filename, ColumnPos):
    #   input ~ name of file and the position of the column used for the output list
    #   output ~ a list of float values from the column selected
    file = open(filename, 'r', encoding='utf8', errors='ignore')
    unecessary_header = file.readline()
    output_list = []
    for line in file:
        datalist = line.strip().split(',')
        output_data = datalist[ColumnPos]
        output_float = float(output_data)
        output_list.append(output_float)
    return(output_list)

def percentage_error(actual_value, predicted_value):
    #   input ~ the list of test output values, and the list of predicted values 
    #   output ~ a list of values of the percentage errors, removes any cases where the test output value is 0 
    percentage_error_list = []
    for x in range(len(actual_value)):
        if actual_value[x] == 0:
            percentage = 0 
        else:
            percentage_error_list.append((abs(actual_value[x]-predicted_value[x])/actual_value[x])*100)
    return(percentage_error_list)

def count(percentages):
    #   input ~ a list of percentages
    #   output ~ a dictionary of the number of percentages in certain intervals
    less_than_10 = 0
    between_10_20 = 0
    between_20_30 = 0 
    between_30_40 = 0
    between_40_50 = 0
    between_50_60 = 0
    between_60_70 = 0 
    between_70_80 = 0 
    between_80_90 = 0 
    between_90_100 = 0 
    greater_than_100 = 0 
    for i in percentages:
        if i <= 10:
            less_than_10 += 1
        elif 10 < i <= 20:
            between_10_20 += 1
        elif 20 < i <= 30:
            between_20_30 += 1 
        elif 40 < i <= 50:
            between_40_50 += 1
        elif 50 < i <= 60:
            between_50_60 += 1
        elif 60 < i <= 70:
            between_60_70 += 1
        elif 70 < i <= 80:
            between_70_80 += 1
        elif 80 < i <=90:
            between_80_90 += 1
        elif 90 < i <= 100:
            between_90_100 += 1
        elif i > 100:
            greater_than_100 += 1 
    dictionary = {"<10%": less_than_10, "10% < 20%": between_10_20, "20% < 30%": between_20_30, "30% < 40%": between_30_40, "40% < 50%": between_40_50, "50% < 60%": between_50_60, "60% < 70%": between_60_70, "70% < 80%": between_70_80, "80% < 90%": between_80_90, "90% < 100%": between_90_100, "< 100%": greater_than_100}
    return(dictionary)

def graph_dict(dictionary):
    #   input ~ a dictionary 
    #   output ~ draws a graph with turtle from the results obtained from the dictionary
    wn = turtle.Screen()
    j = turtle.Turtle()
    j.penup()
    j.goto(-300, 0)
    j.pendown()
    Font = ('Times New Roman', 12, 'normal')
    for i in dictionary:
        h = dictionary[i]
        j.right(90)
        j.color("white")
        j.forward(15)
        j.color("black")
        j.write(i, align = 'left', font = Font)
        j.left(180)
        j.color("white")
        j.forward(15)
        j.color("black")
        j.forward(h+2)
        j.write(h, align = 'left', font = Font)
        j.right(180)
        j.left(90)
        j.forward(75)
        j.right(90)
        j.forward(h+2)
        j.left(90)
    input("")


