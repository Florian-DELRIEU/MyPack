"""
Regroupe différentes méthodes générales pour diveres applications
"""
import numpy as np
import string
import time as t

alphabet_low = list(string.ascii_lowercase)
alphabet_up = list(string.ascii_uppercase)


def truncSignificatif(num,nbSignificatif):
    """
    Tronque  :num: et ne garde que :nbSignificatif: chiffres significatifs
        - si num est un :int(): alors ne fait rien
    :param num: float a tronquer
    :param nbSignificatif: Nombre de chiffre significatif a garder
    :return:
    """
    if type(num) == int:
        return num
    NumInString = str(num)
    if nbSignificatif <= len(NumInString.split('.')[0]): # si plus petit que la taille de la partie non decimale
        TrunquedNum = NumInString[:nbSignificatif] # Affiche les chiffres significatifs voulue
        for _ in np.arange(len(NumInString.split('.')[0]) - nbSignificatif):
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
    """
    FIXME
        Ne marche quand num est en ecriture scientifique
            - ex: 1.2348e-05 renvoie 1.2348 au lieu de 0.000012348
    :param num:
    :param nbDecimal:
    :return:
    """
    if type(num) == int:
        return num
    NumInString = str(num)
    NumInList = NumInString.split(".")
    if len(NumInList) == 1:
        TrunquedNum = num
    else:
        NonDecimal = NumInString.split(".")[0]
        Decimal = NumInString.split(".")[1]
        if nbDecimal < len(Decimal):
            TrunquedNum = f"{NonDecimal}.{Decimal[:nbDecimal]}"
            TrunquedNum = float(TrunquedNum)
        else:
            TrunquedNum = num
        if nbDecimal == 0:
            TrunquedNum = int(NonDecimal)
    return TrunquedNum

def AskUser(Phrase,ValeurDefaut):
    Phrase += f" [{ValeurDefaut}] :  "
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
    newDico = {}
    for thisKey in KeyList:
        if thisKey in Dico.keys(): newDico[thisKey] = Dico[thisKey]
        elif Log:
            print(f"{str(thisKey)} not found !")
    return newDico

def int2rom(number=int()):
    """
    Renvoie la traduction d'un chiffre arabe en chiffre romains.
        -> Le programme ne peut pas traduire des chiffres au dela de 3999 car il est necéssaire d'avoir le signe pour
        5000 et au delà en chiffre romain. Je n'ai pas trouvé comment faire ce signe
    :param number: Entier entre 0 et 3999
    """
    roman= str()
    assert type(number) is int and number > 0 , "Must be an integer greater than 0"
    assert number < 4000 , "This program can't translate number over 3999 now. Need the roman sign for 5000"
    while number != 0:
        if number//1000 != 0:
            roman += "M"
            number -= 1000
        elif number//500 != 0:
            roman += "D"
            number -= 500
        elif number//100 != 0:
            roman += "C"
            number -= 100
        elif number//50 != 0:
            roman += "L"
            number -= 50
        elif number//10 != 0:
            roman += "X"
            number -= 10
        elif number//5 != 0:
            roman += "V"
            number -= 5
        elif number//1 != 0:
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

def rom2int(roman=str()):
    """
    Renvoie la traduction d'un chiffre romain en chiffre arabe
        ->  Le programme ne peut pas traduire des chiffres au dela de 3999 car il est necéssaire d'avoir le signe pour
            5000 et au delà en chiffre romain. Je n'ai pas trouvé comment faire ce signe
        ->  :ErrorList: doit être complété par l'ensemble des erreurs d'écriture des chiffres romains
    :param roman: Chiffre romain a traduire (I,V,X,L,C,D,M seulement)
    """
    number = 0
    ErrorList = ["IL","IC","ID","IM",  # Liste des erreures d'ecritures
                 "VL","VC","VD","VM",
                 "XD","XM",
                 "LM"]
    assert type(roman) is str , "roman must be a string"
    for l in roman:
        if l not in ["I","V","X","L","C","D","M"]:  assert False , "roman must be composed by I,V,X,L,C,D,M signs only"
    for el in ErrorList:
        if roman.find(el) != -1:                assert False, "Error roman number badly written"

    while roman != "":
        if "M" in roman:
            number += 1000
            roman = roman.replace("M","",1)
        elif "CM" in roman:
            number += 900
            roman = roman.replace("CM","",1)
        elif "CD" in roman:
            number += 400
            roman = roman.replace("CD","",1)
        elif "XC" in roman:
            number += 90
            roman = roman.replace("XC","",1)
        elif "XL" in roman:
            number += 40
            roman = roman.replace("XL","",1)
        elif "IX" in roman:
            number += 9
            roman = roman.replace("IX","",1)
        elif "IV" in roman:
            number += 4
            roman = roman.replace("IV","",1)
        elif "D" in roman:
            number += 500
            roman = roman.replace("D","",1)
        elif "C" in roman:
            number += 100
            roman = roman.replace("C","",1)
        elif "L" in roman:
            number += 50
            roman = roman.replace("L","",1)
        elif "X" in roman:
            number += 10
            roman = roman.replace("X","",1)
        elif "V" in roman:
            number += 5
            roman = roman.replace("V","",1)
        elif "I" in roman:
            number += 1
            roman = roman.replace("I","",1)
    return number

def Join_AsStrings(object:list() or tuple(),join_item = ""):
    """
    Join all element in :list: or :tuple: in a single :string: joined by optionnal item
    :param object: list or tuple that contains all string to join
    :param join_item: item added between all items added
    """
    txt = str()
    for string in object:
        txt += str(string) + join_item
    return txt

def random_string(lenght=int()):
    return "".join(np.random.choice(alphabet_low + alphabet_up) for _ in range(lenght))

def progress_print(iterable, loop_total=int(), loop_increment=list() or int(), show_time=1):
    if type(loop_increment) == int:
        loop_increment = loop_increment*np.arange(loop_total//loop_increment)
    if iterable in loop_increment:
        print(f"Progress Status:{iterable}  ({iterable/loop_total*100}%)")
    if iterable == loop_total - 1:
        print("Done -- 100 %")

def reorder_array(arr,axe_indice=1):
    """
    TODO
        Faire une description détaillé

    fixme  ne marche pas correctement, les valeurs ne sont pas dans le bon ordre
    :param arr:
    :param axe_indice:
    :return:
    """
    array_order = len(arr.shape)
    if array_order == 3:
        new_array = np.empty_like(arr)
        for i in range(arr.shape[1]):
            for j in range(arr.shape[2]):
                new_array[:,i,j] = arr[:,i,j] #fixme erreur ici



### TEST_ZONE
A = np.array([
       [
        ['aa0', 'ab0', 'ac0'],
        ['ba0', 'bb0', 'bc0'],
        ['ca0', 'cb0', 'cc0']],
       [['aa1', 'ab1', 'ac1'],
        ['ba1', 'bb1', 'bc1'],
        ['ca1', 'cb1', 'cc1']],
       [['aa2', 'ab2', 'ac2'],
        ['ba2', 'bb2', 'bc2'],
        ['ca2', 'cb2', 'cc2']],
       [['aa3', 'ab3', 'ac3'],
        ['ba3', 'bb3', 'bc3'],
        ['ca3', 'cb3', 'cc3']],
       [['aa4', 'ab4', 'ac4'],
        ['ba4', 'bb4', 'bc4'],
        ['ca4', 'cb4', 'cc4']],
       [['aa5', 'ab5', 'ac5'],
        ['ba5', 'bb5', 'bc5'],
        ['ca5', 'cb5', 'cc5']],
       [['aa6', 'ab6', 'ac6'],
        ['ba6', 'bb6', 'bc6'],
        ['ca6', 'cb6', 'cc6']],
       [['aa7', 'ab7', 'ac7'],
        ['ba7', 'bb7', 'bc7'],
        ['ca7', 'cb7', 'cc7']],
       [['aa8', 'ab8', 'ac8'],
        ['ba8', 'bb8', 'bc8'],
        ['ca8', 'cb8', 'cc8']],
       [['aa9', 'ab9', 'ac9'],
        ['ba9', 'bb9', 'bc9'],
        ['ca9', 'cb9', 'cc9']]])
reorder_array(A)