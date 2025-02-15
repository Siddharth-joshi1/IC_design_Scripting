# Import necessary libraries
import os
import numpy as np
import pandas as pd  # Incorrect alias, should be 'pd'
import shutil
import csv

# List all directories in the 'results' folder
data_files = os.listdir("results")  


# Define the types of files to be processed
file_types = ['power.txt','timing.txt','utilization.txt']

# Define the required data fields to extract from the files
req_data = ['Total On-Chip Power','Data Path Delay','Slice LUTs']

# Initialize lists to store extracted values
Power = []
Delay = []
LUTs = []

# Iterate through each data file in the results directory
for data in data_files :
    for file in file_types:
        # Open each file and read its content
        with open("results/{}/{}".format(data,file),'r') as File:
             content = File.read()

        # Split content into lines
        words = content.split('\n')   

        # Extract power values if the file is 'power.txt'
        for req_word in words:
            if file_types[0] in file:
                if req_data[0] in req_word:
                    pwr = float(req_word.split()[6])  # Extract power value
                    print(pwr)
                    Power.append(pwr)
  
        # Extract delay values if the file is 'timing.txt'
        for req_word in words:
            if file_types[1] in file:
                if req_data[1] in req_word:
                    delay = float(req_word.split()[3][:-2])  # Extract delay value
                    print(delay)
                    Delay.append(delay)

        # Extract LUT values if the file is 'utilization.txt'
        for req_word in words:
            if file_types[2] in file:
                if req_data[2] in req_word:
                    luts = float(req_word.split()[4])  # Extract LUT count
                    print(luts) 
                    LUTs.append(luts) 
                    print("_____")          

# Combine extracted values into a single list
Final_results = [Power,Delay,LUTs]
row_name = ['Total On-Chip Power','Data Path Delay','Slice LUTs']

# Create a DataFrame from extracted results
df = pd.DataFrame(Final_results, index = row_name)
df.columns = data_files  # Set column names based on data file names

# Save the results to a CSV file
df.to_csv('Results_siddharth.csv', index = row_name)
print(df)
