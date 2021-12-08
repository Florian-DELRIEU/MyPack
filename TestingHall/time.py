from MyPack2.Time import Hour2decimal

DEBUG_CASE = 2

hour_list = [
    "00:01:00",
    "00:34:00",
    "00:23:00",
    "02:10:00",
]

if DEBUG_CASE == 1:
    for h in hour_list:
        print(Hour2decimal(h))

elif DEBUG_CASE == 2:
    l = [Hour2decimal(h) for h in hour_list]