class Node():
	"""docstring for Node"""
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None
	def __str__(self):
		if self.next != None:
			return (str(self.value) + ' -->')
		return str(self.value)
		

class LinkedList():
	"""docstring for LinkedList"""
	def __init__(self, node):
		self.head = node
		self.tail = node
		self.__length = 1

	def __str__(self):
		node = self.head
		while node != None:
			print(node,end =" ")
			node = node.next
		return ''

	def getLength():
		return __length

	def addNewNode(self, node):
		self.tail.next = node
		node.prev = self.tail
		self.tail = self.tail.next
		self.__length += 1

	def deleteNode(self, node):
		if node.next == None:
			self.tail = self.tail.prev
			node = None
		else
			node.value = node.next.value
			node.next = node.next.next
		self.__length -= 1






def run():
	tmp = Node(2)

	ll = LinkedList(tmp)
	ll.addNewNode(Node(6))
	ll.addNewNode(Node(3))
	ll.addNewNode(Node(4))
	ll.addNewNode(Node(5))
	ll.addNewNode(Node(7))
	ll.addNewNode(Node(9))
	print (ll)

run()

import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()




		
