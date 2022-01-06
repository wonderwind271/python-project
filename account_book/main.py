import pandas as pd
import numpy as np

records=pd.read_csv('account.csv',names=['item','price','date','method','note'])
# print(records.loc[0])
records_data=np.array(records)
# print(records_data)

print("successfully read data, please input commands. Input help to get a manual for the commands")

help_list=[]
cmd=""
while cmd!='q':
    cmd=input("> ")
    # start processing
    if cmd=='help':
        print(help_list)
    elif cmd=='l' or cmd=='list':
        print(records.to_string())



