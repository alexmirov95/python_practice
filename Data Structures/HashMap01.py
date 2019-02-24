'''
HashMap
By: Alex Mirov
'''

import sympy
import LinkedList01

class HashMap:

	def __init__(self, initialSize=7, loadFactor=0.5, hashFunction=hash):
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
				li = el.getList()
				for listEl in li:
					self.insert(**listEl)


	def insert(self, key, value):

		index = self.hashFunction(key) % len(self.table)

		if self.table[index] is None:
			# create new linked list
			self.table[index] = LinkedList01.LinkedList()
		
		self.table[index].insert({
			"key": key,
			"value": value
		})

		# Check if current utilized capacity has exceeded load factor
		if self._getLoad() >= self.loadFactor: self._rehash()


	def find(self, key):
		'''
		Returns value associated with key.
		Returns None if key is not found.
		'''
		index = self.hashFunction(key) % len(self.table)
		if self.table[index] is not None:
			li = self.table[index].getList()
			for el in li:
				if el["key"] is key: 
					print("Found", key, " Val=", el["value"])
					return el["value"]
		return None



	def delete(self, key):
		'''
		Returns True if the element was found and successfully deleted.
		Else returns False.
		'''
		index = self.hashFunction(key) % len(self.table)
		if self.table[index] is not None:
			li = self.table[index].getList()
			for el, listIndex in zip(li, range(0, len(li))):
				if el["key"] is key: 
					self.table[index].delete(listIndex)
					if self.table[index].length() == 0: self.table[index] = None
					return True
		return False


	def printTable(self):
		print("Hash Table:  Size:", len(self.table), "  Load Factor:", self.loadFactor, "  Current Capcaity:", self._getLoad())
		for el, i in zip(self.table, range(0, len(self.table))):
			print("  ", i, " ", end="")
			if el is None: print(el)
			else:
				el.printList()




if __name__ == "__main__":

	myHashMap = HashMap()
	myHashMap.insert("aa", 23)
	myHashMap.insert("bb", 24)
	myHashMap.insert("dc", 18)
	myHashMap.insert("cc", 23)
	myHashMap.insert("dd", 2)
	myHashMap.insert("ee", 25)
	myHashMap.insert("ff", 5)
	myHashMap.insert("hh", 9)

	myHashMap.printTable()

	myHashMap.find("bb")
	myHashMap.find("dd")
	myHashMap.find("aa")


	myHashMap.delete("dc")
	myHashMap.printTable()

