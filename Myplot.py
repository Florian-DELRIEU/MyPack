import matplotlib.pyplot as plt
import matplotlib
from MyPack2.Myos import TERMINAL
matplotlib.use("TkAgg")

def get_ScreenSize():
    if TERMINAL == "MAC":
        return 1440, 900
    elif TERMINAL == "PC":
        return 1800, 980
    else:
        return None, None

def get_ScreenFormat():
    screen = get_ScreenSize()
    return screen[0] / screen[1]

def move_figure(figure, x, y):
    """Move figure's upper left corner to pixel (x, y)
    from: https://stackoverflow.com/questions/7449585/how-do-you-set-the-absolute-position-of-figure-windows-with-matplotlib#:~:text=def%20move_figure(f,move(x%2C%20y)
    """
    x = x * get_ScreenSize()[0]
    y = y * get_ScreenSize()[1]
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        figure.canvas.manager.window.wm_geometry("+%d+%d"%(x, y))
    elif backend == 'WXAgg':
        figure.canvas.manager.window.SetPosition((x, y))
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        figure.canvas.manager.window.move(x, y)

def add_figure(pos:tuple=(0.2,0.1),size:tuple=(8,6),dpi=80,fullscreen=False):
    """
    :param pos: position of the figure:
                        - (0,0) is the upper left corner
                        - (1,1) is the lower right corner
    :param size: size of the figure:
                        - number of dpi in each side
                        - MAC: full size is (18,11.25) if dpi = 80
    :param dpi: dpi of the figure
    :return:    - figure
    """
    if fullscreen:
        size = (get_ScreenSize()[0]/dpi,get_ScreenSize()[1]/dpi)
        pos = (0,0)
    size_x = size[0]
    size_y = size[1]
    fig = plt.figure(figsize=(size_x,size_y),dpi=dpi)
    move_figure(fig,pos[0],pos[1])
    return fig

def add_subplots(subplots:tuple,pos:tuple=(0.2,0.1),size:tuple=(8,6),dpi=80,fullscreen=False):
    """
    :param subplots: tuple that return the number of subplots (n_row,n_colon)
    :param pos: position of the figure:
                        - (0,0) is the upper left corner
                        - (1,1) is the lower right corner
    :param size: size of the figure:
                        - number of dpi in each side
                        - MAC: full size is (18,11.25) if dpi = 80
    :param dpi: dpi of the figure
    :return:    - figure
                - ax : list of axes
    """
    if fullscreen:
        size = (get_ScreenSize()[0]/dpi,get_ScreenSize()[1]/dpi)
        pos = (0,0)
    size_x = size[0]
    size_y = size[1]
    fig,ax = plt.subplots(subplots[0],subplots[1],figsize=(size_x,size_y),dpi=dpi)
    move_figure(fig,pos[0],pos[1])
    return fig,ax

def add_subfigures(nb_x:int,nb_y:int,dpi=80):
    """
    FIXME
        - Don't work
        - /Users/floriandelrieu/OneDrive/Python/MyPack2/Myplot.py:50: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
          fig = plt.figure(figsize=(size_x,size_y),dpi=dpi)
    :param nb_x:
    :param nb_y:
    :return:
    """
    part_x = get_ScreenSize()[0] / nb_x
    part_y = get_ScreenSize()[1] / nb_y
    size = (part_x/dpi,part_y/dpi)
    i_x = 0
    i_y = 0
    fig_list = []
    while i_x * i_y <= (nb_x-1) * (nb_y-1):
        fig_list.append(
            add_figure(
                (0+i_x*size[0],0+i_y*size[1]),
                size, dpi=dpi
            )
        )
        if i_x == nb_x:
            i_x =  0
            i_y += 1
    return fig_list