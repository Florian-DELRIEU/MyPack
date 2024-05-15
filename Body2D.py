import numpy as np

class Character2D:
    "Objet 2D se comportant comme un personnages dans un plan 2D"

    def __init__(self, x=0, y=0, V=1, angle=0):
        self.x = x
        self.y = y
        self.V = V
        self.angle = angle

        self.color = "bo"
        self.size = 1

    def move(self, dt):
        self.rd_angle()
        # Modification d'angle aléatoire
        Vx = self.V * np.cos(self.angle)
        Vy = self.V * np.sin(self.angle)
        self.x += Vx*dt
        self.y += Vy*dt

    def rd_angle(self):
        """
        Fais une selection random de l'angle
        """
        angle = np.radians(self.angle)
        angle += np.random.random(2) * np.pi
        self.angle += np.degrees(angle)
