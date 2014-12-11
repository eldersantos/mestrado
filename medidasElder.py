
''' Falta finalizar '''

class Graph():

	def __init__(self, inputFile):		
		self.file = open(inputFile)
		self.lines = self.file.readlines()
		self.matrix = []

		for line in self.lines:
			self.matrix.append(line.split(' '))
			t = len(self.matrix)
			for i in range(len(self.lines)):
				self.matrix[t-1][i] = int(self.matrix[t-1][i])

		self.ladj = self.getLadj(self.matrix)

	def getLadj(self, matrix):
		list = []
		for i in range(len(matrix)):
			for j in range(i,len(matrix)):
				if matrix[i][j]:
					list.append([i,j])
		return list

	def getOrdem(self):
		return len(self.matrix)

	def getTamanho(self):
		return len(self.ladj)

	def printDegrees(self):
		print('\nDegrees')
		for i in range(self.getOrdem()):
			k = sum(self.matrix[i])
			print('k(' + str(i) + ') =', k)

	def printK(self):
		print('<k> =', (2 * self.getTamanho()) / self.getOrdem())

	def printMadj(self):
		print('\nMadj')
		for row in self.matrix:
			print(row)

	def printLadj(self):
		print('\nLadj')
		for line in self.ladj:
			print(line[0] + 1, line[1] + 1)

	def printOrdem(self):
		print('\nOrdem (N):', self.getOrdem())

	def printTamanho(self):
		print('\nTamanho (L):', self.getTamanho())



import sys

if __name__ == "__main__":

	g = Graph(sys.argv[1])
	g.printMadj()
	g.printLadj()
	g.printOrdem()
	g.printTamanho()
	g.printDegrees()
	g.printK()
