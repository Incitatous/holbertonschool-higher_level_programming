#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @size.setter
    def data(self, value):
        if isinstance(data, int) is False:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__value

    @next_node.setter
    def next_node(self, value):
        if isinstance(next_node, (None, Node)) is False:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    def __init__(self, head):
        return self.__head

    def sorted_insert(self, value):
        
