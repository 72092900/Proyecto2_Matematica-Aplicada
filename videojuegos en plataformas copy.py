#Importaños a matplotlib
from tkinter import font
import matplotlib.pyplot as plt
 
# Declaramos valores para el eje y, en este caso son videojuegos
videojuegos = ['Pokémon R/V/A/A', 'GTA v', 'Tetris (Nintendo)', 'Minecraft', 'PUBG', 'Super Mario Bros', 'Wii sports', 'Wii Fit y Wii Fit Plus', 'Tetris (EA)', 'Pac-Man']
 
# Declaramos valores para el eje x, ahora son los descargas
Descargas = [47, 130, 43, 200, 60, 48, 82, 43, 100,39]

#Declaramos colores a las barras
color = ["red", "blue", "black", "purple", "orange", "pink", "violet", "brown", "fuchsia", "gray"]
 
# Creamos Gráfica y ponesmos las barras de colores
plt.barh(videojuegos, Descargas, color=color)

# Colocamos la leyenda del eje y (Videojuegos)
plt.ylabel('Videojuegos', color = "red")

# Colocamos la leyenda del eje x (Ventas)
plt.xlabel('Ventas (Millones)', color = "red")

#Colocamos el titulo
plt.title('Popularidad de los videojuegos', color = "red",)

# Mostramos la grafica
plt.show()