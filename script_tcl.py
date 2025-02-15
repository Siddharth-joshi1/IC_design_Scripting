# Import necessary libraries
import os
import numpy as np
import pandas as pd1  # Incorrect alias, should be 'pd'
import shutil
import csv

# List all files in the 'Modules' directory
models = os.listdir("Modules") 
print(models)



# Run Vivado in batch mode with the TCL script to create the project
os.system("vivado -mode batch -source tcl_create.tcl")  

# Iterate over all modules and add them using a TCL script
for model in models:
    os.system("vivado -mode batch -source  tcl_add.tcl -tclargs {}".format(model))

# Create a directory to store results
os.mkdir("results")

# Iterate over all modules, create individual result directories, and run the TCL script
data_files = [] #only append implemented files in the data files list

for filename in models:
    os.mkdir("results/"+filename[:-2])
    os.system("vivado -mode batch -source  tcl_run.tcl -tclargs {}".format(filename))
    synth_file = open("synth_status", "r")
    synth_status = synth_file.read().split()[-1]
    if synth_status == "ERROR":
        print(f"Synthesis failed for {filename}")
        continue
    impl_file = open("impl_status", "r")
    impl_status = impl_file.read().split()[-1]
    if impl_status == "ERROR":
        print(f"Implementation failed for {filename}")
        continue
    data_files.append(filename[:-2])
    print("{} reported".format(filename)) 
