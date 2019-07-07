import unittest
import random
import time

def mergeSort(input):
    pass





def createArray(size: int) -> list:
    result = []
    for _ in range(size):
        result.append(random.randint(1,10001))
    print (result)
    return result
start_time = time.time()
createArray(50000)
print("--- %s seconds ---" % (time.time() - start_time))
# class TestLinkedList(unittest.TestCase):


#     def setUp(self):
#         """create a new linklist before each unit test"""
#         self.LinkedListLength = 100
#         self.ll = createNewLinkList(self.LinkedListLength)