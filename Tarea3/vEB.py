import math

# Stores a VEB-tree where the values may be between 0 and x (where x is the lowest power hierarchal squaring starting at 2 less than or equal to u)


class VEBNode:
    def __init__(self, universe, min, max, keys, datos, parents, clusters):
		self.u=universe
		self.min=min
		self.max=max
		self.keys=keys #tipo 01 o 23 o 45
		self.datos=datos # 01, 11,00
		self.parents= parents 
		self.cluster=clusters #es una lista que deriva en los clusters
    
    #set y get parent , así vemos si es hoja y le añadimos los 1010
    
    



class VEB:


	def high(self, x):
		return int(math.floor(x / math.sqrt(self.u)))

	def low(self, x):
		return int((x % math.ceil(math.sqrt(self.u))))

	def index(self, x, y):
		return int((x * math.floor(math.sqrt(self.u))) + y)
    
    #acá hay que configurar tal que tenga tengamos la clase arbol y nodo
    #podríamos tratar de unificar nodos con y sin hijos.

    #la idea sería que el BTree guarde la cabeza del arbol (un archivo)
    #se identifique a si mismo


    #Ahora debemos idear el nodo, nos interesa saber su min maxx
    #el padre quizas pero solo para revisar, las llaves(datos tipo 2345) junto
    #con el dato binario (1001) eso implica que el valor 2 y 5 están presentes



	def __init__(self, u):
		self.filename="root"
		self.__root=VEBNode(u,self.filename)
		if u < 0:
			raise Exception("u cannot be less than 0 --- u = " + str(u));
		self.u = 2
		while self.u < u:
			self.u *= self.u
		self.min = None
		self.max = None
		self.path = ""
		if (u > 2):
			self.clusters = [ None for i in range(self.high(self.u)) ] #VEB(self.high(self.u))
			self.summary = None # VEB(self.high(self.u))
		self.root.write()

	def to_VEBNode(self,node_descriptor):
		node_text = node_descriptor.read().split('\n')[0]
		min, max, clusters, keys, summary, universe, parents, kids= node_text.split(',')
		if keys == '':
			keys = []
		else:
			keys = list(map(int, keys.split(' ')))
		if(kids == ''):
			kids = []
		else:
			kids = list(kids.split(' '))
		if (clusters == ''):
			clusters = []
		else:
			clusters = list(clusters.split(' '))
		if (parents == ''):
			parents = []
		else:
			parents = list(parents.split(' '))
		return VEBNode(min, max, clusters, keys, summary, universe,parents, kids)

	def _search_tricky(self, element, node=None):
		if node == None:
			node = self.__filename
		with open(f'btree/{node}.txt', 'r') as root:
			node_root = self.to_VEBNode(root)
			found, index = node_root.search(element)
			if(index == -1):
				root.close()
				return found, node
			else:
				next_node = node_root.get_ptrs()[index]
				root.close()
		return self._search_tricky(element, next_node)


	def search(self, element):
		found, node = self._search_tricky(element)
		return found


	def member(self, x):
		if x == self.min or x == self.max:	# found it as the minimum or maximum
			return True
		elif self.u <= 2:					# has not found it in the "leaf"
			return False
		else:
			cluster = self.clusters[self.high(x)]
			if cluster != None:
				return cluster.member(self.low(x))	# looks for it in the clusters inside
			else:
				return False

	def emptyInsert(self, x):
		self.min = x
		self.max = x

	def insert(self, x):
		if self.min == None:
			self.emptyInsert(x)
		else:
			if x < self.min:
				temp = self.min
				self.min = x
				x = temp
			if self.u > 2:
				h = self.high(x)
				if self.clusters[h] == None:
					self.clusters[h] = VEB(self.high(self.u))
				if self.summary == None:
					self.summary = VEB(self.high(self.u))
				if self.clusters[h].min == None:
					self.summary.insert(h)
					self.clusters[h].emptyInsert(self.low(x))
				else:
					self.clusters[h].insert(self.low(x))
			if x > self.max:
				self.max = x