"""
Module for importing data and convert a file into a list or a dictionnary
"""
import numpy as np
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def File2List(DataFileName):
    """
    For import DataFile have only 
    -------------
    DATA
    DATA
    DATA
    -------------
    """
    File_cont = open(DataFileName,"r").read()
    Data = list()
    for el in File_cont.splitlines():
        if el == "\n" or el ==  "" : continue
#        else:
#        	try: Data.append(float(el))
#            finally:

    return np.array(Data)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def File2Dict(DataFileName,separator="***"):
    convert = bool
    Output = {}
    convertList = []
    FileToImport = open(DataFileName,"r")
    FileList = FileToImport.read().split(separator+"\n")
    for data in FileList:
        curList = data.splitlines()
        for line in curList:
            if line == "": curList.remove(line)
            if line == "\n": curList.remove(line)
        curTitle = curList[0]
        curList.remove(curTitle)
        for line in curList:
            try:
                line = float(line)
                convertList.append(line)
                convert = True
            except:
                convert = False
                continue
        Output[curTitle] = convertList.copy() if convert else curList.copy()
        curList.clear()
        convertList.clear()

    return Output

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def Dict2File(Dico,FileName,separator="***"):
    try:
        assert type(Dico) is dict
    except:
        return AssertionError , "Dico must be a dictionnary"
    File = open(FileName,"w")
    for loop, k in enumerate(Dico.keys()):
        if loop != 0:
            File.write(separator+"\n")
        File.write(str(k)+"\n")
        for el in Dico[k]:
            File.write(str(el)+"\n")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def List2File(List,FileName):
    try:
        assert type(List) is list
    except:
        return AssertionError , "List must be a list"

    File = open(FileName,"w")
    
    for el in List:
        File.write(str(el))
        if el != List[-1]: File.write("\n")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def AsPoint(DataFileName,convert=True):
    """
    Import data from file 
    Return two list (X_data and Y_Data)
    ****************
    TITLE
    -- Separator ---
    x data
    y data
    -- Separator ---
    x data
    y data
    ****************
    """
    X_data = []
    Y_data = []
    LastImport = None
    Data = open(DataFileName,"r")
    LineList = Data.readlines()
    for line in LineList:
        if str(line).isalpha():
            continue
        if str(line).isnumeric():
            if LastImport == (None or "Y"): 
                X_data.append(float(line))
                LastImport = "X"
            if LastImport == (None or "X"):
                Y_data.append(float(line))
                LastImport = "Y"
    return X_data,Y_data

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def SaveInFile(VarName,DataFileName):
    """
    Add --VarName-- into a txt file to save it
    """
    try:
        file = open(DataFileName,"a")
    except:
        file = open(DataFileName,"w")
    
    file.write("\n {}".format(VarName))
    file.close()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------


