from manim import *

class Circunferencia(Scene):
    def construct(self):
        # Crear una circunferencia con radio 2
        circunferencia = Circle(radius=2.0)
        
        # Cambiar el color de la circunferencia
        circunferencia.set_color(BLUE)
        
        # Mostrar la circunferencia en la escena
        self.play(Create(circunferencia))
        
        # Mantener la circunferencia en pantalla por un momento
        self.wait(2)

# Para ejecutar la animación, usa el siguiente comando en la terminal:
# manim -pql circunferencia.py Circunferencia
