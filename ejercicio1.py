class Coche:
    def __init__(self, marca, modelo):
        
        self.marca = marca  # Asigna la marca proporcionada al atributo 'marca'
        self.modelo = modelo  # Asigna el modelo proporcionado al atributo 'modelo'
       
       

    def conducir(self):
        return f"Conduciendo el {self.marca} {self.modelo}"


sedan = Coche("Toyota", "Corolla")
print(sedan.conducir()) 