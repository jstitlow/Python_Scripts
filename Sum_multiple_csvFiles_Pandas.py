import os 
import pandas as pd

# Get current working directory 
cwd = os.getcwd()

# Read all files in directory, filter out non-csv
files = [os.path.join(cwd, f) 
         for f in os.listdir(cwd) if f.endswith(".csv")] 
# Make list of tuples [(filename, sum)]
sums =  [(filename, pd.read_csv(filename, skiprows=3)["Value"].sum())
         for filename in files ]
# Make a dataframe
df = pd.DataFrame(sums, columns=["filename", "sum"])
df.to_csv(os.path.join(cwd, "files_with_sum.csv"))