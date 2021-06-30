from MyPack.Convert import *
import matplotlib.pyplot as plt
import numpy as np

def Unzip(CSV_list):
    LIST = list()
    for i,csv in enumerate(CSV_list):
        LIST.append(Csv2Dict(csv))
    return LIST

CSV_list = [
    "b1_Kinetic.csv",
    "b2_Kinetic.csv",
    "b3_Kinetic.csv"
]

x = Extract("b1_Kinetic.csv","x")

L = Unzip(CSV_list)