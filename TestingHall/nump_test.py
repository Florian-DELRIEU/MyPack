# sourcery skip: use-fstring-for-concatenation
import numpy as np
from Utilities import reorder_array

# a.shape is (5,4)
A = []
for _i in range(10):
    i = str(_i)
    A.append([
        ["aa"+i,"ab"+i,"ac"+i],
        ["ba"+i,"bb"+i,"bc"+i,],
        ["ca"+i,"cb"+i,"cc"+i,],
    ])
A = np.array(A)
B = reorder_array(A)
