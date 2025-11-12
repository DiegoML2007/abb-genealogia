class Nodo:
    def __init__(self, clave, datos=None):
        self.clave = clave
        self.datos = datos or {}
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, datos=None):
        def _insertar(nodo, clave, datos):
            if nodo is None:
                return Nodo(clave, datos)
            if clave < nodo.clave:
                nodo.izquierdo = _insertar(nodo.izquierdo, clave, datos)
            elif clave > nodo.clave:
                nodo.derecho = _insertar(nodo.derecho, clave, datos)
            return nodo
        self.raiz = _insertar(self.raiz, clave, datos)

    def buscar(self, clave):
        nodo = self.raiz
        while nodo:
            if clave == nodo.clave:
                return nodo
            elif clave < nodo.clave:
                nodo = nodo.izquierdo
            else:
                nodo = nodo.derecho
        return None

    def recorrido_inorden(self):
        resultado = []
        def _inorden(n):
            if n:
                _inorden(n.izquierdo)
                resultado.append(n.clave)
                _inorden(n.derecho)
        _inorden(self.raiz)
        return resultado
