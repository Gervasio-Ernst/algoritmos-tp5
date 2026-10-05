class NodoArbol:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe  # True si es héroe, False si es villano
        self.izq = None
        self.der = None

class ArbolMCU:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        self.raiz = self._insertar_recursivo(self.raiz, nombre, es_heroe)

    def _insertar_recursivo(self, nodo, nombre, es_heroe):
        if nodo is None:
            return NodoArbol(nombre, es_heroe)
        if nombre.lower() < nodo.nombre.lower():
            nodo.izq = self._insertar_recursivo(nodo.izq, nombre, es_heroe)
        elif nombre.lower() > nodo.nombre.lower():
            nodo.der = self._insertar_recursivo(nodo.der, nombre, es_heroe)
        return nodo

    # b. Listar villanos ordenados alfabéticamente
    def listar_villanos(self, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is not None:
            self.listar_villanos(nodo.izq, False)
            if not nodo.es_heroe:
                print(f"- {nodo.nombre}")
            self.listar_villanos(nodo.der, False)

    # c. Mostrar todos los superhéroes que empiezan con C
    def heroes_con_c(self, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is not None:
            self.heroes_con_c(nodo.izq, False)
            if nodo.es_heroe and nodo.nombre.upper().startswith("C"):
                print(f"- {nodo.nombre}")
            self.heroes_con_c(nodo.der, False)

    # d. Determinar cuántos superhéroes hay en el árbol
    def contar_heroes(self, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is None:
            return 0
        cant = 1 if nodo.es_heroe else 0
        return cant + self.contar_heroes(nodo.izq, False) + self.contar_heroes(nodo.der, False)

    # e. Búsqueda por proximidad para modificar a Doctor Strange
    def modificar_nombre(self, termino, nuevo_nombre, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is not None:
            if termino.lower() in nodo.nombre.lower():
                print(f"Modificando '{nodo.nombre}' por '{nuevo_nombre}'")
                nodo.nombre = nuevo_nombre
            self.modificar_nombre(termino, nuevo_nombre, nodo.izq, False)
            self.modificar_nombre(termino, nuevo_nombre, nodo.der, False)

    # f. Listar superhéroes en orden descendente
    def listar_heroes_descendente(self, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is not None:
            self.listar_heroes_descendente(nodo.der, False)
            if nodo.es_heroe:
                print(f"- {nodo.nombre}")
            self.listar_heroes_descendente(nodo.izq, False)

    # g. Generar un bosque (dos árboles separados: héroes y villanos)
    def generar_bosque(self):
        arbol_heroes = ArbolMCU()
        arbol_villanos = ArbolMCU()
        self._separar_en_bosque(self.raiz, arbol_heroes, arbol_villanos)
        return arbol_heroes, arbol_villanos

    def _separar_en_bosque(self, nodo, arbol_h, arbol_v):
        if nodo is not None:
            if nodo.es_heroe:
                arbol_h.insertar(nodo.nombre, True)
            else:
                arbol_v.insertar(nodo.nombre, False)
            self._separar_en_bosque(nodo.izq, arbol_h, arbol_v)
            self._separar_en_bosque(nodo.der, arbol_h, arbol_v)

    def contar_nodos(self, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is None:
            return 0
        return 1 + self.contar_nodos(nodo.izq, False) + self.contar_nodos(nodo.der, False)

    def barrido_inorden(self, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is not None:
            self.barrido_inorden(nodo.izq, False)
            print(f"- {nodo.nombre}")
            self.barrido_inorden(nodo.der, False)