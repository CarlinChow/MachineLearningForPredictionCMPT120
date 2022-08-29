#####################
### Building an Interactive Machine Learning Model
### Author: Eric Li, Carlin Chow
####################

#   import module sklearn and our function file
import function as f
from sklearn.linear_model import LinearRegression

#   ask user for input on the csv file provided that is added to folder
csv_file = input('What is the name of the csv file provided? (eg. "SeoulBikesData.csv") --> ')

#   ask user for columns used in input and output lists *** DATA SELECTED MUST BE ABLE TO CONVERT TO FLOAT VALUES ***
input_columnS = int(input("what column should the data being collected for your input list start at? (eg. 0, 5, 3) --> "))
input_columnE = (int(input("what column would the data for your input list stop at? (eg. 8, 7 , 3) --> "))+1)
output_column = int(input("what column is the output(predictions) in? (eg. 0, 1, 2) --> "))

#   generates an input and output list using our functions
input_list= f.generate_input(csv_file, input_columnS, input_columnE)
output_list = f.generate_output(csv_file, output_column)

#   splits input and output lists into testing and training list by slicing
training_input = input_list[0:int(len(input_list)*0.8)]
test_input = input_list[int(len(input_list)*0.8):]

training_output = output_list[0:int(len(output_list)*0.8)]
test_output = output_list[int(len(output_list)*0.8):]

#   train machine learning model by inputing our training set
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X = training_input, y = training_output)

#   input test data and makes a prediction with model
x_test = test_input
outcome = predictor.predict(X = x_test)

#   uses our functions to calculate the percentage errors and counting the number of percentage errors between certain intervals, and adding
#       into a dictionary, then graph dictionary data using turtle  
f.graph_dict(f.count(f.percentage_error(test_output, outcome)))

