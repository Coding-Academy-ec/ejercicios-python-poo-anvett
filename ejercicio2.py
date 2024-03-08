class Animal:
    def __init__(self, nombre):
        self.nombre = nombre  # Asigna el nombre proporcionado al atributo 'nombre'

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        # Devuelve el sonido de un perro (ladrido)
        return f"¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        # Devuelve el sonido de un gato (maullido)
        return f"¡Miau!"
        

perro = Perro("Firulais")
gato = Gato("Minks")

print (perro.hacer_sonido())  
print (gato.hacer_sonido())  
