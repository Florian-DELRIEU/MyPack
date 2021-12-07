from MyPack2.Myplot import add_subplots,add_figure
import matplotlib.pyplot as plt


fig1 = add_figure((0,0))
plt.plot([1,2,1])

f,a = add_subplots((1,2),(0,0),(12,6))
a[0].plot([1,2,1],"bo")
a[1].plot([1,2,1],"r-")
