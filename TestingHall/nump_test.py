# sourcery skip: use-fstring-for-concatenation
import numpy as np
from Utilities import reorder_array

# a.shape is (5,4)
A1 = []
for _i in range(10):
    i = str(_i)
    A1.append([
        ["aa"+i,"ab"+i,"ac"+i],
        ["ba"+i,"bb"+i,"bc"+i,],
        ["ca"+i,"cb"+i,"cc"+i,],
    ])
A1 = np.array(A1)
A2 = reorder_array(A1)

########################################################################################################
B1 = []
for _i in range(10):
    i = str(_i)
    B1.append([
        ["a"+i,"b"+i,"c"+i]
    ])
B1 = np.array(B1)
B2 = reorder_array(B1)

print(B1)
print("")
print(B2)