# Python program to read an excel file
import openpyxl
import pandas as pd

PATH = "dataset_symptoms.xlsx"


df = pd.read_excel(PATH)
dict = df.to_dict()

#create symptom and disease list
d_list=[]
s_list=[]
#put disease into the list
for index in range (len(dict["Disease"])):
    if not dict["Disease"][index] in d_list:
        d_list.append(dict["Disease"][index])

for key in dict:
    print(key)