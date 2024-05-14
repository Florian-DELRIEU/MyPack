import matplotlib.pyplot as plt
from Body2D import Character2D

def plot_character(Character = Character2D):
    assert type(Character) is Character2D
    plt.plot(Character.x,Character.y,Character.color)

C1 = Character2D(0,0,1,0)

plt.figure("TEST")
#plot_character(C1)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()
