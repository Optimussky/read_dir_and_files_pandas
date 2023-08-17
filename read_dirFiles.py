#read_dirFiles.py

import os
import pandas as pd

# Set the directory where the Files are stored
directory = './' # pat to directory

# Iterate over all files in the directory
for file in os.listdir(directory):
    #Checkif the file is an Excel file
    if file.endswith('.xls') or file.endswith('xlsx'):
        #Read the Excel file into a pandas DtaFrame
        df = pd.read_excel(os.path.join(directory,file))
        #Print the DataFrame
        print(df)

