#patron de diseno singleton
class SingletonParaCreacionInstancia:
    
    _instancia = None
    
    def __new__(cls, *args, **kwargs): #distintivo para patron de diseno singleton, constructor con instancia de clase y 2 argumentos args y kwargs
        if not cls._instancia:
            cls._instancia = super(SingletonParaCreacionInstancia, cls).__new__(cls)
        return cls._instancia