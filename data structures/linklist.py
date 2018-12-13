import unittest

class Node():
    """LinkedList node class"""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        """Override the default print behavior"""
        if self.next is not None:
            return (str(self.value) + ' -->')
        return str(self.value)

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.value == other.value


class LinkedList():
    """docstring for LinkedList"""
    def __init__(self, node):
        self.head = node
        self.tail = node
        self.__length = 1

    def __str__(self):
        node = self.head
        while node is not None:
            print(node,end =" ")
            node = node.next
        return ''

    def getLength(self) -> int:
        return self.__length

    def addToTail(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next
        self.__length += 1

    def addToHead(self, node):
        node.next = self.head
        self.head.prev = node
        self.head= node
        self.__length += 1

    def addToMid(self, index, node):
        current = self.head
        while index is not 0:
            current = current.next
            index -= 1
        prev = current.prev
        node.next = current
        node.prev = prev
        current.prev = node
        prev.next = node

    def deleteNode(self, node):
        if node is self.tail:
            self.tail = self.tail.prev
            node = None
        elif node is self.head:
            node = node.next
            node.next = node.next.next
            self.head = node
        else:
            node = node.next
            node.prev = node.prev.prev
            node.next = node.next.next

        self.__length -= 1

    def clear(self):
        self.head = None
        self.tail = None
        self.__length = 0

    def indexOf(self, value):
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index
            else:
                current = current.next
                index += 1

        print('value is not in LinkedList')
        return None

    def addToIndex(self, index, node):
        if index > self.__length - 1 or index < 0 or node is None:
            print('index is out of bound or node is null')
        if index == 0:
            return self.addToHead(node)
        elif index == self.__length - 1:
            return self.addToTail(node)
        else:
            return self.addToMid(index, node)

    def set(self, index, newValue):
        if index > self.__length - 1 or index < 0:
            print('index is out of bound')
        else:
            current = self.head
            while index is not 0:
                current = current.next
                index -= 1
            current.value = newValue

    def reverse(self):
        """reverse the linkedlist"""
        current = self.head
        while current is not None:
            nextNode = current.next
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = nextNode


        newTail = self.head
        self.head = self.tail
        self.tail = newTail
        
        

def createNewLinkList(length):
    for value in range(length):
        if value == 0:
            ll = LinkedList(Node(value))
        else:
            ll.addToTail(Node(value))
    return ll


class TestLinkedList(unittest.TestCase):


    def setUp(self):
        """create a new linklist before each unit test"""
        self.LinkedListLength = 100
        self.ll = createNewLinkList(self.LinkedListLength)
   

    def test_init(self):
        self.assertEqual(self.ll.getLength(),self.LinkedListLength)
        self.assertEqual(self.ll.head.value,self.LinkedListLength - self.LinkedListLength)
        self.assertEqual(self.ll.tail.value,self.LinkedListLength - 1)

    def test_delete_head(self):
        head = self.ll.head
        nextHead = head.next
        self.ll.deleteNode(head)
        self.assertEqual(self.ll.head,nextHead)
        self.assertEqual(self.ll.getLength(),self.LinkedListLength - 1)
        self.assertEqual(self.ll.tail.value ,self.LinkedListLength - 1)

    def test_delete_tail(self):
        tail = self.ll.tail
        nextTail = tail.prev
        self.ll.deleteNode(tail)
        self.assertEqual(self.ll.tail,nextTail)
        self.assertEqual(self.ll.getLength(),self.LinkedListLength - 1)

    def test_delete_middle(self):
        mid = self.ll.head.next.next
        nextmid = mid.next
        self.ll.deleteNode(mid)
        self.assertNotEqual(mid ,nextmid.prev)
        self.assertEqual(self.ll.tail.value ,self.LinkedListLength - 1)
        self.assertEqual(self.ll.head.value ,0)
        self.assertEqual(self.ll.getLength(),self.LinkedListLength - 1)

    def test_clear(self):
        self.ll.clear()
        self.assertEqual(self.ll.tail,None)
        self.assertEqual(self.ll.head,None)
        self.assertEqual(self.ll.getLength(),0)

    def test_indexOf(self):
        self.assertEqual(self.ll.indexOf(self.LinkedListLength - 1) ,self.LinkedListLength - 1)
        self.assertEqual(self.ll.indexOf(0) ,0)

    def test_add_to_Index(self):
        self.ll.addToIndex(0, Node(100))
        self.ll.addToIndex(self.ll.getLength() - 1, Node(200))
        self.ll.addToIndex(self.ll.getLength() - 2, Node(300))


        self.assertEqual(self.ll.head.value,100)
        self.assertEqual(self.ll.tail.value,200)
        self.assertEqual(self.ll.indexOf(300),self.ll.getLength() - 2)
        self.assertEqual(self.ll.getLength(),self.LinkedListLength - 1 + 3)

    def test_set(self):
        self.ll.set(0,100)
        self.ll.set(self.ll.getLength() - 1, 200)
        self.ll.set(self.ll.getLength() - 2, 300)

        self.assertEqual(self.ll.head.value,100)
        self.assertEqual(self.ll.tail.value,200)
        self.assertEqual(self.ll.indexOf(300),self.ll.getLength() - 2)
        self.assertEqual(self.ll.getLength(),self.LinkedListLength)

    def test_reverse(self):
        self.ll.reverse()
        self.assertEqual(self.ll.head.value,self.ll.getLength() - 1)
        self.assertEqual(self.ll.tail.value,0)
        self.assertEqual(self.ll.indexOf(self.ll.getLength() - 2),1)


if __name__ == '__main__':
    unittest.main()
    




        
