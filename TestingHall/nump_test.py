import numpy as np

# a.shape is (5,4)
A = []
for _i in range(10):
    i = str(_i)
    A.append([
        ["aa"+i,"ab"+i,"ac"+i],
        ["ba"+i,"bb"+i,"bc"+i,],
        ["ca"+i,"cb"+i,"cc"+i,],
    ])

A = np.array(A) # shape is (10,3,3)
B = A.reshape(3,3,10)
C = A.copy()

# Affiche chaque éléments au cours du temps (ex aa(t), ab(t), etc...)
for i in range(A.shape[1]):
    for j in range(A.shape[2]):
        print(A[:,i,j])