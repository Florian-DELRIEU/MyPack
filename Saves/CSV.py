"""
Regroup all functions that can write and read in a CSV file for a Python Object
"""
import numpy as np
import csv

def Csv2Dict(DataFileName, separator="***"):
    """
    Convert a CSV file into a dict with the first line as titles and other as data. Like column tabular
    """
    DATA = {}
    CSV = csv.reader(open(DataFileName, "r"))
    line = 0
    col = 0
    LOOP = True
    for row in CSV:
        N_col = len(row)
    del row

    while col < N_col:
        CSV = csv.reader(open(DataFileName, "r"))
        for row in CSV:
            if line == 0:
                curTitle = row[col]
                DATA[curTitle] = []
            else:
                try:
                    DATA[curTitle].append(float(row[col]))
                except:
                    DATA[curTitle].append(row[col])
            line += 1
        col += 1
        line = 0
    return DATA
# ----------------------------------------------------------------------------------------------------------------------
def Dict2CSV(Dict, DataFileName, separator="***"):
    """
    Convert a Dictionnary into a CSV file.
    Keys are title in the first line line of the CSV file and data are below
    Data from any keys must have length

    """
    file = open(DataFileName, "w")
    row = 0
    N_keys = len(Dict.keys())
    N_row = []
    i_key = 0
    for k in Dict.keys():
        if i_key < N_keys - 1:
            file.write(str(k) + ",")
        elif i_key == N_keys - 1:
            file.write(str(k) + "\n")
        i_key += 1
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
            if i_key < N_keys - 1:
                try:
                    file.write(str(Dict[k][row]) + ",")
                except:
                    file.write(",")
            if i_key == N_keys - 1:
                try:
                    file.write(str(Dict[k][row]) + "\n")
                except:
                    file.write("\n")
            i_key += 1
        row += 1
        i_key = 0
# ----------------------------------------------------------------------------------------------------------------------
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
# ----------------------------------------------------------------------------------------------------------------------
def ExtractCSV(CSVfile,key):
    """
    Extrait une donné d'un CSV sans passer par un dict()
    :param CSVfile:
    :param key: Colonne à extraire
    :return:
    """
    data = Csv2Dict(CSVfile)
    return np.array(data[key])
# ----------------------------------------------------------------------------------------------------------------------
def UnzipCSV(CSV_list):
    """
    Permet d'extraire plusieurs fichiers CSV dans une list de dict
    :param CSVfile:
    :return:
    """
    LIST = []
    for i, csv in enumerate(CSV_list):
        LIST.append(Csv2Dict(csv))
    return LIST