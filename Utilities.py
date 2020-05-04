"""
Regroupe différentes méthodes générales pour diveres applications
"""
import numpy as np

def truncSignificatif(num,nbSignificatif):
    """
    Tronque  :num: et ne garde que :nbSignificatif: chiffres significatifs
    :param num: float a tronquer
    :param nbSignificatif: Nombre de chiffre significatif a garder
    :return:
    """
    NumInString = str(num)
    if nbSignificatif <= len(NumInString.split('.')[0]):    # si plus petit que la taille de la partie non decimale
        TrunquedNum = NumInString[:nbSignificatif] # Affiche les chiffres significatifs voulue
        for i in np.arange(len(NumInString.split('.')[0]) - nbSignificatif):
            """
            Verifie la difference entre la taille de la partie non decimale de :num: et le nombre de chiffre
            significatif pour afficher les "0" manquant
            ex : 123 000
                    | si 3 chiffres significatifs et partie non decimal de taille 6
            """
            TrunquedNum += "0"
        TrunquedNum = int(TrunquedNum)
    elif len(NumInString.split(".")) == 1:
        TrunquedNum = num
    else:
        Decimal_a_afficher = nbSignificatif - len(NumInString.split(".")[0]) # Nombre de decimal a afficher
        TrunquedNum = NumInString.split(".")[0] + "."
        TrunquedNum += NumInString.split(".")[1][:Decimal_a_afficher]
        TrunquedNum = float(TrunquedNum)
    return TrunquedNum

def truncDecimal(num,nbDecimal):
    NumInString = str(num)
    NonDecimal = NumInString.split(".")[0]
    Decimal = NumInString.split(".")[1]
    if nbDecimal < len(Decimal):
        TrunquedNum = NonDecimal + "." + Decimal[:nbDecimal]
        TrunquedNum = float(TrunquedNum)
    else:
        TrunquedNum = num
    if nbDecimal == 0:
        TrunquedNum = int(NonDecimal)

    return TrunquedNum

def AskUser(Phrase,ValeurDefaut):
    Phrase += " [{}] :  ".format(ValeurDefaut)
    output = input(Phrase)
    if output == "": output = ValeurDefaut

    return output

def getFromDict(Dico,KeyList,Log=False):
    """
    Creer un nouveau dictionnaire possedant une partie des :keys: de l'ancien
    param :Dico: Dictionnaire à copier en partie
    param :KeyList: Liste des :keys: à copier dans :Dico:
    param :Log: Si :True: affiche un log en cas d'erreur
    """
    newDico = dict()
    for thisKey in KeyList:
        if thisKey in Dico.keys(): newDico[thisKey] = Dico[thisKey]
        else:
            if Log: print(str(thisKey) + " not found !")
    return newDico

def inRoman(number):
    """
    Renvoie la traduction d'un chiffre arabe en chiffre romains.
        -> Le programme ne peut pas traduire des chiffres au dela de 3999 car il est necéssaire d'avoir le signe pour
        5000 et au delà en chiffre romain. Je n'ai pas trouvé comment faire ce signe
    :param number: Entier entre 0 et 3999
    """
    roman= str()
    assert type(number) is int and number > 0 , "Must be an integer greater than 0"
    assert number < 4000 , "This program can't translate number over 3999 now. Need the roman sign for 5000"
    while number is not 0:
        if number//1000 is not 0:
            roman += "M"
            number -= 1000
        elif number//500 is not 0:
            roman += "D"
            number -= 500
        elif number//100 is not 0:
            roman += "C"
            number -= 100
        elif number//50 is not 0:
            roman += "L"
            number -= 50
        elif number//10 is not 0:
            roman += "X"
            number -= 10
        elif number//5 is not 0:
            roman += "V"
            number -= 5
        elif number//1 is not 0:
            roman += "I"
            number -= 1
        else:  number = 0
    if "DCCCC" in roman: roman = roman.replace("DCCCC","CM")
    if "CCCC" in roman: roman = roman.replace("CCCC","CD")
    if "LXXXX" in roman: roman = roman.replace("LXXXX","XC")
    if "XXXX" in roman: roman = roman.replace("XXXX","XL")
    if "VIIII" in roman: roman = roman.replace("VIIII","IX")
    if "IIII" in roman: roman = roman.replace("IIII","IV")
    return roman