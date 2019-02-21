'''
Open Addressing Hash Table with Linear Probing
By: Alex Mirov
Feb 2019
'''

import sympy

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


	def _getLoad (self):
		'''
		Returns the current percent utilized capacity (load) of the table.
		'''
		ct = 0
		for el in self.table:
			if el is not None: ct += 1

		return ct / len(self.table)


	def _rehash (self):
		'''
		When the capacity (load) of the table reaches the loadFactor threshold, _rehash creates a new
		table of size == the next prime number after 2x the current table size.
		'''
		# Get new table size
		newTableSize = len(self.table) * 2
		while not sympy.isprime(newTableSize): newTableSize += 1
		
		# Init empty new table
		oldTable = self.table
		self.table = [None] * newTableSize

		# Re-insert every element from old table into new table
		for el in oldTable:
			if el is not None:
				self.insert(el)


	def insert (self, data):
		'''
		Inserts 'data' into the table using linear probing
		'''
		for i in range(0, len(self.table)):
			index = (self.hashFunction(data, len(self.table)) + i) % len(self.table)

			if self.table[index] is None:
				self.table[index] = data
				break

		# Check if current utilized capacity has exceeded load factor
		if self._getLoad() >= self.loadFactor: self._rehash()


	def find (self, data):
		pass


	def delete(self, data):
		pass


	def printTable(self):
		print("Hash Table:  Size:", len(self.table), "  Load Factor:", self.loadFactor, "  Current Capcaity:", self._getLoad())
		for el, i in zip(self.table, range(0, len(self.table))):
			print("  ", i, el)





if __name__ == "__main__":

	myHash = HashTable()

	myHash.insert(33)
	myHash.insert(11)
	myHash.insert(1)
	myHash.insert(2)
	myHash.insert(1)
	myHash.insert(7)
	myHash.insert(12)
	myHash.insert(17)
	myHash.insert(16)

	myHash.printTable()
