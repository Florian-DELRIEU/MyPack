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
