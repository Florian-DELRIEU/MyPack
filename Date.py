
def get_mounth(number:str or int):
    """
    Return the mounth regarding the number
    :param number:
    :return:
    """
    number = int(number) # verify :number: is a :int:
    Mounth_list = [
        "Janvier",
        "Fevrier",
        "Mars",
        "Avril",
        "Mai",
        "Juin",
        "Juillet",
        "Aout",
        "Septembre",
        "Octobre",
        "Novembre",
        "Decembre"
    ]
    return Mounth_list[number-1]