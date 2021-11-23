import os

def getOS():
    """
    Verifie sur quelle machine le code est exécuté
    :return: :MAC: ou :PC:
    """
    return "MAC" if os.getcwd()[0] == "/" else "PC"

def goto_Onedrive():
    TERMINAL = getOS()
    if TERMINAL == "MAC":
        os.chdir("/Users/floriandelrieu/OneDrive/")
    elif TERMINAL == "PC":
        os.chdir("D:/OneDrive/")

def OneDrive_path():
    if TERMINAL == "MAC":   return "/Users/floriandelrieu/OneDrive/"
    elif TERMINAL == "PC":  return "D:/OneDrive/"
    else:                   return EnvironmentError , "Terminal not recognized"

def createPath(path):
    path_list = []
    current_path = os.getcwd()
    Terminal = getOS()
    ##
    if Terminal == "PC":    separator = "\\"
    elif Terminal == "MAC": separator = "/"
    else:                   return EnvironmentError, "Wrong terminal"
    ##
    if "/" in path:         path_list = path.split("/")
    elif "\\" in path:      path_list = path.split("\\")
    for el in path_list:  # Garde uniquement les noms de dossiers
        if ("/" or "\\" or "") in el: path_list.remove(el)
    for i, el in enumerate(path_list):
        try: os.mkdir(current_path+separator+el)
        except: pass
        finally:current_path += separator + el
    return path_list

TERMINAL = getOS()