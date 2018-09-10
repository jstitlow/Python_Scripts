## Find AND Sum Volume.csv files from Imaris segmentation
## Run script from directory (STATS) containing all of the Statistics output 
## directories from Imaris segmentation. 
## 22 June 2016- Josh Titlow
## rev 16 December 2016 JST

import glob
import os
import shutil
import pandas as pd

## Make directory called Volumes and place Volume files in it
os.makedirs ('Volumes')

files = glob.glob('*/*Volume.csv')

for file in files:
    shutil.copy(file, 'Volumes')

## Read all files in directory, filter out non-csv
files = [os.path.join('Volumes', f)
         for f in os.listdir('Volumes') if f.endswith(".csv")]

## Make list of tuples [(filename, sum)] and calculate sum
sums =  [(filename, pd.read_csv(filename, skiprows=3)["Value"].sum())
         for filename in files ]

## Place sums into a dataframe
df = pd.DataFrame(sums, columns=["filename", "sum"])
df.to_csv(os.path.join('Volumes', "files_with_Volume_sum.csv"))


## Make directory called Intensities and place Intensity Sum files in it
os.makedirs ('Intensities')

files = glob.glob('*/*Sum_Ch=1.csv')

for file in files:
    shutil.copy(file, 'Intensities')

## Read all files in directory, filter out non-csv
files = [os.path.join('Intensities', f)
         for f in os.listdir('Intensities') if f.endswith(".csv")]

## Make list of tuples [(filename, sum)] and calculate sum
sums =  [(filename, pd.read_csv(filename, skiprows=3)["Value"].sum())
         for filename in files ]

## Place sums into a dataframe
df = pd.DataFrame(sums, columns=["filename", "sum"])
df.to_csv(os.path.join('Intensities', "files_with_Intensity_sum.csv"))
