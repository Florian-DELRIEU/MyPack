import os

def getOS():
    """
    Verifie sur quelle machine le code est exécuté
    :return: :MAC: ou :PC:
    """
    if os.getcwd()[0] == "":TERMINAL = "MAC"
    else:                   TERMINAL = "PC"
    return TERMINAL

def goto_Onedrive():
    if this_Terminal.os == "MAC":
        os.chdir("/Users/floriandelrieu/OneDrive/")
    elif this_Terminal.os == "PC":
        os.chdir("D:/OneDrive/")

def OneDrive_path():
    if this_Terminal.os == "MAC":
        path = "/Users/floriandelrieu/OneDrive/"
    elif this_Terminal.os == "PC":
        path = "D:/OneDrive/"
    return path

TERMINAL = getOS()