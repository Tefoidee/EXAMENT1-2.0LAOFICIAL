class Puestos:
    def __init__(self, codigo = 0, descripcion = "", areaSolicitante = "", plazas = 0, sueldo = 0.0):
        self.codigo = codigo
        self.descripcion = descripcion
        self.area = areaSolicitante
        self.plazas = plazas
        self.sueldo = sueldo

    def mostrar(self):
        print("Codigo:", self.codigo,
              " Desc:", self.descripcion,
              " Area:", self.area,
              " Plazas:", self.plazas,
              " Sueldo:", self.sueldo)
puestos = []
def validar_string(texto):
    return len(texto) >= 3
def validar_numero(n):
    return n > 0

def AgregaPuesto():
    codigo = int(input("Codigo: "))
    descripcion = input("Descripcion: ")
    area = input("Area: ")
    plazas = int(input("Plazas: "))
    sueldo = float(input("Sueldo: "))
    if not validar_string(descripcion):
        print("Texto inválido")
        return
    if not validar_string(area):
        print("Texto inválido")
        return
    if not validar_numero(codigo):
        print("Número inválido")
        return
    if  not validar_numero(plazas):
        print("Número inválido")
        return
    if  not validar_numero(sueldo):
        print("Número inválido")
        return
    for p in puestos:
        if p.codigo == codigo:
            print("Ya existe un puesto con esos datos")
            return
        if p.descripcion == descripcion:
            print("Ya existe un puesto con esos datos")
            return
        if p.area == area:
            print("Ya existe un puesto con esos datos")
            return
    nuevo_puesto = Puestos(codigo, descripcion, area, plazas, sueldo)
    puestos.append(nuevo_puesto)
    print("Puesto agregado")

def MostrarTodo():
    if len(puestos) == 0:
        print("Lista vacía")
        return
    for p in puestos:
        p.mostrar()


def ordenar_burbuja():
    n = len(puestos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if puestos[j].codigo < puestos[j + 1].codigo:
                aux = puestos[j]
                puestos[j] = puestos[j + 1]
                puestos[j + 1] = aux

def BorraPuesto():
    codigo = int(input("Codigo a borrar: "))
    ordenar_burbuja()
    for i in range(len(puestos)):
        if puestos[i].codigo == codigo:
            puestos.pop(i)
            print("Eliminado")
            return
    print("No encontrado")

def ordenar_insercion():
    for i in range(1, len(puestos)):
        aux = puestos[i]
        j = i - 1
        while j >= 0 and puestos[j].sueldo < aux.sueldo:
            puestos[j + 1] = puestos[j]
            j -= 1
        puestos[j + 1] = aux

def BuscaSueldo():
    if len(puestos) == 0:
        print("Lista vacía")
        return
    ordenar_insercion()
    buscar = float(input("Sueldo a buscar: "))
    izq = 0
    der = len(puestos) - 1
    pos = -1
    while izq <= der:
        mid = (izq + der) // 2
        if puestos[mid].sueldo == buscar:
            pos = mid
            break
        elif puestos[mid].sueldo < buscar:
            der = mid - 1
        else:
            izq = mid + 1
    if pos == -1:
        print("No encontrado")
        return
    i = pos
    while i >= 0 and puestos[i].sueldo == buscar:
        puestos[i].mostrar()
        i -= 1
    i = pos + 1
    while i < len(puestos) and puestos[i].sueldo == buscar:
        puestos[i].mostrar()
        i += 1

def ordenar_seleccion():
    n = len(puestos)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            total_j = puestos[j].plazas * puestos[j].sueldo
            total_max = puestos[max_idx].plazas * puestos[max_idx].sueldo
            if total_j > total_max:
                max_idx = j
        aux = puestos[i]
        puestos[i] = puestos[max_idx]
        puestos[max_idx] = aux

def PuestosAContratar():
    if len(puestos) == 0:
        print("Lista vacía")
        return
    monto = float(input("Monto total: "))
    ordenar_seleccion()
    suma = 0
    for p in puestos:
        total = p.plazas * p.sueldo

        if suma + total <= monto:
            p.mostrar()
            suma += total

def menu():
    while True:
        print("1.Agregar 2.Mostrar 3.Borrar 4.Buscar Sueldo 5.Contratar 6.Salir")
        op = int(input("Opcion: "))
        if op == 1:            
            AgregaPuesto()            
        elif op == 2:
            MostrarTodo()
        elif op == 3:
            BorraPuesto()
        elif op == 4:
            BuscaSueldo()        
        elif op == 5:
            PuestosAContratar()
        elif op == 6:
            break             
menu()