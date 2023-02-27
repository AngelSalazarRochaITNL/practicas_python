class Usuario:
    def __init__(self, usuario, password, nombre, curp, ciudad,rol = "cliente") -> None:
        self._usuario = usuario
        self._password = password
        self._rol = rol
        self._nombre = nombre
        self._curp = curp
        self._ciudad = ciudad
    
    ## Propiedades usuario
    # Getter
    @property
    def Usuario(self):
        return self._usuario
    
    # Setter
    @Usuario.setter
    def Usuario(self, u):
        self._usuario = u

    
    ## Propiedades password
    # Getter
    @property
    def Password(self):
        return self._password
    
    # Setter
    @Password.setter
    def Password(self, u):
        self._password = u


    ## Propiedades rol
    # Getter
    @property
    def Rol(self):
        return self._rol
    
    # # Setter por default es cliente
    # @Usuario.setter
    # def Usuario(self, u):
    #     self._usuario = u


    ## Propiedades nombre
    # Getter
    @property
    def Nombre(self):
        return self._nombre
    
    # Setter
    @Nombre.setter
    def Nombre(self, u):
        self._nombre = u


    ## Propiedades curp
    # Getter
    @property
    def Curp(self):
        return self._curp
    
    # Setter
    @Curp.setter
    def Curp(self, u):
        self._curp = u


    ## Propiedades Ciudad
    # Getter
    @property
    def Ciudad(self):
        return self._ciudad
    
    # Setter
    @Ciudad.setter
    def Ciudad(self, u):
        self._ciudad = u
