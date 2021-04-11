class Producto:
    def __init__(self):
        self.imagen = ""
        self.descripcion = ""
        self.grupo = ""

class Arma(Producto):
    def __init__(self):
        Producto.__init__(self)

class ArmaHumanos(Arma):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/arma.png"
        self.descripcion = "arma de los humanos"
        
class ArmaOrcos(Arma):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/arma.png"
        self.descripcion = "arma de los orcos"

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

class EscudoHumanos(Arma):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/escudo.png"
        self.descripcion = "escudo de los humanos"
        
class EscudoOrcos(Arma):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/escudo.png"
        self.descripcion = "escudo de los orcos"

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)

class MonturaHumanos(Montura):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/montura.png"
        self.descripcion = "montura de los humanos"
        
class MonturaOrcos(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/montura.png"
        self.descripcion = "montura de los orcos"

class Personaje(Producto):
    def __init__(self):
        Producto.__init__(self)

class PersonajeHumanos(Personaje):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/personaje.png"
        self.descripcion = "personaje de los humanos"
        
class PersonajeOrcos(Personaje):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/personaje.png"
        self.descripcion = "personaje de los orcos"