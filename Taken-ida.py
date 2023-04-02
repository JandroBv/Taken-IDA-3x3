import math

class Taken:
	def __init__(self, tablero):
		self.tablero = tablero
		self.orden = [1, 2, 3, 4, 5, 6, 7, 8, 0]
	
	def mover(self, direccion, tablero):		
		copia = tablero.copy()
		espacio = tablero.index(0)

		if direccion == "o":
			copia[espacio], copia[espacio - 1] = copia[espacio - 1], copia[espacio]
		elif direccion == "e":
			copia[espacio], copia[espacio + 1] = copia[espacio + 1], copia[espacio]
		elif direccion == "n":
			copia[espacio], copia[espacio - 3] = copia[espacio - 3], copia[espacio]
		else:
			copia[espacio], copia[espacio + 3] = copia[espacio + 3], copia[espacio]
		return copia

	def h(self, tablero):
		suma = 0
		for i in range(len(tablero)-1):
			x2 = (i % 3) + 1
			x1 = ((tablero.index(i+1)) % 3) + 1
			y2 = math.ceil(3 - (i/3))
			y1 = math.ceil(3 - (tablero.index(i+1)/3))
			suma += (abs(x2 - x1) + abs(y2 - y1))
		return suma

	def movimientosPosibles(self, tablero):
		movimientos = []
		posicion_0 = tablero.index(0)
		if posicion_0 % 3 != 0:
			movimientos.append("o")
		if (posicion_0 + 1) % 3 != 0:
			movimientos.append("e")
		if posicion_0 < 6:
			movimientos.append("s")
		if posicion_0 >= 3:
			movimientos.append("n")
		return movimientos
		
	def inverso(self, pos1, pos2):
		if (pos1 == "n" and pos2 == "s") or (pos1 == "s" and pos2 =="n"):
			return True
		if (pos1 == "e" and pos2 == "o") or (pos1 == "o" and pos2 == "e"):
			return True
		return False

	def idaStar(self,tablero):	
		if  tablero == self.orden:
		    return 
		cota = self.h(tablero)
		camino = [tablero]
		direcciones = []
		while True:
		    resultado = self.busqIDA(camino, 0, cota, direcciones)
		    if resultado == True:
		        return " ".join(direcciones)
		    elif resultado == math.inf:
		        return None
		    cota = resultado

	def busqIDA(self, camino, profundidad, cota, direcciones):
		actual = camino[-1]
		f = profundidad + self.h(actual)
		if f > cota:
			return f
		if actual == self.orden:
			return True
		min = math.inf

		for movimiento in self.movimientosPosibles(actual):
			if direcciones and self.inverso(movimiento, direcciones[-1]):
				continue
			hijo = self.mover(movimiento, actual)
			if hijo in camino:
				continue
			camino.append(hijo)
			direcciones.append(movimiento)
			resultado = self.busqIDA(camino, profundidad + 1, cota, direcciones)
			if resultado == True:				
				return True
			if resultado < min:
				min = resultado

			camino.pop()
			direcciones.pop()

		return min


tablero = [2,3,8,5,6,7,4,1,0]

prueba = Taken(tablero)
print(f"Tablero inicial: {tablero}")
print("Resolviendo...")
print(f"Solución: {prueba.idaStar(tablero)}")

