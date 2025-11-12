from src.bst import ArbolBinarioBusqueda

def test_insercion_y_busqueda():
    arbol = ArbolBinarioBusqueda()
    arbol.insertar("Carlos", {"nacimiento": 1900})
    arbol.insertar("Ana", {"nacimiento": 1920})
    arbol.insertar("Luis", {"nacimiento": 1950})

    assert arbol.buscar("Ana") is not None
    assert arbol.buscar("Pedro") is None
