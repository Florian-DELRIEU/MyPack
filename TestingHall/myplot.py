from MyPack2.Myplot import add_subplots, add_figure, add_subfigures
import matplotlib.pyplot as plt

DEBUG_CASE = 2

if DEBUG_CASE == 1:
    fig1 = add_figure((0,0))
    plt.plot([1,2,1])

    f,a = add_subplots((1,2),fullscreen=True)
    a[0].plot([1,2,1],"bo")
    a[1].plot([1,2,1],"r-")

elif DEBUG_CASE == 2:
    add_subfigures(2,2)