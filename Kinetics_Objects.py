import numpy as np
from MyPack2.Saves.CSV import Dict2CSV
import matplotlib as plt

class Domain2D:
    """
    Objet représentant le domaine d'évolution des corps 2D. Cet objet regroupe des paramètres de gravité, de frottement
    etc...
    """
    def __init__(self):
        self.g_vector   = 9.81*np.array(0,-1)
        self.rho_atmos  = 1.25

class KineticBody2D:
    """
    Objet possédant les caractérisques d'un corps en mouvement dans un plan 2D.
    """
    def __init__(self, m=5, x=0, y=0, vx=0, vy=0, drag_surface=1, drag_coef=0.1,Domain=Domain2D):
        self.rho = Domain.rho_atmos
        self.g = Domain.g_vector

        self.mass = m
        self.drag_surface = drag_surface
        self.drag_coefficient = drag_coef
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = 0
        self.ay = 0

        self.V = np.sqrt(self.vx**2 + self.vy**2)
        self.A = np.sqrt(self.ax**2 + self.ay**2)

        self.color = "r"
        self.Name = ""

        self.list_x = []
        self.list_y = []
        self.list_vx = []
        self.list_vy = []
        self.list_ax = []
        self.list_ay = []

    def save_kinetics(self):
        self.list_x.append(self.x)
        self.list_y.append(self.y)
        self.list_vx.append(self.vx)
        self.list_vy.append(self.vy)
        self.list_ax.append(self.ax)
        self.list_ay.append(self.ay)

    def refresh(self,dt=1):
        """

        :param dt:
        :return:
        """

    def calcul_acceleration(self):
        velocity = self.vx**2 + self.vy**2
        vel_unit_vector = np.array(self.vx,self.vy) / velocity

        drag = 1/2 * self.rho * self.drag_surface * velocity**2 * self.drag_coefficient * (-vel_unit_vector)
        grav = self.g*self.mass
        

class AstralBody:
    def __init__(self,Domain,CI_pos:tuple=(0,0),CI_speed:tuple=(0,0),mass:float=0):
        """
        Comporte toutes les caractérisques et données d'un objet célèste
        :param Domain: objet :class Universe: nécéssaire comportant les données du domain dans lequel il évolue
            -
        """
        self.Domain = Domain  # Liaison avex l'objet :Univere:
        self.G = Domain.G  # Recupere G de l'objet :Universe:
    # Variable definitions
        self.Mass = mass
        self.x = CI_pos[0]
        self.y = CI_pos[1]
        self.vx = CI_speed[0]
        self.vy = CI_speed[1]
        self.ax = float(0)
        self.ay = float(0)
        Domain.BodyList.append(self)  # S'ajoute lui-même dans liste de l'univers
        self.Bodylist = Domain.BodyList.copy()  # Listes des autres corps dans :Universe:
        self.IsMoving = True  # Si :False: l'objet ne peut pas bouger
    # Paramètres garphiques
        self.filename = ""
        self.Color = ""
        self.Mark = "o"
        self.Kinetic = {}
        self.Kinetic["Time"] = np.array(Domain.t)
        self.Kinetic["x"] = []
        self.Kinetic["y"] = []
        self.Kinetic["vx"] = np.array([])
        self.Kinetic["vy"] = np.array([])
        self.Kinetic["ax"] = np.array([])
        self.Kinetic["ay"] = np.array([])

    def __repr__(self):
        return f"""Astral Body
            - Pos = ({self.x} , {self.y})
            - Mass = {self.Mass}
        """

    def refresh(self,dt):
        if self.IsMoving:  # si il peut bouger
            self.Body_list = self.Domain.BodyList.copy() # Obliger de faire une copy de la liste
            self.Body_list.remove(self)  # se supprime lui meme pour eviter auto-influence
            self.ax, self.ay = 0,0  # refresh pour eviter cumuls des acc avec itération précédente
            # Calcul de l'accéleration due à la présence de chaque corps
            for this_body in self.Body_list:
                cur_distance = np.sqrt((this_body.x - self.x)**2 + (this_body.y - self.y)**2)  # distance
                # Calcul des accélérations
                self.ax += - self.G * this_body.Mass / cur_distance**3 * (self.x - this_body.x)
                self.ay += - self.G * this_body.Mass / cur_distance**3 * (self.y - this_body.y)
            # Calcul des vitesses
            self.vx += self.ax*dt
            self.vy += self.ay*dt
            # Calcul des nouvelles positions
            self.x += self.vx*dt
            self.y += self.vy*dt
            self.Kinetic["x"] = np.append(self.Kinetic["x"],self.x)
            self.Kinetic["y"] = np.append(self.Kinetic["y"],self.y)
            self.Kinetic["vx"] = np.append(self.Kinetic["vx"],self.vx)
            self.Kinetic["vy"] = np.append(self.Kinetic["vy"],self.vy)
            self.Kinetic["ax"] = np.append(self.Kinetic["ax"],self.ax)
            self.Kinetic["ay"] = np.append(self.Kinetic["ay"],self.ay)

    def Gvector(self,ratio=1):
        """
        Affiche le vecteur accélération de :self:
        """
        self.Body_list = self.Domain.BodyList.copy()  # Obliger de faire une copy de la liste
        self.Body_list.remove(self)  # se supprime lui meme pour eviter auto-influence
        self.ax, self.ay = 0, 0  # refresh pour eviter cumuls des acc avec itération précédente
        # Calcul de l'accéleration due à la présence de chaque corps
        for this_body in self.Body_list:
            cur_distance = np.sqrt((this_body.x - self.x) ** 2 + (this_body.y - self.y) ** 2)  # distance
            # Calcul des accélérations
            self.ax += - self.G * this_body.Mass / cur_distance ** 3 * (self.x - this_body.x)
            self.ay += - self.G * this_body.Mass / cur_distance ** 3 * (self.y - this_body.y)
        plt.arrow(self.x,self.y,ratio*self.ax,ratio*self.ay)
        self.ax, self.ay = 0, 0  # refresh pour eviter cumuls des acc avec itération précédente

    def setbody(self,x,y,Mass):
        """
        Definition rapide d'un astre
        :param x: Position x initiale
        :param y: Position y initiale
        :param Mass: Masse
        """
        self.x = x
        self.y = y
        self.Mass = Mass

    def setvelocity(self,vx,vy):
        """
        Définition rapide d'une vitesse (souvent utilisé pour ajouter une vitesse initiale
        :param vx: vitesse selon x
        :param vy: vitesse selon y
        """
        self.vx = vx
        self.vy = vy

    def setCI(self,pos:tuple,speed:tuple,mass:float):
        self.setbody(pos[0],pos[1],mass)
        self.setvelocity(speed[0],speed[1])

    def DoBurn(self,Prograde=0,Radial=0):
        """
        Effectue une poussé dans les deux directions tangeantielles ou radiales à la vitesse
        """
        DV_p = Prograde
        DV_r = Radial
        Theta_p = np.arctan(self.vy/self.vx)  # Angle du vecteur vitesse
        Theta_r = Theta_p + np.pi/2  # Angle du vecteur radiale (vers le centre de l'ellipse)
        V_p = np.sqrt(self.vx**2 + self.vy**2)
        V_r = 0

        V_p += DV_p
        V_r += DV_r

        self.vx = np.cos(Theta_p)*V_p + np.cos(Theta_r)*V_r
        self.vy = np.sin(Theta_p)*V_p + np.sin(Theta_r)*V_r

    def SaveKinetic(self,filename=""):
        filename = self.set_filename(filename)
        Dict2CSV(self.Kinetic, f"{filename}.csv")

    def set_filename(self,filename=None):
        # sourcery skip: remove-redundant-if, remove-redundant-pass
        if (filename == "" or None) and (self.filename == "" or None):
            filename = f"Body_{self.bodylist_indic()}"
            self.filename = filename
        elif filename == ["" or None] and self.filename != ["" or None]:
            filename = self.filename
        else: pass
        return filename

    def bodylist_indic(self):
        arr = np.array(self.Domain.BodyList)
        return int(np.where(arr==self)[0])