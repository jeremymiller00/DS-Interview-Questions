"""
Given a stream of elements (of arbitrary size), write a class to find the median at any given time. Your class should have a function to add numbers to thestream and a function to calculate the median.
"""
import sys

class StreamMedian:
    
    def __init__(self):
        self.data = []
        self.sorted = False

    def add_item(self, item):
        self.data.append(item)

    def get_median(self):
        if self.sorted == False:
            self.data.sort()
            self.sorted == True
        m = len(self.data) // 2
        if len(self.data) % 2 == 0:
            return ( (self.data[m-1] + self.data[m]) / 2)
        return self.data[m]
    

def test():
    sm = StreamMedian()
    sm.add_item(1)
    sm.add_item(5)
    sm.add_item(3)
    assert sm.data == [1,5,3]
    assert sm.get_median() == 3
    assert sm.data == [1,3,5]
    sm.add_item(7)
    assert sm.get_median() == 4

####################

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == '--test':
            print("Running test")
            test()
            print("Test passed")