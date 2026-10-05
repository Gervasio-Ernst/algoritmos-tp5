from collections import deque, Counter

class NodoCriatura:
    def __init__(self, nombre, derrotado_por="-", descripcion="", capturada=None):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.descripcion = descripcion
        self.capturada = capturada  # g. Campo adicional
        self.izq = None
        self.der = None

class ArbolMitologia:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, derrotado_por="-", descripcion="", capturada=None):
        self.raiz = self._insertar(self.raiz, nombre, derrotado_por, descripcion, capturada)

    def _insertar(self, nodo, nombre, derrotado_por, descripcion, capturada):
        if nodo is None:
            return NodoCriatura(nombre, derrotado_por, descripcion, capturada)
        if nombre.lower() < nodo.nombre.lower():
            nodo.izq = self._insertar(nodo.izq, nombre, derrotado_por, descripcion, capturada)
        elif nombre.lower() > nodo.nombre.lower():
            nodo.der = self._insertar(nodo.der, nombre, derrotado_por, descripcion, capturada)
        return nodo

    def buscar(self, nombre, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is None or nodo.nombre.lower() == nombre.lower():
            return nodo
        if nombre.lower() < nodo.nombre.lower():
            return self.buscar(nombre, nodo.izq, False)
        return self.buscar(nombre, nodo.der, False)

    # a. Listado inorden de las criaturas y quiénes la derrotaron
    def inorden_criaturas(self, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is not None:
            self.inorden_criaturas(nodo.izq, False)
            print(f"Criatura: {nodo.nombre:<22} | Derrotado por: {nodo.derrotado_por}")
            self.inorden_criaturas(nodo.der, False)

    # b. Cargar una breve descripción sobre una criatura
    def cargar_descripcion(self, nombre, descripcion):
        nodo = self.buscar(nombre)
        if nodo:
            nodo.descripcion = descripcion

    # c. Mostrar toda la información de la criatura Talos
    def mostrar_info(self, nombre):
        nodo = self.buscar(nombre)
        if nodo:
            print(f"--- Información de {nodo.nombre} ---")
            print(f"Derrotado por: {nodo.derrotado_por}")
            print(f"Descripción: {nodo.descripcion}")
            print(f"Capturada por: {nodo.capturada}")
        else:
            print(f"Criatura {nombre} no encontrada.")

    # d. Determinar los 3 héroes/dioses que derrotaron mayor cantidad de criaturas
    def top_3_heroes(self, nodo=None, cont=None):
        if cont is None:
            cont = Counter()
            nodo = self.raiz
        if nodo is not None:
            if nodo.derrotado_por != "-" and nodo.derrotado_por:
                cont[nodo.derrotado_por] += 1
            self.top_3_heroes(nodo.izq, cont)
            self.top_3_heroes(nodo.der, cont)
        if nodo == self.raiz:
            return cont.most_common(3)

    # e. Listar las criaturas derrotadas por Heracles
    def criaturas_por_heroe(self, heroe, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is not None:
            self.criaturas_por_heroe(heroe, nodo.izq, False)
            if nodo.derrotado_por.lower() == heroe.lower():
                print(f"- {nodo.nombre}")
            self.criaturas_por_heroe(heroe, nodo.der, False)

    # f. Listar las criaturas que no han sido derrotadas
    def criaturas_no_derrotadas(self, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is not None:
            self.criaturas_no_derrotadas(nodo.izq, False)
            if nodo.derrotado_por == "-":
                print(f"- {nodo.nombre}")
            self.criaturas_no_derrotadas(nodo.der, False)

    # h. Modificar nodos indicando que Heracles las atrapó (campo capturada)
    def marcar_capturadas_por_heracles(self):
        objetivos = ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]
        for obj in objetivos:
            nodo = self.buscar(obj)
            if nodo:
                nodo.capturada = "Heracles"

    # i. Búsquedas por coincidencia
    def buscar_por_coincidencia(self, cadena, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is not None:
            if cadena.lower() in nodo.nombre.lower():
                print(f"- {nodo.nombre}")
            self.buscar_por_coincidencia(cadena, nodo.izq, False)
            self.buscar_por_coincidencia(cadena, nodo.der, False)

    # j. Eliminar al Basilisco y a las Sirenas
    def eliminar(self, nombre):
        self.raiz = self._eliminar_recursivo(self.raiz, nombre)

    def _eliminar_recursivo(self, nodo, nombre):
        if nodo is None:
            return None
        if nombre.lower() < nodo.nombre.lower():
            nodo.izq = self._eliminar_recursivo(nodo.izq, nombre)
        elif nombre.lower() > nodo.nombre.lower():
            nodo.der = self._eliminar_recursivo(nodo.der, nombre)
        else:
            if nodo.izq is None:
                return nodo.der
            if nodo.der is None:
                return nodo.izq
            min_nodo = self._min_nodo(nodo.der)
            nodo.nombre = min_nodo.nombre
            nodo.derrotado_por = min_nodo.derrotado_por
            nodo.descripcion = min_nodo.descripcion
            nodo.capturada = min_nodo.capturada
            nodo.der = self._eliminar_recursivo(nodo.der, min_nodo.nombre)
        return nodo

    def _min_nodo(self, nodo):
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

    # k. Modificar 'Aves del Estínfalo' agregando que Heracles derrotó a varias
    def modificar_aves_estinfalo(self):
        nodo = self.buscar("Aves del Estínfalo")
        if nodo:
            nodo.derrotado_por = "Heracles (derrotó a varias)"

    # l. Modificar Ladón por Dragón Ladón
    def renombrar_ladon(self):
        nodo = self.buscar("Ladón")
        if nodo:
            det = nodo.derrotado_por
            desc = nodo.descripcion
            cap = nodo.capturada
            self.eliminar("Ladón")
            self.insertar("Dragón Ladón", det, desc, cap)

    # m. Listado por nivel del árbol (Recorrido en Amplitud / BFS)
    def listado_por_nivel(self):
        if not self.raiz:
            return
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            print(f"- {nodo.nombre}")
            if nodo.izq:
                cola.append(nodo.izq)
            if nodo.der:
                cola.append(nodo.der)

    # n. Mostrar las criaturas capturadas por Heracles
    def criaturas_capturadas_por(self, heroe, nodo=None, es_raiz=True):
        if es_raiz:
            nodo = self.raiz
        if nodo is not None:
            self.criaturas_capturadas_por(heroe, nodo.izq, False)
            if nodo.capturada and nodo.capturada.lower() == heroe.lower():
                print(f"- {nodo.nombre}")
            self.criaturas_capturadas_por(heroe, nodo.der, False)