from nodo import Nodo
class Lista(object):
    def __init__(self):
       self.cabeza=None
       self.cola=None
       self.count=0

    def vacia(self):
        if self.cabeza==None:
            return True
        else:
            return False

    def insertarPrincipio(self, dato):
        temporal = Nodo(dato)
        if self.vacia()==True:
            self.cabeza=temporal
            self.cola=temporal
        else:
            temporal.siguiente=self.cabeza
            self.cabeza.anterior = temporal
            self.cabeza = temporal
    
    def listarPrincipio(self):
        temporal = self.cabeza
        while temporal != None:
            print( temporal.verNodo(), end=' ')
            temporal = temporal.siguiente

    def listarFinal(self):
        temporal = self.cola
        while temporal != None:
            print( temporal.verNodo(),end=' ')
            temporal = temporal.anterior

    def borrarPrimero(self):
        if self.vacia()==False:
            self.cabeza=self.cabeza.siguiente
            self.cabeza.anterior=None

    def borrarUltimo(self):
        if self.cola.anterior == None:
            self.cabeza=None
            self.cola=None
        else:
            self.cola= self.cola.anterior
            self.cola.siguiente=None 

    def borrarPosicion(self, pos):
        anterior= self.cabeza
        actual=self.cabeza
        k=0
        if pos>0:
            while k != pos and actual.siguiente != None:
                anterior=actual
                actual=actual.siguiente
                k+=1
            if k==pos:
                temporal=actual.siguiente
                anterior.siguiente=actual.siguiente
                temporal.anterior=anterior 

    def insertarPosicion(self,datoIn, dato1, dato2):
        # print(self.buscar(dato))
        # print(self.count)
        anterior = self.cabeza
        temporal = Nodo(datoIn)
        actual= self.cabeza
        k = 0
        if self.buscar(dato1)==True:
            if self.buscar(dato2)==True:
                self.count = 0
                self.buscar(dato1)
                # print(self.count)
                while k != self.count and actual.siguiente != None:
                    anterior = actual
                    actual = actual.siguiente
                    k+=1
                if k==self.count:
                    # print(actual.verNodo())
                    temporal.siguiente = actual.siguiente
                    actual.siguiente = temporal

    def buscar(self, dato):
        for i in self.iterar():
            if dato == i:
                # print()
                # print(self.count)
                return True
            self.count = self.count +1
        return False

    def iterar(self):
        actual = self.cabeza
        while actual:
            dato =actual.info
            actual = actual.siguiente
            yield dato
