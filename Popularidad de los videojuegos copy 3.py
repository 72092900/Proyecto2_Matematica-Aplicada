#Importaños a matplotlib
import matplotlib.pyplot as plt

#Definimos  la varianle cantidad de juegos mas populares
NumeroJuegos = [6,1,2,1]

#definimos la variable plataformas
Plataforma = ["Multi","Móviles","Wii","Gameboy/NES"]

#creamos la grafica circular
plt.pie(NumeroJuegos, labels=Plataforma, autopct="%0.1f %%")

#Colocamos el titulo
plt.title("Plataforma de los 10 videojuegos mas polulares", color = "red")

#Colocamos la leyenda
plt.legend(["Multi", "Móoviles", "Wii", "Gamevoy/NES"])

#Mostramos la grafica
plt.show()