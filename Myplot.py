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

def add_figure(pos:tuple,size:tuple = (640/1440,480/900)):
    screen_format = get_ScreenFormat()
    size_x = size[0]
    size_y = size[1] / screen_format
    fig = plt.figure(figsize=(size_x,size_y),dpi=get_ScreenSize()[0])
    move_figure(fig,pos[0],pos[1])
    return fig
