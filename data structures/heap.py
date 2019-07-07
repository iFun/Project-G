

class Heap():
    def __init__(self):
        self.array = [None] #start the heap from 1 instead of 0 index

    def __str__(self):
        for num in self.array:
            if num:
                print(num,end =" ")
        return ''

    def _get_left_child_index(self, index:int):
        if index* 2 < len(self.array):
            return index*2
        else:
            return None

    def _get_right_child_index(self, index:int) -> int:
        if index * 2 + 1 < len(self.array):
            return index*2 + 1
        else:
            return None

    def _exchange(self, i:int, j:int) -> None:
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    # peak the max element in the heap
    def peak(self) ->  int:
        if len(self.array) <= 1:
            return None
        return self.array[1]


    def add_back(self, val: int) -> None:
        self.array.append(val)
        self.heapify_up(len(self.array) - 1)

    def add_front(self, val: int) -> None:
        self.array.insert(1,val)
        self.heapify_down(1)

    
    def get_parent_index(self, child_index: int) -> int:
        if child_index <= 1:
            return None
        return child_index // 2
    
    def heapify_up(self,index):
        parents = self.get_parent_index(index)
        if parents and self.array[parents] < self.array[index]:
            self._exchange(parents,index)
            self.heapify_up(parents) # because exchange so using the parents index which is the one thats larger
        else:
            return None

    def heapify_down(self,index):
        left_index = self._get_left_child_index(index)
        right_index = self._get_right_child_index(index)
        largest = index

        if left_index and self.array[left_index] > self.array[largest]:
            largest = left_index
        
        if right_index and self.array[right_index] > self.array[largest]:
            largest = right_index
        
        if largest is not index:
            self._exchange(largest,index)
            self.heapify_down(largest)


def main():
    heap = Heap()
    heap.add_back(5)
    heap.add_back(15)
    heap.add_back(25)
    heap.add_back(35)
    heap.add_back(45)
    heap.add_back(2)
    print(heap)


if __name__ == "__main__":
    main()