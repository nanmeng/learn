from collections import deque

class Edge(object):
	def __init__(self, s, e):
		if s.__class__.__name__ != 'Vertex' or e.__class__.__name__ != 'Vertex':
			raise Exception('Edge shall be initialized with Vertex objects')
		self.s = s
		self.e = e

class Vertex(object):
	def __init__(self, i, pie=None, color=None, distance=None):
		# id
		self.i = i
		self.pie = pie
		self.color = color
		self.distance = distance
	def toString(self):
		s = '[' + str(self.i) + ' p:'
		if self.pie:
			s += str(self.pie.i)
		else:
			s += str(self.pie)
		s += ' c:' + str(self.color)
		s += ' d:' + str(self.distance) + ']'
		return s

class UndirectedGraph(object):
	def __init__(self):
		self.V = []
		self.Adj = {}
	def addVertex(self, v):
		self.V.append(v)
	def addEdge(self, E):
		if E.s not in self.V:
			# add edge's starting vertex if not exist
			self.addVertex(E.s)
		if E.e not in self.V:
			# add edge's ending vertex if not exist
			self.addVertex(E.e)
		if not self.Adj.has_key(E.s.i):
			# init the adjacency list for edge's
			# starting vertex if not exist
			self.Adj[E.s.i] = deque([])
		# add ending vertex to starting vertex's adj list
		self.Adj[E.s.i].append(E.e)
		if not self.Adj.has_key(E.e.i):
			# init the adjacency list for edge's
			# ending vertex if not exist
			self.Adj[E.e.i] = deque([])
		# add starting vertex to ending vertex's adj list
		self.Adj[E.e.i].append(E.s)
	def toString(self):
		print '>>>'
		print 'Vertices:'
		for v in self.V:
			print v.toString()
		print 'Adjacency:'
		for a in self.Adj:
			print a, ':'
			for i in self.Adj[a]:
				print i.toString()
		print '<<<'

def breadthFirstSearch(G, s):
	# G is an UndirectedGraph here (it could be DAG)
	# s is the vertex to start the breadth first search from

	if s.__class__.__name__ != 'Vertex':
		raise Exception('invalid argument')
	if s not in G.V:
		raise Exception('non-existent vertex')
	# label all vertices WHITE
	for v in G.V:
		v.color = 'WHITE'
		# leave v.distance as None
		# leave v.pie as None
	print '=== Labeled every vertex WHITE ==='
	G.toString()
	s.distance = 0
	s.color = 'GRAY'
	# leave s.pie as None since it has no upstream vertex
	Q = deque([])
	Q.append(s)
	while Q:
		print '== Queue =='
		for x in Q:
			print x.toString()
		# while Q is not empty queue
		vertex = Q.popleft()
		print '== vertex popped =='
		print vertex.toString()
		print '== vertex adjacency =='
		for adj in G.Adj[vertex.i]:
			print adj.toString()
			if adj.color == 'WHITE':
				adj.color == 'GRAY'
				adj.distance = vertex.distance + 1
				adj.pie = vertex
				Q.append(adj)
				print '== enqueued vertex =='
				print adj.toString()
		vertex.color = 'BLACK'

if __name__ == '__main__':
	G = UndirectedGraph()
	V = []
	for i in xrange(0, 10):
		V.append(Vertex(i))
		G.addVertex(V[i])
	G.toString()
	G.addEdge(Edge(V[0], V[1]))
	G.addEdge(Edge(V[0], V[2]))
	G.addEdge(Edge(V[0], V[6]))
	G.addEdge(Edge(V[1], V[5]))
	G.addEdge(Edge(V[2], V[3]))
	G.addEdge(Edge(V[2], V[6]))
	G.addEdge(Edge(V[2], V[7]))
	G.addEdge(Edge(V[2], V[8]))
	G.addEdge(Edge(V[3], V[9]))
	G.addEdge(Edge(V[4], V[5]))
	G.addEdge(Edge(V[4], V[9]))
	G.addEdge(Edge(V[7], V[9]))
	G.addEdge(Edge(V[8], V[9]))
	G.toString()
	breadthFirstSearch(G, V[0])
	G.toString()
