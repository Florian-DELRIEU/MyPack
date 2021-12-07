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

def add_figure(pos:tuple,size:tuple = (8,6),dpi=80):
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
    screen_format = get_ScreenFormat()
    size_x = size[0]
    size_y = size[1]
    fig = plt.figure(figsize=(size_x,size_y),dpi=dpi)
    move_figure(fig,pos[0],pos[1])
    return fig

def add_subplots(subplots:tuple,pos:tuple,size:tuple=(8,6),dpi=80):
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
    size_x = size[0]
    size_y = size[1]
    fig,ax = plt.subplots(subplots[0],subplots[1],figsize=(size_x,size_y),dpi=dpi)
    move_figure(fig,pos[0],pos[1])
    return fig,ax

def add_subfigure(nb_x:int,nb_y:int):
    """
    FIXME
        - Don't work
    :param nb_x:
    :param nb_y:
    :return:
    """
    part_x = get_ScreenSize()[0] / nb_x
    part_y = get_ScreenSize()[1] / nb_y
    size = (part_x,part_y)
    i_x = 0
    i_y = 0
    fig_list = []
    while i_x * i_y <= nb_x * nb_y:
        fig_list.append(
            add_figure(
            (0+i_x*size[0],
             0+i_y*size[1]))
        )
        if i_x == nb_x:
            i_x =  0
            i_y += 1
