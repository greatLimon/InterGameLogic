# I realize 2 classes:
# 1. ArraysBufferFifo -> It uses an array to store data. 
#                        It also dynamically expands by size / 2 + 1, so as not to iterate over the array every time, as well as not to take up a lot of memory space
# 2. ListNodeBufferFifo -> It uses a tree structure so that each subsequent element references the previous one. 
#                          When receiving an element from the buffer, the current one is deleted
#
class ArraysBufferFifo:
    def __init__(self, capacity:int = 1) -> None:
        self.__index_last_element = -1
        self.__capacity = capacity
        self.__arr = [0] * capacity
    
    def __len__(self)->int:
        return self.__index_last_element + 1
    
    def capacity(self)->int:
        return self.__capacity

    def get(self)->any:
        if self.__index_last_element == -1:
            raise IndexError('No any elements in BufferFIFO')
        self.__index_last_element -= 1
        return self.__arr[self.__index_last_element+1]

    def put(self, element)->None:
        if self.__index_last_element + 1 == self.__capacity - 1:
            self.__extend_array()
        self.__index_last_element += 1
        self.__arr[self.__index_last_element] = element
    
    def __extend_array(self)->None:
        self.__capacity += int(self.__capacity/2)+1 #add something
        new_arr = [0] * self.__capacity
        for n, el in enumerate(self.__arr):
            new_arr[n] = el
        self.__arr = new_arr
    
    def clean(self)->None:
        if self.__index_last_element == -1:
            self.__capacity = 1
            self.__arr = [0]
        else:
            self.__arr = self.__arr[:self.__index_last_element+1]
            self.__capacity = self.__index_last_element + 1
        
class ListNodeBufferFifo:
    def __init__(self) -> None:
        self.__element = None
        self.__size = 0

    def put(self, element)->None:
        if self.__size == 0:
            self.__element = self.Node(element)
        else:
            self.__element = self.Node(element, self.__element)
        self.__size += 1

    def get(self)->any:
        if self.__size == 0:
            raise IndexError('No any elements in ListNodeBufferFifo')
        self.__size -=1
        result = self.__element.value
        self.__element = self.__element.previous
        return result

    def __len__(self)->int:
        return self.__size
    
    class Node:
        def __init__(self, value = None, previous = None) -> None:
            self.value = value
            self.previous = previous

def testArraysBufferFifo():
    print('_____________testArraysBufferFifo_____________')
    buffer = ArraysBufferFifo()
    expectation = 1
    buffer.put(expectation)
    assert buffer.get() == expectation

    buffer.put(2)
    buffer.put(3)
    buffer.put(4)
    expectation = 3
    assert len(buffer) == expectation
    expectation = 4
    assert buffer.capacity() == expectation
    expectation = 4
    assert buffer.get() == expectation
    expectation = 3    
    assert buffer.get() == expectation
    expectation = 2    
    assert buffer.get() == expectation
    expectation = 0
    assert len(buffer) == expectation
    expectation = 4
    assert buffer.capacity() == expectation 
    buffer.put(5)
    buffer.put(6)
    buffer.put(7)
    expectation = 7
    assert buffer.get() == expectation
    expectation = 6 
    assert buffer.get() == expectation
    expectation = 5 
    assert buffer.get() == expectation 
    try:
        buffer.get()
    except IndexError:
        pass

    buffer.put('Any element')
    expectation = 'Any element'
    assert buffer.get() == expectation 
    buffer.put(1)
    buffer.put(2)
    buffer.put(3)
    expectation = 3
    assert len(buffer) == expectation
    expectation = 4
    assert buffer.capacity() == expectation
    buffer.clean()
    expectation = 3
    assert len(buffer) == expectation
    expectation = 3
    assert buffer.capacity() == expectation

def testListNodeBufferFifo():
    print('_____________testListNodeBufferFifo_____________')
    buffer = ListNodeBufferFifo()
    buffer.put(1)
    assert buffer.get() == 1
    buffer.put(2)
    buffer.put(3)
    buffer.put(4)
    assert len(buffer) == 3
    assert buffer.get() == 4    
    assert buffer.get() == 3    
    assert buffer.get() == 2
    assert len(buffer) == 0  
    buffer.put(5)
    buffer.put(6)
    buffer.put(7)
    assert buffer.get() == 7
    assert buffer.get() == 6
    assert buffer.get() == 5
    try:
        buffer.get()
    except IndexError:
        pass
    buffer.put('Any element')
    assert buffer.get() == 'Any element'
    buffer.put(1)
    buffer.put(2)
    buffer.put(3)
    assert buffer.get() == 3

def main():
    testArraysBufferFifo()
    testListNodeBufferFifo()

if __name__ =='__main__':
    main()