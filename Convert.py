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
    Output = dict()
    convertList = list()
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
        if convert == True: Output[curTitle] = convertList.copy()
        if convert == False: Output[curTitle] = curList.copy()
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

    loop = 0
    for k in Dico.keys():
        if loop != 0:
            File.write(separator+"\n")
        loop += 1
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
    X_data = list()
    Y_data = list()
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
            if LastImport == "X": 
                Y_data.append(float(line))
                LastImport = "Y"

    outputList = X_data + [":"] + Y_data
    return X_data,Y_data

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def Csv2Dict(DataFileName,separator="***"):
    """
    Convert a CSV file into a dict with the first line as titles and other as data. Like column tabular
    """
    import csv

    DATA = dict()
    CSV = csv.reader(open(DataFileName,"r"))

    line = 0
    col = 0
    LOOP = True

    for row in CSV:
        N_col = len(row)
    del row
    
    while col < N_col:
        CSV = csv.reader(open(DataFileName,"r"))
        for row in CSV:
            if line == 0:
                curTitle = row[col]
                DATA[curTitle] = list()
            else:
                try:
                    DATA[curTitle].append(float(row[col]))
                except:
                    DATA[curTitle].append(row[col])
            line+=1
        col+=1
        line = 0
    return DATA

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def Dict2CSV(Dict,DataFileName,separator="***"):
    """
    Convert a Dictionnary into a CSV file.
    Keys are title in the first line line of the CSV file and data are below
    Data from any keys must have length

    """

    file = open(DataFileName,"w")
    row = 0
    N_keys = len(Dict.keys())
    N_row = list()

    i_key = 0
    for k in Dict.keys():
        if i_key < N_keys-1:
            file.write(str(k)+",")
        elif i_key == N_keys-1:
            file.write(str(k)+"\n")
        i_key+=1
    row = 0
    i_key = 0
    for k in Dict.keys():
        try:
            N_row.append(len(Dict[k]))
        except:
            N_row.append(1)
    N_row = max(N_row)
    while row < N_row:
        for k in Dict.keys():
            if i_key < N_keys-1:
                try:
                    file.write(str(Dict[k][row]) +",")
                except:
                    file.write(",")
            if i_key == N_keys-1:
                try:
                    file.write(str(Dict[k][row]) +"\n")
                except:
                    file.write("\n")
            i_key+=1
        row+=1
        i_key = 0

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
def SaveInCSV(VarName,DataFileName,Key):
    """
    Sauvegarde :VarName: dans un fichier .csv
    :param VarName:  Variable a sauvegarder
    :param DataFileName:  Nom du fichier .csv
    :param Key:  Colonne du .csv
    """
    file = open(DataFileName,"a")
    if type(VarName) is not list:
        VarName = [VarName]

    try:    DATA = Csv2Dict(DataFileName)  # Verifie si csv existe
    except: DATA = dict()  # sinon le cree

    for current_value in VarName:  # Sauvegarde tout les élement de :VarName:
        if Key in DATA.keys():  # si :key: existe dans le CSV
            i=0
            while i < len(DATA[Key]):
                el = DATA[Key][i]
                if el == "":  # Verifie si un case de la liste de :Data[key]: est vide
                    DATA[Key].remove(el)
                    i-=1
                i+=1
            DATA[Key].append(current_value)  # Ajoute valeur a save
        else:
            DATA[Key] = list()
            DATA[Key].append(current_value)

    Dict2CSV(DATA,DataFileName)

def Extract(CSVfile,key):
    """
    Extrait une donné d'un CSV sans passer par un dict()
    :param CSVfile:
    :param key: Colonne à extraire
    :return:
    """
    data = Csv2Dict(CSVfile)
    return np.array(data[key])

def Unzip(CSV_list):
    """
    Permet d'extraire plusieurs fichiers CSV dans une list de dict 
    :param CSVfile:
    :return:
    """
    LIST = list()
    for i, csv in enumerate(CSV_list):
        LIST.append(Csv2Dict(csv))
    return LIST

