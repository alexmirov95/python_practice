'''
Open Addressing Hash Table with Linear Probing
By: Alex Mirov
Feb 2019
'''

######## Hash Functions ########

def modulo (val, tableSize):
	return val % tableSize

def quadratic (val, tableSize):
	return val ** 2


######## Hash Table ##########

class HashTable:

	def __init__ (self, initialSize=7, loadFactor=0.5, hashFunction=modulo):
		self.table = [None] * initialSize
		self.loadFactor = loadFactor
		self.hashFunction = hashFunction


	def _rehash (self):
		pass


	def insert (self, data):
		
		for i in range(0, len(self.table)):
			index = self.hashFunction(data, len(self.table)) + i

			if self.table[index] is None:
				self.table[index] = data
				break


		# pass


	def find (self, data):
		pass


	def delete(self, data):
		pass







if __name__ == "__main__":

	myHash = HashTable()
	myHash.insert(10)
