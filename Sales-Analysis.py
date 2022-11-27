import pandas as pd
import os

df = pd.read_csv("SalesAnalysis\Sales_Data\Sales_April_2019.csv")
files = [file for file in os.listdir('SalesAnalysis\Sales_Data')]

all_months_data = pd.DataFrame(
for file in files:
    print (file)
    
