from MyPack_git.Math import div_euclid

def Hour2decimal(time:str="hh:mm:ss",separator=":"):
    hours = int(time.split(separator)[0])
    minutes = int(time.split(separator)[1])
    seconds = int(time.split(separator)[2])
    return  hours + minutes/60 + seconds/3600

def decimal2Hour(time:float,separator=":"):
    hours,rest = div_euclid(time,1)
    minutes,seconds = div_euclid(rest*60,1)
    seconds = round(seconds*60)
    if seconds >= 60:  # little fix loop sometimes round(seconds) = 60
        minutes += 1
        seconds -= 60
    return f"{int(hours)}{separator}{int(minutes)}{separator}{seconds}"

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
