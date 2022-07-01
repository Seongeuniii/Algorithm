from itertools import chain


class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def add_last(self, newNode):
        if self.is_empty():
            newNode.prev = self.head
            newNode.next = self.tail
            self.tail.prev = newNode
            self.head.next = newNode
        else:
            newNode.prev = self.tail.prev
            newNode.next = self.tail
            self.tail.prev.next = newNode
            self.tail.prev = newNode

        self.size += 1

    def find_city(self, city):
        node = self.head.next

        while node.data:
            if node.data == city:
                self.delete(node)
                return True
            node = node.next

        return False

    def delete(self, node):
        print(node.prev.data, node.next.data)
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

def solution(cacheSize, cities):
    if not cacheSize:
        return 5 * len(cities)

    answer = 0
    cache = DoubleLinkedList()

    for city in cities:
        cacheHit = cache.find_city(city.lower())

        if cacheHit: 
            answer += 1
        else:  
            answer += 5
        
        if cache.size == cacheSize:
            # print('delete: ', cache.head.next.data)
            cache.delete(cache.head.next)

        cache.add_last(Node(city.lower()))

        # print(cache.head.next.data, cache.tail.prev.data, cache.size)
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))