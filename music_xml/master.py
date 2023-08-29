import to_mid
import utils
import pandas as pd
import numpy as np
import main
import os

input_path = "xml_folder/saved_xml/classical/Invention_No_13_Bach.musicxml"
output_path = "xml_folder/working_txt//"
name = "test"
main.to_input_txt(input_path,output_path, name)


xml_folder_path = 'xml_folder/saved_xml/classical'  # Replace with the actual path


# Get a list of filenames in the folder
xml_filenames = [filename for filename in os.listdir(xml_folder_path) if filename.endswith('.musicxml')]

print(xml_filenames)






# path = 'predict_results.csv'


# Data = pd.read_csv(path)


# output = np.array(Data["L"])

# input = np.array(Data["R"])


# output = utils.turn_to_training(output)
# input = utils.turn_to_training(input)

# print(output)

# to_mid.audio(input, output, "TEST")