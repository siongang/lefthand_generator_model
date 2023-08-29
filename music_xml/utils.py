# input_list = ['c', 'a', 'a3b#4e2', 'a4a#5', 'a4','b-4']


# turns training data set to the more flexible list set
def turn_to_training(input_list):
    output_list = []
    for item in input_list:
        if len(item) == 2 or len(item) == 1:
            output_list.append([item])
        else:
            temp = []
            var = ""
            for letter in item:
                if letter.isalpha() and var != "":
                    if letter != var: # that means that it is on the next note
                        temp.append(var) # 
                        var = letter # reset the var to the next note
                else:
                    var = var + letter

            temp.append(var)
            output_list.append(temp)
    return output_list
 


import pandas as pd
import os


# turn a folder that holds txt files into a list of dataframes of those txt files.
def to_pd(path):
    file_names = os.listdir(path)
    data = []
    for file_name in file_names:
        full_path = path+file_name

        with open(full_path, 'r') as file:
            lines = file.read().splitlines()
        data.append(lines)
    return data


# turn a folder that holds txt files into a list of dataframes of those txt files.
def to_pd_single(full_path):
    data = []
    with open(full_path, 'r') as file:
        lines = file.read().splitlines()
  
    data.append(lines)
    return data

import pandas as pd
def combine_data(left, right):
    df = pd.DataFrame(left, columns=["L"])
    df["R"] = right
    return df