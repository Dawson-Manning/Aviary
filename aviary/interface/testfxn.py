import numpy as np
import csv
from tkinter import *
import aviary.api as av
from copy import deepcopy
import math
import tkinter as tk
import tkinter.ttk as ttk
data = deepcopy(av.CoreMetaData)
list_values = list(data.values())
list_keys = list(data.keys())
list_len = len(list_values)
root = Tk()
wid=root.winfo_screenwidth()
hei=root.winfo_screenheight()
root.geometry("%dx%d" % (wid,hei))
root.state("zoomed")
root.title("Model Aircraft Input")



name_each_subhead = []
entries_per_subhead = []
old_subhead =''
for key in list_keys:
    if ':' in key:
        subhead = key.split(':')[1]
        if subhead == old_subhead:
            entries_per_subhead[-1] += 1
        else:
            entries_per_subhead.append(1)
            name_each_subhead.append(subhead)
        old_subhead = subhead
    else:
        entries_per_subhead.append(1)
        name_each_subhead.append(key)
rows_per_subhead=[]
compound_subheaders=[]
v=0
for num in entries_per_subhead:
    rows = math.ceil(num/3)
    rows_per_subhead.append(rows)
    compound_subheaders.append(v)
    v+=1
compound_data_rows=[0]
for i,nums in enumerate(rows_per_subhead): 
    val=sum(rows_per_subhead[:i+1])
    compound_data_rows.append(val)
    if len(compound_data_rows)==87:
        break
compound_data_entries=[]
for i, nums in enumerate(entries_per_subhead):
    val = sum(entries_per_subhead[:i+1])
    compound_data_entries.append(val)
index_list=[]
number = 0
mini_list=[0]
for num in compound_data_entries:
    for i in range(number,num):    
        if number < num-1:
            number +=1
            mini_list.append(number)
    index_list.append(mini_list)
    mini_list=[]
#################################################################
# print(data)
import os

path = os.path.abspath(os.path.dirname(__file__))
x = path.replace("interface", "utils\legacy_code_data\gasp_default_values.dat")
dict={}
with open(x, 'r') as file:
    for line in file:
        y = line.split("=")
        name = y[0]
        value = y[-1].split(",")[0]
        dict[name] = value
print(dict)
        
