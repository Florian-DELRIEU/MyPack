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

    def move(self, V, angle, dt):
        # Modification d'angle aléatoire
        angle = np.radians(angle)
        angle += np.random.random(2)*np.pi
        angle += np.degrees(angle)

        Vx = V * np.cos(angle)
        Vy = V * np.sin(angle)
        self.x += Vx*dt
        self.y += Vy*dt