"""
Regroup all functions that can write and read in a JSON file for a Python Object
"""
import json

def SaveAsJSON(data:list or dict,filename:str):
    file = open(filename+".txt","w")
    json.dump(data,file)

def LoadFromJSON(filename:str):
    json_file = open(filename)
    return json.load(json_file)